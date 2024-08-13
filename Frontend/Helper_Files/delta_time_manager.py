class DeltaTimeManager:
    def __init__(self, delta_time: float = 0):
        self.__delta_time = delta_time

    def get_value_per_frame(self, value_per_second: int | float) -> int | float:
        return value_per_second * self.__delta_time

    def set_delta_time(self, delta_time: float = 0) -> None:
        self.__delta_time = delta_time
