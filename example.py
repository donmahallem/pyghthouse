'''
This example should give a simple overview on how to use the Pyghthouse.

A generel orientation of what you need:
- Import of pyghthouse
- Creating an instance of Pyghthouse
- start connection
- Sending images with either a given function or set_image(image)
- close connection (not needed but recommend)

More examples can be found in the examples folder.

Note that this skript handles Pyghthouse as a local module compared to
the skripts in examples; These handle Pyghthouse as an installed package.
Check examples/README.md for more informations.
'''

from pyghthouse import Pyghthouse
import pyghthouse.utils as utils
from examples.config import UNAME, TOKEN

# Optional: This condition only executes if run as a skript. 
#           Importing this program won't execute this block.
if __name__ == '__main__':
    
    # Create instance of Pyghthouse and start connection
    username = UNAME
    token = TOKEN
    p = Pyghthouse(username, token)
    p.start()
    
    # the image is a 3 dimensional list, meaning a list with [[[r,g,b]]] entries
    # create a black image
    img = p.empty_image()

    pos_x = 10
    pos_y = 5
    # color entries are in rgb
    color = [100, 124, 24]
    
    # sends the given image
    img[pos_y][pos_x] = color
    p.set_image(img)

    key = input("Enter 'n' for the next image, enter any other key to skip\n")
    if key.upper() == "N":
        # set rgb color with a converted hsv color
        color = utils.from_hsv(0.5, 1.0, 0.7)
        
        # set all pixels to the current color
        for x in range(28):
            for y in range(14):
                img[y][x] = color
        p.set_image(img)
    
    key = input("Enter 'n' for the next image, enter any other key to skip\n")
    if key.upper() == "N":
        color = [255, 255, 255]
        
        # create 3 white lines
        for x in range(28):
            for y in range(3,10,3):
                img[y][x] = color
        p.set_image(img)

    p.close()