from pygame import mouse
from Frontend.Settings import BACKGROUND_PADDING
from .mouse_parallax_smoothing import MouseParallaxSmoothing


class MouseParallaxEffect:
    __PADDING_RATIO = BACKGROUND_PADDING
    __SMOOTHING = False

    def __init__(self, background_position):
        self.__background_pos = background_position
        self.__smoothing = MouseParallaxSmoothing()
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
        moved_cursor = self.__check_if_move_cursor(mouse_x, mouse_y)
        self.__smoothing.check_if_mouse_parallax(moved_cursor=moved_cursor)
        if not moved_cursor:
            return
        self.__background_pos.x = self.__map_value(mouse_coord=mouse_x, window_size=window_x)
        self.__background_pos.y = self.__map_value(mouse_coord=mouse_y, window_size=window_y)

    def __map_value(self, mouse_coord, window_size):
        # Smoothing doesn't work
        smoothing_percentage = self.__smoothing.get_current_percentage if self.__SMOOTHING else 1
        padding = (window_size // self.__PADDING_RATIO) // 2
        return (-((mouse_coord / window_size) * padding) - padding) * smoothing_percentage
