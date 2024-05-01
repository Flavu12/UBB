package ro.mpp2024.rpcprotocol;

import ro.mpp2024.*;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.Collections;
import java.util.Optional;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.stream.StreamSupport;

public class TriatlonServicesRpcProxy implements ITriatlonServices {
    private String host;
    private int port;

    private ITriatlonObserver client;

    private ObjectInputStream input;
    private ObjectOutputStream output;
    private Socket connection;

    private BlockingQueue<Response> qresponses;
    private volatile boolean finished;

    public TriatlonServicesRpcProxy(String host, int port) {
        this.host = host;
        this.port = port;
        qresponses = new LinkedBlockingQueue<Response>();
    }

    private void closeConnection() {
        finished = true;
        try {
            input.close();
            output.close();
            connection.close();
            client = null;
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void sendRequest(Request request) throws TriatlonException {
        try {
            output.writeObject(request);
            output.flush();
        } catch (IOException e) {
            throw new TriatlonException("Error sending object " + e);
        }
    }

    private Response readResponse() throws TriatlonException {
        Response response = null;
        try {
            response = qresponses.take();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return response;
    }

    private void initializeConnection() throws TriatlonException {
        try {
            connection=new Socket(host,port);
            output=new ObjectOutputStream(connection.getOutputStream());
            output.flush();
            input=new ObjectInputStream(connection.getInputStream());
            finished=false;
            startReader();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void startReader() {
        Thread tw = new Thread(new ReaderThread());
        tw.start();
    }

    private void handleUpdate(Response response) {
        if (response.type() == ResponseType.UPDATE) {
            System.out.println("Update received " + response.type());
            try {
                client.updatedParticipant((Iterable<Participant>) response.data());
            } catch (TriatlonException e) {
                e.printStackTrace();
            }
        }
    }

    private boolean isUpdate(Response response) {
        return response.type() == ResponseType.UPDATE;
    }

    @Override
    public Arbitru login(Arbitru arbitru, ITriatlonObserver client) throws TriatlonException {
        initializeConnection();
        Request req = new Request.Builder().type(RequestType.LOGIN).data(arbitru).build();
        sendRequest(req);
        Response response = readResponse();
        if (response.type() == ResponseType.OK) {
            if (response.data() != null) {
                this.client = client;
                return (Arbitru) response.data(); // Cast the response data to Arbitru and return it
            } else {
                throw new TriatlonException("Received null data in OK response");
            }
        }
        if (response.type() == ResponseType.ERROR) {
            String err = (String) response.data();
            throw new TriatlonException(err);
        }
        throw new TriatlonException("Received unknown response type");
    }


    @Override
    public Optional<Arbitru> findAccount(String username, String password) {
        Request request = new Request.Builder().type(RequestType.FIND_ACCOUNT).data(username + " " + password).build();
        try {
            sendRequest(request);
        } catch (TriatlonException e) {
            throw new RuntimeException(e);
        }
        Response response = null;
        try {
            response = readResponse();
        } catch (TriatlonException e) {
            throw new RuntimeException(e);
        }
        if (response.type() == ResponseType.ERROR) {
            return Optional.empty();
        }
        if (response.data() == null) {
            throw new RuntimeException("Received null data in OK response");
        }
        return Optional.of((Arbitru) response.data());
    }


    @Override
    public Iterable<Arbitru> findAllArbitri() {
        Request request = new Request.Builder().type(RequestType.FIND_ALL_ARBITRI).build();
        try {
            sendRequest(request);
        } catch (TriatlonException e) {
            throw new RuntimeException(e);
        }
        Response response = null;
        try {
            response = readResponse();
        } catch (TriatlonException e) {
            throw new RuntimeException(e);
        }
        if (response.type() == ResponseType.ERROR) {
            return Collections.emptyList();
        }
        return (Iterable<Arbitru>) response.data();
    }

    @Override
    public Optional<Participant> findParticipant(Long id) {
        Request request = new Request.Builder().type(RequestType.FIND_PARTICIPANT).data(id).build();
        try {
            sendRequest(request);
        } catch (TriatlonException e) {
            throw new RuntimeException(e);
        }
        Response response = null;
        try {
            response = readResponse();
        } catch (TriatlonException e) {
            throw new RuntimeException(e);
        }
        if (response.type() == ResponseType.ERROR) {
            return Optional.empty();
        }
        return Optional.of((Participant) response.data());
    }

    @Override
    public Iterable<Participant> findAllParticipants() {
        Request request = new Request.Builder().type(RequestType.FIND_ALL_PARTICIPANTS).build();
        try {
            sendRequest(request);
        } catch (TriatlonException e) {
            throw new RuntimeException(e);
        }
        Response response = null;
        try {
            response = readResponse();
        } catch (TriatlonException e) {
            throw new RuntimeException(e);
        }
        if (response.type() == ResponseType.ERROR) {
            return Collections.emptyList();
        }
        return (Iterable<Participant>) response.data();
    }

    @Override
    public Optional<Participant> updateParticipant(Participant entity) {
        Request request = new Request.Builder().type(RequestType.UPDATE_PARTICIPANT).data(entity).build();
        try {
            sendRequest(request);
            Response response = readResponse();
            if (response.type() == ResponseType.ERROR) {
                return Optional.empty();
            }
            // Notify the client about the changes
            client.updatedParticipant(findAllParticipants());
            client.updatedRezultate(findAllRezultate());
            return Optional.of((Participant) response.data());
        } catch (TriatlonException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void updateRezultat(Long idparticipant, Long idproba, int puncte) {
        Request request = new Request.Builder().type(RequestType.UPDATE_REZULTAT).data(idparticipant + " " + idproba + " " + puncte).build();
        try {
            sendRequest(request);
            Response response = readResponse();
            if (response.type() == ResponseType.ERROR) {
                throw new TriatlonException((String) response.data());
            }

            // Fetch the participant
            Optional<Participant> participantOpt = findParticipant(idparticipant);
            if (participantOpt.isPresent()) {
                Participant participant = participantOpt.get();

                // Update the participant's total points
                // This depends on how you calculate the total points
                // For example, if total points is the sum of all results:
                Iterable<Rezultat> allRezultate = findAllRezultate();
                int totalPoints = StreamSupport.stream(allRezultate.spliterator(), false)
                        .filter(r -> r.getIdparticipant().equals(idparticipant))
                        .mapToInt(Rezultat::getPuncte)
                        .sum();

                participant.setPuncte(totalPoints);

                // Update the participant in the database
                updateParticipant(participant);

                // Notify the client about the changes
                client.updatedParticipant(findAllParticipants());
                client.updatedRezultate(findAllRezultate());
            }
        } catch (TriatlonException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public void addRezultat(Long idparticipant, Long idproba, int puncte) {
        Request request = new Request.Builder().type(RequestType.ADD_REZULTAT).data(new Rezultat(idparticipant, idproba, puncte)).build();
        try {
            sendRequest(request);
            Response response = readResponse();
            if (response.type() == ResponseType.ERROR) {
                throw new TriatlonException((String) response.data());
            }
        } catch (TriatlonException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Iterable<Rezultat> findAllRezultate() {
        Request request = new Request.Builder().type(RequestType.FIND_ALL_REZULTATE).build();
        try {
            sendRequest(request);
        } catch (TriatlonException e) {
            throw new RuntimeException(e);
        }
        Response response = null;
        try {
            response = readResponse();
        } catch (TriatlonException e) {
            throw new RuntimeException(e);
        }
        if (response.type() == ResponseType.ERROR) {
            return Collections.emptyList();
        }
        return (Iterable<Rezultat>) response.data();
    }


    private class ReaderThread implements Runnable{
        public void run() {
            while(!finished){
                try {
                    Object response=input.readObject();
                    if (response instanceof Response) {
                        System.out.println("response received "+response);
                        if (isUpdate((Response)response)){
                            handleUpdate((Response)response);
                        }else{
                            try {
                                qresponses.put((Response)response);
                            } catch (InterruptedException e) {
                                e.printStackTrace();
                            }
                        }
                    } else {
                        System.out.println("Unexpected object received: " + response);
                    }
                } catch (IOException e) {
                    System.out.println("Reading error "+e);
                } catch (ClassNotFoundException e) {
                    System.out.println("Reading error "+e);
                }
            }
        }
    }



    public void logout(Arbitru arbitru) throws TriatlonException {
        Request req = new Request.Builder().type(RequestType.LOGOUT).data(arbitru).build();
        sendRequest(req);

        Response response = readResponse();
        closeConnection();

        if (response.type()== ResponseType.ERROR){
            throw new TriatlonException("");
        }
        else{
            System.out.println("Successfully logged out!");

        }
    }
}