//Name: Evelyn Li
//Date: 04/21/2021

import edu.fcps.Turtle;
import java.awt.Color;
import javax.swing.*;
public class Driver14
{
   public static void main(String[] args)
   {
      JFrame frame = new JFrame("Tree Turtles");
      frame.setSize(400, 400);
      frame.setLocation(200, 100);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setContentPane(new TurtlePanel());
      frame.setVisible(true);
      Turtle.clear(Color.white);
      Turtle smidge = 
             new Turtle(300.0, 500.0, 90.0)
             { 
                public void drawShape() 	
                {} 
             };
      int choice = Integer.parseInt(JOptionPane.showInputDialog("1. Tree\n2. Extension"));
      if (choice==1)
      {
         int level = Integer.parseInt(JOptionPane.showInputDialog("How many levels? (1-7)"));
         smidge.setCrawl(true);       
         smidge.setSpeed(10);
         tree(smidge, 70.0, 30.0, level);
      }
      else      //extension
      {
         smidge.setCrawl(false);        
         smidge.setSpeed(10);
         treeExt(smidge, 70.0, 25.0);
      }
   }
   public static void tree(Turtle t, double size, double angle, int level)
   {
      if (level == 0) 
      {
         return;
      } 
      else
      {
         t.forward(size);
         t.turnLeft(angle);
         tree(t, size-10, angle, level - 1);
         t.turnRight(2*angle);
         
         tree(t, size-10, angle, level - 1);
         t.turnLeft(angle);
         t.turnLeft(180);
         t.forward(size);
         t.turnLeft(180);
      }
      return;
   }
   
   public static void treeExt(Turtle t, double size, double angle)
   {
      //
   }

   public static void setColor(Turtle t, double size)
   {
      //
   }
}