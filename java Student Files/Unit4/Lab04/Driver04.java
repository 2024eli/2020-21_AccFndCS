//Name: Evelyn Li
//Date: 03/17/2021

import java.io.*;      //the File class
import java.util.*;    //the Scanner class
import javax.swing.JOptionPane;

public class Driver04
{
   public static double sum(double[] three)
   {
      double total = 0;
      for(double value : three)
      {
         total = total + value;
      }
      return total;
   }
   public static void main(String[] args)
   {
      Scanner infile = null;
      try
      {
         String filename = JOptionPane.showInputDialog("Enter filename");
         infile = new Scanner(new File(filename));
      }
      catch(FileNotFoundException e)
      {
         JOptionPane.showMessageDialog(null, "Error: File not found.");                    
         System.exit(0);
      }
      
      int SOMENUM = 100000;
      double[] three = new double[SOMENUM];
      int count = 0;
      while (infile.hasNext() && count < SOMENUM)
      {
         three[count] = infile.nextDouble();
         count++;
      }
      three = Arrays.copyOfRange(three, 0, count);
      
      double total = sum(three);
      double avg = total/(count);
      
      System.out.println("Sum: " + sum(three));
      System.out.println("Avg: " + avg);
      Arrays.sort(three);
      System.out.println("Min: " + three[0]);
      System.out.println("Max: " + three[three.length-1]);
   }
}