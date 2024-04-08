lane_list = [64, 192, 320, 448]


def parse_osu_mania(osu_file):
    parsed_lines = []
    timing_points = {}

    with open(osu_file, 'r', encoding='utf-8') as file:
        parsing_hit_objects = False

        for line in file:
            if line.strip() == "[TimingPoints]":
                for timing_line in file:
                    if timing_line.strip() == "":
                        break
                    offset, mpb = map(float, timing_line.strip().split(",")[:2])
                    timing_points[offset] = mpb

            if line.strip() == "[HitObjects]":
                parsing_hit_objects = True
                continue

            if parsing_hit_objects:
                if line.strip() == "":
                    break
                elements = line.strip().split(',')
                x_pos = int(elements[0])
                time = int(elements[2])
                for offset, mpb in timing_points.items():
                    if offset <= time:
                        time += mpb * (time - offset)
                time_seconds = time / 200000
                note_type = 'S' if int(elements[3]) == 128 else 'O'
                parsed_line = [note_type if x_pos == lane_list[i] else " " for i in range(4)] + [f"{time_seconds:.2f}s"]
                parsed_lines.append(parsed_line)

    return reversed(parsed_lines)


def save_parsed_file(output, parsed_lines):
    with open(output, 'w') as file:
        for line in parsed_lines:
            file.write(str(line) + '\n')


OUTPUT_FILE = "osu_parse_1.txt"
OSU_FILE = "osu.osu"
save_parsed_file(OUTPUT_FILE, parse_osu_mania(OSU_FILE))
