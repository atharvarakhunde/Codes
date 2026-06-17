public class SelectionSort {
    public static void main (String args[]){
        int arr[]= {1,2,3,4,5,9,8,7};
        
        // Time complexity is O(n)^2 .
        for(int i =0 ;i < arr.length-1; i++){
            int minindex = i;
            for (int j =i+1 ; j<arr.length;j++){
                if(arr[j]<arr[minindex]){
                    minindex = j;
                }
            }
            int temp = arr[minindex];
                    arr[minindex] = arr[i];
                    arr[i] = temp;
        }
        for(int b : arr ){
            System.out.println(b);
        }
    }
}
