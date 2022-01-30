//Created by Christina Wallin
//Period 4; 3/1/07

public class Sorter{
   public static long sort(String sort, int[] data, int numItems){
      long time = System.currentTimeMillis();
      if(sort.equals("Bubble Sort"))
         bubble(data, numItems);
      else if(sort.equals("Insertion Sort"))
         insert(data, numItems);
      else if(sort.equals("Selection Sort"))
         select(data, numItems);
      else if(sort.equals("Merge Sort"))
         merge(data, numItems);
      else if(sort.equals("Quick Sort"))
         quick(data, numItems);
      else 
         heap(data, numItems);
      return System.currentTimeMillis() - time;
   }
   //BUBBLE SORT - non-optimized
   private static void bubble(int[] data, int numItems)
   {
      for (int i = 0; i < numItems-1; i++)
         for (int j = 0; j < numItems-i-1; j++)
            if (data[j] > data[j+1])
            {
               swap(data, data[j+1], data[j]);
            }
   }
   
   //INSERTION SORT
   private static void insert(int[] data, int numItems)
   {
      for(int i = 2; i < numItems; i++)
      {
         shift(data, i, data[i]);
      }
   }
   private static void shift(int[] array, int index, int value)
   {
      for(int i = index - 1; i >=1; i--)
      {
         if(array[i]>value)
         {
            array[i+1]=array[i];
            if(i==0)
               array[i]=value;
         }
         else
         {
            array[i+1]=value;
            return;
         }
      }
   }
    
   //SELECTION SORT
   private static void select(int[] data, int numItems)
   {
      for (int i = 0; i < numItems; i++) {
        // min is the index of the smallest element with an index greater or equal to i
         int min = i;
         for (int j = i + 1; j < numItems; j++) {
            if (data[j] < data[min]) {
               min = j;
            }
         }
        // Swapping i-th and min-th elements
         swap(data, data[i], data[min]);
      }
   }
         
   //MERGE SORT
   private static void merge(int[] data, int numItems)
   {
      int[] helper = new int[numItems];
      mergeHelper(data, helper, 1, numItems -1);
   }
   private static void mergeHelper(int[] data, int[] copy, int low, int high)
   {
      if(low<high)
      {
         int mid = (high + low)/2;
         mergeHelper(data, copy, low, mid);
         mergeHelper(data, copy, mid + 1, high);
         mergeLists(data, copy, low, mid, high);
      }
   }
   private static void mergeLists(int[] data, int[] copy, int low, int mid, int high)
   {
      int s1 = low;
      int s2 = mid + 1;
      for(int i = low; i <=high; i++)
      {
         if(s1>mid)
         {
            copy[i] = data[s2];
            s2++;
         }
         else if(s2>high)
         {
            copy[i] = data[s1];
            s1++;
         }
         else if(data[s1]<data[s2])
         {
            copy[i] = data[s1];
            s1++;}
         else{
            copy[i] = data[s2];
            s2++;
         }
         
      }
      //copy ==> data
      for(int i = low; i <= high; i++)
      {
         data[i] = copy[i];
      }
   } 
      
       //QUICK SORT
   private static void quick(int[] data, int numItems)
   {
      quickSort(1, numItems - 1, data);
   }
   private static void quickSort(int left, int right, int[] data)
   {
      if(left>=right)
      {
         return;
      }
      int i = left;
      int j = right;
      int pivot = data[(left + right)/2];
      while(i < j)
      {
         while(data[i]<pivot)
            i++;
         while(data[j]>pivot)
            j--;
         if(i<=j)
         {
            swap(data,i,j);
            i++;
            j--;
         }
      }
      quickSort(left, j, data);
      quickSort(i, right, data);
   }
     
       //HEAPSORT -- the items in the array always start at 1 anyway, so there is no need to recopy the array
   private static void heap(int[] data, int numItems)
   {
         //make the data into a maxHeap
      for(int i = numItems - 1; i>1; i--)
      {
         if(data[i]>data[i/2])
         {
            swap(data, i, i/2);
            heapDown(data, i, numItems - 1);
         }  
      }
         //sort the data
      for(int i = 1; i < numItems-1; i++)
      {
         swap(data, 1, numItems - i);
         heapDown(data, 1, numItems - i -1);
      }
   }
      
   private static void heapDown(int[] data, int k, int size)
   {
      int max = -1;
      if((k*2<=size&&data[k*2]>data[k])||((k*2+1)<=size&&data[(k*2+1)]>data[k]))
      {
         if((k*2+1)<=size&&data[k*2]>data[(k*2+1)])
         { //don't also have to check for k*2 because (k*2+1) is always one more than (k*2+1).
            swap(data, k, k*2);
            max = k*2;
         }
         else if(!((k*2+1)<=size))
         {
            swap(data, k, k*2);
            max = k*2;}
         else {
            swap(data, k, (k*2+1));
            max = (k*2+1);
         }
         heapDown(data, max, size);
      }
   }
     
       //private method swap - used for many of the sorts
   private static void swap(int[] data, int a, int b)
   {
      int temp = data[a];
      data[a] = data[b];
      data[b] = temp;
   }
}