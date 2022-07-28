from domain.player import Player


class PlayerMapper:
    def __init__(self, data):
        self._set_name(data)
        self._set_date_of_birth(data)
        self._set_nationality(data)
        self._set_position(data)
        self._set_code(data)

    def _set_name(self, data):
        self.name = data['name']

    def _set_date_of_birth(self, data):
        self.date_of_birth = data['dateOfBirth']

    def _set_position(self, data):
        self.position = data['position']

    def _set_nationality(self, data):
        self.nationality = data['nationality']

    def _set_code(self, data):
        self.code = data['id']

    def map_player(self):
        return Player(name=self.name,
                      date_of_birth=self.date_of_birth,
                      nationality=self.nationality,
                      position=self.position,
                      code=self.code)
