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


//write a java program to add different variables.
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

//write a java program to implement array of objects 
public class ArrayOfObjects{
    public static void main(String[]args)
{
Product[] obj = new Product[5];
obj[0]=new Product(23907,"Dell Laptop");
obj[1]=new Product(91340,"HP 630");
obj[2]=new Product(29823,"LG OLED TV");
obj[3]=new Product(11908,"iQOO 9 5G");
obj[4]=new Product(43590,"Asus ROG");
System.out.println("Product Object 1: ");
obj[0].display();
    }
}
class Product{
    int pro_Id;
    String pro_Name;
    Product(int pid, String n)
{
    pro_Id=pid;
    pro_Name=n;
}
public void display()
{
    System.out.println("Product id: "+pro_Id+" "+"Product Name: "+pro_Name);
}
}
