from PIL import Image
import numpy as np
import random
import os

def xor_encrypt_decrypt(img_array, key_array):
    return np.bitwise_xor(img_array, key_array)

def generate_key(size):
    return np.random.randint(0, 256, size, dtype=np.uint8)

def process_image(image_path, key_path=None, encrypt=True):
    img = Image.open(image_path)
    img_array = np.array(img)
    
    if encrypt:
        key_array = generate_key(img_array.shape)
        encrypted_array = xor_encrypt_decrypt(img_array, key_array)
        encrypted_img = Image.fromarray(encrypted_array)
        encrypted_img.save('encrypted_image.png')
        return key_array
    else:
        key_array = np.load(key_path)
        decrypted_array = xor_encrypt_decrypt(img_array, key_array)
        decrypted_img = Image.fromarray(decrypted_array)
        decrypted_img.save('decrypted_image.png')
        return None

