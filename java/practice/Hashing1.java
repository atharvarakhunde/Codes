import java.util.*;
public class Hashing1 {
    public static void main (String args[]){
        int arr[] = {1,2,3,2,1,2,3,2};
        int n = 5;
        
        HashMap<Integer,Integer> map = new HashMap<>();

        for(int i = 0 ; i<arr.length ; i++){
            map.put(arr[i],map.getOrDefault(arr[i],0)+1);
        }

        for(Map.Entry<Integer,Integer> entry : map.entrySet()){
            System.out.println(entry.getKey()+" " + entry.getValue());
        }

    }
}
