//Name: Evelyn Li
//Date: 03/12/2021

import javax.swing.JFrame;

public class Driver03
{
   public static void main(String[] args)
   {
      JFrame frame = new JFrame("Halistone Numbers");
      frame.setSize(300, 250);
      frame.setLocation(200, 100);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new Panel03());
      frame.setVisible(true);
   }
}