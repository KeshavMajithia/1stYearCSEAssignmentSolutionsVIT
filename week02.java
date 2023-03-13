//write a java program to turn on and off led and halogen lights
class Lamp{
    boolean isOn;
    void turnOn(){
        isOn=true;
        System.out.println("Light status: "+isOn);
    }
    void turnOff(){
        isOn=false;
        System.out.println("Light status: "+isOn);
    }
}
class Main{
    public static void main(String[]args){
        Lamp led=new Lamp();
        Lamp halogen=new Lamp();
        led.turnOn();
        halogen.turnOff();
    }
}


//insert question here
class Adder{
    static int add(int a, int b){
        return a+b;
    }
    static int add(int a, int b, int c){
        return a+b+c;
    }
}
class TestOverLoading1{
    public static void main(String[]args){
        System.out.println(Adder.add(11,11));
        System.out.println(Adder.add(11,11,11));
    }
}
