import java.util.*;

public class Hashing2 {
    public static void main(String args[]) {
        int arr[] = {1, 2, 3, 2, 1, 2, 3, 2, 3};
        int size = arr.length;
        HashMap<Integer, Integer> map = new HashMap<>();

        // Use 'size' instead of 'n'
        int maxFreq = 0, minFreq = size;
        int maxEle = 0, minEle = 0;

        for (int i = 0; i < size; i++) {
            // Must call getOrDefault on the 'map' object
            map.put(arr[i], map.getOrDefault(arr[i], 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int element = entry.getKey();
            int count = entry.getValue();

            if (count > maxFreq) {
                maxFreq = count;
                maxEle = element;
            }

            if (count < minFreq) {
                minFreq = count;
                minEle = element;
            }
        }

        // Print the results
        System.out.println("The highest frequency element is: " + maxEle);
        System.out.println("The lowest frequency element is: " + minEle);
    }
}