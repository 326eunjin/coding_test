package brutal_force;

public class Person {
    String input;
    int height;
    int weight;
    int rank = 1;
    Person(String input)
    {
        this.input=input;
        String[] array1 = input.split(" ");
        weight=Integer.parseInt(array1[0]);
        height=Integer.parseInt(array1[1]);
    }
    public void show() {
        System.out.print(rank + " ");
    }
}
