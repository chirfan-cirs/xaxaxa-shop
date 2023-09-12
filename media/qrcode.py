import pyqrcode
from pyqrcode import QRCode

s = "https://cvprospectprint.wordpress.com"
qr = pyqrcode.create(s)

qr.png("CvProspectPrint.png", scale=8)
