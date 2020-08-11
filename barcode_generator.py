#Author Tony
#Date 28 07 2020

import barcode
from barcode.writer import ImageWriter

def testEan():
    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(u'157131021123', writer=ImageWriter())
    fullname = ean.save('my_ean13_barcode')

if __name__ == '__main__':
    testEan()