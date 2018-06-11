import traceback
import numpy as np
import cv2
from scipy.io import wavfile as spwav
import wave
import struct


class AudioImageProcessing:
    log = []

    @staticmethod
    def readAudioWave(path, channel=0):
        file_audio = spwav.read(path)
        sample_rate = file_audio[0]
        try:
            tp = type(file_audio[1][0])
            if not (tp == np.int16 or tp == np.int32 or tp == np.uint8 or tp == np.float32):
                data_audio = file_audio[1][:, channel]
            else:
                data_audio = file_audio[1]
        except TypeError:
            AudioImageProcessing.logPut('Error when extracting raw data - check number of file\'s channels')
        except IndexError:
            AudioImageProcessing.logPut('Error when reading data')
            data_audio = None
        return [sample_rate, data_audio]

    @staticmethod
    def convertImageToBits(path):
        bytes_list = []
        with open(path, 'rb') as f:
            byte = f.read(1)
            while byte != b'':
                bit_list = [str((ord(byte) >> i) & 1) for i in range(7, -1, -1)]
                bytes_list.append(bit_list)
                byte = f.read(1)
        return bytes_list

    @staticmethod
    def encodeImageInSound(audio_channel, image_bytes_list, step=1, bit_density=1):
        try:
            if not (bit_density == 1 or bit_density == 2 or bit_density == 4 or bit_density == 8):
                raise ValueError('Bit density argument have to be 1, 2, 4 or 8')
            modified_channel = []
            rest_start_index = 0
            cnt_step = 0
            cnt_byte = 0
            cnt_bit = 7
            for i in range(len(audio_channel)):
                cnt_step += 1
                if cnt_step == step:
                    cnt_step = 0
                    if cnt_bit == -1:
                        cnt_bit = 7
                        cnt_byte += 1
                    if cnt_byte > len(image_bytes_list) - 1:
                        rest_start_index = i
                        AudioImageProcessing.logPut('Encoding channel partially completed')
                        break
                    if not image_bytes_list[cnt_byte]:   # if there will be empty bytes for two channels encoding
                        cnt_byte += 1
                        if cnt_byte > len(image_bytes_list) - 1:
                            rest_start_index = i
                            AudioImageProcessing.logPut('Encoding channel partially completed')
                            break

                    modified_value = audio_channel[i]
                    for b in range(bit_density - 1, -1, -1):
                        temp_bit = int(image_bytes_list[cnt_byte][cnt_bit])
                        if temp_bit:
                            modified_value |= (1 << b)
                        else:
                            modified_value &= ~(1 << b)
                        cnt_bit -= 1
                    modified_channel.append(modified_value)

            new_channel = np.concatenate((modified_channel, audio_channel[rest_start_index:]))
            AudioImageProcessing.logPut('Encoding channel completed')
            return new_channel
        except ValueError as err:
            AudioImageProcessing.logPut('Exception during encoding: ', err)
            pass


    @staticmethod
    def encodeImageInSoundWithWriting(soundDir, imageDir, outputDir, channel, bits):
        try:
            # reading audio file
            AudioImageProcessing.logPut('Reading audio from ' +  soundDir + '...')
            if channel == 'L' or channel == 'R' or channel == 'L+R':
                AudioImageProcessing.logPut('Encoding left channel')
                sample_rateL, data_audioL = AudioImageProcessing.readAudioWave(soundDir, channel=0)
                AudioImageProcessing.logPut('Encoding right channel')
                sample_rateR, data_audioR = AudioImageProcessing.readAudioWave(soundDir, channel=1)
            else:
                raise ValueError('Wrong channel value - should be \'L\', \'R\' or \'L+R\'')

            if sample_rateL != sample_rateR:
                raise ValueError('Sample rates from channels differ')
            else:
                sample_rate = sample_rateL

            # readind image
            AudioImageProcessing.logPut('Reading image from '+ imageDir + '...')
            image_bytes_list = AudioImageProcessing.convertImageToBits(imageDir)

            # encoding image in audio
            AudioImageProcessing.logPut('Start encoding...')
            if channel == 'L':
                new_channelL = AudioImageProcessing.encodeImageInSound(data_audioL, image_bytes_list, step=1, bit_density=bits)
                new_channelR = data_audioR
                AudioImageProcessing.logPut('LENGTHS:', len(new_channelL), len(new_channelR))
            elif channel == 'R':
                new_channelR = AudioImageProcessing.encodeImageInSound(data_audioR, image_bytes_list, step=1, bit_density=bits)
                new_channelL = data_audioL
                AudioImageProcessing.logPut('LENGTHS:', len(new_channelR), len(new_channelL))
            elif channel == 'L+R':
                image_bytes_listL = image_bytes_list[:]
                image_bytes_listL = [[] if (i % 2) == 0 else image_bytes_listL[i] for i in range(len(image_bytes_listL))]

                image_bytes_listR = image_bytes_list[:]
                image_bytes_listR = [[] if (i % 2) == 1 else image_bytes_listR[i] for i in range(len(image_bytes_listR))]

                new_channelL = AudioImageProcessing.encodeImageInSound(data_audioL, image_bytes_listL, step=1, bit_density=bits)
                new_channelR = AudioImageProcessing.encodeImageInSound(data_audioR, image_bytes_listR, step=1, bit_density=bits)

            # joining both channels
            AudioImageProcessing.logPut('Preparing encoded data to write to file...')
            if len(new_channelL) != len(new_channelR):
                raise ValueError('Lengths of channels differ')

            # writing to new file
            AudioImageProcessing.logPut('Writing encoded data to ' +  outputDir +'...')
            newF = wave.open(outputDir,'wb')
            newF.setnchannels(2)
            newF.setsampwidth(2)
            newF.setframerate(sample_rate)         
            new_channels = [newF.writeframesraw(struct.pack('<hh', l, r )) for l,r  in zip(new_channelL,new_channelR)]
            newF.close()
            AudioImageProcessing.logPut('Encoding finished')
        except ValueError as err:
            AudioImageProcessing.logPut('Exception: ', err)
            pass
        except Exception as exc:
            traceback.print_exc()
            pass


    @staticmethod
    def decodeImageFromAudio(modifiedAudioDir, outputImageDir, channel, bits_density):
        # begin of jpeg file: 0xFF, 0xD8
        # end of jpeg file: 0xFF, 0xD9
        try:
            # read audio data
            AudioImageProcessing.logPut('Reading encoded audio data from ' +  modifiedAudioDir +'...')
            sample_rateL, data_audioL = AudioImageProcessing.readAudioWave(modifiedAudioDir, channel=0)
            sample_rateR, data_audioR = AudioImageProcessing.readAudioWave(modifiedAudioDir, channel=1)
            if sample_rateL != sample_rateR:
                raise ValueError('Sample rates from channels differ')
            samples_amount = len(data_audioL)

            # decoding
            AudioImageProcessing.logPut('Start decoding...')
            if channel == 'L' or channel == 'R':
                bytes_values = []
                temp_bits = []
                for i in range(samples_amount):
                    if channel == 'L':
                        sample = data_audioL[i]
                    elif channel == 'R':
                        sample = data_audioR[i]
                    temp_bits += AudioImageProcessing.getBitsFromSample(sample, bits_density)
                    if len(temp_bits) == 8:
                        bytes_values.append(AudioImageProcessing.getByteValueFromBits(temp_bits))
                        temp_bits = []
                    if len(bytes_values) >= 2 and bytes_values[-1] == 0xD9 and bytes_values[-2] == 0xFF:
                        AudioImageProcessing.logPut('Decoding ended')
                        break
                    elif len(temp_bits) > 8:
                        raise ArithmeticError('Too large bits list - more than 8 bits read')

            elif channel == 'L+R':
                bytes_values = []
                bytes_valuesL = []
                temp_bitsL = []
                bytes_valuesR = []
                temp_bitsR = []
                for i in range(samples_amount):
                    sampleL = data_audioL[i]
                    sampleR = data_audioR[i]
                    temp_bitsL += AudioImageProcessing.getBitsFromSample(sampleL, bits_density)
                    temp_bitsR += AudioImageProcessing.getBitsFromSample(sampleR, bits_density)
                    if len(temp_bitsR) == 8:
                        bytes_values.append(AudioImageProcessing.getByteValueFromBits(temp_bitsR))
                        temp_bitsR = []
                    if len(bytes_values) >= 2 and bytes_values[-1] == 0xD9 and bytes_values[-2] == 0xFF:
                        AudioImageProcessing.logPut('Decoding ended')
                        break
                    if len(temp_bitsL) == 8:
                        bytes_values.append(AudioImageProcessing.getByteValueFromBits(temp_bitsL))
                        temp_bitsL = []
                    if len(bytes_values) >= 2 and bytes_values[-1] == 0xD9 and bytes_values[-2] == 0xFF:
                        AudioImageProcessing.logPut('Decoding ended')
                        break


            # writing to file\
            AudioImageProcessing.logPut('Processing decoded data...')
            bytes_array = bytearray(bytes_values)
            AudioImageProcessing.logPut('Writing decoded data to ' +  outputImageDir + '...')
            output_image = open(outputImageDir, 'wb')
            output_image.write(bytes_array)
            AudioImageProcessing.logPut('Decoding finished')

        except ArithmeticError as aerr:
            pass

    @staticmethod
    def getBitsFromSample(sample, bits):
        temp_bits = []
        for b in range(bits - 1, -1, -1):
            if sample & (1 << b):
                temp_bits.append(1)
            else:
                temp_bits.append(0)
        return temp_bits

    @staticmethod
    def getByteValueFromBits(byte):
        temp_value = 0
        for i in range(8):
            temp_value += byte[i] * 2 ** i
        return temp_value

    @staticmethod
    def logPut(string):
        AudioImageProcessing.log.append(string)
        
    @staticmethod
    def logGet():
        return AudioImageProcessing.log
    @staticmethod
    def logClear():
        AudioImageProcessing.log = []

###########################################################\

audio_path = 'private_investigations.wav'
output_path = 'MODIFIED.wav'
image_path = 'pig_photo.jpg'

if __name__ == '__main__':
    try:
       AudioImageProcessing.encodeImageInSoundWithWriting(audio_path, image_path, output_path, 'L+R', 4)
       AudioImageProcessing.decodeImageFromAudio(output_path, 'decoded_image.jpg', 'L+R', 4)
    except Exception as exc:
        AudioImageProcessing.logPut('EXCEPTION')
        traceback.print_exc()
