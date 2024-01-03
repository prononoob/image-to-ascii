import cv2


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
        image = cv2.imread(imagePath)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # for i in range(255):
            # image[i] = i - i%16

        # DEBUG print
        # cv2.imshow('image', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        # chars in order of brightness
        # chars: `_>csJiIS6VUm$N@
        # 0 is black, 255 is white
        chars = ['`', '_', '>', 'c', 's', 'J', 'i', 'I', 'S', '6', 'V', 'U', 'm', '$', 'N', '@']
        

        ratio = Calculate.pixelRatio(customWidth, len(image[0]))
        # print(int(ratio * len(image)))
        print(customWidth, int(len(image) * ratio))
        Shader.createEmptyResult(customWidth, int(len(image) * ratio))
    
    @staticmethod
    def setcustomWidth(width: int) -> None:
        customWidth = width


def main():
    Shader.convert('C:/Users/lolle/Desktop/Whiskas.png')



if __name__ == '__main__':
    main()
