package ro.mpp2024.Repo.Utils;

import ro.mpp2024.Rezultat;
import ro.mpp2024.RezultatIRepository;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class RezultatRepository implements RezultatIRepository<Long, Rezultat> {
    String url;

    String username;

    String password;

    public RezultatRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }
    @Override
    public Optional<Rezultat> save(Rezultat entity) {
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("INSERT INTO rezultat (participant_id, proba_id, puncte) VALUES (?,?,?)");
        ){
            preparedStatement.setLong(1,entity.getIdparticipant());
            preparedStatement.setLong(2,entity.getIdproba());
            preparedStatement.setInt(3,entity.getPuncte());
            preparedStatement.executeUpdate();
            return Optional.empty();
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Optional<Rezultat> delete(Long id) {
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("DELETE FROM rezultat WHERE participant_id = ? AND proba_id = ?");
        ){
            preparedStatement.setLong(1,id);
            preparedStatement.executeUpdate();
            return Optional.empty();
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Optional<Rezultat> update(Rezultat entity) {
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("UPDATE rezultat SET puncte = ? WHERE participant_id = ? AND proba_id = ?");
        ){
            preparedStatement.setInt(1,entity.getPuncte());
            preparedStatement.setLong(2,entity.getIdparticipant());
            preparedStatement.setLong(3,entity.getIdproba());
            int affectedRows = preparedStatement.executeUpdate();
            if (affectedRows == 0) {
                return Optional.empty();
            } else {
                return Optional.of(entity);
            }
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Optional<Rezultat> findOne(Long id) {
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("SELECT * FROM rezultat WHERE proba_id=?");
        ){
            preparedStatement.setLong(1,id);
            int affectedRows = preparedStatement.executeUpdate();
            return affectedRows == 0 ? Optional.empty() : Optional.of(new Rezultat(id,0L,0L,0));
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Iterable<Rezultat> findAll() {
        List<Rezultat> rezultatList = new ArrayList<>();
        try(Connection connection= DriverManager.getConnection(this.url,this.username,this.password);
            PreparedStatement preparedStatement=connection.prepareStatement("SELECT * FROM rezultat");
        ){
            preparedStatement.executeQuery();
            while(preparedStatement.getResultSet().next())
            {
                Long idparticipant = preparedStatement.getResultSet().getLong("participant_id");
                Long idproba = preparedStatement.getResultSet().getLong("proba_id");
                int puncte = preparedStatement.getResultSet().getInt("puncte");
                Rezultat rezultat = new Rezultat(idparticipant,idproba,puncte);
                rezultatList.add(rezultat);
            }

            return rezultatList;
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

}
