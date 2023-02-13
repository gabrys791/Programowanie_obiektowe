package zadanie1;
import java.util.ArrayList;
public class CordlessVacuumCleanerDemo {
    public static void main(String[] args) throws CloneNotSupportedException{
        VacuumCleaner p = new CordlessVacuumCleaner("Elektorlux", 1729);
        System.out.println(p.getName());
        CordlessVacuumCleaner s = (CordlessVacuumCleaner) p;
        System.out.println(s.getName());

        Named n = s;
        System.out.println(n.getName());
        CordlessVacuumCleaner d = s.clone();
        System.out.println(d.getName());
        System.out.println(d);

        ArrayList<CordlessVacuumCleaner> odkurzacze = new ArrayList<>();
        odkurzacze.add(new CordlessVacuumCleaner("Samsung", 10));
        odkurzacze.add(new CordlessVacuumCleaner("Dyson", 100));
        odkurzacze.add(new CordlessVacuumCleaner("Bosh", 1000));

        odkurzacze.sort(new NamesComparator());

        System.out.println();
        for (CordlessVacuumCleaner e : odkurzacze) {
            System.out.println("Firma = " + e.getName() + ", id = " + e.getId());
        }
        System.out.println();



    }
}
