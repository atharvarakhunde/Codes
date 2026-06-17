package ExceptionHandling.Exception1;

public class Site {
    private void home(){
        System.out.println("Welcome to your second home");
    }
    public void login (int age ){
        System.out.println("Welcome to this site");
        if(age >= 18 ){
            home();
        }else{
            throw new InvalidAgeException("Age Should be atleast 18 or above ");

        }
        System.out.println("Thank you for visiting site ");
    }
}
