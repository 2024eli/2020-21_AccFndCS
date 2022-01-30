//Name: Evelyn Li
//Date: 03/24/2021
   
import javax.swing.*;
import java.awt.*;

public class ScoreCard09 extends JPanel
{
   private JTextField[] input;
   private JLabel[] arr;
   public ScoreCard09()
   {
      setLayout(new GridLayout(2, 18));
      
      //add 18 JLabels
      arr = new JLabel[18];
      for(int i=1; i <= arr.length; i++)
      {
         add(new JLabel("" + i, SwingConstants.CENTER));
      }
   
      //add an array of 18 JTextFields
      input = new JTextField[18];
      for(int j=0; j < input.length; j++)
      {
         input[j] = new JTextField();
         add(input[j]);
      }
   }
   public void randomize()
   {
      for(int i=0; i<18; i++)
      {
         input[i].setText("" + (int)Math.floor(4 * Math.random() + 1));
      }
   }
   public int findTotal()
   {
      int total = 0;
      for(int i=0; i<18; i++)
      {
         total += Integer.parseInt(input[i].getText());
      }
      return total;
   }
   public int findAces()
   {
      int aces = 0;
      for(int i=0; i<18; i++)
      {
         if(Integer.parseInt(input[i].getText()) == 1)
         {
            aces += 1;
         }
      }
      return aces;
   }
   public int findHardestHole()
   {
      int hh = 0; //hh is hardest hole
      int hole = 0;
      for(int i=0; i<18; i++)
      {
         if(Integer.parseInt(input[i].getText()) > hole)
         {
            hh = i;
            hole = Integer.parseInt(input[i].getText());
         }
      }
      hh++;
      return hh;
   }
}