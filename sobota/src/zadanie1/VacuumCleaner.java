package zadanie1;

public abstract class VacuumCleaner {
    private String name;

    public VacuumCleaner(String name) { this.name = name; }
    public final String getName() { return name; }

    public abstract int getId();

}
