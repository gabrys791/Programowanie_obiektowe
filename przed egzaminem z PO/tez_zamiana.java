public class Main {
    public static void main(String[] args) {

        Pair<Integer, Integer> liczby = new Pair<Integer, Integer>(5,6);
        System.out.println(liczby);
        liczby.swap();
        System.out.println(liczby);
        Integer[] tab = {1,2,3};
        Integer[] tab1 = {3,1,2};
        System.out.println(ArrayUtil.isSorted(tab));
        System.out.println(ArrayUtil.isSorted(tab1));



    }
}
class Pair<T, U>
{
    public Pair()
    {
        first = null;
        second = null;
    }

    public Pair(T first, T second)
    {
        this.first = first;
        this.second = second;
    }

    public T getFirst()
    {
        return first;
    }

    public T getSecond()
    {
        return second;
    }

    public void setFirst(T newValue)
    {
        first = newValue;
    }

    public void setSecond(T newValue)
    {
        second = newValue;
    }
    public void swap()
    {
        T temp;
        temp = first;
        first = second;
        second = temp;

    }
    public String toString()
    {
        return first + "," + second;
    }

    private T first;
    private T second;
}

class ArrayUtil {
    public static <T extends Comparable<T>> boolean isSorted(T[] array) {
        for (int i = 0; i < array.length - 1; i++) {
            if (array[i].compareTo(array[i + 1]) > 0) {
                return false;
            }
        }
        return true;
    }
}

