from enum import Enum


class Status(Enum):
    NEW = 'new'
    CONFIRMED = 'confirmed'
    CANCELLED = 'cancelled'
    SUCCESS = 'success'

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)