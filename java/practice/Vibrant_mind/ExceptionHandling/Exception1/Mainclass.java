package ExceptionHandling.Exception1;

public class Mainclass {
    public static void main (String args []){
        System.out.println("Program Started ");
        Site s = new Site();
        try {
            s.login(10);
        } catch (InvalidAgeException e ){
            System.out.println(e); 
        }
        System.out.println("Program Endded ");
    }
}
