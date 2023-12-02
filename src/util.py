from pathlib import Path

def is_img(file_path: str) -> bool:
    return file_path.endswith('.jpg') or file_path.endswith('.png')

def split_img_and_non_img(path: Path) -> tuple:
    img_list, non_img_list = [], []
 
    for entry in path.iterdir():
        if is_img(str(entry)):
            img_list.append(entry)
        else:
            non_img_list.append(entry)

    return img_list, non_img_list

def rename_from_img(img_list: list[Path], non_img_list: list[Path]):
    result_list = []

    for img_entry in img_list:
        temp_list = img_entry.stem.split('.')[0].split('-')
        if len(temp_list) == 2:
            for non_img_entry in non_img_list:
                if f'{temp_list[0]}{temp_list[1]}' in non_img_entry.stem or\
                    f'{temp_list[0]}-{temp_list[1]}' in non_img_entry.stem.upper():
                    result_list.append(non_img_entry.replace(
                        Path(f'{non_img_entry.parent}',
                             f'{temp_list[0]}-{temp_list[1]}{non_img_entry.suffix}')))
                    break
    return result_list