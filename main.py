from PIL import Image
import os

CHAR="`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_PIXEL_VALUE = 255
Z = MAX_PIXEL_VALUE/len(CHAR)

def get_pixel_matrix(path):
    img = Image.open(path)
    pixels = list(img.getdata())
    return [pixels[i: i+img.width]for i in range(0, len(pixels), img.width)]

def get_brightness_matrix(pixel_matrix):
    brightness_matrix=[]
    for i in pixel_matrix:
        brightness_row=[]
        for j in i:
            brightness_row.append(0.2126*j[0] + 0.7152*j[1] + 0.0722*j[2])
        brightness_matrix.append(brightness_row)
    return brightness_matrix

def get_ascii_matrix(brightness_matrix):
    ascii_matrix=[]
    for i in brightness_matrix:
        ascii_row=[]
        for j in i:
            ascii_row.append(CHAR[round(j/Z)-1])
        ascii_matrix.append(ascii_row)
    return ascii_matrix

def print_ascii(ascii_matrix):
    for i in ascii_matrix:
        for j in i:
            print(j*2, end='')
        print()

def main():
    path = input("Enter the path of your file: ")
    assert os.path.exists(path), "I did not find the file at, "+str(path)      
    pixel_matrix = get_pixel_matrix(path)
    brightness_matrix = get_brightness_matrix(pixel_matrix)
    ascii_matrix = get_ascii_matrix(brightness_matrix)
    print_ascii(ascii_matrix)

if __name__=='__main__':
    main()