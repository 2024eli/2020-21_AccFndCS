//Name: Evelyn Li
//Date: 04/12/2021

import java.io.*;
import java.util.Arrays;

public class Driver01
{
   private static int findMaxLoc(double[] arg)
   {
      //made this to find where the maximum double is in a list
      double max = arg[0];
      for(int k = 1; k < arg.length; k++)
         max = Math.max(max, arg[k]);
      int i = 0;
      for(int j = 1; j < arg.length; j++)
         if (arg[j] == max)
            i = j;
      return i;
   }
   public static void main(String[] args)
   {
      //input
      double[] myArray = {2.0, 3.7, 9.9, 8.1, 8.5, 7.4, 1.0, 6.2};
      double[] newArray = {};
      int numitems = myArray.length; //myArray.length was a little wordy
      				      
      for (int j = 1; j < numitems; j++)
      {
         int n = numitems-j+1; //again, too wordy
         newArray = Arrays.copyOfRange(myArray, 0, n);
         int m = findMaxLoc(newArray);
         if (myArray[numitems - j] < myArray[m]) 
         {
            double temp = myArray[m];
            myArray[m] = myArray[numitems - j];
            myArray[numitems - j] = temp;
         }
      }
      for (double list : myArray)   
         System.out.print(list + "  ");  
   }
}