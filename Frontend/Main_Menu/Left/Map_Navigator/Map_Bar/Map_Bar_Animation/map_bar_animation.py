from Frontend.Helper_Files.Animation import SmoothAnimation, EaseOutSuperFastSmoothing
from Frontend.Helper_Files.Transition.target_manager import TargetManager
from .click_animation import ClickAnimation
from .hover_animation import HoverAnimation


class MapBarAnimation:
    __SPEED_PER_FRAME = 0.03

    def __init__(self, map_bar_pos):
        self.__map_bar_pos = map_bar_pos
        self.__target_manager = TargetManager()
        self.__animation_manager = SmoothAnimation(target_manager=self.__target_manager,
                                                   speed_per_frame=self.__SPEED_PER_FRAME,
                                                   smoothing_method=EaseOutSuperFastSmoothing())
        self.__start_manager = AnimationStartManager()
        self.__hover_animation = HoverAnimation(map_bar_pos=map_bar_pos, smooth_animation=self.__animation_manager,
                                                start_manager=self.__start_manager,
                                                target_manager=self.__target_manager)
        self.__click_animation = ClickAnimation(map_bar_pos=map_bar_pos, smooth_animation=self.__animation_manager,
                                                start_manager=self.__start_manager,
                                                target_manager=self.__target_manager)

    def check_for_animation(self, is_chosen, is_hovered):
        if self.__correct_conditions(is_chosen=is_chosen, is_hovered=is_hovered):
            self.__animate_map_bar()

    def __correct_conditions(self, is_chosen, is_hovered):
        if self.__animation_manager.finished_animation:
            self.__start_manager.start_animation = False
        self.__hover_animation.check_if_init_animate(is_chosen=is_chosen, is_hovered=is_hovered)
        self.__click_animation.check_if_init_animate(is_chosen=is_chosen)
        if not self.__start_manager.start_animation:
            return False
        return True

    def __animate_map_bar(self):
        self.__map_bar_pos.set_current_width(width=self.__animation_manager.get_current_value())


class AnimationStartManager:
    start_animation = False
