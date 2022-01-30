//Name: Evelyn Li
//Date: 03/19/2021

import java.io.*;
public class Driver07
{
   public static void main(String[] args) throws Exception
   {
      PrintWriter toFile = new PrintWriter(new FileWriter("output.txt"));
      
      int numitems = (int)(Math.random() * 150);
      int[] array = new int[numitems];
      
      toFile.println("Shapes");
      toFile.println("------");
      
      for(int i=0; i<(array.length); i++)
      {
         Circle c = new Circle(Math.random() * 100);
         Rectangle r = new Rectangle(Math.random() * 100, Math.random() * 100);    
         Square s = new Square(Math.random() * 100);
         Triangle t = new Triangle(Math.random() * 100);
         
         double x = Math.random();
         
         if(x < 0.25)
         {
            toFile.println("area = " + c.findArea() +  "		" + c.toString());
         }
         else if(0.25 <= x && x < 0.50)
         {
            toFile.println("area = " + r.findArea() +  "		" + r.toString());
         }
         else if(0.50 <= x && x < 0.75)
         {
            toFile.println("area = " + s.findArea() + "		" + s.toString());
         }
         else if(0.75 <= x && x < 1)
         {
            toFile.println("area = " + t.findArea() + "		" + t.toString());
         }
      }
      
      toFile.close();
   }
}