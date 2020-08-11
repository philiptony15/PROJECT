# USAGE
# python barcode_scanner_image.py --image barcode_example.png

# import the necessary packages
from pyzbar import pyzbar
import argparse
import cv2
from PIL import Image, ImageEnhance 

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

# load the input image as greyscale
image = cv2.imread(args["image"],cv2.IMREAD_GRAYSCALE)

#enhancer = ImageEnhance.Contrast(image)
#enhanced_im = enhancer.enhance(4.0)

# brightness adjustments using equalizeHist
image = cv2.equalizeHist(image)


# find the barcodes in the image and decode each of the barcodes
barcodes = pyzbar.decode(image)



# loop over the detected barcodes
for barcode in barcodes:
	# extract the bounding box location of the barcode and draw the
	# bounding box surrounding the barcode on the image
	(x, y, w, h) = barcode.rect
	#cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# the barcode data is a bytes object so if we want to draw it on
	# our output image we need to convert it to a string first
	barcodeData = barcode.data.decode("utf-8")
	barcodeType = barcode.type
	print(barcodeData)

	# draw the barcode data and barcode type on the image
	text = "{} ({})".format(barcodeData, barcodeType)
	cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (0, 0, 255), 2)

# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)

img1 = cv2.imread('product.png')
img2 = cv2.imread('barcode.jpg')

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()