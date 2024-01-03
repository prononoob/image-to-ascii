import cv2
from abc import ABC, abstractmethod


class Calculate:
    # ponizsza metoda liczy proporcje obrazka do  podanego customWidth lub domyslnie do 100
    # imageWidth * ratio = customWidth
    # ratio = customWidth / imageWidth
    @staticmethod
    def pixelRatio(lineWidth: int, imageWidth: int) -> float:
        return lineWidth / imageWidth
    pass



# wzorzec strategii, zeby mozna w latwy sposob zmieniac strategie laczenia pikseli
class PixelMergeStrategy(ABC):
    @abstractmethod
    def merge(self, pixelList: list[int]) -> int:
        pass


class AveragePixelMergeStrategy(PixelMergeStrategy):
    def merge(self, pixelList: list[int]) -> int:
        return int(sum(pixelList) / len(pixelList))


class Shader:
    # chars to tablica 16 znakow w ktorej pierwszy jest najjasniejszy a ostatni najciemniejszy
    # odpowiadaja 16 odcieniom szarosci
    chars = ['`', '_', '>', 'c', 's', 'J', '{', 'I', 'S', '6', 'V', 'U', 'H', '$', 'N', '@']
    pixelMergeStrategy = AveragePixelMergeStrategy()

    @staticmethod
    def createEmptyResult(arrayWidth: int, arrayHeight: int) -> list[list[int]]:
        result = [[] for x in range(arrayHeight)]
        for i in range(len(result)):
            for j in range(arrayWidth):
                result[i].append(0)
        return result
    
    @staticmethod
    def convert(imagePath: str, customWidth: int = 100) -> None:
        image = cv2.imread(imagePath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ratio = Calculate.pixelRatio(customWidth, len(image[0]))
        result = Shader.createEmptyResult(customWidth, int(len(image) * ratio))
        
        tempi = 0
        # petla 'i' i petla 'j' dziela obrazek na segmenty
        for i in range(len(result)):
            tempj = 0
            for j in range(len(result[i])):
                segment = []
                # petla 'x' i petla 'y' pobiera wartosci pikseli z segmentu
                for x in range(int(tempi), int(tempi + len(image) / len(result))):
                    for y in range(int(tempj), int(tempj + len(image[i]) / len(result[i]))):
                        segment.append(image[x][y])
                # ponizej zamieniam segment na jedna liczbe calkowita
                # uzywajac wybranej strategii
                segment = Shader.pixelMergeStrategy.merge(segment)
                segment = segment - segment%16
                result[i][j] = Shader.chars[int(segment / 16)]
                # ponizsze 2 linijki umozliwiaja iteracje po segmentach obrazka podczas
                # zamiany na odcienie szarosci
                tempj += len(image[i]) / len(result[i])
            tempi += len(image) / len(result)
        
        for i in result:
            print(''.join(i))
        
        with open('result.txt', 'w') as file:
            for i in result:
                file.write(''.join([x*2 for x in i]) + '\n')
        
        # [DEBUG print szarego obrazka]
        # cv2.imshow('image', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # [DEBUG print wymiarow tablicy]
        print(len(result), len(result[0]))
        

    @staticmethod
    def setPixelMergeStrategy(self, pixelMergeStrategy: PixelMergeStrategy) -> None:
        pixelMergeStrategy = pixelMergeStrategy


def main():
    # Shader.convert('C:/Users/lolle/Desktop/Whiskas.png')
    Shader.convert('tux-bkg.png')



if __name__ == '__main__':
    main()
