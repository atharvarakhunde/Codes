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
        //logic
    }
    private void home (Student s){
        //show data
    }
}
