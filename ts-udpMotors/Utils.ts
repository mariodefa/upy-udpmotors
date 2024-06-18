import { Command1 } from "./Command1";

export class Utils {

  public static fromCommandArrayToUint8Array(commands: Command1[]): Uint8Array{
    let matrix : Uint8Array[] = commands.map(cmd=>cmd.getData());
    return Utils.concatByteMatrix(matrix);
  }

  private static concatByteMatrix(array: Uint8Array[]): Uint8Array {
    const totalLength = array.reduce((acc, arr) => acc + arr.length, 0);
    const result = new Uint8Array(totalLength);
    let offset = 0;
    for (const arr of array) {
      result.set(arr, offset);
      offset += arr.length;
    }
    return result;
  }
  public static concatByteArrays(...arrays: Uint8Array[]): Uint8Array {
    return Utils.concatByteMatrix(arrays);
  }

  public static mathMap(x : number, in_min : number, in_max : number, 
      out_min : number, out_max : number):number{
    return Math.round((x-in_min)*(out_max-out_min)/(in_max-in_min)+out_min);
  }

  /*
  public static clone<T>(obj:T):T{
    return JSON.parse(JSON.stringify(obj));
  }

  public static constraintNumber(x : number, min : number, max : number):number{
    if(x<min){
        return min;
    }
    if(x>max){
        return max;
    }
    return x;
  }
  */
}
