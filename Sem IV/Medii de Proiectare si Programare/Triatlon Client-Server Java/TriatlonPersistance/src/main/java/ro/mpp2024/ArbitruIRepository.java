package ro.mpp2024;


import java.util.Optional;

public interface ArbitruIRepository<ID, E extends Entity<ID>> extends Repository<Long, Arbitru>{
    //find account by username and password
    Optional<Arbitru> findAccount(String username, String password);


}
