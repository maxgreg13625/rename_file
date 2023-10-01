from src.util import *
from pathlib import Path
from pytest_mock import MockFixture

def test_is_img():
    assert is_img('/c/test.jpg')
    assert not is_img('/d/test.txt')

def test_split_img_and_non_img(mocker: MockFixture):
    iter_dir_mocker = mocker.patch('pathlib.Path.iterdir')
    iter_dir_mocker.return_value = [Path('/c/test.jpg'), Path('/c/test.txt')]
    # act
    result_img_list, result_non_img_list = split_img_and_non_img(Path('/c/'))
    # assert
    assert len(result_img_list) == 1 and len(result_non_img_list) == 1

def test_rename_from_img(mocker: MockFixture):
    replace_mocker = mocker.patch('pathlib.Path.replace')
    replace_mocker.return_value = Path('/c/test-123.txt')
    img_list = [Path('/c/test-123.jpg')]
    non_img_list = [Path('/c/hellOtest123.txt')]
    # act
    result_list = rename_from_img(img_list, non_img_list)
    # assert
    assert result_list[0].stem == 'test-123'