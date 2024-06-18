import { Direction } from "./Direction";
export class Command1 {
  private pwm: number;
  private direction: Direction;
  constructor(obj: any) {
    this.pwm = obj.pwm;
    this.direction = obj.direction;
  }
  public getData(): Uint8Array {
    const pwmByte: number = this.pwm & 0xff;
    const directionByte: number = this.direction.charCodeAt(0) & 0xff;
    return new Uint8Array([pwmByte, directionByte]);
  }
}
