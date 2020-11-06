from math import *
from cs1media import *

img = load_picture("D:\\Training\\python-training\\CS101\\images\\test.png")
# w, h = img.size()

#----------------------------------------------------------#
#
# Function skew
#
# Input:
#		img: loaded image
#		direction: vertical or horizontal
#		angle: -89 to 89 degrees
#
# Output:
#		new_img: skewed image
#		print “Wrong input!!!” if inputs are not in range
#
#----------------------------------------------------------#

def skew(img, direction, angle):
	# check if correct direction input
	if direction.lower() != 'vertical' and direction.lower() != 'horizontal':
		print('Wrong Input!!')
		return

	if angle < -89 or angle > 89:
		print('Wrong Input!!')
		return

	if direction.lower() == 'vertical':
		skew_vertical(img, angle)
		return
	
	if direction.lower() == 'horizontal':
		skew_horizontal(img, angle)
		return

def skew_vertical(img, angle):
	w, h = img.size()

	# calculate the amount of skewness (height-wise)
	# use the a (opposite) side formula for right triangle
	angle_radians = radians(abs(angle))
	opp = abs(tan(angle_radians)) * h

	# calculate the factor for skewing the sides durin looping for each pixel
	f = opp / h

	# create a black container canvass for the image
	canvas = create_picture(w + round(opp), h, (0,0,0))

	# determine the starting location of x and y
	starting_y = 0
	increasing = True
	if angle > 0:
		starting_x = opp
		increasing = False
	else:
		starting_x = 0
		increasing = True

	# loop through each pixels of the image
	for y in range(h):
		if increasing:
			starting_x += f
		else:
			starting_x -= f
		for x in range(w):
			# set the pixels
			canvas.set(starting_x + x, starting_y + y, img.get(x, y))

	# display the canvass
	canvas.show()

def skew_horizontal(img, angle):
	pass

direction = input('Direction: ')
angle = int(input('Angle: '))

skew(img, direction, angle)
