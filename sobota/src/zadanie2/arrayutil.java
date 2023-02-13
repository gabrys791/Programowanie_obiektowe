package zadanie2;

import java.util.ArrayList;
import java.util.Comparator;

public class arrayutil {
    public static void main(String[] args)
    {
        ArrayList<Integer> lista = new ArrayList<>();
        lista.add(2);
        lista.add(3);
        lista.add(4);
        Integer[] tab = {1,2,5,3,1,2};
        System.out.println(maxx(tab));
        System.out.println(binsearch(tab,3));

    }
    public static <T extends Comparable<? super T>> T maxx(ArrayList<T> arr)
    {
        T max = arr.get(0);
        for(int i = 0; i < arr.size() - 1; i++)
        {
            if(arr.get(i).compareTo(max) > 0)
            {
                max = arr.get(i);
            }
        }
        return max;
    }
    public  static <T extends Comparable<T>> T maxx(T[] arr)
    {
        T max = arr[0];
        for(int i = 0; i < arr.length;i++)
        {
            if(arr[i].compareTo(max) > 0)
            {
                max = arr[i];
            }
        }
        return max;
    }
    public static <T extends Comparable<T>> int binsearch(T[] tab, T liczba)
    {
        for(int i = 0; i < tab.length; i++)
        {
            if(tab[i].compareTo(liczba) == 0)
            {
                return i;
            }
        }
        return -1;
    }

}
