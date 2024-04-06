class OsuManiaParser:
    __OUTPUT_FILE = "parsed_osu_2_file.txt"
    __OSU_FILE = "osu_2.osu"
    __ENCODING = 'utf-8'
    __INTERVAL = 0.05
    __MS_PADDING = 1
    __TIME_INDEX = 4

    def __init__(self):
        self.__parsed_lines_dict = {}

    def parse_osu_mania(self):
        self.__parsed_lines_dict.clear()
        with open(self.__OSU_FILE, 'r', encoding=self.__ENCODING) as file:
            for line in file:
                if line.strip() == "[HitObjects]":
                    break
            for line in file:
                if line.strip() == "":
                    break
                elements = line.strip().split(',')
                lane_number = int(elements[0])
                time = round(float(elements[2]) / 1000, 2)
                note_type = 'S' if int(elements[3]) > 1 else 'O'
                self.__add_parsed_lines(time=time, note_type=note_type, lane_number=lane_number)
        parsed_lines = list(self.__parsed_lines_dict.values())
        filtered_parsed_lines = self.__add_interval(parsed_lines=parsed_lines)
        self.__save_parsed_file(parsed_lines=reversed(filtered_parsed_lines))

    def __add_interval(self, parsed_lines: list):
        new_parsed_lines = []
        current_index = 0
        last_time = self.__get_time(parsed_line=parsed_lines[-1])
        for ms_time in self.__get_ms_generator(last_time=last_time):
            out_of_index = current_index == len(parsed_lines)
            if out_of_index:
                break
            elif self.__get_time(parsed_line=parsed_lines[current_index]) < ms_time:
                current_line_list = [parsed_lines[current_index][index] for index in range(4)] + [f"{ms_time:.2f}s"]
                current_index += 1
            else:
                current_line_list = [' ' for _ in range(4)] + [f"{ms_time:.2f}s"]
            new_parsed_lines.append(current_line_list)
        return new_parsed_lines

    def __get_time(self, parsed_line: list):
        return float(parsed_line[self.__TIME_INDEX].removesuffix("s"))

    def __get_ms_generator(self, last_time: float):
        current_ms = 0
        while current_ms <= last_time + self.__MS_PADDING:
            yield round(current_ms, 2)
            current_ms += self.__INTERVAL

    def __add_parsed_lines(self, time, lane_number, note_type):
        if time in self.__parsed_lines_dict:
            for index in range(4):
                if lane_number == index * 64:
                    self.__parsed_lines_dict[time][index] = note_type
                    return
        self.__parsed_lines_dict[time] = [note_type if lane_number == i * 64 else ' ' for i in range(4)] + \
                                         [f"{time:.2f}s"]

    def __save_parsed_file(self, parsed_lines):
        with open(self.__OUTPUT_FILE, 'w') as file:
            for line in parsed_lines:
                file.write(str(line) + '\n')


if __name__ == "__main__":
    parser = OsuManiaParser()
    parser.parse_osu_mania()
