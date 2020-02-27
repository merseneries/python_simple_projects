from pytube import YouTube
import ffmpeg
import os
import re


class YouTubeDownloader:
    """Class that download video from YouTube with given url.
    It downloads video and audio separately and than concatenate
    with help of ffmpeg programs. ffmpeg.exe must be in same directory
    than script.
    """
    CURRENT_PATH = os.getcwd()
    FFMPEG_PATH = CURRENT_PATH + os.sep + "ffmpeg.exe"
    TITLE = ""

    def __init__(self, url: str):
        self.url = url
        self.yt = YouTube(url)
        self.files_path = []

    def get_all_streams(self):
        return self.yt.streams.filter().all()

    def get_audio(self):
        return self.yt.streams.filter(only_audio=True)

    def get_video_adaptive(self):
        return self.yt.streams.filter(only_video=True, adaptive=True)

    def get_itag_video(self, res, mime_type, fps):
        """Return number of stream

        :param str res:
            Resolution of the video.
        :param str mime_type:
            Type of video, can be mp4 or webm.
        :param str fps:
            Frame per second, can be 30fps or 60fps.
        :return: int or None
        """

        video_list = self.get_video_adaptive().all()
        pattern = mime_type + ".*" + res + ".*" + fps
        for row in video_list:
            match = re.search(pattern, str(row))
            if match:
                return int(re.search("\d+", str(row)).group())
        return None

    def get_stream(self, resolution="1080p", video_type="mp4", fps="30fps", audio_type="webm"):
        video_stream = self.get_video_adaptive().get_by_itag(
            self.get_itag_video(res=resolution, mime_type=video_type, fps=fps))
        audio_stream = self.get_audio().get_audio_only(audio_type)
        return video_stream, audio_stream

    def save(self, stream_list):
        if len(stream_list) > 0:
            self.TITLE = stream_list[0].title
            for s in stream_list:
                s.download(self.CURRENT_PATH)
                self.files_path.append(self.CURRENT_PATH + os.sep + s.title + "." + s.mime_type.split("/")[-1])

    def concat_files(self):
        input_ffmpeg = []
        for f in self.files_path:
            input_ffmpeg.append(ffmpeg.input(f))
        ffmpeg.concat(input_ffmpeg[0], input_ffmpeg[1], v=1, a=1).output(
            self.CURRENT_PATH + os.sep + self.TITLE + " video.mp4").run(cmd=self.FFMPEG_PATH)

    def delete_file(self):
        for f in self.files_path:
            if os.path.exists(f):
                os.remove(f)
            else:
                print("The file doesn't exist")

    def download(self, res="1080p"):
        """Download video with given param

        :param str res:
            Video resolution by default 1080p.
        """
        streams = self.get_stream(res)
        self.save(streams)
        self.concat_files()
        self.delete_file()

    @staticmethod
    def print_all(func):
        streams_list = func().all()
        for row in streams_list:
            print(row)


if __name__ == '__main__':
    you_dow = YouTubeDownloader("https://www.youtube.com/watch?v=jLMBLuGJTsA")
    you_dow.download()
