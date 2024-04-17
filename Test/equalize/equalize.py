from pydub import AudioSegment


def equalize_volume(mp3_files, target_volume):
    for mp3_file in mp3_files:
        audio = AudioSegment.from_mp3(f"{mp3_file}.mp3")
        add = abs(audio.dBFS) + target_volume
        adjusted_audio = audio + add
        adjusted_audio.export(f"{mp3_file}_test.mp3", format="mp3")


song_1 = f"song/add_test"
song_2 = f"song/slam_test"
mp3_files = [song_1, song_2]

target_volume = -10

equalize_volume(mp3_files, target_volume)
