package ExceptionHandling;

public class School {
    public void registration(Student s){
        RuntimeException r = verify(s);
        if(r==null)
            home(s);
        else
            throw r;
    }
    private RuntimeException verify (Student s ){
        System.out.println(" Verifying the Student "+s);
        if(s == null){
            return new RuntimeException("Student not found");
        }
        return null;
    }
    private void home (Student s){
        System.out.println("This is a Home Page .");
    }
}
