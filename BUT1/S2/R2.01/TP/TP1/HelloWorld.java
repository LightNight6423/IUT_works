import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World!");

        Scanner keyboard = new Scanner(System.in);

        System.out.print("Enter Your firstName : ");
        String firstName = keyboard.nextLine();

        int groupNumber;
        do {
            System.out.print("Enter your group number (1,2 or 3) : ");
            groupNumber = keyboard.nextInt();
        } while (groupNumber < 1 || groupNumber > 3);

        System.out.print("Welcome " + firstName + " from G" + groupNumber + " to the Object_Oriented Development class!");
    }
}
