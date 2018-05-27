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
    def encodeImageInSound(audio_channel, image_bytes_list, step, bit_density=1):
        print('min max: ', min(audio_channel), max(audio_channel))
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
                        print('Conversion complete')
                        print('i: ', i)
                        print('cnt_byte: ', cnt_byte)
                        break
                    elif not image_bytes_list[cnt_byte]:      # if there will be empty bytes for two channels encoding
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
        print('END CONVERSION')
        return new_channel


        # TODO: implement methods to get settings from GUI
        #
        # @staticmethod
        # def encodeImageInSoundWithWriting(soundDir, imageDir, channel, bits, output_path):
        #     performEncoding(soundDir, imageDir, channel, bits)
        #
        #
        #
        #     spwav.write(output_path, sample_rateL, new_audio)
        #
        #
        # @staticmethod
        # def performEncoding(soundDir, imageDir, channel, bits):



        # @staticmethod
        # def encodeImageInSound(audio_channel, image_bytes_list, step):
        #     print('min max: ', min(audio_channel), max(audio_channel))
        #     modified_channel = []
        #     rest_start_index = 0
        #     cnt_step = 0
        #     cnt_byte = 0
        #     cnt_bit = 7
        #     for i in range(len(audio_channel)):
        #         cnt_step += 1
        #         if cnt_step == step:
        #             cnt_step = 0
        #             if cnt_bit == -1:
        #                 cnt_bit = 7
        #                 cnt_byte += 1
        #                 if cnt_byte >= len(image_bytes_list) - 1:
        #                     rest_start_index = i
        #                     print('Conversion complete')
        #                     print('i: ', i)
        #                     print('cnt_byte: ', cnt_byte)
        #                     break
        #                 elif not image_bytes_list[cnt_byte]:  # if there will be empty bytes for two channels encoding
        #                     cnt_byte += 1
        #             temp_bit = int(image_bytes_list[cnt_byte][cnt_bit])
        #             if temp_bit:
        #                 modified_value = audio_channel[i] | 1
        #             else:
        #                 modified_value = audio_channel[i] & ~1
        #             modified_channel.append(modified_value)
        #             cnt_bit -= 1
        #     new_channel = np.concatenate((modified_channel, audio_channel[rest_start_index:]))
        #     print('END CONVERSION')
        #     return new_channel


audio_path = 'private_investigations.wav'
output_path = 'MODIFIED.wav'
image_path = 'pig_photo.jpg'

if __name__ == '__main__':
    sample_rateL, data_audioL = AudioImageProcessing.readAudioWave(audio_path, channel=0)
    sample_rateR, data_audioR = AudioImageProcessing.readAudioWave(audio_path, channel=1)

    print('min and max in audio: ', min(data_audioL), max(data_audioR))

    print(len(data_audioL))
    image_bytes_list = AudioImageProcessing.convertImageToBits(image_path)
    print(len(image_bytes_list))
    modified_channel = AudioImageProcessing.encodeImageInSound(data_audioL, image_bytes_list, 1)

    print('min and max in modified: ', min(modified_channel), max(modified_channel))
    new_channels = [[modified_channel[i], data_audioR[i]] for i in range(len(modified_channel))]

    new_audio = np.array(new_channels, dtype=np.int16)
    spwav.write('MODIFIED.wav', sample_rateL, new_audio)


    #print(im)




    #print(bytes_list)
    #print(len(bytes_list))