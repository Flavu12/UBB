package ro.mpp2024;

public class Participant extends Entity<Long>{
    private String nume;
    private int puncte;

    //getters
    public String getNume() {
        return nume;
    }

    public Integer getPuncte() {
        return puncte;
    }

    //setters
    public void setNume(String nume) {
        this.nume = nume;
    }

    public void setPuncte(int puncte) {
        this.puncte = puncte;
    }

    //constructor
    public Participant(Long id, String nume, int puncte) {
        this.setId(id);
        this.nume = nume;
        this.puncte = puncte;
    }

    public Participant(String nume, int puncte) {
        this.nume = nume;
        this.puncte = puncte;
    }

    @Override
    public String toString() {
        return "Participant{" +
                "id=" + this.getId() +
                ", nume='" + nume + '\'' +
                ", puncte=" + puncte +
                '}';
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Participant participant)) return false;
        return nume.equals(participant.nume) && puncte == participant.puncte;
    }

    @Override
    public int hashCode() {
        return nume.hashCode() + puncte;
    }


}
