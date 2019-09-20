import pytest

from Scalpels import GLOBALS
from Scalpels.extractor import FakeExtractor


def test_Extract_SmallJsonFile_ReturnListOfUrls():
    extractor = FakeExtractor()

    actual = extractor.extract(GLOBALS.EXPERT_JSON_LOCATION, 'url')
    expected = ["www.yahoo.com.tw",
                "www.google.com.tw",
                "https://ants.example.com/",
                "http://www.example.org/", ]
    assert actual == expected


@pytest.mark.parametrize("filename", [
    "expert.jon",
    "readme.md",
    "expert.cfg",
])
def test_Extract_InvalidFileExtension_RaiseException(filename):
    extractor = FakeExtractor()

    with pytest.raises(Exception):
        extractor.extract(filename, 'url')