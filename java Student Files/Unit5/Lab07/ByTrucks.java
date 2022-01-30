//Name: Evelyn Li
//Date: 04/19/2021

import java.util.Comparator;
public class ByTrucks implements Comparator<Salesperson>
{
   public int compare(Salesperson arg1, Salesperson arg2)
   {
      return arg1.getTrucks() - arg2.getTrucks();
   }
}