import machine
import time
from Motors1 import Motors1
from Hotspot1 import Hotspot1
from Udp1 import Udp1
from WifiConn1 import WifiConn1

uart = machine.UART(0, baudrate=115200, tx=machine.Pin(1), rx=machine.Pin(3)) # GPIO 1 TX, GPIO 3 RX 
Motors1.setup1()
Hotspot1.start1()
uart.write("Hotspot iniciado. Conéctate a la red WiFi y visita la dirección IP 192.168.4.1 para configurar la red WiFi doméstica.\n")

# main loop
while True:
    if WifiConn1.is_connected():
        Udp1.handle_udp_pcks()
    else:
        Hotspot1.handle_reqs()
    # time.sleep(0.1)
