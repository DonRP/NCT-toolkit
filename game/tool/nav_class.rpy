init -9 python:
    class Room:
        """Class of a Room"""
        def __init__(self, id, id_location, name='', icon=''):
            self.id = id
            self.id_location = id_location
            self.name = name
            self.icon = icon
        def enter(self):
            return enterRoom(id = self.id)
