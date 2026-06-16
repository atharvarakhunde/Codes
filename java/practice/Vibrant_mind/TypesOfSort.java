public class TypesOfSort {
    public static void main (String args[])
    {
        
        String text = "Hello, Java1 World!";

        // 1. Extract from index 7 to the end
        // Index 7 is 'J'
        String sub1 = text.substring(7);
        System.out.println("Result 1: " + sub1); // Outputs: Java World!

        // 2. Extract from index 7 up to (but not including) index 11
        // Indices 7, 8, 9, 10 -> "Java"
        String sub2 = text.substring(7, 11);
        System.out.println("Result 2: " + sub2); // Outputs: Java
    }
}
