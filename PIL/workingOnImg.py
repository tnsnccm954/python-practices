from PIL import Image


'''
The processing principles should be different. For example, 
the first photo should have a filter applied, and the second should be mirrored.
'''

# filp the image
with Image.open('imageProcess/original.jpg') as img:
    img.show()
    # box = (250,100,600,400)
    flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
    flipped.save('imageProcess/cropped.jpg')
    flipped.show()

with Image.open('imageProcess/original.jpg') as img:
    img.show()
    # box = (250,100,600,400)
    converted = img.convert('L')
    converted.save('imageProcess/cee.jpg')
    converted.show()
