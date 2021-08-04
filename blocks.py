from PIL import Image
import sys

# a dictionary to store the unicode block characters
symdict = {
    '0001': '\u2597',
    '0010': '\u2596',
    '0100': '\u259D',
    '1000': '\u2598',
    '1100': '\u2580',
    '0011': '\u2584',
    '1010': '\u258C',
    '0110': '\u259E',
    '1001': '\u259A',
    '0101': '\u2590',
    '1110': '\u259B',
    '0111': '\u259F',
    '1011': '\u2599',
    '1101': '\u259C',
    '1111': '\u2588',
    '0000': ' '
}


class converter:
    def __init__(self, IMAGEPATH, deswidth=100):
        """
        initializing Class to open image,
        resize to desired width, #TODO: keep aspect ration
        convert image to blocks 
        """
        self.img = Image.open(IMAGEPATH)
        self.img = self.img.resize([deswidth, deswidth])
        # converting image to black and white.(not desaturating)
        self.img = self.img.convert('1')
        self.data = self.img.getdata()
        self.text = ''
        for i in range(0, self.img.height, 2):
            for j in range(0, self.img.width, 2):
                """converting 4 adjacent points into string pattern compatible with the ones in symdict"""
                l = []
                for k in range(2):
                    offset = self.img.width*(i+k)
                    l.append([self.data[offset+j], self.data[offset+j+1]])
                code = '%d%d%d%d' % (l[0][0]/255, l[0][1] /
                                     255, l[1][0]/255, l[1][1]/255)
                self.text += symdict[code]
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
    width = 250
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
