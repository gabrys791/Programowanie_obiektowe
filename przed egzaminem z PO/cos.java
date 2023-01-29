import java.time.LocalDate;

public class Main {
    public static void main(String[] args) throws CloneNotSupportedException{
        System.out.println("Hello world!");
        Student student1 = new Student("Kowalski", LocalDate.of(1995, 8, 1), 4.5);
        Student student2 = new Student("Nowak", LocalDate.of(1995, 8, 1), 4.5);
        Student student3 = new Student("Kowalski", LocalDate.of(1995, 8, 1), 5.0);
        Student student4 = new Student("Kowalski", LocalDate.of(1995, 8, 1), 4.5);
        System.out.println(student2.compareTo(student1));
        Integer[] tab = {1,2,3,4,5};
        Integer[] tab1 = {5,2,3,4,6};
        System.out.println(Arrayutil.isSorted(tab));
        System.out.println(Arrayutil.isSorted(tab1));
        Osoba kopia = (Osoba) student1.clone();
        System.out.println(kopia);

    }
}
class Osoba implements Cloneable,Comparable<Osoba>
{
    private String nazwisko;
    private LocalDate dataurodzenia;
    public Osoba(String nazwisko, LocalDate dataurodzenia)
    {
        this.nazwisko = nazwisko;
        this.dataurodzenia = dataurodzenia;

    }
    public LocalDate getDataurodzenia() {
        return dataurodzenia;
    }
    public String getNazwisko()
    {
        return nazwisko;
    }


    @Override
    public int compareTo(Osoba o) {
        int compare = this.nazwisko.compareTo(o.nazwisko);
        if(compare == 0)
        {
            compare = this.dataurodzenia.compareTo(o.dataurodzenia);
        }
        return compare;
    }
    @Override
    public Osoba clone()throws CloneNotSupportedException
    {
        return (Osoba) super.clone();
    }
}
class Student extends Osoba implements Cloneable, Comparable<Osoba>
{
    private double sredniaocen;
    public Student(String nazwisko, LocalDate dataurodzenia, double sredniaocen)
    {
        super(nazwisko,dataurodzenia);
        this.sredniaocen = sredniaocen;
    }
    public int compareTo(Student s)
    {
        int compare =  super.compareTo(s);
        if(compare == 0)
        {
            compare = Double.compare(this.sredniaocen,s.sredniaocen);
        }
        return compare;
    }
    public Student clone() throws CloneNotSupportedException
    {
        return (Student) super.clone();
    }

}
class Arrayutil
{
    public static <T extends Comparable<T>> boolean isSorted(T[] array)
    {
        for(int i=0; i < array.length-1; i++)
        {
            if(array[i].compareTo(array[i+1]) > 0)
            {
                return false;
            }
        }
        return true;

    }
}