package ro.mpp2024;

public class Arbitru extends Entity<Long>{
    private String nume;
    private String username;

    private Long probaId;

    private String password;



    public Arbitru(Long id, String nume, String username, String password, Long probaId) {
        this.setId(id);
        this.nume = nume;
        this.username = username;
        this.password = password;
        this.probaId = probaId;
    }
    public Arbitru(String username, String password) {
        this.setId(id);
        this.username = username;
        this.password = password;
    }


    public Arbitru(String nume, String username, String password, Long probaId) {
        this.nume = nume;
        this.username = username;
        this.password = password;
        this.probaId = probaId;
    }

    public String getNume() {
        return nume;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Long getProbaId() {
        return probaId;
    }

    public void setProbaId(Long probaId) {
        this.probaId = probaId;
    }

    @Override
    public String toString() {
        return "Arbitru{" +
                "id=" + getId() +
                ", nume='" + nume + '\'' +
                ", username='" + username + '\'' +
                ", password='" + password + '\'' +
                ", probaId='" + probaId + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Arbitru arbitru)) return false;
        return nume.equals(arbitru.nume) && username.equals(arbitru.username) && password.equals(arbitru.password) && probaId.equals(arbitru.probaId);
    }

    @Override
    public int hashCode() {
        return nume.hashCode() + username.hashCode() + password.hashCode() + probaId.hashCode();
    }


}
