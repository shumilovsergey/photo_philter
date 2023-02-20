from PIL import Image
from PIL import ImageDraw
import glob
from datetime import datetime

def philter(r, g, b):
    rgb = [r, g, b]
    new_rgb = []

    for color in rgb:
        new_color = color
        new_rgb.append(new_color)

    color_max = 0
    count = 0
    for color in new_rgb:
        if color >= color_max:
            color_max = 150 # high threshhold
            count_max = count
        count += 1
       
    color_min = 256
    count = 0
    for color in new_rgb:
        if color <= color_min:
            color_min = 50 #lowthreshhold
            count_min = count
        count += 1
    
    new_rgb = [70,70,70] #midl
    color_max = 200 #high
    color_min = 20 #low
    new_rgb[count_max] = color_max
    new_rgb[count_min] = color_min
    return new_rgb

def conv(filename):
 
    image = Image.open(filename +'.jpg')
    pix = image.load()  
    width = int(image.size[0])
    height = int(image.size[1])

    for y in range(height):
        for x in range(width):
            r = int(pix[x, y][0])
            g = int(pix[x, y][1])
            b = int(pix[x, y][2])

            rgb = philter(r, g, b)                #philter

            r = rgb[0]
            g = rgb[1]
            b = rgb[2]
            draw = ImageDraw.Draw(image)  
            draw.point((x, y),(r, g, b))

    image.save('result/'+ filename + ".jpg")
    return

def main():
    for filename in glob.glob("*.jpg"):

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(filename, "TIME START :", current_time)        

        filename = filename.split('.')
        filename = filename[0]
        conv(filename)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(filename, "TIME FINISH :", current_time)        


if __name__ == '__main__':
    main()