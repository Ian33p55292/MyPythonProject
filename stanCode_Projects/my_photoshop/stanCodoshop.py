"""
File: stanCodoshop.py
Name: Ian
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_distance = ((pixel.red - red)**2 + (pixel.green - green)**2 + (pixel.blue - blue)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    total_red = 0
    total_green = 0
    total_blue = 0
    for i in range(len(pixels)):  # pixels: a list of pixels -> len(pixels): total number of pixels
        total_red += pixels[i].red   # add all the pixel's red
        total_green += pixels[i].green
        total_blue += pixels[i].blue
    avg_red = total_red // len(pixels)   # average all the pixel's red
    avg_green = total_green // len(pixels)
    avg_blue = total_blue // len(pixels)
    avg_lst = [avg_red, avg_green, avg_blue]  # store avg_red, avg_green, avg_blue into a list
    return avg_lst


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg_lst = get_average(pixels)  # call the function get_average
    find_best_pixel = []
    for i in range(len(pixels)):
        color_distance = get_pixel_dist(pixels[i], avg_lst[0], avg_lst[1], avg_lst[2])
        find_best_pixel.append(color_distance)  # it stores distances in a list

    for i in range(len(pixels)):  # loop over every pixel
        if find_best_pixel[i] == min(find_best_pixel):   # if the i-th pixel has the smallest distance, that is, the min(find_best_pixel)
            return pixels[i]  # return i-th pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # green_im = SimpleImage.blank(20, 20, 'green')
    # green_pixel = green_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))
    #
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))
    #
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)

    for i in range(width):
        for j in range(height):
            image_pixel_lst = []  # before finding every best pixel at pixel(i,j), we need to reset the list to empty
            for k in images:   # images (List[SimpleImage]): list of images to be processed
                image_pixel = k.get_pixel(i, j)
                image_pixel_lst.append(image_pixel)  # image_pixel_lst: a list of pixels to be compared
            best_pixel = get_best_pixel(image_pixel_lst)
            result_pixel = result.get_pixel(i, j)
            result_pixel.red = best_pixel.red   # replace the result_pixel by best_pixel (red)
            result_pixel.green = best_pixel.green  # replace the result_pixel by best_pixel (green)
            result_pixel.blue = best_pixel.blue   # replace the result_pixel by best_pixel (blue)
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
