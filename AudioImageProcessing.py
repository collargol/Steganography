import traceback
import numpy as np
import cv2
from scipy.io import wavfile as spwav


class AudioImageProcessing:

    @staticmethod
    def readAudioWave(path, channel=0):
        file_audio = spwav.read(path)
        sample_rate = file_audio[0]
        #print(file_audio)
        try:
            tp = type(file_audio[1][0])
            if not (tp == np.int16 or tp == np.int32 or tp == np.uint8 or tp == np.float32):
                data_audio = file_audio[1][:, channel]
            else:
                data_audio = file_audio[1]
        except TypeError:
            print('Error when extracting raw data - check number of file\'s channels')
        except IndexError:
            print('Error when reading data')
            data_audio = None
        return [sample_rate, data_audio]

    @staticmethod
    def readImage(path):
        file_image = cv2.imread(path)

        return file_image

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
                    if cnt_byte >= len(image_bytes_list) - 1:
                        rest_start_index = i
                        print('Encoding channel partially completed')
                        # print('i: ', i)
                        # print('cnt_byte: ', cnt_byte)
                        break
                    if not image_bytes_list[cnt_byte]:   # if there will be empty bytes for two channels encoding
                        print('IN IF')
                        cnt_byte += 1

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
            print('Encoding channel completed')
        except ValueError as err:
            print('Exception during encoding: ', err)
            pass
        return new_channel

    @staticmethod
    def encodeImageInSoundWithWriting(soundDir, imageDir, outputDir, channel, bits):
        try:
            # reading audio file
            print('Reading audio from ', soundDir, '...')
            if channel == 'L' or channel == 'R' or channel == 'L+R':
                sample_rateL, data_audioL = AudioImageProcessing.readAudioWave(soundDir, channel=0)
                sample_rateR, data_audioR = AudioImageProcessing.readAudioWave(soundDir, channel=1)
            else:
                raise ValueError('Wrong channel value - should be \'L\', \'R\' or \'L+R\'')

            if sample_rateL != sample_rateR:
                raise ValueError('Sample rates from channels differ')
            else:
                sample_rate = sample_rateL

            # readind image
            print('Reading image from ', imageDir, '...')
            image_bytes_list = AudioImageProcessing.convertImageToBits(imageDir)

            # encoding image in audio
            print('Start encoding...')
            if channel == 'L':
                new_channelL = AudioImageProcessing.encodeImageInSound(data_audioL, image_bytes_list, step=1, bit_density=bits)
                new_channelR = data_audioR
            elif channel == 'R':
                new_channelR = AudioImageProcessing.encodeImageInSound(data_audioR, image_bytes_list, step=1, bit_density=bits)
                new_channelL = data_audioL
            elif channel == 'L+R':
                image_bytes_listL = image_bytes_list[:]
                image_bytes_listL = [[] if (i % 2) == 0 else image_bytes_listL[i] for i in range(len(image_bytes_listL))]
                image_bytes_listR = image_bytes_list[:]
                image_bytes_listR = [[] if (i % 2) == 1 else image_bytes_listR[i] for i in range(len(image_bytes_listR))]
                new_channelL = AudioImageProcessing.encodeImageInSound(data_audioL, image_bytes_listL, step=1, bit_density=bits)
                new_channelR = AudioImageProcessing.encodeImageInSound(data_audioR, image_bytes_listR, step=1, bit_density=bits)

            # joining both channels
            print('Writing to ', outputDir, '...')
            new_channels = [[new_channelL[i], new_channelR[i]] for i in range(len(new_channelL))]
            new_audio = np.array(new_channels, dtype=np.int16)

            # writing to new file
            spwav.write(outputDir, sample_rate, new_audio)

        except ValueError as err:
            print('Exception: ', err)
            pass
        except Exception as exc:
            traceback.print_exc()
            pass


audio_path = 'private_investigations.wav'
output_path = 'MODIFIED.wav'
image_path = 'pig_photo.jpg'

if __name__ == '__main__':
    try:
        AudioImageProcessing.encodeImageInSoundWithWriting(audio_path, image_path, output_path, 'L+R', 1)
    except Exception as exc:
        print('EXCEPTION')
        traceback.print_exc()