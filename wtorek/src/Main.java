import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> lista = new ArrayList<Integer>();
        lista.add(12);
        lista.add(8);
        lista.add(10);
        lista.add(9);
        System.out.println(Arrayutil.maxval(lista));

    }
}
class Arrayutil
{
    public static <T extends Comparable<T>> T maxval(ArrayList<T> array)
    {
        T max = array.get(0);
        for(int i = 0;i < array.size(); i++)
        {
           if(array.get(i).compareTo(max) > 0)
           {
               max = array.get(i);
           }
        }

        return max;
    }










}
