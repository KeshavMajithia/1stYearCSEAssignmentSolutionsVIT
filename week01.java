public class Student{
    int id;
    String name;
    Student(){
        System.out.println("this is a default constructor");
}
Student(int i, String n){
    id=i;
    name=n;
}
public static void main(String[] args){
    Student s=new Student();
    System.out.println("\nDefault Constructor values: \n");
    System.out.println("Student id: :"+s.id+"\nStudent Name: "+s.name);
    System.out.println("\nParameterized Constructor Values: \n");
    Student student=new Student(10, "David");
    System.out.println("Student id: "+student.id+"\nStudent Name: "+student.name);
}
}
