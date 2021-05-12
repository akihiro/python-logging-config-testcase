from logging import Formatter as Formatter


class FooBarFormatter(Formatter):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)
