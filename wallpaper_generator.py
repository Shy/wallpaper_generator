from PIL import Image, ImageDraw, ImageOps

# Super sample and then downscale to reduce jaggy edges.
multiplier = 2

#Wallpaper Parameters
x = 2560 * multiplier
y = 1600 * multiplier

#Colours
colour2 = (197,60,2,0)
colour1 = (38,90,143,0)
colour3 = (255,255,255,0)
background = (53,53,53)

logo = Image.open("logoSR.png")

cx = x/4
cy = y/3


cr1 = 450 * multiplier
width = cr1/5
cwidth = cr1/8

linebuffer = 250 * multiplier
spacing = width + (55 * multiplier)

image = Image.new('RGB', (x, y),background)
draw = ImageDraw.Draw(image)

endy = - linebuffer
endx = cx + (cy-endy)

startx = - linebuffer
starty = cy + (cx-startx)

draw.line([(startx,starty-spacing),(endx,endy-spacing)], colour1, width)
draw.line([(startx,starty),(endx,endy)], colour2, width)
draw.line([(startx,starty+spacing),(endx,endy+spacing)], colour3, width)

cr2 = cr1 - cwidth
cr3 = cr2 - cwidth
cr4 = cr3 - cwidth

logowidth,logoheight=logo.size
logo = ImageOps.fit(logo, ((cr1+50) , (cr1+50)*logoheight/logowidth), Image.ANTIALIAS)
logowidth,logoheight=logo.size

draw.ellipse((cx-cr1, cy-cr1, cx+cr1, cy+cr1), fill=colour1)
draw.ellipse((cx-cr2, cy-cr2, cx+cr2, cy+cr2), fill=colour2)
draw.ellipse((cx-cr3, cy-cr3, cx+cr3, cy+cr3), fill=background)
# draw.ellipse((cx-cr4, cy-cr4, cx+cr4, cy+cr4), fill=background)

#Passing logo twice since it indicates a mask that will be used to paste the image. If you pass a image with transparency, then the alpha channel is used as mask.
image.paste(logo, (cx - logowidth/2,cy - logoheight/2), logo)

image = ImageOps.fit(image, (x/multiplier, y/multiplier) , Image.ANTIALIAS)

image.save("outputSR.png")