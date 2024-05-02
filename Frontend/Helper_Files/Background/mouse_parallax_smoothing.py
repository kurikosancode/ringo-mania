from Frontend.Helper_Files.Animation import SmoothAnimation
from Frontend.Helper_Files.Transition import TargetManager
from Backend.Timer import ActivationTimer


class MouseParallaxSmoothing:
    __ANIMATION_SPEED = 0.05
    __TIMER_INTERVAL = 0

    def __init__(self):
        self.__target_manager = TargetManager()
        self.__animation_manager = SmoothAnimation(target_manager=self.__target_manager,
                                                   speed_per_frame=self.__ANIMATION_SPEED)
        self.__activation_timer = ActivationTimer(interval=self.__TIMER_INTERVAL)
        self.__moved_cursor, self.__start_end_parallax = False, False

    def check_if_mouse_parallax(self, moved_cursor):
        self.__mouse_condition(moved_cursor=moved_cursor)
        self.__check_if_end_parallax()

    def __mouse_condition(self, moved_cursor: bool):
        if self.__moved_cursor == moved_cursor:
            return
        if moved_cursor:
            self.__setup_in()
        else:
            self.__setup_out()
        self.__moved_cursor = moved_cursor

    def __check_if_end_parallax(self):
        if not self.__start_end_parallax:
            return
        if self.__animation_manager.finished_animation:
            self.__start_end_parallax = True

    @property
    def get_current_percentage(self):
        return self.__animation_manager.get_current_value()

    def __setup_in(self):
        self.__animation_manager.reset()
        current_value = self.__animation_manager.get_current_value()
        self.__target_manager.setup(current_value=current_value, target_value=1)

    def __setup_out(self):
        self.__animation_manager.reset()
        current_value = self.__animation_manager.get_current_value()
        self.__target_manager.setup(current_value=current_value, target_value=0)
