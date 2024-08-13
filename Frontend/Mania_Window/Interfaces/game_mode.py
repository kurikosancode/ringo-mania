from abc import abstractmethod
from Frontend.Helper_Files import WindowInterface, DeltaTimeManager


class GameModeWindow(WindowInterface):
    def __init__(self, *, display, font, music, play_tracker, timer, play_state,
                 delta_time_manager: DeltaTimeManager):
        self._display = display
        self._font = font
        self._music = music
        self._play_tracker = play_tracker
        self._timer = timer
        self._state = play_state
        self._delta_time_manager = delta_time_manager

    @abstractmethod
    def run(self):
        pass
