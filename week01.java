//Write a java program to define a class, describe its constructor, overload the constructors and instantiate its object
public class Student{
    int id;
    String name;
    Student(){
        System.out.println("this is a default constructor\n");
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



//Write a java program to define a class, describe instance methods for setting and retrieving values of intance variables and instantiate its object
public class Studentsrecords  
{
    public String name; 
    String division; 
    private int age; 
    public Studentsrecords(String sname)  
    {  
        name = sname;  
    } 
    public void setDiv(String sdiv)  
    {  
        division = sdiv;  
    }
    public void setAge(int sage)  
    {  
        age = sage;  
    }
    public void printstud()  
    {  
        System.out.println("Doctor Name: " + name );  
        System.out.println("Doctor Division: " + division);   
        System.out.println("Doctor Age: " + age);  
    }
    public static void main(String args[])  
    {  
        Studentsrecords s = new Studentsrecords("Dr. Johnny Sins\n");  
        s.setAge(46);  
        s.setDiv("Brazzers\n");  
        s.printstud();  
    }  
}
