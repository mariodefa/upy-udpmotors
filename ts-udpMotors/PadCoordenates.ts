export class PadCoordenates{
    private x : number;
    private y : number;
    constructor(obj: any){
        this.x = obj.x;
        this.y = obj.y;
    }
    public getX():number{
        return this.x;
    }
    public getY():number{
        return this.y;
    }
    public toString():string{
        return 'x='+this.x+', y='+this.y;
    }
}