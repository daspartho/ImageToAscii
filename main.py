from PIL import Image
import os
import argparse

CHAR="`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_PIXEL_VALUE = 255

def get_pixel_matrix(path):
    og_img = Image.open(path)
    img = og_img.resize((315, 170))
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

def normalize_brightness_matrix(brightness_matrix):
    normalized_brightness_matrix=[]
    max_pixel = max(map(max, brightness_matrix))
    min_pixel = min(map(min, brightness_matrix))
    for i in brightness_matrix:
        normalized_brightness_row=[]
        for j in i:
            normalized_brightness_row.append(((j-min_pixel)/(max_pixel-min_pixel))*MAX_PIXEL_VALUE)
        normalized_brightness_matrix.append(normalized_brightness_row)
    return normalized_brightness_matrix

def get_ascii_matrix(brightness_matrix):
    ascii_matrix=[]
    for i in brightness_matrix:
        ascii_row=[]
        for j in i:
            ascii_row.append(CHAR[int((j/MAX_PIXEL_VALUE) * len(CHAR)) - 1])
        ascii_matrix.append(ascii_row)
    return ascii_matrix

def print_ascii(ascii_matrix):
    for i in ascii_matrix:
        for j in i:
            print(j*2, end='')
        print()

def get_path():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='image file path?')
    arg = parser.parse_args()
    return arg.path

def main(): 
    path = get_path()
    assert os.path.exists(path), "I did not find the file at, "+str(path)
    pixel_matrix = get_pixel_matrix(path)
    brightness_matrix = get_brightness_matrix(pixel_matrix)
    normalized_brightness_matrix= normalize_brightness_matrix(brightness_matrix)
    ascii_matrix = get_ascii_matrix(normalized_brightness_matrix)
    print_ascii(ascii_matrix)

if __name__=='__main__':
    main()
