from enum import Enum

class UserRole(Enum):
    DIRECTOR = 'director'
    BAKER =  "baker"
    VENDOR = "vendor"
    CLIENT = 'client'

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)