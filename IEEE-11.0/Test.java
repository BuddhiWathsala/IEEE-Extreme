import java.util.Scanner;

class Test{  
 public static void main(String args[]){  
   Scanner sc=new Scanner(System.in);  
     
   
   String name=sc.next();  
   
   do{
     System.out.println(name);
       
     
   }while((name=sc.readLine()));
   
   sc.close();  
 }  
}   