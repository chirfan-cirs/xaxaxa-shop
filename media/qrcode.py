import pyqrcode
from pyqrcode import QRCode

s = "https://xaxaxafam.wordpress.com/"
qr = pyqrcode.create(s)

qr.png("myweb.png", scale=8)
