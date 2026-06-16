import java.util.*;

public class Prac6 {

    public static boolean isJollyJumper(int[] sequence) {
        int n = sequence.length;
        if (n <= 1) return true;

        boolean[] diffSeen = new boolean[n];

        for (int i = 1; i < n; i++) {
            int diff = Math.abs(sequence[i] - sequence[i - 1]);
            if (diff >= n || diff == 0 || diffSeen[diff]) {
                return false;
            }
            diffSeen[diff] = true;
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the size of the sequence: ");
        int n = sc.nextInt();
        int[] sequence = new int[n];

        System.out.println("Enter the sequence:");
        for (int i = 0; i < n; i++) {
            sequence[i] = sc.nextInt();
        }

        if (isJollyJumper(sequence)) {
            System.out.println("The sequence is a Jolly Jumper.");
        } else {
            System.out.println("The sequence is NOT a Jolly Jumper.");
        }

        sc.close();
    }
}
