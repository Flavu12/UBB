package ro.mpp2024;

import java.util.Objects;

public class Rezultat extends Entity<Long>{

    private Long id;
    private Long idparticipant;

    private Long idproba;

    private int puncte;

    public Rezultat(Long idparticipant, Long idproba, int puncte) {
        this.idparticipant = idparticipant;
        this.idproba = idproba;
        this.puncte = puncte;
    }

    public Rezultat(Long id, Long idparticipant, Long idproba, int puncte) {
        this.id = id;
        this.idparticipant = idparticipant;
        this.idproba = idproba;
        this.puncte = puncte;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Long getIdparticipant() {
        return idparticipant;
    }

    public Long getIdproba() {
        return idproba;
    }

    public int getPuncte() {
        return puncte;
    }

    public void setIdparticipant(Long idparticipant) {
        this.idparticipant = idparticipant;
    }

    public void setIdproba(Long idproba) {
        this.idproba = idproba;
    }
    public void setPuncte(int puncte) {
        this.puncte = puncte;
    }

    @Override
    public String toString() {
        return "Rezultat{" +
                "idparticipant=" + idparticipant +
                ", idproba=" + idproba +
                ", puncte=" + puncte +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Rezultat rezultat = (Rezultat) o;
        return puncte == rezultat.puncte && Objects.equals(id, rezultat.id) && Objects.equals(idparticipant, rezultat.idparticipant) && Objects.equals(idproba, rezultat.idproba);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), id, idparticipant, idproba, puncte);
    }
}
