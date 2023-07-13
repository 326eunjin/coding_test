package chapter5;
class Person{
    private int weight;
    int age;
    protected int height;
    public String name;
    public void setWeight(int weight)
    {
        this.weight=weight;
    }
    public int getWeight()
    {
        return weight;
    }
}
class Student extends Person{
    public void set(){
        age=30;
        name="hong";
        height=175;
        //weight=99; private!
        setWeight(99);
    }
    public void print()
    {
        System.out.println(age);
        System.out.println(name);
        System.out.println(height);
        System.out.println(getWeight());
    }
}
public class InheritanceEx {
    public static void main(String[] args)
    {
        Student s= new Student();
        s.set();
        s.print();
    }
}
