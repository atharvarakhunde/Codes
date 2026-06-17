package ExceptionHandling.Exception1;

public class InvalidAgeException extends RuntimeException{
    private String msg = "Invalid Age ";
    InvalidAgeException(){}
    InvalidAgeException(String msg){
        this.msg = msg;
    }
    public String toString(){
        return msg ;
    }
}
