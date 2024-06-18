from enum import Enum

class Direction(Enum):
    forward = 'f'
    backward = 'b'

class Command1:
    def __init__(self, pwm=0, direction=Direction.forward):
        self.pwm = pwm
        self.direction = direction

    def get_pwm(self):
        return self.pwm

    def get_direction(self):
        return self.direction
