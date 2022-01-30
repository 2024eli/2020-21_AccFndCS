//Name: Evelyn Li
//Date: 03/22/2021

public class Triangle extends Shape
{
   private double mySide;
   
   public Triangle(double x)
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
      return ((Math.sqrt(3)/4) * Math.pow(mySide, 2));
   }
   public double findPerimeter()
   {
      return 3 * mySide;
   }
}