import unittest
from command1 import Command1, Direction
from UdpReader1 import UdpReader1
from udp_constants import PACKET_SIZE, N_COMMANDS, CHUNK_SIZE

class TestUdpReader1(unittest.TestCase):

    def tearDown(self):
        pass

    def test_create_command_list_from_packet(self):
        # fixtures
        packet = bytearray([0xFF, ord('b'), ord('d'), ord('f'), ord('\0'), ord('f'), 0x7F, ord('f'), 0x5A, ord('f'), 0xB4, ord('f')])

        # EXPECTED
        expected = [
            Command1(255, Direction.backward),
            Command1(100, Direction.forward),
            Command1(0, Direction.forward),
            Command1(127, Direction.forward),
            Command1(90, Direction.forward),  # servo1
            Command1(180, Direction.forward)  # servo2
        ]

        # test
        actual = UdpReader1.create_command_list_from_packet(packet, actual)

        # check
        for i in range(N_COMMANDS):
            self.assertEqual(actual[i].get_pwm(), expected[i].get_pwm())
            self.assertEqual(actual[i].get_direction(), expected[i].get_direction())

    def test_create_command_from_chunk(self):
        # fixtures
        chunk = bytearray([0xFF, ord('b')])

        # EXPECTED
        expected = Command1(255, Direction.backward)

        # test
        actual = UdpReader1.create_command_from_chunk(chunk)

        # check
        self.assertEqual(actual.get_pwm(), expected.get_pwm())
        self.assertEqual(actual.get_direction(), expected.get_direction())

if __name__ == '__main__':
    unittest.main()
