from cv2 import imread


class Calculate:
    # Calculate how many pixels to put in one character
    pass



class Shader:
    def __init__(self, imagePath: str):
        self.image = imread(imagePath)
    
    def createEmptyResult(self, arrayWidth, arrayHeight):
        self.result = [[] for x in range(arrayHeight)]
        for i in range(len(self.result)):
            for j in range(arrayWidth):
                self.result[i].append('')


def main():
    s = Shader('C:/Users/lolle/Desktop/Whiskas.png')
    s.createEmptyResult(100, 100)


if __name__ == '__main__':
    main()
