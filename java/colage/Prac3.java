import java.util.*;

public class Prac3  {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter estimated budget for traveling: ");
        double estimatedTravel = scanner.nextDouble();
        System.out.print("Enter estimated budget for food: ");
        double estimatedFood = scanner.nextDouble();
        System.out.print("Enter estimated budget for stay: ");
        double estimatedStay = scanner.nextDouble();
        double estimatedTotal = estimatedTravel + estimatedFood + estimatedStay;
        System.out.println("Total estimated budget: " + estimatedTotal);

        System.out.print("Enter actual expenditure for traveling: ");
        double actualTravel = scanner.nextDouble();
        System.out.print("Enter actual expenditure for food: ");
        double actualFood = scanner.nextDouble();
        System.out.print("Enter actual expenditure for stay: ");
        double actualStay = scanner.nextDouble();
        double actualTotal = actualTravel + actualFood + actualStay;
        System.out.println("Total actual expenditure: " + actualTotal);

        System.out.print("Enter number of people on the trip: ");
        int numPeople = scanner.nextInt();
        double[] personBudget = new double[numPeople];
        double totalAvailableBudget = 0;

        for (int i = 0; i < numPeople; i++) {
            System.out.print("Enter budget of person " + (i + 1) + ": ");
            personBudget[i] = scanner.nextDouble();
            totalAvailableBudget += personBudget[i];
        }

        double perPersonEstimated = estimatedTotal / numPeople;
        double perPersonActual = actualTotal / numPeople;
        double remainingAmount = actualTotal;
        double[] contribution = new double[numPeople];

        List<Integer> contributors = new ArrayList<>();
        List<Integer> insufficientFunds = new ArrayList<>();
        
        for (int i = 0; i < numPeople; i++) {
            if (personBudget[i] >= perPersonActual) {
                contribution[i] = perPersonActual;
                remainingAmount -= perPersonActual;
                contributors.add(i);
            } else {
                contribution[i] = personBudget[i];
                remainingAmount -= personBudget[i];
                insufficientFunds.add(i);
            }
        }
        
        if (remainingAmount > 0 && !contributors.isEmpty()) {
            double extraPerContributor = remainingAmount / contributors.size();
            for (int index : contributors) {
                contribution[index] += extraPerContributor;
            }
        }

        System.out.println("\nFinal Payment Distribution:");
        for (int i = 0; i < numPeople; i++) {
            System.out.println("Person " + (i + 1) + " pays: " + contribution[i]);
        }
        
        double diff = perPersonActual - perPersonEstimated;
        System.out.println("\nDifference in estimated vs actual expenditure per person: " + diff);
        
        scanner.close();
    }
}
