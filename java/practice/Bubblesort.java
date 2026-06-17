public class Bubblesort {
    public static void main (String args []){
        // Time COmplexity 
        // best caseO(N)
        // worst and average case O(n)^2 
        int arr[] = {8,7,6,5,4,3,2};
            for(int i = 0 ; i< arr.length -1 ; i++){
                for(int j=0 ; j<arr.length-i-1;j++){
                    if(arr[j]> arr[j+1]){
                        int temp = arr[j];
                        arr[j] = arr [j+1];
                        arr[j+1] = temp ; 
                    }
                }
            }

            for(int num : arr){
                System.out.println(num);
            }
    }
}
