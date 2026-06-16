import java.util.Scanner;
public class Prac1 {
    public static void Prac1(int n) {
        if (n <= 0) {
            n = Math.abs(n);
        }
            System.out.print(n + " = ");
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = 3 * n + 1;
            }
        System.out.print(n);
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println();
            System.out.println("Enter a natural number or 0 to Exit : ");
            try {
                int num = scanner.nextInt();
                if (num == 0) {
                    System.out.println("Exiting...");
                    break;
                }
                Prac1(num);
            } catch (Exception e) {
                System.out.println("Invalid input. Please enter a valid number.");
                scanner.next();
            }
        }
        scanner.close();
    }
}
