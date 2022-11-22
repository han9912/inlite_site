package java_workspace;

import java.util.Scanner;

public class Main {
    int x = 5;
    static void myMethod(String name) {
        System.out.println(name + ", my Method executed.");
    }
    static void myStaticMethod() {
        System.out.println("Static methods can be called without creating objects.");
    }

    public void myPublicMethod() {
        System.out.println("Public must be called by creating objs.");
    }

    
    public static void main(String args[]) {
        Standby myStandby = new Standby(0);
        System.out.println(myStandby.getName());
        myStandby.setName("Ouch");
        System.out.println(myStandby.getName());

        try (Scanner myScanner = new Scanner(System.in)) {
            System.out.println("Enter username");

            String userName = myScanner.nextLine();
            System.out.println("Username is: " + userName);
        }
        Main.myStaticMethod();
        Main myObj = new Main();
        myObj.myPublicMethod();
        System.out.println(myObj.x);
        myMethod("Jenny");
        // System is a class and println is a method
        System.out.println("Hello World");
        boolean myBool = true;
        double myDouble = 8.99d;
        System.out.println(myDouble);
        System.out.println(myBool);
        
        int myInt = (int) myDouble;

        myDouble = (myInt == 10) ? myInt = Math.max(1, 10) : Math.sqrt(3.3);
        switch(Math.max(2, 4)) {
            case 1:
                break;
            default:
        }

        do{
            System.out.println(999);
        }while(myInt == 1);

        String[] cars = {"Volvo", "BWM", "Benz"};
        for (String i : cars) {
            System.out.println(i);
        }
    }
    public static int sum(int k) {
        if (k > 0) {
            return k + sum(k - 1);
        } else {
            return 0;
        }
    }
}