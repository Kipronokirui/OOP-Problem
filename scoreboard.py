#Python Object Oriented Programming
class Participant:
    def __init__(self, name, chickenwings, hamburgers, hotdogs):
        self.name = name
        self.chickenwings = chickenwings
        self.hamburgers = hamburgers
        self.hotdogs = hotdogs

    @property
    def score(self):
        return (self.chickenwings * 5) + (self.hamburgers * 3) + (self.hotdogs * 2)

def create_scoreboard(participants):
    scoreboard = []
    for participant in participants:
        scoreboard.append({"name": participant.name, "score": participant.score})

    # Sort the scoreboard by score first, and then by name alphabetically if scores are equal
    scoreboard.sort(key=lambda x: (-x['score'], x['name']))

    return scoreboard
