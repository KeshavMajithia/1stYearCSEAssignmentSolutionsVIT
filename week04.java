//write a java program to implement inheretance demonstrate use of method overwriting
class h{
    void hello(){
        System.out.println("hello");
    }
}
class e extends h{
    void hello(){
        System.out.println("Hello");
    }
}
class main{
    public static void main(String[] args){
        h H=new h();
        H.hello();
        h he=new h();
        he.hello();
    }
}
