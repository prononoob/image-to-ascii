import cv2
from abc import ABC, abstractmethod


class Calculate:
    # Calculate how many pixels to put in one character
    # imageWidth * ratio = customWidth
    # ratio = customWidth / imageWidth
    @staticmethod
    def pixelRatio(lineWidth: int, imageWidth: int) -> float:
        return lineWidth / imageWidth
    pass



class PixelMergeStrategy(ABC):
    @abstractmethod
    def merge(self, pixelList: list[int]) -> int:
        pass


class AveragePixelMergeStrategy(PixelMergeStrategy):
    def merge(self, pixelList: list[int]) -> int:
        return int(sum(pixelList) / len(pixelList))


class Shader:
    chars = ['`', '_', '>', 'c', 's', 'J', '{', 'I', 'S', '6', 'V', 'U', 'H', '$', 'N', '@']
    pixelMergeStrategy = AveragePixelMergeStrategy()

    @staticmethod
    def createEmptyResult(arrayWidth: int, arrayHeight: int) -> list[list[int]]:
        result = [[] for x in range(arrayHeight)]
        for i in range(len(result)):
            for j in range(arrayWidth):
                result[i].append(0)
            # print(''.join(str(result[i])))
        return result
    
    @staticmethod
    def convert(imagePath: str, customWidth: int = 100) -> None:
        image = cv2.imread(imagePath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # for i in range(255):
            # image[i] = i - i%16
        #for i in range(len(image)):
        #    for j in range(len(image[i])):
        #        image[i][j] = image[i][j] - image[i][j]%16

        # DEBUG print
        # cv2.imshow('image', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        # chars in order of brightness
        # chars: `_>csJ{IS6VUH$N@
        # 0 is black, 255 is white

        ratio = Calculate.pixelRatio(customWidth, len(image[0]))
        result = Shader.createEmptyResult(customWidth, int(len(image) * ratio))
        tempi, tempj = 0, 0
        for i in range(len(result)):
            tempj = 0
            for j in range(len(result[i])):
                segment = []
                for x in range(int(tempi), int(tempi + len(image) / len(result))):
                    for y in range(int(tempj), int(tempj + len(image[i]) / len(result[i]))):
                        segment.append(image[x][y])
                segment = Shader.pixelMergeStrategy.merge(segment)
                segment = segment - segment%16
                result[i][j] = Shader.chars[int(segment / 16) - 1]

                # image[i][j] = image[int(tempi)][int(tempj)]
                tempj += len(image[i]) / len(result[i])
                # print(tempi, tempj)
            tempi += len(image) / len(result)
        
        for i in result:
            print(''.join(i))
        
        # DEBUG print
        # cv2.imshow('image', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        print(len(result), len(result[0]))

        # print(int(ratio * len(image)))
        # print(customWidth, int(len(image) * ratio))
        h, w = int(len(image) * ratio), customWidth
        hInterval, wInterval = len(image) / h, len(image[0]) / w
        Shader.createEmptyResult(customWidth, int(len(image) * ratio))
        
    
    @staticmethod
    def setcustomWidth(width: int) -> None:
        customWidth = width

    @staticmethod
    def setPixelMergeStrategy(self, pixelMergeStrategy: PixelMergeStrategy) -> None:
        pixelMergeStrategy = pixelMergeStrategy


def main():
    # Shader.convert('C:/Users/lolle/Desktop/Whiskas.png')
    Shader.convert('tux-bkg.png')



if __name__ == '__main__':
    main()
