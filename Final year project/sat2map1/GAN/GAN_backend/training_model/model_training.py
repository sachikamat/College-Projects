from GAN.GAN_backend.preprocess.training_preprocess import load_images
from GAN.GAN_backend.preprocess.define_architecture import define_discriminator, define_generator, define_gan, train
from GAN.GAN_backend.config import dataset_path

def start_training():
    [src_images, tar_images] = load_images(path=dataset_path)
    print('Loaded: ', src_images.shape, tar_images.shape)
    # define input shape based on the loaded dataset
    image_shape = src_images.shape[1:]
    # define the models
    d_model = define_discriminator(image_shape)
    g_model = define_generator(image_shape)
    # define the composite model
    gan_model = define_gan(g_model, d_model, image_shape)

    #Define data
    # load and prepare training images

    data = [src_images, tar_images]
    dataset = preprocess_data(data)
    train_model(d_model=d_model, g_model=g_model, gan_model=gan_model, dataset=dataset)

def preprocess_data(data):
	# load compressed arrays
	# unpack arrays
	X1, X2 = data[0], data[1]
	# scale from [0,255] to [-1,1]
	X1 = (X1 - 127.5) / 127.5
	X2 = (X2 - 127.5) / 127.5
	return [X1, X2]

def train_model(d_model, g_model, gan_model, dataset, n_epochs=10, n_batch=1):
    from datetime import datetime
    start1 = datetime.now()

    train(d_model, g_model, gan_model, dataset, n_epochs=10, n_batch=1)
    #Reports parameters for each batch (total 1096) for each epoch.
    #For 10 epochs we should see 10960

    stop1 = datetime.now()
    #Execution time of the model
    execution_time = stop1-start1
    print("Execution time is: ", execution_time)
