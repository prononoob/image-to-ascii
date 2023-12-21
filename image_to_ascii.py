from cv2 import imread


class Calculate:
    # Calculate how many pixels to put in one character
    # Max length of one line is 100 characters
    '''@staticmethod
    def ratioTo ???
    ratio = 100/x'''
    pass



class Shader:
    @staticmethod
    def createEmptyResult(arrayWidth: int, arrayHeight: int) -> None:
        result = [[] for x in range(arrayHeight)]
        for i in range(len(result)):
            for j in range(arrayWidth):
                result[i].append('a')
            print(''.join(result[i]))
    
    @staticmethod
    def convert(imagePath: str, customHeight: int = 100) -> None:
        image = imread(imagePath)
        Shader.createEmptyResult(customHeight, customHeight)
    
    @staticmethod
    def setCustomHeight(height: int) -> None:
        customHeight = height


def main():
    Shader.convert('C:/Users/lolle/Desktop/Whiskas.png')



if __name__ == '__main__':
    main()
