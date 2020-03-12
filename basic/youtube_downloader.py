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

    def __init__(self, url):
        self._url = url
        self._yt = YouTube(url)
        self.files_path = []

    def get_all_streams(self):
        return self._yt.streams.filter()

    def get_audio(self):
        return self._yt.streams.filter(only_audio=True)

    def get_video_adaptive(self):
        return self._yt.streams.filter(only_video=True, adaptive=True)

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

        def is_input_valid():
            expected_params = [
                ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p"],
                ["mp4", "webm"], ["30fps", "60fps"]
            ]
            for index, value in enumerate((res, mime_type, fps)):
                if value not in expected_params[index]:
                    return False
            return True

        if is_input_valid():
            video_list = self.get_video_adaptive()
            pattern = mime_type + ".*" + res + ".*" + fps
            for row in video_list:
                match = re.search(pattern, str(row))
                if match:
                    return int(re.search(r"\d+", str(row)).group())
        return None

    def get_stream(self, resolution="1080p", video_type="mp4", fps="30fps", audio_type="webm"):
        video_stream = self.get_video_adaptive().get_by_itag(
            self.get_itag_video(res=resolution, mime_type=video_type, fps=fps))
        audio_stream = None if video_type is None else self.get_audio().get_audio_only(audio_type)
        return video_stream, audio_stream

    def save(self, stream_list):
        if len(stream_list) > 0:
            self.TITLE = re.sub(r"[#\\/<>?*\":|]", "", stream_list[0].title)
            for i, s in enumerate(stream_list):
                s.download(self.CURRENT_PATH)
                old_path = self.TITLE + "." + s.mime_type.split("/")[-1]
                dot_index = old_path.rfind(".")
                new_path = old_path[:dot_index] + "_" + str(i) + "." + old_path[dot_index + 1:]
                os.replace(old_path, new_path)
                self.files_path.append(new_path)

    def concat_files(self):
        input_ffmpeg = []
        for f in self.files_path:
            input_ffmpeg.append(ffmpeg.input(f))
        ffmpeg.concat(input_ffmpeg[0], input_ffmpeg[1], v=1, a=1).output(
            self.CURRENT_PATH + os.sep + self.TITLE + ".mp4").run(cmd=self.FFMPEG_PATH)

    def delete_file(self):
        for f in self.files_path:
            if os.path.exists(f):
                os.remove(f)
            else:
                raise Exception("File doesn't exist")

    def download(self, res="1080p", video_type="mp4"):
        """Download video with given param

        :param video_type:
            Video format mp4 or webm.
        :param str res:
            Video resolution by default 1080p.
        """
        streams = self.get_stream(res, video_type)
        self.save(streams)
        self.concat_files()
        self.delete_file()

    @staticmethod
    def print_all(func):
        streams_list = func().all()
        for row in streams_list:
            print(row)


if __name__ == '__main__':
    you_dow = YouTubeDownloader("https://www.youtube.com/watch?v=LXb3EKWsInQ")
    you_dow.download("1440p", "webm")
