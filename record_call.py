import os
import datetime

class OutputVideo:
    def __init__(self, logger, filename, dimentions):
        print(dimentions)
        self.logger = logger
        self.filename = filename + "_" + str(datetime.datetime.now().isoformat()).replace(".", "_").replace(":","-")
        self.offset_x = 0
        self.offset_y = 0
        self.width = dimentions[2]
        self.height = dimentions[3]
        self.audio_device = "Microphone (USB Audio CODEC )"
        self.compressor = "-af acompressor=threshold=0.089:ratio=9:attack=200:release=1000"

    def WriteVideo(self):
        os.system(f"""ffmpeg -f gdigrab -framerate 20 -offset_x {self.offset_x} -offset_y {self.offset_y} -video_size {self.width}x{self.height} -thread_queue_size 1024 -i desktop -f dshow -i audio="{self.audio_device}" {self.compressor} -c:v hevc_amf -qp 0 -c:a aac -strict -2 -ac 2 -b:a 128k -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" {self.filename}.mkv""")
