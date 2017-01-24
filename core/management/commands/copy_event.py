# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

import djclick as click

from core.command_helpers import gather_event_date_from_prompt
from core.models import Event
from core.deploy_event import copy_event


def get_event(id_str):
    try:
        return Event.objects.get(id=int(id_str))
    except (ValueError, Event.DoesNotExist):
        return False


def gather_information():
    click.echo("Hello there sunshine! We're gonna copy an event website now.")

    event = get_event(
        click.prompt(
            "First, give me the ID of the Event object we're gonna copy. "
            "If there is more than one event in this city already, give me "
            "ID of the latest one"
        )
    )

    while not event:
        event = get_event(click.prompt("Wrong ID! Try again"))

    date = gather_event_date_from_prompt()

    return (event, date)


@click.command()
def command():
    """Duplicates Django Girls event with a new date"""

    # Gather data
    (event, date) = gather_information()
    organizers = event.team.all()

    # Print stuff
    click.echo("OK! That's it. Now I'll copy your event.")

    new_event = copy_event(event, date)
    new_event.team = organizers

    click.echo("Website is ready here: http://djangogirls.org/{0}".format(new_event.page_url))
    click.echo("Congrats on yet another event!")
