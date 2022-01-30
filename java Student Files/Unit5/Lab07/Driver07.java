//Name: Evelyn Li
//Date: 04/19/2021

import java.io.*;      //the File class
import java.util.*;    //the Scanner class
import javax.swing.JOptionPane;
import java.util.Comparator;
public class Driver07
{
   public static void main(String[] args)
   {
      Salesperson[] array = input("data.txt");
      menu(array);
      System.exit(0);
   }
    
   public static Salesperson[] input(String filename)
   {    
      Scanner infile = null;
      try
      {
         infile = new Scanner(new File(filename));
      }
      catch(FileNotFoundException e)
      {
         JOptionPane.showMessageDialog(null,"The file could not be found.");
         System.exit(0);
      }
      int numitems = infile.nextInt();
      Salesperson[] array = new Salesperson[numitems];
      for(int k = 0; k < numitems; k++)
      {
         int m = infile.nextInt();
         int n = infile.nextInt();
         String l = infile.next();
         array[k] = new Salesperson(l, m, n);
      }
      infile.close();
      return array;
   }
   	
   public static void menu(Salesperson[]array)
   {
      int choice = 0;
      while(choice != 7)
      {
         String message = "";
         message = message + "\n1. List Alphabetically.";
         message = message + "\n2. List by Cars Sold.";
         message = message + "\n3. List by Trucks Sold.";
         message = message + "\n4. List by Total Sales.";
         message = message + "\n5. Add Sales.";
         message = message + "\n6. Save data to file.";
         message = message + "\n7. Quit.";
         choice = Integer.parseInt(JOptionPane.showInputDialog(message));
         switch(choice)
         {
            case 1: display(array, new ByName());
               break;
            case 2: display(array, new ByCars());
               break;
            case 3: display(array, new ByTrucks());
               break;
            case 4: display(array, new ByTotalSales());
               break;
            case 5: add(array);
               break;
            case 6: save(array);
               break;
            case 7: 
               for(int k = 0; k < 25; k++) 
                  System.out.println();
               System.out.println("Bye-bye!");
               break;
            default: System.out.println("Not a valid selection.");
               break;
         }
         System.out.println();
      }
   }
    
   public static void save(Salesperson[] array)
   {
      PrintWriter outfile = null;
      try{
         outfile = new PrintWriter(new FileWriter("data.txt"));
      }
      catch(Exception e)
      {
         JOptionPane.showMessageDialog(null,"The file could not be created.");
      }
      outfile.println(array.length);
      for(int k = 0; k < array.length; k++)
      {
         outfile.println(array[k].getCars());
         outfile.println(array[k].getTrucks());
         outfile.println(array[k].getName());
      }
      outfile.close();
      System.out.println("Saved.");
   }
   public static void add(Salesperson[] array)
   {	
      String name;
      String carsOrTrucks;
      String num; 
      int x;
      
      do
      {
         name = JOptionPane.showInputDialog("What salesperson?");
         x = search(array, name);
      }
      while(x == -99);
      do
      {
         carsOrTrucks = JOptionPane.showInputDialog("Cars or trucks?");
         carsOrTrucks = carsOrTrucks.toLowerCase();
      }
      while((!carsOrTrucks.equals("cars")) && (!carsOrTrucks.equals("trucks")));
      
      num = JOptionPane.showInputDialog("How many " + carsOrTrucks + "?");
      int n = Integer.parseInt(num);  
      for(int i = 0; i < array.length; i++)
      {
         if(array[i].getName().equals(name))
         {
            if(carsOrTrucks.equals("cars"))
            {
               array[i].setCars(array[i].getCars() + n);
            }
            else if(carsOrTrucks.equals("trucks"))
            {
               array[i].setTrucks(array[i].getTrucks() + n);
            }
         }
      }
      System.out.println("Sales added.");
   }
   public static int search(Salesperson[] array, String name)
   {
      for(int i = 0; i < array.length; i++)
      {
         if(name.equals(array[i].getName()))
         {
            return i;
         }
      }      
      return -99;       //in order to compile
   }
   public static void display(Salesperson[] array, Comparator c)
   {
      sort(array, c);
      System.out.println("Name	Cars	Trucks	Total");
      System.out.println("-----------------------------");
      for(int i = 0; i < array.length; i++)
      {
         int total = array[i].getCars() + array[i].getTrucks();
         System.out.println(array[i].getName() + "\t" + array[i].getCars() + "\t" + array[i].getTrucks() + "\t" + total);
      }
   }
   public static void sort(Object[] array, Comparator c)
   {
      int minPos;
      for(int k = 0; k < array.length; k++)
      {
         minPos = findMin(array, array.length - k, c);
         swap(array, minPos, array.length - k - 1);
      }
   }
   public static int findMin(Object[] array, int upper, Comparator c)
   {
      int min = 0;     
      for (int i = 1; i < upper; i++)
      {
         if (c.compare(array[i], array[min]) < 0)
         {
            min = i;
         }
      }
      return min;
   }
   public static void swap(Object[] array, int a, int b)
   {
      Object temp = array[a];
      array[a] = array[b];
      array[b] = temp;
   }
}