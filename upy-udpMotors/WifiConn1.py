import network
import time
from Udp1 import Udp1
from WifiConn1 import WifiConn1

class WifiConn1:  

    @staticmethod
    def connect_to_domestic_wifi(wifi_name, wifi_pass):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(wifi_name, wifi_pass)

        timeout = 0
        while not wlan.isconnected() and timeout < 10:
            time.sleep(1)
            timeout += 1

        if wlan.isconnected():
            print("Conexión exitosa a la red WiFi doméstica.")
            print("Dirección IP:", wlan.ifconfig()[0])
            Udp1.start_udp_socket()
        else:
            print("Error al conectar a la red WiFi doméstica.")

    @staticmethod
    def is_connected():
        wlan = network.WLAN(network.STA_IF)
        return wlan.isconnected()
