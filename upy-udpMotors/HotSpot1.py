from machine import Pin
import network
import set_pass
from server1 import Server1
from WifiConn1 import WifiConn1

SSID1 = "Azucarito"
PASSWORD = "********"

class HotSpot1:
    server1 = None

    @staticmethod
    def start1():
        wlan = network.WLAN(network.AP_IF)
        wlan.active(True)
        wlan.config(essid=SSID1, authmode=network.AUTH_WPA2_PSK, password=PASSWORD)
        
        HotSpot1.server1 = Server1()
        HotSpot1.server1.add_route("/", HotSpot1.handle_root)
        HotSpot1.server1.add_route("/config", HotSpot1.handle_config)
        HotSpot1.server1.start()

    @staticmethod
    def handle_reqs():
        if HotSpot1.server1:
            HotSpot1.server1.process_request()

    @staticmethod
    def handle_root(client):
        client.write("HTTP/1.1 200 OK\r\n")
        client.write("Content-Type: text/html\r\n")
        client.write("\r\n")
        client.write(set_pass.SET_PASS_PAGE)
        client.close()

    @staticmethod
    def handle_config(client):
        request = client.readline()
        wifi_name = None
        wifi_pass = None
        
        while request and (request != b'\r\n'):
            if request.startswith(set_pass.WIFI_NAME_ID.encode()):
                wifi_name = request.split(b"=")[1].strip().decode()
            elif request.startswith(set_pass.WIFI_PASS_ID.encode()):
                wifi_pass = request.split(b"=")[1].strip().decode()
            request = client.readline()
        
        if wifi_name and wifi_pass:
            WifiConn1.connect_to_domestic_wifi(wifi_name, wifi_pass)
        
        client.write(set_pass.OK_SAVED_PAGE)
        client.close()
