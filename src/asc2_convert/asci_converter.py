"""
This function converts a pillow image to ASCII, which one can plot in console. The conversion happens depending on the
intensity of the pixel (0,1) and how "fat" the ASCII character ist.
"""
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import rescale, resize, downscale_local_mean

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]
# turn vise versa the characters to switch white and black spaces
#ASCII_CHARS = ASCII_CHARS[::-1]


def to_aci(name, scale=1):
    # sample image, cast it to numpy array later
    image = Image.open(name)
    # if you want, turn or flip the image
    # method – Image. :
    # Transpose.FLIP_LEFT_RIGHT, Transpose.FLIP_TOP_BOTTOM, Transpose.ROTATE_90, Transpose.ROTATE_180,
    # Transpose.ROTATE_270, Transpose.TRANSPOSE
    #image = image.transpose(method=Image.Transpose.ROTATE_90)

    # convert to a single intensity value, resize and normalize it to [0,1]
    # original images have too high resolution to be able to see them in console.
    # the scale must be picked for each image
    image = ImageOps.grayscale(image)
    image_numpy = np.asarray(image)

    image_numpy_normalized = resize(image_numpy,
                           (image_numpy.shape[0] // scale, image_numpy.shape[1] // scale),
                           anti_aliasing=False)

    #image_numpy_normalized = image_resized / 255

    image_asci = ""
    thresholds = np.linspace(0, 1, 12)
    width, height = image_numpy_normalized.shape
    # for each pixel map the interval [0,1] to lin-space(0,11) for the index of ASCII
    for x in range(width):
        for y in range(height):
            pixel = image_numpy_normalized[x, y]
            intensity_index = np.digitize(pixel, thresholds) - 1
            character = ASCII_CHARS[intensity_index]
            image_asci += (str(character))
        # add a line breaker at the end of each row
        image_asci += "\n"
    return image_asci


def to_aci_numpy(name, scale):
    # the same as before but the output is a numpy.array of strings
    # just for fun, its actually much difficult to plot this array
    image = Image.open(name)
    image = ImageOps.grayscale(image)
    image_numpy = np.asarray(image)
    image_resized = resize(image_numpy,
                           (image_numpy.shape[0] // scale, image_numpy.shape[1] // scale),
                           anti_aliasing=True)

    image_numpy_normalized = image_resized / 255
    thresholds = np.linspace(0, 1, 12)
    width, height = image_numpy_normalized.shape
    image_asci = np.zeros((width, height), dtype=str)
    for x in range(width):
        for y in range(height):
            pixel = image_numpy_normalized[x, y]
            intensity_index = np.digitize(pixel, thresholds) - 1
            character = ASCII_CHARS[intensity_index]
            image_asci[x, y] = character
    return image_asci


lena = "lena.png"
moon = "moon.jpeg"
cameraman = "cameraman.png"
image = lena
image_asci = to_aci(image, 1)
print(image_asci)

with open("output.txt", "w") as file:
    # Write the long string to the file
    file.write(image_asci)

plt.imshow(Image.open(image))
plt.show()
