package ro.mpp2024.Repo.Utils;

import ro.mpp2024.ProbaIRepository;
import ro.mpp2024.Proba;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class ProbaRepository implements ProbaIRepository<Long, Proba> {
    String url;
    String username;
    String password;

    public ProbaRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Optional<Proba> findOne(Long aLong) {
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("SELECT * FROM proba WHERE id = ? ");
        ){
            preparedStatement.setLong(1,aLong);
            ResultSet resultSet = preparedStatement.executeQuery();
            if(resultSet.next())
            {
                String nume = resultSet.getString("nume");
                Long idparticipanti = resultSet.getLong("id_participant");
                Proba proba = new Proba(nume,idparticipanti);
                proba.setId(aLong);
                return Optional.of(proba);
            }

            return Optional.empty();
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Iterable<Proba> findAll() {
        List<Proba> probaList = new ArrayList<>();
        try(Connection connection= DriverManager.getConnection(this.url,this.username,this.password);
            PreparedStatement preparedStatement=connection.prepareStatement("SELECT * FROM proba");
        ){
            ResultSet resultSet = preparedStatement.executeQuery();
            while(resultSet.next())
            {
                //participanti
                String nume = resultSet.getString("nume");
                Long idparticipanti = resultSet.getLong("id_participant");
                Proba proba = new Proba(nume,idparticipanti);
                probaList.add(proba);
            }
            return probaList;
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Optional<Proba> save(Proba entity) {
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("INSERT INTO proba(nume,id_participant) VALUES (?,?)");
        ){
            preparedStatement.setString(1,entity.getNume());
            preparedStatement.setLong(2,entity.getIdparticipanti());
            preparedStatement.executeUpdate();
            return Optional.empty();
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Optional<Proba> delete(Long aLong) {
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("DELETE FROM proba WHERE id = ?");
        ){
            preparedStatement.setLong(1,aLong);
            preparedStatement.executeUpdate();
            return Optional.empty();
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Optional<Proba> update(Proba entity) {
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("UPDATE proba SET nume = ?, id_participant = ? WHERE id = ?");
        ){
            preparedStatement.setString(1,entity.getNume());
            preparedStatement.setLong(2,entity.getIdparticipanti());
            preparedStatement.setLong(3,entity.getId());
            preparedStatement.executeUpdate();
            return Optional.empty();
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }


}
