from pygame import mouse


class MouseParallaxEffect:
    __PADDING_RATIO = 20

    def __init__(self, background_position):
        self.__background_pos = background_position
        self.__mouse_x, self.__mouse_y = 0, 0

    def __check_if_move_cursor(self, mouse_x, mouse_y):
        if mouse_x == self.__mouse_x and mouse_y == self.__mouse_y:
            return False
        self.__mouse_x = mouse_x
        self.__mouse_y = mouse_y
        return True

    def check_for_mouse_parallax(self, window_size):
        mouse_x, mouse_y = mouse.get_pos()
        window_x, window_y = window_size
        if not self.__check_if_move_cursor(mouse_x, mouse_y):
            return
        self.__background_pos.x = self.__map_value(mouse_coord=mouse_x, window_size=window_x)
        self.__background_pos.y = self.__map_value(mouse_coord=mouse_y, window_size=window_y)

    def __map_value(self, mouse_coord, window_size):
        padding = (window_size // self.__PADDING_RATIO) // 2
        return -((mouse_coord / window_size) * padding) - padding
