from GAN.GAN_backend.core.main_engine import use_trained_model
import os
import base64
from GAN.GAN_backend.config import source_image, dest_file, dest_path, source_path, model_name, model_path

def main():
    if len(os.listdir(model_path)) == 0:
        from GAN.GAN_backend.training_model.model_training import start_training
        start_training()

    use_trained_model()
    path = dest_file
    # print("This is path "+str(path)  )
    base64 = convert_image_to_base_64(path)
    # print("thsi "+str(base64))
    return(base64)

def convert_image_to_base_64(imagefile):
    with open(imagefile, "rb") as image_file:
        base64string = base64.b64encode(image_file.read())
        return base64string


def cleaner():
    for file in os.listdir(source_path):
        os.remove(str(source_path)+"/"+str(file))
    for file in os.listdir(dest_path):

        os.remove(dest_path+"/"+str(file))
    # for f in os.listdir(dest_path):
    #     os.remove(os.path.join(dest_path, f))
