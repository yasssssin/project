class Championnat:
    def __init__(self, clubs):
        self.clubs = clubs
        self.matches = []

    def create_matches(self):

        for i in range(len(self.clubs)):
            for j in range(i + 1, len(self.clubs)):
                match1 = Match(self.clubs[i], self.clubs[j])
                match2 = Match(self.clubs[j], self.clubs[i])
                self.matches.append(match1)
                self.matches.append(match2)

    def jouer_matches(self):
        for match in self.matches:
            match.play()

