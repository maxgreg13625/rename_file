from src.util import *
from pathlib import Path

def test_is_img():
    assert is_img('/c/test.jpg')
    assert not is_img('/d/test.txt')

def test_split_img_and_non_img(mocker):
    iter_dir_mocker = mocker.patch('pathlib.Path.iterdir')
    iter_dir_mocker.return_value = [Path('/c/test.jpg'), Path('/c/test.txt')]
    # act
    result_img_list, result_non_img_list = split_img_and_non_img(Path('/c/'))
    # assert
    assert len(result_img_list) == 1 and len(result_non_img_list) == 1