//Name: Evelyn Li
//Date: 04/19/2021

public class Salesperson 
{
   //data fields
   private String myName;
   private int myCars, myTrucks;
   
   public Salesperson()
   {
      myName = "";
      myCars = 0;
      myTrucks = 0;
   }
   public Salesperson(java.lang.String i, int j, int k)
   {
      myName = i;
      myCars = j;
      myTrucks = k;
   }
   public java.lang.String getName()
   {
      return myName;
   }
   public int getCars()
   {
      return myCars;
   }
   public int getTrucks()
   {
      return myTrucks;
   }
   public void setName(java.lang.String i)
   {
      myName = i;
   }
   public void setCars(int i)
   {
      myCars = i;
   }
   public void setTrucks(int i)
   {
      myTrucks = i;
   }
   public java.lang.String toString()
   {
      return myName + ": " + myCars + " cars, " + myTrucks + " trucks";
   }
}