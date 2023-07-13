package practice;

public class Lion extends Animal implements Predator{
    @Override
    public String getFood() {
        return "apple";
    }
}
