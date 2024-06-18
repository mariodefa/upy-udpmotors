import { Constants } from "./Constants";
import { GamePadListener } from "./GamePadListener";

GamePadListener.initialize();
GamePadListener.connectGamePad();
GamePadListener.setupCommandsListener();

function sendNewCommands(){
    console.log(GamePadListener.getCommands());
}

setInterval(sendNewCommands, Constants.REFRESH_INTERVAL);