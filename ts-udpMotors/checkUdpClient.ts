import { Command1 } from "./Command1";
import { Utils } from "./Utils";
import { Direction } from "./Direction";
import { UdpClient } from "./UdpClient";
import { Constants } from "./Constants";

UdpClient.setDestination(Constants.SERVER_ADDRESS);
async function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function main(): Promise<void> {
  let commands: Uint8Array = new Uint8Array(4);
  let command1: Command1 = new Command1({
    pwm: 255,
    direction: Direction.backward,
  });
  let command2: Command1 = new Command1({
    pwm: 100,
    direction: Direction.forward,
  });
  let command3: Command1 = new Command1({
    pwm: 127,
    direction: Direction.backward,
  });
  let command4: Command1 = new Command1({
    pwm: 50,
    direction: Direction.forward,
  });
  let command5: Command1 = new Command1({
    pwm: 90,
    direction: Direction.forward,
  });
  let command6: Command1 = new Command1({
    pwm: 180,
    direction: Direction.forward,
  });
  commands = Utils.concatByteArrays(
    command1.getData(),
    command2.getData(),
    command3.getData(),
    command4.getData(),
    command5.getData(),
    command6.getData()
  );
  UdpClient.sendCommands(commands);
  await delay(1000);
  let command7: Command1 = new Command1({
    pwm: 0,
    direction: Direction.backward,
  });
  let command8: Command1 = new Command1({
    pwm: 0,
    direction: Direction.forward,
  });
  let command9: Command1 = new Command1({
    pwm: 0,
    direction: Direction.backward,
  });
  let command10: Command1 = new Command1({
    pwm: 0,
    direction: Direction.forward,
  });
  let command11: Command1 = new Command1({
    pwm: 0,
    direction: Direction.forward,
  });
  let command12: Command1 = new Command1({
    pwm: 0,
    direction: Direction.forward,
  });
  commands = Utils.concatByteArrays(
    command7.getData(),
    command8.getData(),
    command9.getData(),
    command10.getData(),
    command11.getData(),
    command12.getData()
  );
  UdpClient.sendCommands(commands);
}

main();

setTimeout(() => {
  UdpClient.close();
}, 5000);
