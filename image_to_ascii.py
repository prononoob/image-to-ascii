from cv2 import imread


class Calculate:
    # Calculate how many pixels to put in one character
    # imageWidth * ratio = customWidth
    # ratio = customWidth / imageWidth
    @staticmethod
    def pixelRatio(lineWidth: int, imageWidth: int) -> float:
        return lineWidth / imageWidth
    pass



class Shader:
    @staticmethod
    def createEmptyResult(arrayWidth: int, arrayHeight: int) -> None:
        result = [[] for x in range(arrayHeight)]
        for i in range(len(result)):
            for j in range(arrayWidth):
                result[i].append('a')
            # print(''.join(result[i]))
    
    @staticmethod
    def convert(imagePath: str, customWidth: int = 100) -> None:
        image = imread(imagePath)
        ratio = Calculate.pixelRatio(customWidth, len(image[0]))
        # print(int(ratio * len(image)))
        Shader.createEmptyResult(customWidth, customWidth)
    
    @staticmethod
    def setcustomWidth(wihth: int) -> None:
        customWidth = wihth


def main():
    Shader.convert('C:/Users/lolle/Desktop/Whiskas.png')



if __name__ == '__main__':
    main()
