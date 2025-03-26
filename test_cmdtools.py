# test_cmdtools.py
import unittest
import datetime
import sys
import os

# Ensure the parent directory is in the system path (helps Python find cmdtools)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the functions correctly
from cmdtools.core import greet, get_time, get_date, get_inspirational_quote, get_time_greeting


class TestCmdTools(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Alice"), "Nice to meet you, Alice!")

    def test_get_time_format(self):
        time_str = get_time()
        try:
            datetime.datetime.strptime(time_str, "%H:%M:%S")
        except ValueError:
            self.fail("get_time() returned an invalid time format.")

    def test_get_date_format(self):
        date_str = get_date()
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            self.fail("get_date() returned an invalid date format.")

    def test_get_inspirational_quote(self):
        quotes = [
            "Keep going. Everything you need will come to you at the perfect time.",
            "You are stronger than you think.",
            "Stay focused. Stay consistent. Stay strong.",
            "One step at a time is all it takes to get you there.",
            "Discipline is remembering what you want.",
            "The struggle you're in today is developing the strength you need for tomorrow.",
            "Progress, not perfection."
        ]
        quote = get_inspirational_quote()
        self.assertIn(quote, quotes)

    def test_get_time_greeting(self):
        greeting = get_time_greeting()
        self.assertIn(greeting, [
            "Good morning!",
            "Good afternoon!",
            "Good evening!",
            "Good night!"
        ])

if __name__ == "__main__":
    unittest.main()
