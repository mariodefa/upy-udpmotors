from machine import Pin, PWM
from udp_constants import N_COMMANDS

pwm_pins = [13, 12, 27, 33, 32, 14, 4, 5]

class Motors1:

    @staticmethod
    def setup1(self):
        self.servo1 = PWM(Pin(18), freq=50)
        self.servo2 = PWM(Pin(19), freq=50)
        for pin in pwm_pins:
            pwm_pin = PWM(Pin(pin))
            pwm_pin.freq(50)
            pwm_pin.duty(0)

        self.servo1.duty(90)
        self.servo2.duty(90)

    @staticmethod
    def apply_motors_commands(self, commands):
        for i in range(N_COMMANDS - 2):
            self.set_motor_pwms(i * 2, commands[i])

        self.servo1.duty(commands[N_COMMANDS-2].get_pwm())
        self.servo2.duty(commands[N_COMMANDS-1].get_pwm())

    @staticmethod
    def set_motor_pwms(self, motor_index, command):
        pwm_value = command.get_pwm()
        direction = command.get_direction()

        if direction == "forward":
            PWM(Pin(pwm_pins[motor_index]), freq=50, duty=pwm_value)
            PWM(Pin(pwm_pins[motor_index + 1]), freq=50, duty=0)
        elif direction == "backward":
            PWM(Pin(pwm_pins[motor_index]), freq=50, duty=0)
            PWM(Pin(pwm_pins[motor_index + 1]), freq=50, duty=pwm_value)

