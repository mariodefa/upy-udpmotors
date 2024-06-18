# Página HTML para la configuración de la contraseña
SET_PASS_PAGE = """<html><body><h1>Configurar Red WiFi</h1><form action='/config' method='get'>SSID: <input type='text' name='ssid'><br>Contraseña: <input type='password' name='password'><br><input type='submit' value='Enviar'></form></body></html>"""

# Identificadores de los campos en el formulario HTML
WIFI_NAME_ID = "ssid"
WIFI_PASS_ID = "password"

OK_SAVED_PAGE = """HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE HTML>
<html>
<head><title>Config Page</title></head>
<body>
<h1>Configuration saved!</h1>
</body>
</html>
"""