import java.util.ArrayList;
import java.time.LocalDate;
public class Main extends Pair {
    public static void main(String[] args) {
        ArrayList<LocalDate> czasy = new ArrayList<LocalDate>();
        ArrayList<Integer> liczby = new ArrayList<Integer>();
        liczby.add(1);
        liczby.add(2);
        liczby.add(3);
        liczby.add(2);
        liczby.add(1);

        System.out.println(Arrayutil.isSorted(liczby));
        ArrayList<String> slowa = new ArrayList<>();
        slowa.add("ala");
        slowa.add("ma");
        slowa.add("zota");
        System.out.println(Arrayutil.isSorted(slowa));


    }
}
class Arrayutil
{
    public static <T extends Comparable<T>> T maxx(ArrayList<T> arr)
    {
        T max = arr.get(0);
        for(int i = 0; i < arr.size(); i++)
        {
            if(arr.get(i).compareTo(max) > 0)
            {
                max = arr.get(i);
            }
        }
        return max;
    }
    public static <T extends Comparable<? super T>> boolean isSorted(ArrayList<T> arr)
    {
        for(int i = 0; i < arr.size() - 1; i++)
        {
            if(arr.get(i).compareTo(arr.get(i+1)) > 0)
            {
                return false;
            }
        }
        return true;
    }
    public static <T extends Comparable<T>> boolean isPalindrome(ArrayList<T> arr)
    {
        for(int i = 0; i < arr.size(); i++)
        {
            if(arr.get(i).compareTo(arr.get(arr.size()-i-1)) != 0)
            {
                return false;
            }
        }
        return true;
    }
}