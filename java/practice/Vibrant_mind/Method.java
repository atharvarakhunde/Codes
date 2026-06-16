public class Method {
    public static boolean isPrime(int n ){
        if(n==1||n==0){
            return false;
        }
        for(int i=2 ; i<=Math.sqrt(n);i++){
            if(n%i==0){
                System.out.println(n+" "+ i );
                return false;
            }
        }
        return true;
    }

    public static int isPalindrome(int n , int temp){
        if (n==0){
            return temp;
        }
        temp = (temp*10)+ (n%10);
        return isPalindrome((n/10),temp);
    }

    public static int checkArmstrong(int n ,int rog , int pov){
        rog = n ;
        while (n!=0){
            pov++;
            n= n/10;
        }
        while (rog != 0){
            n+= Math.pow(rog%10,pov);
            rog /= 10;
        }
        return n ;
    }
    public static long factorial(int n ){
        int result = 1;
        for(int i=n ; i>=1; i--){
            result =result * i;
        }
        return result ;
    }
}
