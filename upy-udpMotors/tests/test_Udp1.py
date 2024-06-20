import unittest
from unittest.mock import Mock, patch
from Udp1 import Udp1
from udp_constants import PACKET_SIZE, N_COMMANDS
from UdpReader1 import UdpReader1
from Motors1 import Motors1

class TestUdp1(unittest.TestCase):

    def setUp(self):
        self.mockUDP = Mock()
        self.mockUART = Mock()
        self.mockUdpReader1 = Mock()
        self.mockMotors1 = Mock()
        
        # Patching the global instances in Udp1
        patcher_udp = patch('Udp1.UDP', return_value=self.mockUDP)
        patcher_uart = patch('Udp1.uart', self.mockUART)
        patcher_udpread = patch('UdpReader1.UdpReader1', self.mockUdpReader1)
        patcher_motors = patch('Motors1.Motors1', self.mockMotors1)
        
        self.addCleanup(patcher_udp.stop)
        self.addCleanup(patcher_uart.stop)
        self.addCleanup(patcher_udpread.stop)
        self.addCleanup(patcher_motors.stop)
        
        self.mockUDP = patcher_udp.start()
        self.mockUART = patcher_uart.start()
        self.mockUdpReader1 = patcher_udpread.start()
        self.mockMotors1 = patcher_motors.start()

    def tearDown(self):
        self.mockUDP.reset_mock()
        self.mockUART.reset_mock()
        self.mockUdpReader1.reset_mock()
        self.mockMotors1.reset_mock()

    def test_start_udp_socket(self):
        # test
        Udp1.start_udp_socket()

        # EXPECTs
        self.mockUDP.bind.assert_called_once_with("0.0.0.0", 4210)
        self.mockUART.write.assert_called_once_with("UDP listo para recibir\n")

    def test_handle_udp_pcks_called(self):
        # Mocks
        self.mockUDP.readinto.side_effect = lambda buffer, size: buffer.extend(b'\x7F' * PACKET_SIZE) or PACKET_SIZE
        self.mockUdpReader1.create_command_list_from_packet.return_value = [Mock() for _ in range(N_COMMANDS)]

        # test
        Udp1.handle_udp_pcks()

        # check
        self.mockUDP.readinto.assert_called_once_with(ANY, PACKET_SIZE)
        self.mockUdpReader1.create_command_list_from_packet.assert_called_once_with(ANY)
        self.mockMotors1.apply_motors_commands.assert_called_once_with(ANY)

    def test_handle_udp_pcks(self):
        # EXPECTED        
        expected = bytearray([0x7F, ord('b'), ord('d'), ord('f'), 0x00, ord('f'), 0x00, ord('f'), 0x00, ord('f'), 0xB4, ord('f')])

        # MOCKs
        commands = [Mock() for _ in range(N_COMMANDS)]
        self.mockUDP.readinto.side_effect = lambda buffer, size: buffer.extend(expected) or PACKET_SIZE
        self.mockUdpReader1.create_command_list_from_packet.side_effect = lambda packet: commands
        self.mockMotors1.apply_motors_commands.return_value = None

        # test
        Udp1.handle_udp_pcks()

        # check
        self.mockUDP.readinto.assert_called_once_with(ANY, PACKET_SIZE)
        self.mockUdpReader1.create_command_list_from_packet.assert_called_once_with(Udp1.incomingPacket)
        self.mockMotors1.apply_motors_commands.assert_called_once_with(commands)
        self.assertEqual(Udp1.incomingPacket, expected) # compare actualCaptured with expected

    def test_receive_packet_smaller_than_expected(self):
        # MOCK
        self.mockUDP.readinto.return_value = 6  # packet size smaller than expected

        # test
        Udp1.handle_udp_pcks()

        # EXPECTED
        self.mockUdpReader1.create_command_list_from_packet.assert_not_called()
        self.mockMotors1.apply_motors_commands.assert_not_called()

    def test_receive_packet_larger_than_expected(self):
        # MOCK
        self.mockUDP.readinto.return_value = 10  # packet size larger than expected

        # test
        Udp1.handle_udp_pcks()

        # EXPECTED
        self.mockUdpReader1.create_command_list_from_packet.assert_not_called()
        self.mockMotors1.apply_motors_commands.assert_not_called()

if __name__ == '__main__':
    unittest.main()
