import * as dgram from "dgram";
import { Direction } from "./Direction";
import { Command1 } from "./Command1";

// Puerto y dirección para el servidor UDP
const UDP_PORT: number = 4210;
const SERVER_ADDRESS: string = "0.0.0.0"; // Escuchar en todas las interfaces

// Crear un socket UDP
const server: dgram.Socket = dgram.createSocket("udp4");

// Función para manejar los datos recibidos
function handleMessage(msg: Buffer, rinfo: dgram.RemoteInfo) {
  console.log(`Servidor recibió: ${msg} de ${rinfo.address}:${rinfo.port}`);
  
  // Procesar el mensaje recibido en comandos
  let commands: Uint8Array = new Uint8Array(msg);
  for (let i = 0; i < commands.length; i += 2) {
    let pwm : number = commands[i];
    let direction : Direction = commands[i + 1] === Direction.forward.charCodeAt(0) ? Direction.forward : Direction.backward;
    let command : Command1 = new Command1({ pwm, direction });
    console.log(`Comando recibido - PWM: ${command['pwm']}, Dirección: ${command['direction']}`);
  }
}

// Manejar errores en el socket
server.on("error", (err: Error) => {
  console.error(`Error en el servidor UDP:\n${err.stack}`);
  server.close();
});

// Manejar mensajes recibidos
server.on("message", handleMessage);

// Indicar que el servidor está escuchando
server.on("listening", () => {
  const address = server.address();
  console.log(`Servidor escuchando en ${address.address}:${address.port}`);
});

// Iniciar el servidor UDP
server.bind(UDP_PORT, SERVER_ADDRESS);
