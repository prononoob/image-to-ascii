from cv2 import imread


class Calculate:
    '''def width(arrayWidth: int, imageWidth: int) -> int:
        return int(imageWidth / arrayWidth)
    
    def height(arrayHeight: int, imageHeight: int) -> int:
        return int(imageHeight / arrayHeight)'''
    
    def size(imageWidth: int, imageHeight: int) -> list[int]:
        if imageWidth == imageHeight:
            return []
        temp = [imageWidth, imageHeight]
        # ^ o co tu chodzilo ?

        if imageWidth > imageHeight:
            pass



class Shader:
    def __init__(self, imagePath: str):
        self.image = imread(imagePath)
        # ^ type numpy.NDArray
        # na razie 80x80 znakow probujemy
        # self.createEmptyResult(arrayWidth, arrayHeight)
        # int: charWidth, charHeight

        # inny koncept wip
        self.temp = Calculate.size()
        self.charWidth = Calculate.widthPixelsToChar(arrayWidth, len(self.image[0]))
        self.charHeight = Calculate.heightPixelsToChar(arrayHeight, len(self.image))
        # jakos tak ^ ?? 

        # NAPRAWIC TO ^^^

    
    def createEmptyResult(self, arrayWidth, arrayHeight):
        self.result = [[] for x in range(arrayHeight)]
        for i in range(len(self.result)):
            for j in range(arrayWidth):
                self.result[i].append('')


def main():
    s = Shader('C:/Users/lolle/Desktop/Whiskas.png')
    #print(s.result[0])
    '''for i in s.result:
        print(i)'''
    print(s.charHeight, s.charWidth)


if __name__ == '__main__':
    main()
