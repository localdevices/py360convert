import os
import numpy as np
from PIL import Image
import py360convert

# set path
data = os.path.join(
    "/home/smathermather/Documents/github/Rainbow/Projects/P006_AusNatUni_ODM/exampledata/",
    "629cd3c8-8e33-4cb4-aa04-e1946b722965")

# iterate through files in the directory
for file in os.listdir(data):
    filename = os.path.splitext(file)[0]
    # iterate through images
    if file.endswith('.JPG'):
        input=print((os.path.join(data, file)))

        # Open the input image
        eqimage = np.array(Image.open(os.path.join(data, file)))

        # create cubeimage
        cubeimage = py360convert.e2c(eqimage, face_w=1024, mode='bilinear', cube_format='dice')

        # Now we need to access the faces
        cube_h = py360convert.cube_dice2h(cubeimage)  # the inverse is cube_h2dice
        cube_dict = py360convert.cube_h2dict(cube_h)  # the inverse is cube_dict2h

        imgF = Image.fromarray(cube_dict["F"], 'RGB')
        imgR = Image.fromarray(cube_dict["R"], 'RGB')
        imgB = Image.fromarray(cube_dict["B"], 'RGB')
        imgL = Image.fromarray(cube_dict["L"], 'RGB')
        imgU = Image.fromarray(cube_dict["U"], 'RGB')
        imgD = Image.fromarray(cube_dict["D"], 'RGB')
        imgF.save(os.path.join(data, "F", file))
        imgR.save(os.path.join(data, "R", file))
        imgB.save(os.path.join(data, "B", file))
        imgL.save(os.path.join(data, "L", file))
        imgU.save(os.path.join(data, "U", file))
        imgD.save(os.path.join(data, "D", file))
    else:
        pass

