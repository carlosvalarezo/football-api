from domain.coach import Coach


class CoachMapper:
    def __init__(self, data):
        self._set_name(data)
        self._set_nationality(data)
        self._set_code(data)

    def _set_name(self, data):
        self.name = data['name']

    def _set_nationality(self, data):
        self.nationality = data['nationality']

    def _set_code(self, data):
        self.code = data['id']

    def map_coach(self):
        return Coach(name=self.name,
                     nationality=self.nationality,
                     code=self.code)
