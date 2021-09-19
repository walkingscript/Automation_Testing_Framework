import base64
import os
import re

import requests
from PIL import Image

from framework import config


class ImageUtils:
    ALLOWED_IMAGE_EXTENSIONS = ('png', 'jpg', 'gif')

    @staticmethod
    def compare_images(path_1: str, path_2: str) -> bool:
        with Image.open(path_1) as im1, Image.open(path_2) as im2:
            return im1 == im2

    @classmethod
    def download_image(cls, src_link: str, save_dir: str = '') -> str:
        response = requests.get(src_link)
        filename = re.search(rf'\w+\.({"|".join(cls.ALLOWED_IMAGE_EXTENSIONS)})', src_link, re.IGNORECASE).group()
        if not save_dir:
            save_dir = config.DOWNLOADS_DIR
        path_to_save = os.path.join(save_dir, filename)
        with open(path_to_save, 'wb') as file:
            file.write(response.content)
        return path_to_save

    @staticmethod
    def encode_image_in_base64(file_path):
        with open(file_path, 'rb') as image:
            data = base64.b64encode(image.read())
        return data

    @staticmethod
    def save_image_from_base64(base64_data: str, save_dir: str, filename_for_save: str):
        final_path = os.path.join(save_dir, filename_for_save)
        b64string = base64_data.split(',')[-1]
        binary_data = base64.b64decode(b64string)
        with open(final_path, 'wb') as file:
            file.write(binary_data)
        return final_path


__all__ = ['ImageUtils']
