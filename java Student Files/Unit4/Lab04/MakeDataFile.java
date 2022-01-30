//Name: Evelyn Li
//Date: 03/17/2021

import java.io.*;
import java.util.*;    
import javax.swing.JOptionPane;

public class MakeDataFile
{
   public static void main(String[] args) throws Exception
   {
      PrintWriter outfile = new PrintWriter(new FileWriter("data.txt") );
   
      int numitems = (int)(Math.random() * 5000 + 5000);
      outfile.println(numitems);
   
      for(int x = 0; x < numitems; x++)
      {
         outfile.println(Math.random() * 1000);
      }
      outfile.close();
   }
}