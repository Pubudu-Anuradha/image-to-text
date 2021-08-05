# Braille works using a pattern as shown below

# 1 4     0 0
# 2 5     0 0
# 3 6     0 0
# 7 8     0 0

# or 14253678

# the relevant character can be obtained with \N{BRAILLE PATTERN DOTS-X} :  X should be in ascending order

# Loop used for generating the braille unicode characters

# for i in range(1, 256):
#     string = ("%08d" % (int(format(i, 'b'))))
#     # print(string)
#     re = '\''+string+'\':\'\\N{BRAILLE PATTERN DOTS-'
#     if(string[0] == '1'):
#         re += '1'
#     if(string[2] == '1'):
#         re += '2'
#     if(string[4] == '1'):
#         re += '3'
#     if(string[1] == '1'):
#         re += '4'
#     if(string[3] == '1'):
#         re += '5'
#     if(string[5] == '1'):
#         re += '6'
#     if(string[6] == '1'):
#         re += '7'
#     if(string[7] == '1'):
#         re += '8'
#     print(re, end='}\',\n')

symdict = {
    '00000000': ' ',
    '00000001': '\N{BRAILLE PATTERN DOTS-8}',
    '00000010': '\N{BRAILLE PATTERN DOTS-7}',
    '00000011': '\N{BRAILLE PATTERN DOTS-78}',
    '00000100': '\N{BRAILLE PATTERN DOTS-6}',
    '00000101': '\N{BRAILLE PATTERN DOTS-68}',
    '00000110': '\N{BRAILLE PATTERN DOTS-67}',
    '00000111': '\N{BRAILLE PATTERN DOTS-678}',
    '00001000': '\N{BRAILLE PATTERN DOTS-3}',
    '00001001': '\N{BRAILLE PATTERN DOTS-38}',
    '00001010': '\N{BRAILLE PATTERN DOTS-37}',
    '00001011': '\N{BRAILLE PATTERN DOTS-378}',
    '00001100': '\N{BRAILLE PATTERN DOTS-36}',
    '00001101': '\N{BRAILLE PATTERN DOTS-368}',
    '00001110': '\N{BRAILLE PATTERN DOTS-367}',
    '00001111': '\N{BRAILLE PATTERN DOTS-3678}',
    '00010000': '\N{BRAILLE PATTERN DOTS-5}',
    '00010001': '\N{BRAILLE PATTERN DOTS-58}',
    '00010010': '\N{BRAILLE PATTERN DOTS-57}',
    '00010011': '\N{BRAILLE PATTERN DOTS-578}',
    '00010100': '\N{BRAILLE PATTERN DOTS-56}',
    '00010101': '\N{BRAILLE PATTERN DOTS-568}',
    '00010110': '\N{BRAILLE PATTERN DOTS-567}',
    '00010111': '\N{BRAILLE PATTERN DOTS-5678}',
    '00011000': '\N{BRAILLE PATTERN DOTS-35}',
    '00011001': '\N{BRAILLE PATTERN DOTS-358}',
    '00011010': '\N{BRAILLE PATTERN DOTS-357}',
    '00011011': '\N{BRAILLE PATTERN DOTS-3578}',
    '00011100': '\N{BRAILLE PATTERN DOTS-356}',
    '00011101': '\N{BRAILLE PATTERN DOTS-3568}',
    '00011110': '\N{BRAILLE PATTERN DOTS-3567}',
    '00011111': '\N{BRAILLE PATTERN DOTS-35678}',
    '00100000': '\N{BRAILLE PATTERN DOTS-2}',
    '00100001': '\N{BRAILLE PATTERN DOTS-28}',
    '00100010': '\N{BRAILLE PATTERN DOTS-27}',
    '00100011': '\N{BRAILLE PATTERN DOTS-278}',
    '00100100': '\N{BRAILLE PATTERN DOTS-26}',
    '00100101': '\N{BRAILLE PATTERN DOTS-268}',
    '00100110': '\N{BRAILLE PATTERN DOTS-267}',
    '00100111': '\N{BRAILLE PATTERN DOTS-2678}',
    '00101000': '\N{BRAILLE PATTERN DOTS-23}',
    '00101001': '\N{BRAILLE PATTERN DOTS-238}',
    '00101010': '\N{BRAILLE PATTERN DOTS-237}',
    '00101011': '\N{BRAILLE PATTERN DOTS-2378}',
    '00101100': '\N{BRAILLE PATTERN DOTS-236}',
    '00101101': '\N{BRAILLE PATTERN DOTS-2368}',
    '00101110': '\N{BRAILLE PATTERN DOTS-2367}',
    '00101111': '\N{BRAILLE PATTERN DOTS-23678}',
    '00110000': '\N{BRAILLE PATTERN DOTS-25}',
    '00110001': '\N{BRAILLE PATTERN DOTS-258}',
    '00110010': '\N{BRAILLE PATTERN DOTS-257}',
    '00110011': '\N{BRAILLE PATTERN DOTS-2578}',
    '00110100': '\N{BRAILLE PATTERN DOTS-256}',
    '00110101': '\N{BRAILLE PATTERN DOTS-2568}',
    '00110110': '\N{BRAILLE PATTERN DOTS-2567}',
    '00110111': '\N{BRAILLE PATTERN DOTS-25678}',
    '00111000': '\N{BRAILLE PATTERN DOTS-235}',
    '00111001': '\N{BRAILLE PATTERN DOTS-2358}',
    '00111010': '\N{BRAILLE PATTERN DOTS-2357}',
    '00111011': '\N{BRAILLE PATTERN DOTS-23578}',
    '00111100': '\N{BRAILLE PATTERN DOTS-2356}',
    '00111101': '\N{BRAILLE PATTERN DOTS-23568}',
    '00111110': '\N{BRAILLE PATTERN DOTS-23567}',
    '00111111': '\N{BRAILLE PATTERN DOTS-235678}',
    '01000000': '\N{BRAILLE PATTERN DOTS-4}',
    '01000001': '\N{BRAILLE PATTERN DOTS-48}',
    '01000010': '\N{BRAILLE PATTERN DOTS-47}',
    '01000011': '\N{BRAILLE PATTERN DOTS-478}',
    '01000100': '\N{BRAILLE PATTERN DOTS-46}',
    '01000101': '\N{BRAILLE PATTERN DOTS-468}',
    '01000110': '\N{BRAILLE PATTERN DOTS-467}',
    '01000111': '\N{BRAILLE PATTERN DOTS-4678}',
    '01001000': '\N{BRAILLE PATTERN DOTS-34}',
    '01001001': '\N{BRAILLE PATTERN DOTS-348}',
    '01001010': '\N{BRAILLE PATTERN DOTS-347}',
    '01001011': '\N{BRAILLE PATTERN DOTS-3478}',
    '01001100': '\N{BRAILLE PATTERN DOTS-346}',
    '01001101': '\N{BRAILLE PATTERN DOTS-3468}',
    '01001110': '\N{BRAILLE PATTERN DOTS-3467}',
    '01001111': '\N{BRAILLE PATTERN DOTS-34678}',
    '01010000': '\N{BRAILLE PATTERN DOTS-45}',
    '01010001': '\N{BRAILLE PATTERN DOTS-458}',
    '01010010': '\N{BRAILLE PATTERN DOTS-457}',
    '01010011': '\N{BRAILLE PATTERN DOTS-4578}',
    '01010100': '\N{BRAILLE PATTERN DOTS-456}',
    '01010101': '\N{BRAILLE PATTERN DOTS-4568}',
    '01010110': '\N{BRAILLE PATTERN DOTS-4567}',
    '01010111': '\N{BRAILLE PATTERN DOTS-45678}',
    '01011000': '\N{BRAILLE PATTERN DOTS-345}',
    '01011001': '\N{BRAILLE PATTERN DOTS-3458}',
    '01011010': '\N{BRAILLE PATTERN DOTS-3457}',
    '01011011': '\N{BRAILLE PATTERN DOTS-34578}',
    '01011100': '\N{BRAILLE PATTERN DOTS-3456}',
    '01011101': '\N{BRAILLE PATTERN DOTS-34568}',
    '01011110': '\N{BRAILLE PATTERN DOTS-34567}',
    '01011111': '\N{BRAILLE PATTERN DOTS-345678}',
    '01100000': '\N{BRAILLE PATTERN DOTS-24}',
    '01100001': '\N{BRAILLE PATTERN DOTS-248}',
    '01100010': '\N{BRAILLE PATTERN DOTS-247}',
    '01100011': '\N{BRAILLE PATTERN DOTS-2478}',
    '01100100': '\N{BRAILLE PATTERN DOTS-246}',
    '01100101': '\N{BRAILLE PATTERN DOTS-2468}',
    '01100110': '\N{BRAILLE PATTERN DOTS-2467}',
    '01100111': '\N{BRAILLE PATTERN DOTS-24678}',
    '01101000': '\N{BRAILLE PATTERN DOTS-234}',
    '01101001': '\N{BRAILLE PATTERN DOTS-2348}',
    '01101010': '\N{BRAILLE PATTERN DOTS-2347}',
    '01101011': '\N{BRAILLE PATTERN DOTS-23478}',
    '01101100': '\N{BRAILLE PATTERN DOTS-2346}',
    '01101101': '\N{BRAILLE PATTERN DOTS-23468}',
    '01101110': '\N{BRAILLE PATTERN DOTS-23467}',
    '01101111': '\N{BRAILLE PATTERN DOTS-234678}',
    '01110000': '\N{BRAILLE PATTERN DOTS-245}',
    '01110001': '\N{BRAILLE PATTERN DOTS-2458}',
    '01110010': '\N{BRAILLE PATTERN DOTS-2457}',
    '01110011': '\N{BRAILLE PATTERN DOTS-24578}',
    '01110100': '\N{BRAILLE PATTERN DOTS-2456}',
    '01110101': '\N{BRAILLE PATTERN DOTS-24568}',
    '01110110': '\N{BRAILLE PATTERN DOTS-24567}',
    '01110111': '\N{BRAILLE PATTERN DOTS-245678}',
    '01111000': '\N{BRAILLE PATTERN DOTS-2345}',
    '01111001': '\N{BRAILLE PATTERN DOTS-23458}',
    '01111010': '\N{BRAILLE PATTERN DOTS-23457}',
    '01111011': '\N{BRAILLE PATTERN DOTS-234578}',
    '01111100': '\N{BRAILLE PATTERN DOTS-23456}',
    '01111101': '\N{BRAILLE PATTERN DOTS-234568}',
    '01111110': '\N{BRAILLE PATTERN DOTS-234567}',
    '01111111': '\N{BRAILLE PATTERN DOTS-2345678}',
    '10000000': '\N{BRAILLE PATTERN DOTS-1}',
    '10000001': '\N{BRAILLE PATTERN DOTS-18}',
    '10000010': '\N{BRAILLE PATTERN DOTS-17}',
    '10000011': '\N{BRAILLE PATTERN DOTS-178}',
    '10000100': '\N{BRAILLE PATTERN DOTS-16}',
    '10000101': '\N{BRAILLE PATTERN DOTS-168}',
    '10000110': '\N{BRAILLE PATTERN DOTS-167}',
    '10000111': '\N{BRAILLE PATTERN DOTS-1678}',
    '10001000': '\N{BRAILLE PATTERN DOTS-13}',
    '10001001': '\N{BRAILLE PATTERN DOTS-138}',
    '10001010': '\N{BRAILLE PATTERN DOTS-137}',
    '10001011': '\N{BRAILLE PATTERN DOTS-1378}',
    '10001100': '\N{BRAILLE PATTERN DOTS-136}',
    '10001101': '\N{BRAILLE PATTERN DOTS-1368}',
    '10001110': '\N{BRAILLE PATTERN DOTS-1367}',
    '10001111': '\N{BRAILLE PATTERN DOTS-13678}',
    '10010000': '\N{BRAILLE PATTERN DOTS-15}',
    '10010001': '\N{BRAILLE PATTERN DOTS-158}',
    '10010010': '\N{BRAILLE PATTERN DOTS-157}',
    '10010011': '\N{BRAILLE PATTERN DOTS-1578}',
    '10010100': '\N{BRAILLE PATTERN DOTS-156}',
    '10010101': '\N{BRAILLE PATTERN DOTS-1568}',
    '10010110': '\N{BRAILLE PATTERN DOTS-1567}',
    '10010111': '\N{BRAILLE PATTERN DOTS-15678}',
    '10011000': '\N{BRAILLE PATTERN DOTS-135}',
    '10011001': '\N{BRAILLE PATTERN DOTS-1358}',
    '10011010': '\N{BRAILLE PATTERN DOTS-1357}',
    '10011011': '\N{BRAILLE PATTERN DOTS-13578}',
    '10011100': '\N{BRAILLE PATTERN DOTS-1356}',
    '10011101': '\N{BRAILLE PATTERN DOTS-13568}',
    '10011110': '\N{BRAILLE PATTERN DOTS-13567}',
    '10011111': '\N{BRAILLE PATTERN DOTS-135678}',
    '10100000': '\N{BRAILLE PATTERN DOTS-12}',
    '10100001': '\N{BRAILLE PATTERN DOTS-128}',
    '10100010': '\N{BRAILLE PATTERN DOTS-127}',
    '10100011': '\N{BRAILLE PATTERN DOTS-1278}',
    '10100100': '\N{BRAILLE PATTERN DOTS-126}',
    '10100101': '\N{BRAILLE PATTERN DOTS-1268}',
    '10100110': '\N{BRAILLE PATTERN DOTS-1267}',
    '10100111': '\N{BRAILLE PATTERN DOTS-12678}',
    '10101000': '\N{BRAILLE PATTERN DOTS-123}',
    '10101001': '\N{BRAILLE PATTERN DOTS-1238}',
    '10101010': '\N{BRAILLE PATTERN DOTS-1237}',
    '10101011': '\N{BRAILLE PATTERN DOTS-12378}',
    '10101100': '\N{BRAILLE PATTERN DOTS-1236}',
    '10101101': '\N{BRAILLE PATTERN DOTS-12368}',
    '10101110': '\N{BRAILLE PATTERN DOTS-12367}',
    '10101111': '\N{BRAILLE PATTERN DOTS-123678}',
    '10110000': '\N{BRAILLE PATTERN DOTS-125}',
    '10110001': '\N{BRAILLE PATTERN DOTS-1258}',
    '10110010': '\N{BRAILLE PATTERN DOTS-1257}',
    '10110011': '\N{BRAILLE PATTERN DOTS-12578}',
    '10110100': '\N{BRAILLE PATTERN DOTS-1256}',
    '10110101': '\N{BRAILLE PATTERN DOTS-12568}',
    '10110110': '\N{BRAILLE PATTERN DOTS-12567}',
    '10110111': '\N{BRAILLE PATTERN DOTS-125678}',
    '10111000': '\N{BRAILLE PATTERN DOTS-1235}',
    '10111001': '\N{BRAILLE PATTERN DOTS-12358}',
    '10111010': '\N{BRAILLE PATTERN DOTS-12357}',
    '10111011': '\N{BRAILLE PATTERN DOTS-123578}',
    '10111100': '\N{BRAILLE PATTERN DOTS-12356}',
    '10111101': '\N{BRAILLE PATTERN DOTS-123568}',
    '10111110': '\N{BRAILLE PATTERN DOTS-123567}',
    '10111111': '\N{BRAILLE PATTERN DOTS-1235678}',
    '11000000': '\N{BRAILLE PATTERN DOTS-14}',
    '11000001': '\N{BRAILLE PATTERN DOTS-148}',
    '11000010': '\N{BRAILLE PATTERN DOTS-147}',
    '11000011': '\N{BRAILLE PATTERN DOTS-1478}',
    '11000100': '\N{BRAILLE PATTERN DOTS-146}',
    '11000101': '\N{BRAILLE PATTERN DOTS-1468}',
    '11000110': '\N{BRAILLE PATTERN DOTS-1467}',
    '11000111': '\N{BRAILLE PATTERN DOTS-14678}',
    '11001000': '\N{BRAILLE PATTERN DOTS-134}',
    '11001001': '\N{BRAILLE PATTERN DOTS-1348}',
    '11001010': '\N{BRAILLE PATTERN DOTS-1347}',
    '11001011': '\N{BRAILLE PATTERN DOTS-13478}',
    '11001100': '\N{BRAILLE PATTERN DOTS-1346}',
    '11001101': '\N{BRAILLE PATTERN DOTS-13468}',
    '11001110': '\N{BRAILLE PATTERN DOTS-13467}',
    '11001111': '\N{BRAILLE PATTERN DOTS-134678}',
    '11010000': '\N{BRAILLE PATTERN DOTS-145}',
    '11010001': '\N{BRAILLE PATTERN DOTS-1458}',
    '11010010': '\N{BRAILLE PATTERN DOTS-1457}',
    '11010011': '\N{BRAILLE PATTERN DOTS-14578}',
    '11010100': '\N{BRAILLE PATTERN DOTS-1456}',
    '11010101': '\N{BRAILLE PATTERN DOTS-14568}',
    '11010110': '\N{BRAILLE PATTERN DOTS-14567}',
    '11010111': '\N{BRAILLE PATTERN DOTS-145678}',
    '11011000': '\N{BRAILLE PATTERN DOTS-1345}',
    '11011001': '\N{BRAILLE PATTERN DOTS-13458}',
    '11011010': '\N{BRAILLE PATTERN DOTS-13457}',
    '11011011': '\N{BRAILLE PATTERN DOTS-134578}',
    '11011100': '\N{BRAILLE PATTERN DOTS-13456}',
    '11011101': '\N{BRAILLE PATTERN DOTS-134568}',
    '11011110': '\N{BRAILLE PATTERN DOTS-134567}',
    '11011111': '\N{BRAILLE PATTERN DOTS-1345678}',
    '11100000': '\N{BRAILLE PATTERN DOTS-124}',
    '11100001': '\N{BRAILLE PATTERN DOTS-1248}',
    '11100010': '\N{BRAILLE PATTERN DOTS-1247}',
    '11100011': '\N{BRAILLE PATTERN DOTS-12478}',
    '11100100': '\N{BRAILLE PATTERN DOTS-1246}',
    '11100101': '\N{BRAILLE PATTERN DOTS-12468}',
    '11100110': '\N{BRAILLE PATTERN DOTS-12467}',
    '11100111': '\N{BRAILLE PATTERN DOTS-124678}',
    '11101000': '\N{BRAILLE PATTERN DOTS-1234}',
    '11101001': '\N{BRAILLE PATTERN DOTS-12348}',
    '11101010': '\N{BRAILLE PATTERN DOTS-12347}',
    '11101011': '\N{BRAILLE PATTERN DOTS-123478}',
    '11101100': '\N{BRAILLE PATTERN DOTS-12346}',
    '11101101': '\N{BRAILLE PATTERN DOTS-123468}',
    '11101110': '\N{BRAILLE PATTERN DOTS-123467}',
    '11101111': '\N{BRAILLE PATTERN DOTS-1234678}',
    '11110000': '\N{BRAILLE PATTERN DOTS-1245}',
    '11110001': '\N{BRAILLE PATTERN DOTS-12458}',
    '11110010': '\N{BRAILLE PATTERN DOTS-12457}',
    '11110011': '\N{BRAILLE PATTERN DOTS-124578}',
    '11110100': '\N{BRAILLE PATTERN DOTS-12456}',
    '11110101': '\N{BRAILLE PATTERN DOTS-124568}',
    '11110110': '\N{BRAILLE PATTERN DOTS-124567}',
    '11110111': '\N{BRAILLE PATTERN DOTS-1245678}',
    '11111000': '\N{BRAILLE PATTERN DOTS-12345}',
    '11111001': '\N{BRAILLE PATTERN DOTS-123458}',
    '11111010': '\N{BRAILLE PATTERN DOTS-123457}',
    '11111011': '\N{BRAILLE PATTERN DOTS-1234578}',
    '11111100': '\N{BRAILLE PATTERN DOTS-123456}',
    '11111101': '\N{BRAILLE PATTERN DOTS-1234568}',
    '11111110': '\N{BRAILLE PATTERN DOTS-1234567}',
    '11111111': '\N{BRAILLE PATTERN DOTS-12345678}'
}

if __name__ == "__main__":
    for i in symdict.keys():
        print(symdict[i])
