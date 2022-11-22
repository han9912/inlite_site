package java_workspace;

public class Standby {
    int x;
    final float pi = 3.14f;
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String newName) {
        this.name = newName;
    }
    // Create a class constructor for the Standby class
    public Standby(int y) {
        x = y;
    }

    public static void main(String[] args) {
        
        Standby myObj = new Standby(5);
        System.out.println(myObj);
        Student myStu = new Student();
        myStu.study();
    }

}
