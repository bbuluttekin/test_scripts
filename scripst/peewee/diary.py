#!/usr/bin/env python3
import datetime
from collections import OrderedDict
import sys

from peewee import *

db = SqliteDatabase("diary.db")


class Entry(Model):
    # content
    content = TextField()
    # timestamp
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Create the database and the table if not exist"""
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the menu"""
    choice = None
    while choice != "q":
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print("{}) {}".format(key, value.__doc__))
        choice = input("Action: ").lower().strip()

        if choice in menu:
            menu[choice]()


def add_entry():
    """Add entry"""
    print("Enter your entry press ctrl+d when finished.")
    data = sys.stdin.read().strip()

    if data:
        if input("Save entry? [Yn]").lower() != 'n':
            Entry.create(connect=data)
            print("Saved successfully!")


def view_entries(search_query=None):
    """View previous entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))

    for entry in entries:
        timestamp = entry.timestamp.strftime("%A %B %d, %Y %I:%M%p")
        print(timestamp)
        print("="*len(timestamp))
        print(entry.content)
        print("N) next entry")
        print("q) return to main menu")

        next_action = input("Action: [Nq]").lower().strip()
        if next_action == "q":
            break


def search_entries():
    """Search entries for a string"""
    view_entries(input("Search query: "))


def delete_entry():
    """Delete an entry"""


menu = OrderedDict([
    ("a", add_entry),
    ("v", view_entries)
    ("s", search_entries)
])

if __name__ == '__main__':
    initialize()
    menu_loop()
