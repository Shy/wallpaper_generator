from PIL import Image, ImageDraw, ImageOps

#Wallpaper Parameters
x = 2560
y = 1600

#Colours
colour1 = (197,60,2,0)
colour2 = (38,90,143,0)
colour3 = (253,238,0,0)
background = (53,53,53)

logo = Image.open("logo.png")

cx = x/4
cy = y/3

width = 50
cr1 = 400
linebuffer = 150

image = Image.new('RGB', (x, y),background)
draw = ImageDraw.Draw(image)

draw.line([(0-linebuffer, ((cy*2) - (2 * width))+linebuffer), (cx+cy,0 - (2* width))], colour1, width)
draw.line([((0)-linebuffer, cy*2+linebuffer), ((cx+cy+linebuffer),0-linebuffer)], colour2, width)
draw.line([(0-linebuffer, ((cy*2) + (2 * width))+linebuffer), (cx+cy+linebuffer , 0 + (2* width)-linebuffer)], colour3, width)

cr2 = cr1 - width
cr3 = cr2 - width
cr4 = cr3 - width

logowidth,logoheight=logo.size
logo = ImageOps.fit(logo, (cr1 , cr1*logoheight/logowidth), Image.ANTIALIAS)
logowidth,logoheight=logo.size

draw.ellipse((cx-cr1, cy-cr1, cx+cr1, cy+cr1), fill=colour1)
draw.ellipse((cx-cr2, cy-cr2, cx+cr2, cy+cr2), fill=colour2)
draw.ellipse((cx-cr3, cy-cr3, cx+cr3, cy+cr3), fill=colour3)
draw.ellipse((cx-cr4, cy-cr4, cx+cr4, cy+cr4), fill=background)

#Passing logo twice since it indicates a mask that will be used to paste the image. If you pass a image with transparency, then the alpha channel is used as mask.
image.paste(logo, (cx - logowidth/2,cy - logoheight/2), logo)

image.save("output.png")