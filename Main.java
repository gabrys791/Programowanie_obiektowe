import java.util.Objects;
import java.time.LocalDate;
public class Main {
    public static void main(String[] args) {
        Mebel stolik = new Mebel("maly mebel",1,0.5,4);
        System.out.println(stolik.toString());
        System.out.println(Mebel.getIle());
        Mebel sredni = new Mebel(2,1,4);
        System.out.println(sredni.toString());
        System.out.println(stolik==sredni);
        Biurko male_biurko = new Biurko("male biurko",2,1,4,22);
        System.out.println(male_biurko.toString());
        System.out.println(Mebel.getIle());
        Biurko giga = new Biurko("giga biurko",3,2,4,25);
        Mebel[][] spis = new Mebel[2][2];
        spis[0][0] = stolik;
        spis[0][1] = sredni;
        spis[1][0] = male_biurko;
        spis[1][1] = giga;
        for(int i=0; i<2; i++)
        {
            for(int j = 0; j<2; j++)
            {
                System.out.println(spis[i][j].toString());
            }
        }
        String[] spisNazw = {stolik.getNazwa(), sredni.getNazwa(), male_biurko.getNazwa(), giga.getNazwa()};
        for(String x :spisNazw)
        {
            System.out.println(x);
        }
        System.out.println();

    }
}
class Mebel
{

    public Mebel(String nazwa, double dlugosc, double szerokosc, Integer iloscnog)
    {
        this.nazwa = nazwa;
        this.dlugosc = dlugosc;
        this.szerokosc = szerokosc;
        this.iloscnog = iloscnog;
        ile++;
    }
    public Mebel(double dlugosc, double szerokosc, Integer iloscnog)
    {
        this("jakis mebel",dlugosc,szerokosc,iloscnog);
        ile++;
    }

    public double getDlugosc() {
        return dlugosc;
    }

    public double getSzerokosc() {
        return szerokosc;
    }

    public Integer getIloscnog() {
        return iloscnog;
    }

    public String getNazwa() {
        return nazwa;
    }
    @Override
    public String toString()
    {
        if (nazwa.equals("jakis mebel")) {
            return getClass().getName() +
                    "[dlugosc=" + dlugosc +
                    ", szerokosc=" + szerokosc +
                    ", iloscNog=" + iloscnog +
                    ']';
        }
        return getClass().getName() +
                "[nazwa=" + nazwa +
                ", dlugosc=" + dlugosc +
                ", szerokosc=" + szerokosc +
                ", iloscNog=" + iloscnog +
                ']';
    }

    @Override
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
        Mebel other = (Mebel) otherobject;
        return nazwa.equals(other.nazwa) && dlugosc == other.dlugosc && szerokosc == other.szerokosc && iloscnog == other.iloscnog;

    }
    public static int getIle()
    {
        return ile;
    }
    private String nazwa;
    private double dlugosc;
    private double szerokosc;
    private Integer iloscnog;
    private static int ile;
}
class Biurko extends Mebel
{

    public Biurko(String nazwa, double dlugosc, double szerokosc, Integer iloscnog, double przekantamonitora)
    {
        super(nazwa, dlugosc, szerokosc, iloscnog);
        this.Dataprodukcji = LocalDate.now();
        this.przekantamonitora = przekantamonitora;
    }

    public void setDataprodukcji(LocalDate dataprodukcji) {
        this.Dataprodukcji = dataprodukcji;
    }
    public LocalDate getDataprodukcji()
    {
        return Dataprodukcji;
    }
    @Override
    public String toString()
    {
        return super.toString()+",["+Dataprodukcji+"],"+"["+przekantamonitora+"]";
    }

    @Override
    public boolean equals(Object otherobject) {
        if(!super.equals(otherobject))
        {
            return false;
        }
        Biurko other = (Biurko) otherobject;
        return Dataprodukcji == other.Dataprodukcji && przekantamonitora == other.przekantamonitora;
    }

    private LocalDate Dataprodukcji;
    private double przekantamonitora;

}