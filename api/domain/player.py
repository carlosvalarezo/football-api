class Player:
    def __init__(self,
                 name: str,
                 date_of_birth: str,
                 nationality: str,
                 position: str,
                 code: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.nationality = nationality
        self.position = position
        self.code = code
        self.team = None

    def set_team(self, team):
        self.team = team
