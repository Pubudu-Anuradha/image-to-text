from braille_generator import symdict
from PIL import Image
import sys


def array_to_braille(l):
    # l will be of the form l = [[0,0],[0,0],[0,0],[0,0]]
    for i in range(len(l)):
        if(l[i] == None):
            l[i] = [0, 0]
    string = "%d%d%d%d%d%d%d%d" % (
        l[0][0], l[0][1], l[1][0], l[1][1], l[2][0], l[2][1], l[3][0], l[3][1]
    )
    return symdict[string]


class converter:
    def __init__(self, IMAGEPATH, deswidth=None):
        """
        initializing Class to open image,
        resize to desired width, #TODO: optimize for smaller pictures
        convert image to braiile 
        """
        self.img = Image.open(IMAGEPATH)
        if(deswidth != None):
            self.img = self.img.resize(
                [deswidth, int(deswidth*self.img.height/self.img.width)])
        # converting image to black and white.(not desaturating)
        self.img = self.img.convert('1')
        self.data = self.img.getdata()
        self.text = ''
        for i in range(0, self.img.height, 4):
            for j in range(0, self.img.width, 2):
                l = []
                offset = i*self.img.width
                for k in range(4):
                    try:
                        l.append([int(self.data[offset+k+j]/255),
                                  int(self.data[offset+k+j+1]/255)])
                    except:
                        print('went over', offset+k+j+1)
                        l.append(None)
                if(len(l) == 4):
                    self.text += array_to_braille(l)
                else:
                    print('unexpected behaviour, please inform the author', len(l))
            self.text += '\n'

    def print(self):
        """method to print the result"""
        print(self.text)

    def print_to_file(self, fname='result.txt'):
        """method to print the result to a file"""
        file = open(fname, 'w')
        file.write(self.text)
        file.close()


if __name__ == "__main__":
    iname = "test1.jpg"
    oname = 'result.txt'
    p = True
    width = None
    if(len(sys.argv) > 1):
        """handling command line arguments
        -i specify input file
        -w specify the width of the result #TODO: keep aspect ratio
        -o specify output file
        -p turn off printing the result to console
        TODO: add option to recognize console dimensions
        """
        i = 1
        while(i < len(sys.argv)):
            if(sys.argv[i] == '-i'):
                # changing input file
                iname = sys.argv[i+1]
                i += 2
            elif(sys.argv[i] == '-w'):
                # changing target width
                width = int(sys.argv[i+1])
                i += 2
            elif(sys.argv[i] == '-o'):
                # changing output file
                oname = sys.argv[i+1]
                i += 2
            elif(sys.argv[i] == '-p'):
                # turning off printing to console
                p = False
                i += 1
            else:
                print(sys.argv[i])
                print("Invalid arguments")
                sys.exit(1)
    pic = converter(iname, width)
    if(p):
        pic.print()
    pic.print_to_file(oname)
