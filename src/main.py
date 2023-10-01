import click
from pathlib import Path
from util import split_img_and_non_img, rename_from_img

@click.command()
@click.argument('path')
def main(path: str):
    """
    Input path in windows format ex. C:\\
    Or linux like format if trigger by git bash ex. /c/
    """
    click.echo(f'Input path: {path}')
    target_dir = Path(path)
    if not target_dir.exists():
        click.echo(f'The path: "{path}" doesn\' exist!')
        raise SystemExit(1)

    img_list, non_img_list = split_img_and_non_img(target_dir)
    click.echo(f'img list: {img_list}')
    click.echo(f'non img list: {non_img_list}')
    rename_from_img(img_list, non_img_list)

if __name__ == '__main__':
    main()