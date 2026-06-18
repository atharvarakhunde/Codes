import ExceptionHandling.Exception1.Site;

public class Mainclass{
    public static void main (String args[]){
        System.out.println("Program Started ");
       Student std = new Student(9,"Atharva",21,"atharva.v.rakhunde@gmail.com","12345678");
       School sch = new School();
       sch.registration(std);
        System.out.println("Program Endded ");
    }
}