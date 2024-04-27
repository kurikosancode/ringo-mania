from pygame import image, transform
from os import path


class CircleImage:
    __PATH = "Frontend\Mania_Window\Img"

    def __init__(self, size, img="Purp.png"):
        self.__original_circle_image = image.load(path.join(self.__PATH, img)).convert_alpha()
        self.__current_circle_img = transform.scale(self.__original_circle_image, (size, size))

    @property
    def circle_image(self):
        return self.__current_circle_img

    def change_size(self, size) -> None:
        self.__current_circle_img = transform.scale(self.__original_circle_image, (size, size))
