package ro.mpp2024.Repo.Utils;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import ro.mpp2024.ParticipantIRepository;
import ro.mpp2024.Participant;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class ParticipantRepository implements ParticipantIRepository<Long,Participant> {

    String url;

    String username;

    String password;

    private static final Logger LOGGER = LogManager.getLogger();

    public ParticipantRepository(String url, String username, String password) {
        LOGGER.info("Initializing ParticipantRepository with properties: {} ",url);
        this.url = url;
        this.username = username;
        this.password = password;
    }
    @Override
    public Optional<Participant> findOne(Long aLong) {
        LOGGER.traceEntry("finding participant with id {} ",aLong);
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("SELECT * FROM participant WHERE id = ? ");
        ){
            preparedStatement.setLong(1,aLong);
            ResultSet resultSet = preparedStatement.executeQuery();
            if(resultSet.next())
            {
                Long idParticipant=resultSet.getLong("id");
                String nume = resultSet.getString("nume");
                int puncte = resultSet.getInt("puncte");
                Participant participant = new Participant(idParticipant,nume, puncte);
                participant.setId(aLong);
                LOGGER.trace("Found {}",participant);
                LOGGER.traceExit();
                return Optional.of(participant);
            }

            return Optional.empty();
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Iterable<Participant> findAll() {
        LOGGER.traceEntry();
        List<Participant> participantList = new ArrayList<>();
        try(Connection connection= DriverManager.getConnection(this.url,this.username,this.password);
            PreparedStatement preparedStatement=connection.prepareStatement("SELECT * FROM participant");

        ){
            ResultSet resultSet = preparedStatement.executeQuery();
            while(resultSet.next())
            {
                Long id=resultSet.getLong("id");
                String nume = resultSet.getString("nume");
                int puncte = resultSet.getInt("puncte");
                Participant participant = new Participant(id,nume, puncte);
                participantList.add(participant);
            }
            LOGGER.trace("Found {} instances", participantList.size());
            LOGGER.traceExit();
            return participantList;
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Optional<Participant> save(Participant entity) {
        LOGGER.traceEntry("saving participant {} ", entity);
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("INSERT INTO participant (nume, puncte) VALUES (?,?)");
        ){
            preparedStatement.setString(1,entity.getNume());
            preparedStatement.setInt(2,entity.getPuncte());
            preparedStatement.executeUpdate();
            LOGGER.trace("Saved {} instances", entity);
            LOGGER.traceExit("Saved {} instances", entity);
            return Optional.empty();
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }
    }

    @Override
    public Optional<Participant> delete(Long aLong) {
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("DELETE FROM participant WHERE id = ?");
        ){
            preparedStatement.setLong(1,aLong);
            int affectedRows = preparedStatement.executeUpdate();
            LOGGER.trace("Deleted {} instances", affectedRows);
            LOGGER.traceExit();
            return affectedRows == 0 ? Optional.empty() : Optional.of(new Participant(aLong,"",0));
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }

    }

    @Override
    public Optional<Participant> update(Participant entity) {
        try(Connection connection= DriverManager.getConnection(url,username,password);
            PreparedStatement preparedStatement=connection.prepareStatement("UPDATE participant SET nume = ?, puncte = ? WHERE id = ?");
        ){
            preparedStatement.setString(1,entity.getNume());
            preparedStatement.setInt(2,entity.getPuncte());
            preparedStatement.setLong(3,entity.getId());
            int affectedRows = preparedStatement.executeUpdate();
            LOGGER.trace("Updated {} instances", affectedRows);
            LOGGER.traceExit();
            return affectedRows == 0 ? Optional.empty() : Optional.of(entity);
        }
        catch (SQLException e){
            throw new RuntimeException(e);
        }

    }

}
