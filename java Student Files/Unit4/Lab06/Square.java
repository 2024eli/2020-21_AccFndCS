//Name: Evelyn Li
//Date: 03/22/2021

public class Square extends Shape
{
   private double mySide;
   
   public Square(double x)
   {
      mySide = x;
   }
   public double getSide()
   {
      return mySide;
   }
   public void setSide(double x)
   {
      mySide = x;
   }
   public double findArea()
   {
      return Math.pow(mySide, 2);
   }
   public double findPerimeter()
   {
      return 4 * mySide;
   }
   public double findDiagonal()
   {
      return Math.sqrt(Math.pow(mySide, 2));
   }
}