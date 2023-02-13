package zadanie1;

import java.util.Comparator;
import java.util.Date;
import java.util.ArrayList;

public class CordlessVacuumCleaner extends VacuumCleaner implements Cloneable, Named{
    private final int id;
    private Date dateOfProd = null;

    public CordlessVacuumCleaner(String name, int id) {
        super(name);
        this.id = id;
        this.dateOfProd = new Date();
    }

    public int getId() {
        return id;
    }

    @Override
    public String toString() {
        return "ID = " + id
                + ", dateOfProd = " + dateOfProd
                + "]";
    }
    @Override
    public CordlessVacuumCleaner clone() throws CloneNotSupportedException
    {
        CordlessVacuumCleaner cloned = (CordlessVacuumCleaner) super.clone();
        cloned.dateOfProd = (Date) dateOfProd.clone();
        return cloned;
    }



}
