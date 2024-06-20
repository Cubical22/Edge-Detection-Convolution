import math

from PIL import Image

convolve_cube = [  # the list used for applying different effects on the image
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1],
]

""" 
    > The default is as follows:
        [
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1],
        ]
    > used for detecting edges
    
    > NOTE: it has to be an square for now.
            if you want to use weird shapes, then, you can use zeros just like this:
        [
            [0,  1, 0],
            [1, -3, 1],
            [0,  1, 0],
        ]
            you can pretty much consider the zeros as "not part of the selection"
            but know that they DO effect the selection area!
            
    > NOTE: not how it's supposed to be done, but, the top left corner is the one being edited
    
    > just simply place your image (as png) and name it "test-image.png", then run the code
    > wait for the process to finish and then view the "output.png" file, being your new image
"""


def calc_convolution(h, w, img):
    # calculating the convolution of the point based on the ones
    # that land towards the right and bellow.
    added = 0

    for i in range(len(convolve_cube)): # going through the array items to calculate the value based on others
        for j in range(len(convolve_cube[0])):
            coordinate = (w + j, h + i) # the coordinate used for the values that effect the main pixel

            pix = img.getpixel(coordinate)

            m = (pix[0] + pix[1] + pix[2]) / 3 # making the image grayscale

            added += convolve_cube[i][j] * m # getting the sum of all calculated values

    return added


if __name__ == '__main__':
    img = Image.open("./../test-image.png") # opening the image
    print("the process started...")

    for h in range(img.height - len(convolve_cube)): # going through the image pixel by pixel up to the edges
        for w in range(img.width - len(convolve_cube[0])):
            added = calc_convolution(h, w, img)
            added = math.floor(added) # turning the added number into <int> since that's the only accepted type

            if added > 0:
                color = (0, 0, added) # the color shall be blue when being positive
            else:
                color = (-added, 0, 0) # and shall be red when being negative

            img.putpixel((w, h), color)

        # printing the process upon improvement
        if h == math.floor(img.height / 4):
            print("25% done...")
        elif h == math.floor(img.height / 2):
            print("50% done...")
        elif h == math.floor(img.height / 4 * 3):
            print("75% done...")
        elif h == img.height:
            print("almost done...")

    img.save("./../output.png") # saving the image
    print("done...!")

    img.close() # closing the stream and image
