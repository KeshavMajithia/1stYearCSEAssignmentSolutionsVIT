//question here
public class WrapperExample{
    public static void main(String args[]){
        int a=20;
        Integer i=Integer.valueOf(a);
        Integer j=a;
        System.out.println(a+" "+i+" "+j);
    }
}

//same question part 2
public class WrapperExample2{
    public static void main(String args[]){
        Integer a=new Integer(3);
        int i=a.intValue();
        int j=a;
        System.out.println(a+" "+i+" "+j);
    }
}
