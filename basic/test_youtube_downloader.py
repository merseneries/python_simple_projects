import pytest
from youtube_downloader import YouTubeDownloader


# Video with 2K resolution
@pytest.fixture
def high_you_tube():
    return YouTubeDownloader("https://www.youtube.com/watch?v=LXb3EKWsInQ")


# Video with 240p resolution
@pytest.fixture
def low_you_tube():
    return YouTubeDownloader("https://www.youtube.com/watch?v=1w4zhAtBl3k")


def test_methods_return(high_you_tube):
    assert high_you_tube.get_video_adaptive() is not None
    assert high_you_tube.get_all_streams() is not None
    assert high_you_tube.get_audio() is not None


def test_get_stream_low(low_you_tube):
    assert low_you_tube.get_stream("240p", audio_type="mp4") is not None