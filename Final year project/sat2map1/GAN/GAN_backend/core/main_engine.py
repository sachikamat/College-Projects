#Test trained model on a few images...
from GAN.GAN_backend.config import model_name, source_image, dest_file, model_path
from keras.models import load_model
from keras.preprocessing.image import img_to_array, array_to_img
from numpy.random import randint
from PIL import Image
from numpy import asarray, load
from numpy import vstack
import numpy as np
from matplotlib import pyplot

# plot source, generated and target images
def plot_images(src_img, gen_img):

	images = vstack((src_img, gen_img))
	# scale from [-1,1] to [0,1]
	images = (images + 1) / 2.0
	titles = ['Source', 'Generated']
	# plot images row by row
	for i in range(len(images)):
		# define subplot
		pyplot.subplot(1, 2, 1 + i)
		# turn off axis
		pyplot.axis('off')
		# plot raw pixel data
		pyplot.imshow(images[i])
		# show title
		pyplot.title(titles[i])
	pyplot.show()
	# pyplot.savefig(dest_file)


def save_output(gen_img):
    gen_img= np.reshape(gen_img, (256,256,3))
    # print(gen_img.shape)
    pyplot.axis('off')
    pyplot.imshow(gen_img)
    # print("kujcehdbkhjbvkdg HELLLOOOOOOOOOOOO+_______-------______"+str(gen_img.shape))
    pyplot.savefig(dest_file)


def resolution_handler():
	import os

	img = Image.open(source_image()) # image extension *.png,*.jpg
	img = img.resize((256,256), Image.ANTIALIAS)
	# print("hello this is "+source_image())
	#img.save('name.jpg')
	return img

def use_trained_model():
	import os
	# select random example for prediction
	# load the image
	files = []
	for file in os.listdir(model_path):
		file = model_path+file
		files.append(file)
	used_model = max(files, key=os.path.getmtime)
	model = load_model(used_model)

	try_list= list()
	#try_img = load_img('name.jpg')
	try_img= resolution_handler()
	try_img = img_to_array(try_img)
	try_list.append(try_img)
	final_img = asarray(try_list)
	final_img = (final_img - 127.5) / 127.5
	reverse_img = (final_img * 127.5) + 127
	# generate image from source
	gen_image = model.predict(final_img)
	# plot all three images
	#plot_images(final_img, gen_image)
	save_output(gen_img=gen_image)
	# # im = Image.fromarray(gen_image)
	# #
	# # im.save("sot.jpg")
	# abcd=np.reshape(gen_image, (256,256,3))
	#
	# pil_img = array_to_img(abcd)
	# pil_img.save(dest_file)

	# import scipy.misc
	# scipy.misc.imsave('outfile.jpg', gen_image)
