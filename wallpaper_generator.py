from PIL import Image, ImageDraw, ImageOps

# Super sample and then downscale to reduce jaggy edges.
multiplier = 2

#Wallpaper Parameters
x = 2560 * multiplier
y = 1600 * multiplier

#Colours
colour1 = (38,90,143,0)
colour2 = (197,60,2,0)
colour3 = (255,255,255,0)
background = (53,53,53)

#Load center logo
logo = Image.open("logoSR.png")

#Find center of primary circle
cx = x/4
cy = y/3

#Set initial radius
cr1 = y/4

#calculate line width and circle width
width = cr1/5
cwidth = cr1/8

#Calculate space between lines
spacing = width + cwidth

#Extend x line 1/10 further on both sides to ensure lines fully draw
linebuffer = x/10

#Create initial image
image = Image.new('RGB', (x, y),background)
draw = ImageDraw.Draw(image)

#calculate start and end points from middle line
endy = - linebuffer
endx = cx + (cy-endy)
startx = - linebuffer
starty = cy + (cx-startx)

#draw initial lines
draw.line([(startx,starty),(endx,endy)], colour2, width)

#Draw lines offset by spacing
draw.line([(startx,starty-spacing),(endx,endy-spacing)], colour1, width)
draw.line([(startx,starty+spacing),(endx,endy+spacing)], colour3, width)

#Calculate radius for smaller circles
cr2 = cr1 - cwidth
cr3 = cr2 - cwidth
cr4 = cr3 - cwidth

#draw circles
draw.ellipse((cx-cr1, cy-cr1, cx+cr1, cy+cr1), fill=colour1)
draw.ellipse((cx-cr2, cy-cr2, cx+cr2, cy+cr2), fill=colour2)
draw.ellipse((cx-cr3, cy-cr3, cx+cr3, cy+cr3), fill=background)
# draw.ellipse((cx-cr4, cy-cr4, cx+cr4, cy+cr4), fill=background)

#Calculate and resize logo to fit inside center circle using radius of largest circle.
logowidth,logoheight=logo.size
logo = ImageOps.fit(logo, ((cr1+(cwidth)) , (cr1+(cwidth))*logoheight/logowidth), Image.ANTIALIAS)
logowidth,logoheight=logo.size

#Passing logo twice since it indicates a mask that will be used to paste the image. If you pass a image with transparency, then the alpha channel is used as mask.
image.paste(logo, (cx - logowidth/2,cy - logoheight/2), logo)

#Scale image down from multiplier
image = ImageOps.fit(image, (x/multiplier, y/multiplier) , Image.ANTIALIAS)

#Save and output image.
image.save("outputSR.png")