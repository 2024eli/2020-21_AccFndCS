//Name: Evelyn Li
//Date: 03/03/2021

import edu.fcps.karel2.Display;
import edu.fcps.Digit;

public class Zero extends Digit
{
   public Zero(int x, int y)
   {
      super(x, y);
   }
   public void display()
   {
      segment1_On();
      segment2_On();
      segment3_On();
      segment4_On();
      segment5_On();
      segment6_On();
      segment7_Off();
   }
}