from pytube import YouTube
import ffmpeg
import os
import re

current_path = os.getcwd() + os.sep
ffmpeg_path = r"E:\PycharmProjects\Simple_projects\basic\ffmpeg.exe"
URL = "https://www.youtube.com/watch?v=_fYRLklrp_g"


class YouTubeDownloader:
    CURRENT_PATH = os.getcwd()
    FFMPEG_PATH = CURRENT_PATH + os.sep + "ffmpeg.exe"
    TITLE = ""

    def __init__(self, url: str):
        self.url = url
        self.yt = YouTube(url)
        self.files = []

    def get_all_streams(self):
        return self.yt.streams.filter().all()

    def get_audio(self):
        return self.yt.streams.filter(only_audio=True)

    def get_video_adaptive(self):
        return self.yt.streams.filter(only_video=True, adaptive=True)

    def get_itag_video(self, res, mime_type="mp4", fps="30fps"):
        """Return number of stream

        :param str res:
            Resolution of the video.
        :param str mime_type:
            (Optional) Type of video, can be mp4 or webm.
        :param str fps:
            (Optional) Frame per second, can be 30fps or 60fps.
        :return: int or None
        """

        video_list = self.get_video_adaptive().all()
        pattern = mime_type + ".*" + res + ".*" + fps
        for row in video_list:
            match = re.search(pattern, str(row))
            if match:
                return int(re.search("\d+", str(row)).group())
        return None

    def get_stream(self, resolution="1080p", audio_type="webm"):
        audio_stream = self.get_audio().get_audio_only(audio_type)
        video_stream = self.get_video_adaptive().get_by_itag(self.get_itag_video(res=resolution))
        return video_stream, audio_stream

    def save(self, stream_list):
        for s in stream_list:
            s.download(self.CURRENT_PATH)
            file_name = s.title + "." + s.mime_type.split("/")[-1]
            self.files.append(s.title + file_name)
            self.TITLE = s.title

    def concat_files(self):
        input_ffmpeg = []
        for f in self.files:
            input_ffmpeg.append(ffmpeg.input(self.CURRENT_PATH + os.sep + f))
        ffmpeg.concat(input_ffmpeg[0], input_ffmpeg[1], v=1, a=1).output(self.CURRENT_PATH + os.sep + self.TITLE).run(
            cmd=self.FFMPEG_PATH)

    def download(self):
        streams = self.get_stream()
        self.save(streams)
        self.concat_files()

    @staticmethod
    def print_all(func):
        streams_list = func().all()
        for row in streams_list:
            print(row)


you_dow = YouTubeDownloader(URL)
you_dow.download()
