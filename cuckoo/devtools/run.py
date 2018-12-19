# -*- coding: utf-8 -*-

import os

import click
from plumbum import ProcessExecutionError
from plumbum.cmd import python

LOCATION = os.path.dirname(os.path.abspath(__file__))

__version__ = '1.0'


def _make_admin_migrations():
    """ make migrations for app """
    cmd = python['manage.py', 'makemigrations']
    cmd.run_fg()


def _make_app_migrations():
    """ Make migrations for survey app """
    cmd = python['manage.py', 'makemigrations', 'survey']
    cmd.run_fg()


def _migrate():
    """ Migrate models """
    cmd = python['manage.py', 'migrate']
    cmd.run_fg()


def _add_superuser():
    """ Add Superuser """
    cmd = python['manage.py', 'createsuperuser']
    cmd.run_fg()


def _loaddata():
    """ Add mock data for testing via json datadump """
    cmd = python[
        'manage.py',
        'loaddata',
        '{0}/data.json'.format(LOCATION)]
    cmd.run_fg()


def success(msg):
    """ output a success message """
    click.secho(msg, fg='green')


def error(msg):
    """ output error message """
    click.secho(msg, fg='red')


class CatchAllExceptions(click.Group):
    """ Wrap click.Groups to catch exceptions """
    def __call__(self, *args, **kwargs):   # noqa: D102
        try:
            return self.main(*args, **kwargs)
        except ProcessExecutionError as exc:
            error(exc.stderr)
            exit()


@click.command(help='Startup')
def startup():
    """ Do all the setup stuff here """
    _make_admin_migrations()
    _make_app_migrations()
    success('Migrations Made')

    _migrate()
    success('Migrations Made')

    _loaddata()
    success('Mock Data Loaded')

    _add_superuser()
    success('Test Superuser Added')


@click.group()
@click.version_option(version=__version__)
def cli():
    pass


cli.add_command(startup)


if __name__ == '__main__':
    cli()
