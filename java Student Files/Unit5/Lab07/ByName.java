//Name: Evelyn Li
//Date: 04/19/2021

import java.util.Comparator;
public class ByName implements Comparator<Salesperson>
{
   public int compare(Salesperson arg1, Salesperson arg2)
   {
      return arg2.getName().compareTo(arg1.getName());
   }
}