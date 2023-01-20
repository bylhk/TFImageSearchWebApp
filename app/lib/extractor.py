import numpy as np
from PIL import Image
from tempfile import SpooledTemporaryFile
from tensorflow import expand_dims
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import img_to_array


class Vgg16Extractor:
    def __init__(
        self
    ):
        vgg16 = VGG16(weights='imagenet')
        self.model = Model(
            inputs=vgg16.input, 
            outputs=vgg16.get_layer('fc1').output
        )
    
    def predict(
        self,
        image,
    ):
        if isinstance(image, str) or isinstance(image, SpooledTemporaryFile):
            image = Image.open(image)            
        image = image.resize((224, 224)).convert('RGB')
        x = img_to_array(image)
        x = expand_dims(x, axis=0)
        x = preprocess_input(x)
        y = self.model.predict(x, verbose=0)[0]
        return y/np.linalg.norm(y)
