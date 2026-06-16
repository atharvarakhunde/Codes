class SecondLargest{
    public static void main (String args[]){
        int arr[] = {1,2,3,4,5,6,10,34};
        int largest = Integer.MIN_VALUE;
        int secondlargest = Integer.MIN_VALUE;
        
        for(int i=0;i<arr.length;i++){
            if(arr.length<2){
                System.out.println("The second largest number is not present that is null");
                return;
            }
            else if(arr[i]>largest){
                secondlargest = largest;
                largest = arr[i]; 
            }else if(arr[i]>secondlargest && arr[i]!=largest){
                secondlargest = arr[i];
            }
        }
        System.out.println("The second largest Number is "+ secondlargest);
    }
}