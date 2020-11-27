from PIL import Image  
import PIL
import qrcode

img = qrcode.make('http://digitalix.pythonanywhere.com/')
im1 = img.save('qr.png')

