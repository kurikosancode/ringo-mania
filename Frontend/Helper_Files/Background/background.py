from .mouse_parallax_effect import MouseParallaxEffect


class Background:
    __OPACITY = 255
    __SCORE_SCREEN_OPACITY = 15
    __PARALLAX = True

    def __init__(self):
        self.__background = None
        self.__background_position = BackgroundPosition()
        self.__mouse_parallax_effect = MouseParallaxEffect(self.__background_position)

    def show_background(self, image, window, window_size):
        self.__background = image
        self.__background.set_alpha(self.__OPACITY)
        self.__show_background(window, window_size)

    def show_background_score_screen(self, image, window, window_size):
        self.__background = image
        self.__background.set_alpha(self.__SCORE_SCREEN_OPACITY)
        self.__show_background(window, window_size)

    def __show_background(self, window, window_size):
        self.__mouse_parallax_effect.check_for_mouse_parallax(window_size=window_size)
        window.blit(self.__background, self.__background_position.background_position)

    @property
    def current_position(self):
        return self.__background_position.background_position

    @property
    def background(self):
        return self.__background


class BackgroundPosition:
    x: int = 0
    y: int = 0

    @property
    def background_position(self):
        return self.x, self.y
