from PIL import Image, ImageFilter

class ImageEditor():
    def __init__(self,filename):
        self.filename = filename
        self.original = None
        self.changed = list()

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('File not found')
        self.original.show()
    
    def crop(self):
        box = (250,100,600,400)
        cropped = self.original.crop(box)
        self.changed.append(cropped)

        tempFilename = self.filename.split('.')
        newFilename = tempFilename[0]+str(len(self.changed)) + '.jpg'
        cropped.save(newFilename)

myImage = ImageEditor('imageProcess\original.jpg')
myImage.open()
myImage.crop()
for img in myImage.changed:
    img.show()
