import network
import time
from Udp1 import Udp1
from WifiConn1 import WifiConn1

class WifiConn1:  
    wlan = None

    @staticmethod
    def connect_to_domestic_wifi(wifi_name, wifi_pass):        
        WifiConn1.wlan.network.WLAN(network.STA_IF)
        WifiConn1.wlan.active(True)
        WifiConn1.wlan.connect(wifi_name, wifi_pass)

        timeout = 0
        while not WifiConn1.wlan.isconnected() and timeout < 10:
            time.sleep(1)
            timeout += 1

        if WifiConn1.wlan.isconnected():
            print("Conexión exitosa a la red WiFi doméstica.")
            print("Dirección IP:", WifiConn1.wlan.ifconfig()[0])
            Udp1.start_udp_socket()
        else:
            print("Error al conectar a la red WiFi doméstica.")

    @staticmethod
    def is_connected():
        return WifiConn1.wlan is not None and WifiConn1.wlan.isconnected()
