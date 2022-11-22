package java_workspace;

public interface Animal {
    public void animalSound();
    public void run();
}

/**
 * Pig implements Animal
 */
class Pig implements Animal {

    @Override
    public void animalSound() {
        // TODO Auto-generated method stub
        System.out.println("The pig says: wee wee");
    }

    @Override
    public void run() {
        // TODO Auto-generated method stub
        System.out.println("The pig runs out");
    }
    
}

class Main {
    public static void main(String[] args) {

    }
}