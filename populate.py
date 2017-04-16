import click

from graphdb_test.models import graph, User


@click.command()
@click.option('--size', default=50000, help='Number of Users to be created.')
def populate(size):
    """ Workaround to avoid memory error for old computers """
    # pagination number
    max_limit = 50000
    if size < max_limit:
        flash_error = """
        Minimum size allowed is 50000, you can use any value as bellow using:
        `User.populate_with_random_data(min, max)`, e.g (1,100)
        """
        click.echo(flash_error)

    range_min = 1
    range_max = size

    for x in range(int(size/max_limit)):
        val = graph.run(
            "MATCH (n:User) RETURN n.id ORDER BY n.id DESC LIMIT 1").data()[0]
        if val['n.id']:
            click.echo('-> {}!'.format(val['n.id']))
            range_min = val['n.id'] + 1
            range_max += val['n.id']

            User.populate_with_random_data(range_min, range_max)
        click.echo('-> {}!'.format(x))


if __name__ == '__main__':
    populate()
