import pytest
from youtube_downloader import YouTubeDownloader


# Video with 4K resolution, 60fps
@pytest.fixture
def high_youtube():
    return YouTubeDownloader("https://www.youtube.com/watch?v=LXb3EKWsInQ")


# Video with 480p resolution, 30fps
@pytest.fixture
def low_youtube():
    return YouTubeDownloader("https://www.youtube.com/watch?v=HqAblLqkhyc")


def test_methods_return(high_youtube):
    assert high_youtube.get_video_adaptive() is not None
    assert high_youtube.get_all_streams() is not None
    assert high_youtube.get_audio() is not None


@pytest.mark.parametrize(
    "video_params", [("", "", ""), ("123", "456", "789"), ("\w\w", "\w\w", "\w\w"), (".*.*", ".*.*", ".*.*"),
                     ("720", "mp4", "60fps"), ("4320p", "mp4", "60fps"), ("1080p", "web", "30fps"),
                     ("480p", "webm", "30")])
def test_get_itag_video_invalid(high_youtube, video_params):
    assert high_youtube.get_itag_video(*video_params) is None, "Invalid values accepted"


@pytest.mark.parametrize(
    "video_params_high, video_params_low", [(("720p", "mp4", "30fps"), ("144p", "mp4", "30fps")),
                                            (("1080p", "mp4", "60fps"), ("360p", "webm", "30fps")),
                                            (("2160p", "webm", "60fps"), ("480p", "mp4", "30fps"))])
def test_get_itag_video_valid(high_youtube, low_youtube, video_params_high, video_params_low):
    assert high_youtube.get_itag_video(*video_params_high) is not None, "Valid values not accepted"
    assert low_youtube.get_itag_video(*video_params_low) is not None, "Valid values not accepted"


@pytest.mark.parametrize(
    "video_params", [("240p", "mp4", "30fps", "mp4"), ("480p", "webm")]
)
def test_get_stream_low(low_youtube, video_params):
    assert low_youtube.get_stream(*video_params) is not (None, None), "Invalid value accepted"
