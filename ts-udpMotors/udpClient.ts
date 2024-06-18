import * as dgram from "dgram";

const UDP_PORT: number = 4210;
export class UdpClient{
  private static destination : string = "192.168.4.32";
  private static SOCKET: dgram.Socket = dgram.createSocket("udp4");
  private static sendCallback(error: Error | null) {
    if (error) {
      console.error("Error al enviar el comando:", error);
    } else {
      console.log("Comando enviado exitosamente");
    }
  }

  public static setDestination(dest:string){
    UdpClient.destination = dest;
  }
  public static sendCommands(commands: Uint8Array) {
    const message = Buffer.from(commands);
    UdpClient.SOCKET.send(message, UDP_PORT, UdpClient.destination, UdpClient.sendCallback);
  }

  public static close(){
    UdpClient.SOCKET.close();
  }
}
