package ro.mpp2024;

import java.util.Optional;
import java.rmi.Remote;


public interface ITriatlonServices extends Remote {
    Arbitru login(Arbitru arbitru, ITriatlonObserver client) throws TriatlonException;


    public Optional<Arbitru> findAccount(String username, String password);

    public Iterable<Arbitru> findAllArbitri();

    public Optional<Participant> findParticipant(Long id);

    public Iterable<Participant> findAllParticipants();

    public Optional<Participant> updateParticipant(Participant entity);

    public void addRezultat(Long idparticipant, Long idproba, int puncte);

    public Iterable<Rezultat> findAllRezultate();

    public void updateRezultat(Long idparticipant, Long idproba, int puncte);

    public

    void logout(Arbitru arbitru) throws TriatlonException;
}

