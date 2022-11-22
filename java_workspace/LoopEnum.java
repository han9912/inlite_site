package java_workspace;

import java.util.Scanner;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class LoopEnum {
    public static void main(String[] args) {
        for (Level myVar : Level.values()) {
            System.out.println(myVar);
        }
        try (Scanner myObj = new Scanner(System.in)) {
            System.out.println("Enter username");

            String userName = myObj.nextLine();
            boolean isMale = myObj.nextBoolean();
            System.out.println("username is: " + userName);
            System.out.println(isMale ? "male" : "female");

            LocalDateTime dateObj = LocalDateTime.now();
            DateTimeFormatter formatterObj = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");

            System.out.println(dateObj);
            System.out.println(dateObj.format(formatterObj));
        }

    }
}
