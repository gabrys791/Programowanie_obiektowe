package zadanie2;

import java.util.Comparator;
import java.util.Objects;

public class Main {
    public static void main(String[] args) throws CloneNotSupportedException{
        Osoba pan = new Osoba(47,"Krzysztof");
        Osoba pani = new Osoba(49,"Justyna");
        System.out.println(pan);
        System.out.println(pani);
        System.out.println(pan.equals(pani));
        System.out.println(pan.compareTo(pani));
        Student ja = new Student(21,"Gabrys","166292","informatyka");
        System.out.println(ja);
        Student jakolejny = ja.clone();
        System.out.println(jakolejny);
        System.out.println(pani.compareTo(pan));
    }
}
class Osoba implements Cloneable, Comparable<Osoba>, Comparator<Osoba>
{
    public Osoba(int wiek, String imie)
    {
        this.imie = imie;
        this.wiek = wiek;
    }
    public int getWiek()
    {
        return wiek;
    }

    public String getImie() {
        return imie;
    }

    @Override
    public int compare(Osoba o1, Osoba o2) {
        return o1.getImie().compareTo(o2.getImie());
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj)
        {
            return true;
        }
        if(obj == null)
        {
            return false;
        }
        if(getClass() != obj.getClass())
        {
            return false;
        }
        Osoba o = (Osoba) obj;
        return imie.equals(o.getImie()) && wiek == o.getWiek();
    }
    @Override
    public String toString()
    {
        return getClass() + " [imie= "+imie+" wiek = "+wiek+"]";
    }
    public Osoba clone() throws CloneNotSupportedException{
        return (Osoba) super.clone();
    }


    private int wiek;
    private String imie;

    @Override
    public int compareTo(Osoba o) {
        int compare = imie.compareTo(o.imie);
        if(compare == 0)
        {
            compare = Integer.compare(wiek, o.wiek);
        }
        return compare;
    }
}
class Student extends Osoba implements Comparable<Osoba>, Comparator<Osoba>, Cloneable
{
    private String index;
    private String kierunek;
    public Student(int wiek, String imie, String index, String kierunek)
    {
        super(wiek,imie);
        this.index = index;
        this.kierunek = kierunek;
    }

    public String getIndex() {
        return index;
    }

    public String getKierunek() {
        return kierunek;
    }

    @Override
    public boolean equals(Object otherobject)
    {
        if(!super.equals(otherobject))
        {
            return false;
        }
        Student s = (Student) otherobject;
        return index.equals(s.index) && kierunek.equals(s.kierunek);
    }

    public int compareTo(Student s) {
        int compare = index.compareTo(s.index);
        if(compare == 0)
        {
            compare = kierunek.compareTo(s.kierunek);
        }
        return compare;
    }

    public int compare(Student s1, Student s2)
    {
        return s1.getImie().compareTo(s2.getImie());
    }
    public Student clone() throws CloneNotSupportedException
    {
        return (Student) super.clone();
    }

}