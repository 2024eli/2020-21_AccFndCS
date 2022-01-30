//Name: Evelyn Li
//Date: 03/22/2021

public class Square extends Rectangle
{  
   public Square(double x)
   {
      super(x, x);
   }
   public double getSide()
   {
      return getLength();
   }
   public void setSide(double x)
   {
      setLength(x);
      setHeight(x);
   }
}