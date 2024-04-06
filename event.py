class Event:
    def __init__(self, ID: int, time: int, message: str):
        self.ID = ID
        self.time = time
        self.message = message

    def __str__(self):
        return "Event #{ID}, time: {time}, \"{message}\"".format_map(
            {
                "ID": self.ID,
                "time": self.time,
                "message": self.message
            }
        )