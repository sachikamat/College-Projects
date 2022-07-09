model_name = "GAN/GAN_backend/model/trained"
model_path = "GAN/GAN_backend/model/"
source_path = 'GAN/GAN_backend/input/'
dataset_path= 'GAN/GAN_backend/dataset/maps/train/'
dest_path = "GAN/GAN_backend/output/"
dest_file = 'GAN/GAN_backend/output/final.jpg'
# dest_file = "final.jpg"
from os import listdir,getcwd, path, remove

def source_image():
    for file in listdir(source_path):
        path = getcwd()+"/GAN/GAN_backend/input/"+file
        return path
#
# def dest_file:
#     for file in listdir(source_path):
#         path_name = getcwd()+"/GAN.GAN_backend/output/"+file
#         return(path_name)
