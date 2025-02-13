//Name: Evelyn Li
//Date: 04/21/2021
 
import javax.swing.JOptionPane;
public class Driver11
{
   public static int power(int base, int exp)  //do not use Math.pow
   {
      if (exp==0)
         return 1;
      else 
         return base * power(base, exp-1);
   }
   public static int factorial(int n)
   {
      if (n==1)
         return 1;
      else
         return n * factorial(n-1); 
   }
   public static int fib(int n)
   {
      if (n<=1)
         return 1;
      else
         return fib(n-1) + fib(n-2); 
   }
   public static int gcd(int a, int b)
   {
      //If we have 0 and another num, GCD is the other num
      if (a==0)
         return b;
      if (b==0)
         return a;
      
      //if they equal each other, the GCD is the num
      if (a==b)
         return a;
      
      if (a>b)
         return gcd(a-b, b);
      else
         return gcd(a, b-a);
   }
   public static void main(String[] args)
   {
      int choice = 0, a, b;
      while(choice != 6)
      {
         String message = "";
         message = message + "\n1. Find powers.";
         message = message + "\n2. Find factorials.";
         message = message + "\n3. Find Fibonacci numbers.";
         message = message + "\n4. Find a greatest common divisor (GCD).";
         message = message + "\n5. Quit.";
         choice = Integer.parseInt(JOptionPane.showInputDialog(message));
         switch(choice)
         {
            case 1: 
               a = Integer.parseInt(JOptionPane.showInputDialog("Enter base:"));
               b = Integer.parseInt(JOptionPane.showInputDialog("Enter exponent:"));
               JOptionPane.showMessageDialog(null, 
                                    a + "^" + b + " = " + power(a, b));
               break;
            case 2: 
               a = Integer.parseInt(JOptionPane.showInputDialog("Enter n:"));
               JOptionPane.showMessageDialog(null, 
                                    "factorial(" + a + ") = " + factorial(a) );
               break;
            case 3: 
               a = Integer.parseInt(JOptionPane.showInputDialog("Enter n:"));
               JOptionPane.showMessageDialog(null, 
                                    "fib(" + a + ") = " + fib(a) );
               break;
            case 4: 
               a = Integer.parseInt(JOptionPane.showInputDialog("First number:"));
               b = Integer.parseInt(JOptionPane.showInputDialog("Second number:"));
               JOptionPane.showMessageDialog(null, 
                                    "gcd(" + a + ", " + b + ") = " + gcd(a, b));
               break;
            case 5: 
               JOptionPane.showMessageDialog(null, "Bye-bye!");
               System.exit(0);
            default: 
               JOptionPane.showMessageDialog(null, "Not a valid selection.");
               break;
         }
      }
      System.exit(0);
   }
 
}