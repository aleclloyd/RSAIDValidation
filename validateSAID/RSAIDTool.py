from SAIDValidator import isSAIdValid
import click
import json

@click.group()
def cli():
    """South African ID tool"""


@cli.group('id')
def id():
    """Commands for Validating id number"""


@id.command('validate')
@click.option('--id', default=None, help='Validate id (tag id:<number>)')

def validate(id):
    """Validate single id number"""

    # instances = filter_instances(project, force)
    if id:
        print(id)
        idResult = isSAIdValid(id)
        print(idResult)

    return


@id.command('validatebatch')
@click.option('--path', default=None, help='Validate batch of ID numbers (path:<pathtojsonfile>)')
def validate(path):
    """Validate a batch of id numbers in a file"""

    if path:
        try:
            idnumbers = json.loads(open(path).read())
        except IOError as e:
            print("Could not load file {0}".format(path))
            return

        for id in idnumbers:
            idResult = isSAIdValid(id)
            print(idResult)
    else:
        print("No file specified")

    return


if __name__ == '__main__':
    cli()
