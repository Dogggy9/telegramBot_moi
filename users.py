
from states import State


class User:
    def __init__(self, id, state: State):
        self.id = id
        self.state = state.name
        self.cached_message = None