from Frontend.Settings import DEFAULT_CIRCLE_SIZE


class Circle:
    def __init__(self, circle_image_manager):
        self.__circle_image_manager = circle_image_manager

    def draw_circles(self, window, x: int, y: int) -> None:
        window.blit(self.__circle_image_manager.circle_image, (x, y))

    def change_size(self, size) -> None:
        self.__circle_image_manager.change_size(size=size)

    @property
    def circle_img(self):
        return self.__circle_image_manager.circle_image
