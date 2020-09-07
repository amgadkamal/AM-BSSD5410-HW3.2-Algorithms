from PIL import Image,ImageDraw
from SortFunctions import binarySearchSub,selectionSort,mergeSort
import colorsys

def comparePixels(pix1, pix2):
    return pix1[0][0] > pix2[0][0]

def storePixels(im):
    width = int(im.size[0])
    height = int(im.size[1])
    pixel_array=[]
    yiq_pixels = []

    for i in range (width):
        for j in range(height):
            r,g,b = im.getpixel((i,j))
            yiq = colorsys.rgb_to_yiq(r/255,g/255,b/255)
            yiq_pixels.append([yiq,(i,j)])
            pixel_array.append([(r,g,b),(i,j)])

    return (pixel_array,yiq_pixels)


def pixelsToImage(im, pixels):
    outimg = Image.new("RGB",im.size);

    if type (pixels[0][0][0])==float:
        print("yiq")
        yiq_out=[]
        for p in pixels:
            r,g,b = colorsys.yiq_to_rgb(p[0][0],p[0][1],p[0][2])
            r,g,b = int (r*255), int(g*255),int(b*255)
            yiq_out.append((r,g,b))
        outimg.putdata(yiq_out)
    else:
        outimg.putdata([p[0] for p in pixels])
    outimg.show()
    return outimg


def pixelsToPoints(im,pixels):
    for p in pixels:
        if type(p[0][0])==float:
            im.putpixel(p[1],tuple([int(v*255) for v in colorsys.yiq_to_rgb(p[0][0],p[0][1],p[0][2])]))
        else:
           im.putpixel(p[1],p[0])
    im.show()
    #return outimg
def grayScale(im,pixels):
    draw = ImageDraw.Draw(im)
    for px in pixels:
        gray_av = int((px[0][0]+px[0][1]+px[0][2])/3)
        draw.point(px[1],(gray_av,gray_av,gray_av))
def main():
    IMG_NAME = "pie"
    with Image.open(IMG_NAME+'.jpg') as im:
     pixels,yiq_pixels = storePixels(im)

     selectionSort(yiq_pixels,comparePixels)

     sorted_im = pixelsToImage(im,yiq_pixels)
     sorted_im.save('sorted_'+IMG_NAME+'.jpg','JPEG')

     grayScale(im,pixels)

     target = (183/255, 198/255,144/255)
     yiq_target = colorsys.rgb_to_yiq(target[0],target[1],target[2])
     subi = binarySearchSub([r[0][0] for r in yiq_pixels],0,len(yiq_pixels)-1,yiq_target[0])
     print(subi)
     tolerance = int(len(yiq_pixels) / 4)
     pixelsToPoints(im,yiq_pixels[subi:])
     im.show()



     while(True):

          command = input("Type  Q to quit and save, R for revers, T to edit tolerance, C to add r,g,b:")
          if (command == 'Q'):
              im.save('Highlighted' + IMG_NAME + '.jpg', 'JPEG')
          if (command == 'R'):
              pixelsToPoints(im, yiq_pixels[:subi])
              im.show()
          if (command == 'T'):
              subi=subi+tolerance
              im.show()
          if (command == 'C'):
               r=input("Red=")
               g=input("green=")
               b=input("blue=")
               target = (int(r)/ 255, int(g) / 255, int(b)/ 255)
               yiq_target = colorsys.rgb_to_yiq(target[0], target[1], target[2])
               subi = binarySearchSub([r[0][0] for r in yiq_pixels], 0, len(yiq_pixels) - 1, yiq_target[0])
               im.show()


if __name__ == "__main__":
     main()