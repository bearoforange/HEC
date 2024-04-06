import json
import time

from event import Event

class TimeGen:
    def __init__(self, written: map):
        self.initial = int(written["initial"])
        minute = written["frequency"]["minute"]
        hour = written["frequency"]["hour"]
        day = written["frequency"]["day"]

        if minute != 0 or hour != 0 or day != 0:
            while time.time() > self.initial:
                self.initial += minute * 60 + hour * 3600 + day * 86400

class State:
    def __init__(self):
        self.upcoming = Event(-1, 1, "Not coming yet.")
        self.latest = Event(-2, 1, "Hadn't happened yet.")

    def UpdateEvents(self, events_file):
        if self.upcoming.time < time.time():
            self.latest = self.upcoming

        with open(events_file, "r") as file:
            raw = json.load(file)

        initial = []
        for index, written in enumerate(raw):
            initial.append(Event(written["ID"], TimeGen(written["time"]).initial, written["message"]))

        for index, planned in enumerate(initial):
            if planned.time < time.time():
                initial.pop(index)

        events = sorted(initial, key=lambda e: e.time)
        self.upcoming = events[0]

    def WriteMissed(self, missed_file): #Make sure the state was already updated after the event was missed.
        with open(missed_file, "a") as file:
            file.write(json.dumps((self.latest.ID, self.latest.time), separators=(',', ':')) + "\n")