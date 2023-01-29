import java.util.*;

public class Main {
    public static void main(String[] args) {
        Pair<Integer> para = new Pair<>(3,2);
        System.out.println(para.max());
        List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
        Printer.print(list);
    }
}
class Pair<T extends Comparable<T>>{
    public Pair(T left, T right) {
        this.left = left;
        this.right = right;
    }

    public T getLeft() {
        return left;
    }

    public T getRight() {
        return right;
    }

    public T max() {
        int compare = this.left.compareTo(this.right);
        if(compare > 0)
        {
            return left;
        }
        return right;

    }

    private T left;
    private T right;
}
class Printer
{
    public static <E> void print(Iterable<E> itreable)
    {
        StringBuilder napis = new StringBuilder("");
        for(E ele:itreable) {
            napis.append(ele);
        }
        System.out.println(napis);


    }
}
