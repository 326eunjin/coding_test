package chapter4;

public class Circle {
    int radius;
    String name;

    public Circle(){
        radius=1;
        name="";
    }
    public Circle(int r, String n)
    {
        radius=r;
        name=n;
    }

    public double getArea()
    {
        return 3.14*radius*radius;
    }
    public static void main(String[] args)
    {
        Circle pizza;
        pizza=new Circle();
       // pizza.radius=10;
        pizza.name="Domino";
        double area=pizza.getArea();
        System.out.println(pizza.name+"'s dimension is "+area);
        Circle donut = new Circle(10,"DUNKIN");
        //donut.radius=2;
        //donut.name="DUNKIN";
        area=donut.getArea();
        System.out.println(donut.name+"'s dimension is "+area);
    }
}

