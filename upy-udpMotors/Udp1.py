from command1 import Command1
from UdpReader1 import UdpReader1
from Motors1 import Motors1
from machine import UDP, UART
from udp_constants import PACKET_SIZE, N_COMMANDS

class Udp1:
    udp = UDP()
    incomingPacket = bytearray(PACKET_SIZE)
    commands = [None] * N_COMMANDS

    @staticmethod
    def start_udp_socket():
        Udp1.udp.bind("0.0.0.0", 4210)
        uart.write("UDP listo para recibir\n")
        Udp1.incomingPacket = bytearray(PACKET_SIZE)

    @staticmethod
    def handle_udp_pcks():
        if Udp1.udp:
            packetSize = Udp1.udp.readinto(Udp1.incomingPacket, PACKET_SIZE)
            if packetSize > 0 and packetSize == PACKET_SIZE:
                Udp1.commands = UdpReader1.create_command_list_from_packet(Udp1.incomingPacket)
                Motors1.apply_motors_commands(Udp1.commands)
