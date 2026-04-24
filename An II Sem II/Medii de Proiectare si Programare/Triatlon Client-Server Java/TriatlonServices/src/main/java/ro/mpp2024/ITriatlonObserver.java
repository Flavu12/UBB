package ro.mpp2024;

import java.util.Optional;

public interface ITriatlonObserver {
    void updatedParticipant(Iterable<Participant> allParticipanti) throws TriatlonException;
    void updatedRezultate(Iterable<Rezultat> updatedRezultate) throws TriatlonException;



}
