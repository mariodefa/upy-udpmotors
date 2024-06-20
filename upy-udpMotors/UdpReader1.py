from command1 import Command1, Direction
from udp_constants import PACKET_SIZE, CHUNK_SIZE, N_COMMANDS

class UdpReader1:
    
    @staticmethod
    def create_command_list_from_packet(packet):
        commands = [None] * N_COMMANDS
        for i in range(PACKET_SIZE // CHUNK_SIZE):
            commands[i] = UdpReader1.create_command_from_chunk(packet[i * CHUNK_SIZE:(i + 1) * CHUNK_SIZE])
        
        return commands;

    @staticmethod
    def create_command_from_chunk(chunk):
        pwm = chunk[0]
        direction = Direction.forward
        if chr(chunk[1]) == 'b':
            direction = Direction.backward
        return Command1(pwm, direction)
