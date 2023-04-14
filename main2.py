class Club:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.points = 0
        self.goals_scored = 0

    def add_player(self, player):
        self.players.append(player)

    def update_points(self, points):
        self.points += points

    def update_goals_scored(self, goals):
        self.goals_scored += goals

    # Accesseurs
    def get_name(self):
        return self.name

    def get_players(self):
        return self.players

    def get_points(self):
        return self.points

    def get_goals_scored(self):
        return self.goals_scored


class Player:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.goals = 0

    def update_goals(self, goals):
        self.goals += goals

    # Accesseurs
    def get_name(self):
        return self.name

    def get_rating(self):
        return self.rating

    def get_goals(self):
        return self.goals


class Match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_goals = 0
        self.away_goals = 0

    def play(self):
        # Simulate the match by generating random goals for each team
        import random
        self.home_goals = random.randint(0, 5)
        self.away_goals = random.randint(0, 5)

        # Update club and player statistics
        self.home_team.update_goals_scored(self.home_goals)
        self.away_team.update_goals_scored(self.away_goals)

        if self.home_goals > self.away_goals:
            self.home_team.update_points(3)
        elif self.home_goals == self.away_goals:
            self.home_team.update_points(1)
            self.away_team.update_points(1)
        else:
            self.away_team.update_points(3)

        for player in self.home_team.get_players():
            player.update_goals(self.home_goals)

        for player in self.away_team.get_players():
            player.update_goals(self.away_goals)

        # Verify that the winning team has scored more goals
        assert self.home_goals > self.away_goals or self.home_goals == self.away_goals, "Error: Winning team must have scored more goals"

    # Accesseurs
    def get_home_team(self):
        return self.home_team

    def get_away_team(self):
        return self.away_team

    def get_home_goals(self):
        return self.home_goals

    def get_away_goals(self):
        return self.away_goals


class Championnat:
    def __init__(self, clubs):
        self.clubs = clubs
        self.matches = []

    def create_matches(self):
        # Create matches for each club against all other clubs
        for i in range(len(self.clubs)):
            for j in range(i + 1, len(self.clubs)):
                match1 = Match(self.clubs[i], self.clubs[j])
                match2 = Match(self.clubs[j], self.clubs[i])
                self.matches.append(match1)
                self.matches.append(match2)

    def play_matches(self):
        # Play all matches in the championship
        for match in self.matches:
            match.play()

    # Vérifier que le nombre de points distribués lors d'une journée est compris entre 2 et 3 fois le nombre de match