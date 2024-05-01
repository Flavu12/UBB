package ro.mpp2024.Repo.Utils;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import ro.mpp2024.Arbitru;
import ro.mpp2024.ArbitruIRepository;


import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class ArbitruRepository implements ArbitruIRepository<Long, Arbitru> {
    private String url;

    private String username;

    private String password;

    private static final Logger LOGGER = LogManager.getLogger();

    public ArbitruRepository(String url, String username, String password) {
        LOGGER.info("Initializing ArbitruRepository with properties: {} ",url);
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Optional<Arbitru> findOne(Long id) {
        LOGGER.traceEntry("finding arbitru with id {} ",id);
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("SELECT * FROM arbitru WHERE id = ? ");
        ){
            preparedStatement.setLong(1,id);
            ResultSet resultSet = preparedStatement.executeQuery();
            if(resultSet.next())
            {
                Long idArbitru=resultSet.getLong("id");
                String nume = resultSet.getString("nume");
                String username = resultSet.getString("username");
                String password = resultSet.getString("password");
                Long probaId = resultSet.getLong("probaId");
                Arbitru arbitru = new Arbitru(idArbitru, nume, username, password, probaId);
                arbitru.setId(id);
                LOGGER.trace("Found {}",arbitru);
                LOGGER.traceExit(arbitru);
                return Optional.of(arbitru);
            }

            return Optional.empty();
        }
        catch (SQLException e){
            throw new RuntimeException(e);

        }

    }

    @Override
    public Iterable<Arbitru> findAll() {
        LOGGER.traceEntry();
        List<Arbitru> arbitruList = new ArrayList<>();
        try(Connection connection= DriverManager.getConnection(this.url,this.username,this.password);
            PreparedStatement preparedStatement=connection.prepareStatement("SELECT * FROM arbitru");

        ){
            ResultSet resultSet = preparedStatement.executeQuery();
            while(resultSet.next())
            {
                Long id=resultSet.getLong("id");
                String nume = resultSet.getString("nume");
                String username = resultSet.getString("username");
                String password = resultSet.getString("password");
                Long probaId = resultSet.getLong("probaId");
                Arbitru arbitru = new Arbitru(id, nume, username, password, probaId);
                arbitru.setId(id);
                arbitruList.add(arbitru);


            }
            LOGGER.trace("Found {} instances", arbitruList.size());
            LOGGER.traceExit(arbitruList);
            return arbitruList;
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Optional<Arbitru> save(Arbitru entity) {
        LOGGER.traceEntry("saving arbitru {}",entity);
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("INSERT INTO arbitru(nume,username,password,probaId) VALUES(?,?,?)");
        ){
            preparedStatement.setString(1,entity.getNume());
            preparedStatement.setString(2,entity.getUsername());
            preparedStatement.setString(3,entity.getPassword());
            preparedStatement.setLong(4,entity.getProbaId());
            int affectedRows = preparedStatement.executeUpdate();
            LOGGER.trace("Saved {} instances", affectedRows);
            LOGGER.traceExit();
            return affectedRows == 0 ? Optional.empty() : Optional.of(entity);
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Optional<Arbitru> delete(Long id) {
        LOGGER.traceEntry("deleting arbitru with {}",id);
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("DELETE FROM arbitru WHERE id = ?");
        ){
            preparedStatement.setLong(1,id);
            int affectedRows = preparedStatement.executeUpdate();
            LOGGER.trace("Deleted {} instances", affectedRows);
            LOGGER.traceExit();
            return affectedRows == 0 ? Optional.empty() : Optional.ofNullable(null);
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Optional<Arbitru> update(Arbitru entity) {
        LOGGER.traceEntry("updating arbitru {}",entity);
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("UPDATE arbitru SET nume = ?, username = ?, password = ? WHERE id = ?");
        ){
            preparedStatement.setString(1,entity.getNume());
            preparedStatement.setString(2,entity.getUsername());
            preparedStatement.setString(3,entity.getPassword());
            preparedStatement.setLong(4,entity.getProbaId());
            preparedStatement.setLong(5,entity.getId());
            int affectedRows = preparedStatement.executeUpdate();
            LOGGER.trace("Updated {} instances", affectedRows);
            LOGGER.traceExit();
            return affectedRows == 0 ? Optional.empty() : Optional.of(entity);
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Optional<Arbitru> findAccount(String username, String password) {
        LOGGER.traceEntry("finding arbitru with username {} and password {} ",username,password);
        try(Connection connection= DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement preparedStatement=connection.prepareStatement("SELECT * FROM arbitru WHERE username = ? AND password = ?");
        ){
            preparedStatement.setString(1,username);
            preparedStatement.setString(2,password);
            ResultSet resultSet = preparedStatement.executeQuery();
            if(resultSet.next())
            {
                Long id=resultSet.getLong("id");
                String nume = resultSet.getString("nume");
                String user = resultSet.getString("username");
                String pass = resultSet.getString("password");
                Long probaId = resultSet.getLong("probaId");
                Arbitru arbitru = new Arbitru(nume, user, pass, probaId);
                arbitru.setId(id);
                LOGGER.trace("Found {}",arbitru);
                LOGGER.traceExit();
                return Optional.of(arbitru);
            }

            return Optional.empty();
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }


}
