class Team:
    def __init__(self,
                 name: str,
                 team_flag: str,
                 venue,
                 code: str):
        self.name = name
        self.team_flag = team_flag
        self.venue = venue
        self.code = code
        self.coach = None
        self.squad = set()

    def set_squad(self, squad):
        self.squad = squad

    def set_coach(self, coach):
        self.coach = coach
