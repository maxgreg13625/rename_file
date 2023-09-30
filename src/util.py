from pathlib import Path

def is_img(file_path: str) -> bool:
    return file_path.endswith('.jpg') or file_path.endswith('.png')

def split_img_and_non_img(path: Path) -> tuple:
    img_list =[]
    non_img_list = []
 
    for entry in path.iterdir():
        if is_img(str(entry)):
            img_list.append(entry)
        else:
            non_img_list.append(entry)

    return img_list, non_img_list