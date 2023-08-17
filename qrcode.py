import pyqrcode
from pyqrcode import QRCode

s = "https://drive.google.com/file/d/1XKR4P5Jk6z6_fw5XDXbr_-Lz7pybm-o7/view?usp=sharing"

qr = pyqrcode.create(s)

qr.svg("mymenu.svg", scale=8)