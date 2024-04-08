def parse_osu_mania(osu_file):
    parsed_lines = []
    timing_points = {}  # Dictionary to store timing points

    with open(osu_file, 'r', encoding='utf-8') as file:
        parsing_hit_objects = False

        for line in file:
            if line.strip() == "[TimingPoints]":
                # Start parsing timing points
                for timing_line in file:
                    if timing_line.strip() == "":
                        break  # End of timing points
                    timing_elements = timing_line.strip().split(',')
                    offset = int(timing_elements[0])
                    mpb = float(timing_elements[1])
                    timing_points[offset] = mpb

            if line.strip() == "[HitObjects]":
                parsing_hit_objects = True
                continue  # Move to parsing hit objects

            if parsing_hit_objects:
                if line.strip() == "":
                    break  # End of hit objects
                elements = line.strip().split(',')
                x_pos = int(elements[0])
                time = int(elements[2])
                time_seconds = time / 1000
                note_type = 'S' if int(elements[3]) > 1 else 'O'
                parsed_line = [note_type if x_pos == i * 64 else ' ' for i in range(4)] + [f"{time_seconds:.2f}s"]
                parsed_lines.append(parsed_line)

    return reversed(parsed_lines)


def save_parsed_file(output, parsed_lines):
    with open(output, 'w') as file:
        for line in parsed_lines:
            file.write(str(line) + '\n')


OUTPUT_FILE = "osu_parsed_2.txt"
OSU_FILE = "osu.osu"
save_parsed_file(OUTPUT_FILE, parse_osu_mania(OSU_FILE))
