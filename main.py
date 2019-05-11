import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# https://www.kancloud.cn/thinkphp/python-guide/39205
# https://github.com/Heisenberg0391/TextImageGenerator
# https://juejin.im/post/5a41a654518825258a5fe3f7#heading-5
# https://segmentfault.com/a/1190000017558652
def rndChar():
    return chr(random.randint(65, 90))

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def makeImage():
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))

    #  (字体文件路径，字号)
    font = ImageFont.truetype('./fonts/shusong.ttf', 48)
    draw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    for t in range(8):
        draw.text((30 * t , 8), rndChar(), font=font, fill=rndColor2())
    return  image

# image = image.filter(ImageFilter.BLUR)
for x in range(50):
    image = makeImage()
    name = str(x) + '.jpg'
    path = './OutputImage/' + name
    # name.format(name=x)
    image.save(path, 'jpeg')

