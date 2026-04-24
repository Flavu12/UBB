package ro.mpp2024;
import ro.mpp2024.Repo.Utils.ArbitruRepository;
import ro.mpp2024.Repo.Utils.ParticipantRepository;
import ro.mpp2024.Repo.Utils.ProbaRepository;
import ro.mpp2024.Repo.Utils.RezultatRepository;

import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class TriatlonServicesImpl implements ITriatlonServices{
    private ParticipantRepository repositoryParticipant;
    private ProbaRepository repositoryProba;
    private ArbitruRepository repositoryArbitru;
    private RezultatRepository repositoryRezultat;
    //arbitru logat
    private Map<String, List<ITriatlonObserver>> arbitruLogat;
    private List<ITriatlonObserver> observers = new ArrayList<>();



    public TriatlonServicesImpl(ParticipantRepository repositoryParticipant, ProbaRepository repositoryProba, ArbitruRepository repositoryArbitru, RezultatRepository repositoryRezultat) {
        this.repositoryParticipant = repositoryParticipant;
        this.repositoryProba = repositoryProba;
        this.repositoryArbitru = repositoryArbitru;
        this.repositoryRezultat = repositoryRezultat;
        arbitruLogat = new HashMap<>();
    }

    private int defaultThreads = 5;

    @Override
    public Optional<Arbitru> findAccount(String username, String password) {
        return repositoryArbitru.findAccount(username, password);
    }

    @Override
    public Iterable<Arbitru> findAllArbitri() {
        return repositoryArbitru.findAll();
    }


    @Override
    public Optional<Participant> findParticipant(Long id) {
        return repositoryParticipant.findOne(id);
    }

    @Override
    public Iterable<Participant> findAllParticipants() {
        return repositoryParticipant.findAll();
    }

    //notify all observers
    private void notify(Participant participant) {
        ExecutorService executor = Executors.newFixedThreadPool(defaultThreads);
        for (Map.Entry<String, List<ITriatlonObserver>> entry : arbitruLogat.entrySet()) {
            for (ITriatlonObserver observer : entry.getValue()) {
                executor.execute(() -> {
                    try {
                        System.out.println("Notifying observer " + observer);
                        observer.updatedParticipant(Collections.singletonList(participant));
                    } catch (TriatlonException e) {
                        System.err.println("Error notifying observer " + observer);
                    }
                });
            }
        }
        executor.shutdown();
    }

    @Override
    public Optional<Participant> updateParticipant(Participant entity) {
        notify(entity);
       return repositoryParticipant.update(entity);
    }

    @Override
    public void addRezultat(Long idparticipant, Long idproba, int puncte) {
        // Crearea unui nou rezultat
        Rezultat rezultat = new Rezultat(idparticipant, idproba, puncte);

        // Adăugarea rezultatului în repository
        repositoryRezultat.save(rezultat);

        // Găsirea participantului în repository
        Optional<Participant> participantOptional = repositoryParticipant.findOne(idparticipant);

        // Verificarea dacă participantul există
        if (!participantOptional.isPresent()) {
            throw new RuntimeException("Participant not found");
        }

        // Actualizarea punctelor participantului
        Participant participant = participantOptional.get();
        participant.setPuncte(participant.getPuncte() + puncte);

        // Salvarea participantului actualizat în repository
        repositoryParticipant.update(participant);

        // Notificarea tuturor observatorilor despre actualizarea participantului
        notify(participant);
    }

    @Override
    public Iterable<Rezultat> findAllRezultate() {
        return repositoryRezultat.findAll();
    }


    @Override
    public void updateRezultat(Long idparticipant, Long idproba, int puncte) {
        Rezultat rezultat = new Rezultat(idparticipant, idproba, puncte);
        Optional<Rezultat> updatedRezultat = repositoryRezultat.update(rezultat);
        if (updatedRezultat.isEmpty()) {
            throw new RuntimeException("Failed to update result");
        }
        Participant participant = findParticipant(idparticipant).orElseThrow(() -> new RuntimeException("Participant not found"));
        notify(participant);
    }

    @Override
    public Arbitru login(Arbitru arbitru, ITriatlonObserver client) throws TriatlonException {
        Optional<Arbitru> arbitru1 = repositoryArbitru.findAccount(arbitru.getUsername(), arbitru.getPassword());
        if(arbitru1.isEmpty())
            throw new TriatlonException("Authentication failed.");

        // Check if any clients are already logged in with the given username
        if (arbitruLogat.containsKey(arbitru.getUsername())) {
            throw new TriatlonException("User already logged in.");
        }

        arbitruLogat.put(arbitru.getUsername(), new ArrayList<>());
        arbitruLogat.get(arbitru.getUsername()).add(client);
        observers.add(client); // Add the client as an observer
        return arbitru1.get(); // Return the Arbitru object
    }

    @Override
    public void logout(Arbitru arbitru) throws TriatlonException {
        System.out.println("logout method in TriatlonServicesImpl called");
        if (!arbitruLogat.containsKey(arbitru.getUsername())) {
            throw new TriatlonException("User not logged in.");
        }

        arbitruLogat.remove(arbitru.getUsername());
    }


}
