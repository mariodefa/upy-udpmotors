import network

class Server1:
    def __init__(self):
        self.routes = []
        self.sock = network.Server()

    def add_route(self, path, handler):
        self.routes.append((path, handler))

    def start(self):
        self.sock.bind(('', 80))
        self.sock.listen(1)

    def process_request(self):
        try:
            client_sock, client_addr = self.sock.accept()
            client_stream = client_sock
            request_line = client_stream.readline()
            if request_line:
                method, path, protocol = request_line.split(b" ", 2)
                for route_path, route_handler in self.routes:
                    if path == route_path:
                        route_handler(client_stream)
                        break
            client_stream.close()
        except OSError as e:
            print("Error in server:", e)
