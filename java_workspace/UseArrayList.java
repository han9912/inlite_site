package java_workspace;

import java.util.ArrayList;

public class UseArrayList {
    public static void main(String[] args) {
        ArrayList<String> cars = new ArrayList<String>();     
        cars.add("Volvo");
        cars.add("Volvo");
        cars.set(1, "Opel");
        System.out.println(cars);.
        for (String car : cars) {
            System.out.println(car);
        }
    }
}
