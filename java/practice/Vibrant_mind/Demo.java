class Demo{
    boolean isPalindrome(int n ){
        int r=0;
        int sum=0;
        int rev = n;
        while (n>0){
            r=n%10;
            sum = sum*10+r;
            n/=10;
        }
        return sum==rev;
    }
    public static void main (String args[]){
        Demo d1 = new Demo();
        System.out.println(d1.isPalindrome(1314));
    }
}