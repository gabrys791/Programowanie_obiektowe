import java.time.LocalDate;

public class Main {
    public static void main(String[] args) throws CloneNotSupportedException{
        System.out.println("Hello world!");
        Integer[] tab1 = {1,2,3,4,5,6,7};
        Integer[] tab2 = {3,2,1,4,5,1};
        System.out.println(Arrayutil.isSorted(tab1));
        System.out.println(Arrayutil.isSorted(tab2));
    }
}
class osoba implements Cloneable, Comparable<osoba>
{
    public osoba(String nazwisko, LocalDate data_urodzenia)
    {
        this.nazwisko = nazwisko;
        this.data_urodzenia = data_urodzenia;

    }

    public LocalDate getData_urodzenia() {
        return data_urodzenia;
    }

    public String getNazwisko() {
        return nazwisko;
    }
    public boolean equals(Object otherobject)
    {
        if(this == otherobject)
        {
            return true;
        }
        if(otherobject == null)
        {
            return false;
        }
        if(getClass() != otherobject.getClass())
        {
            return false;
        }
        osoba o = (osoba) otherobject;
        return nazwisko.equals(o.nazwisko) && data_urodzenia == o.data_urodzenia;
    }
    @Override
    public int compareTo(osoba o)
    {
        int compare = this.data_urodzenia.compareTo(o.data_urodzenia);
        if(compare == 0)
        {
            compare = this.nazwisko.compareTo(o.nazwisko);
        }
        return compare;
    }
    public osoba clone() throws CloneNotSupportedException
    {
        return (osoba) super.clone();
    }


    private String nazwisko;
    private LocalDate data_urodzenia;

}
class Student extends osoba implements Cloneable, Comparable<osoba>
{


    public Student(String nazwisko, LocalDate data_urodzenia, double srednia) {
        super(nazwisko, data_urodzenia);
        this.srednia = srednia;
    }
    public double getSrednia()
    {
        return srednia;
    }

    public int compareTo(Student s)
    {
        int compare = super.compareTo(s);
        if(compare == 0)
        {
            compare = Double.compare(this.srednia,srednia);
        }
        return compare;
    }
    @Override
    public Student clone() throws CloneNotSupportedException
    {
        return (Student) super.clone();
    }

    @Override
    public boolean equals(Object otherobject) {
        if(!super.equals(otherobject))
        {
            return false;
        }
        Student o = (Student) otherobject;
        return srednia == o.srednia;
    }

    private double srednia;
}
class Arrayutil
{
    public static <T extends Comparable<T>> boolean isSorted(T[] array)
    {
        for(int i = 0; i < array.length - 1; i++)
        {
            if(array[i].compareTo(array[i+1]) > 0)
            {
                return false;
            }

        }
        return true;
    }
}