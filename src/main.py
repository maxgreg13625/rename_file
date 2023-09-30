import click

@click.command()
@click.argument('path')
def main(path):
    print(path)

if __name__ == '__main__':
    main()