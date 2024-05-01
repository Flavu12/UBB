package ro.mpp2024;

import java.util.Objects;

public class Proba extends Entity<Long> {

    private Long id;
    private String nume;

    private Long idparticipanti;



    public Proba(String nume, Long idparticipanti) {
        this.nume = nume;
        this.idparticipanti = idparticipanti;
    }

    public Proba(Long id, String nume, Long idparticipanti) {
        this.id = id;
        this.nume = nume;
        this.idparticipanti = idparticipanti;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNume() {
        return nume;
    }

    public Long getIdparticipanti() {
        return idparticipanti;
    }
    public void setNume(String nume) {
        this.nume = nume;
    }

    public void setIdparticipanti(Long idparticipanti) {
        this.idparticipanti = idparticipanti;
    }
    @Override
    public String toString() {
        return "Proba{" +
                "nume='" + nume + '\'' +
                ", idparticipanti=" + idparticipanti +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Proba proba = (Proba) o;
        return Objects.equals(id, proba.id) && Objects.equals(nume, proba.nume) && Objects.equals(idparticipanti, proba.idparticipanti);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, nume, idparticipanti);
    }
}
