import java.util.*;

public class Prac7{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Map<Integer, Integer> freq = new HashMap<>();

        // Input: 5 card ranks
        for (int i = 0; i < 5; i++) {
            int card = sc.nextInt(); // assuming input like 2 3 3 4 4
            freq.put(card, freq.getOrDefault(card, 0) + 1);
        }

        Collection<Integer> counts = freq.values();

        if (counts.contains(4)) {
            System.out.println("Four of a Kind");
        } else if (counts.contains(3) && counts.contains(2)) {
            System.out.println("Full House");
        } else if (counts.contains(3)) {
            System.out.println("Three of a Kind");
        } else if (Collections.frequency(counts, 2) == 2) {
            System.out.println("Two Pair");
        } else if (counts.contains(2)) {
            System.out.println("One Pair");
        } else {
            System.out.println("High Card");
        }

        sc.close();
    }
}
