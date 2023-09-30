import click
from pathlib import Path

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

    for entry in target_dir.iterdir():
        click.echo(entry)

if __name__ == '__main__':
    main()