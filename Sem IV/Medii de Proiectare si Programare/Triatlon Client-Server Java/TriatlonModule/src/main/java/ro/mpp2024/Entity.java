package ro.mpp2024;

import java.io.Serializable;
import java.util.Objects;

public class Entity<ID> implements Serializable {
    protected ID id;
    public ID getId() {
        return id;
    }
    public void setId(ID id) {
        this.id = id;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Entity<?> entity)) return false;
        return Objects.equals(id, entity.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }

    @Override
    public String toString() {
        return "Entity{" +
                "id=" + id +
                '}';
    }

}
