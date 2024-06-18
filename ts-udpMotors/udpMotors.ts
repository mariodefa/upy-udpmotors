import { Constants } from "./Constants";
import { GamePadListener } from "./GamePadListener";
import { Utils } from "./Utils";
import { UdpClient } from "./UdpClient";

UdpClient.setDestination("192.168.4.32");
GamePadListener.initialize();
GamePadListener.connectGamePad();
GamePadListener.setupCommandsListener();

function sendNewCommands(){
    let packet : Uint8Array = Utils.fromCommandArrayToUint8Array(GamePadListener.getCommands());
    UdpClient.sendCommands(packet);
}

setInterval(sendNewCommands, Constants.REFRESH_INTERVAL);