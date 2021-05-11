###
### Author: Dillon barr
### Course: CSC 110
### Description: This program takes the users input for a 'greenscreen' image as well as
###              a 'fill' image and then proceeds to determine which pixel from which image to 
###              use and creates a file based on user input that is a combination of the two images.

def get_image_dimensions_string(file_name):
    '''
    Given the file name for a valid PPM file, this function will return the
    image dimensions as a string. For example, if the image stored in the
    file is 150 pixels wide and 100 pixels tall, this function should return
    the string '150 100'.
    file_name: A string. A PPM file name.
    '''
    image_file = open(file_name, 'r')
    image_file.readline()
    return image_file.readline().strip('\n')

def load_image_pixels(file_name):
    ''' Load the pixels from the image saved in the file named file_name.
    The pixels will be stored in a 3d list, and the 3d list will be returned.
    Each list in the outer-most list are the rows of pixels.
    Each list within each row represents and individual pixel.
    Each pixels is representd by a list of three ints, which are the RGB values of that pixel.
    '''
    pixels = []
    image_file = open(file_name, 'r')

    image_file.readline()
    image_file.readline()
    image_file.readline()

    width_height = get_image_dimensions_string(file_name)
    width_height = width_height.split(' ')
    width = int(width_height[0])
    height = int(width_height[1])

    for line in image_file:
        rgb_row = line.split(' ')
        row = []
        for i in range(0, len(rgb_row)-1, 3):
            pixel = [int(rgb_row[i]), int(rgb_row[i+1]), int(rgb_row[i+2])]
            row.append(pixel)
        pixels.append(row)

    return pixels

def compare_pixels(gs_pixel_list, channel, channel_difference, fi_pixel_list):
    '''
    This function takes in the two lists of pixels as and uses for loops to compare the channel
    color pixel to the values of the other pixels multiplied by the channel value. If the channel
    pixel is greater than both the pixel from the fill image is appended to a new_pixels list,
    otherwise the image from the greenscreen image is used.
    '''
    new_pixels = []
    index = 0
    sub_index = 0
    for i in gs_pixel_list:
        for j in i:
            if channel == 'r':
                if j[0] > (j[1] * channel_difference) and j[0] > (j[2] * channel_difference):
                    new_pixels.append(fi_pixel_list[index][sub_index])
                else:
                    new_pixels.append(j)
            elif channel == 'g':
                if j[1] > (j[0] * channel_difference) and j[1] > (j[2] * channel_difference):
                    new_pixels.append(fi_pixel_list[index][sub_index])
                else:
                    new_pixels.append(j)
            elif channel == 'b':
                if j[2] > (j[0] * channel_difference) and j[2] > (j[1] * channel_difference):
                    new_pixels.append(fi_pixel_list[index][sub_index])
                else:
                    new_pixels.append(j)
            sub_index += 1
            if sub_index >= len(i):
                sub_index = 0
        index +=1 
    return new_pixels
    
def save_ppm(out_file, gs_dimesions, new_pixels):
    '''
    This function takes the user chosen output file name as well as the 
    dimensions of one of the images(since they have to be the same to run)
    and the new_pixels list and writes the new image out to a ppm file.
    '''
    counter = 0
    sub_index = 1
    width_height = gs_dimesions.split(' ')
    width = int(width_height[0])
    height = int(width_height[1])
    output_file = open(out_file, 'w')
    output_file.write('P3')
    output_file.write('\n')
    output_file.write(gs_dimesions)
    output_file.write('\n')
    output_file.write('255')
    output_file.write('\n')
    for i in new_pixels:
        for j in i:
            if sub_index == (width * 3):
                output_file.write(str(j))
            else:
                output_file.write(str(j) + ' ')
                sub_index += 1
        counter += 1
        if counter >= width:
            output_file.write('\n')
            sub_index = 1
            counter = 0
    output_file.close()
    print('Output file written. Exiting.')

                
    
        

def main():
    valid_string = ['r', 'g', 'b']
    # Get the 5 input values from the user, as described in the PA specification
    # These input values will be validated later in main
    while True:
        channel = input('Enter color channel\n')
        if channel not in valid_string:
            print('Channel must be r, g, or b. Will exit.')
            break
        channel_difference = float(input('Enter color channel difference\n'))
        if channel_difference < 1.0 or channel_difference > 10.0:
            print('Invalid channel difference. Will exit.')
            break
        gs_file = input('Enter greenscreen image file name\n')
        gs_dimesions = get_image_dimensions_string(gs_file)
        fi_file = input('Enter fill image file name\n')
        fi_dimensions = get_image_dimensions_string(fi_file)
        gs_width_height = gs_dimesions.split(' ')
        fi_width_height = fi_dimensions.split(' ')
        if int(gs_width_height[0]) != int(fi_width_height[0]) or int(gs_width_height[1]) != int(fi_width_height[1]):
            print('Images not the same size. Will exit.')
            break
        out_file = input('Enter output file name\n')
        gs_pixel_list = load_image_pixels(gs_file)
        fi_pixel_list = load_image_pixels(fi_file)
        new_pixels = compare_pixels(gs_pixel_list, channel, channel_difference, fi_pixel_list)
        save_ppm(out_file, gs_dimesions, new_pixels)
        break
    
    # Next, Do some valiation of the input values
    # The PA specification tell's you what you need to validate
    
    # If the the input is valid, implement the greenscreen.
    # You should:
    #    * Load in the image data from the two input image files.
    #      Use the provided load_image_pixels functions for this!
    #    * Generate a NEW image based on the two input values,
    #      using the greenscreen algorithm described in the specification
    #    * Save the newly-generated image to a file
    # You probably will want to create other function(s) that you call from here.

main()
