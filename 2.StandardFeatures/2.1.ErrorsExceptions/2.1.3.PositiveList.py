class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, value):
        if value > 0:
            super().append(value)
        else:
            raise NonPositiveError
