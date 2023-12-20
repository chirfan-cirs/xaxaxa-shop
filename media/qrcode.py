import pyqrcode
from pyqrcode import QRCode

link = input("Insert the link : ")
qr = pyqrcode.create(link)

qr.png("link.png", scale=8)
