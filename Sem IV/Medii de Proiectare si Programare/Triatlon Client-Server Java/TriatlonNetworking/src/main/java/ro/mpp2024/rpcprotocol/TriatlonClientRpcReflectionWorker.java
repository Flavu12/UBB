package ro.mpp2024.rpcprotocol;

import ro.mpp2024.*;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.Socket;
import java.sql.SQLException;
import java.util.Optional;

public class TriatlonClientRpcReflectionWorker implements Runnable, ITriatlonObserver {
    private ITriatlonServices server;
    private Socket connection;

    private ObjectInputStream input;
    private ObjectOutputStream output;
    private volatile boolean connected;

    public TriatlonClientRpcReflectionWorker(ITriatlonServices server, Socket connection) {
        this.server = server;
        this.connection = connection;
        try {
            output = new ObjectOutputStream(connection.getOutputStream());
            output.flush();
            input = new ObjectInputStream(connection.getInputStream());
            connected = true;
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void run() {
        while (connected) {
            try {
                Object request = input.readObject();
                Response response = handleRequest((Request) request);
                if (response != null) {
                    sendResponse(response);
                }
            } catch (IOException | ClassNotFoundException e) {
                e.printStackTrace();
            }

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    /*@Override
    public void updatedRezultate(Iterable<Rezultat> updatedRezultate) throws TriatlonException {
        try {
            Request request = new Request.Builder().type(RequestType.UPDATE_REZULTAT).data(updatedRezultate).build();
            sendRequest(request);
            Response response = readResponse();
            if (response.type() == ResponseType.ERROR) {
                String err = (String) response.data();
                throw new TriatlonException(err);
            }
        } catch (IOException e) {
            throw new TriatlonException("Error sending updated rezultate request " + e);
        }
    }*/

    private static Response okResponse = new Response.Builder().type(ResponseType.OK).build();

    private Response handleRequest(Request request) {
        System.out.println("Request received: " + request.type());
        Response response = null;
        String handlerName = "handle" + (request).type();
        System.out.println("HandlerName " + handlerName);
        try {
            Method method=this.getClass().getDeclaredMethod(handlerName, Request.class);
            response=(Response)method.invoke(this,request);
            System.out.println("Method "+handlerName+ " invoked");
        } catch (NoSuchMethodException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        }

        return response;
    }

    private void sendResponse(Response response) throws IOException {
        System.out.println("sending response " + response);
        synchronized (output) {
            output.writeObject(response);
            output.flush();
        }
    }

    @Override
    public void updatedParticipant(Iterable<Participant> allParticipanti) throws TriatlonException {
        // Create a Response with the updated participants
        Response response = new Response.Builder().type(ResponseType.UPDATE).data(allParticipanti).build();
        try {
            // Send the Response
            sendResponse(response);
        } catch (IOException e) {
            throw new TriatlonException("Error sending updated participant response " + e);
        }
    }

    @Override
    public void updatedRezultate(Iterable<Rezultat> updatedRezultate) throws TriatlonException {
        // Create a Response with the updated results
        Response response = new Response.Builder().type(ResponseType.UPDATE).data(updatedRezultate).build();
        try {
            // Send the Response
            sendResponse(response);
        } catch (IOException e) {
            throw new TriatlonException("Error sending updated rezultate response " + e);
        }
    }
    private void sendRequest(Request request) throws IOException {
        output.writeObject(request);
        output.flush();
    }

    private Response handleLOGIN(Request request){
        Arbitru arbitru=(Arbitru) request.data();
        try {
            server.login(arbitru, this);
            Optional<Arbitru> account = server.findAccount(arbitru.getUsername(), arbitru.getPassword());
            if (account.isPresent()) {
                return new Response.Builder().type(ResponseType.OK).data(account.get()).build();
            } else {
                return new Response.Builder().type(ResponseType.ERROR).data("Account not found").build();
            }
        } catch (TriatlonException e) {
            connected=false;
            return new Response.Builder().type(ResponseType.ERROR).data(e.getMessage()).build();
        }
    }

    //handlefind all participants
    private Response handleFIND_ALL_PARTICIPANTS(Request request){
        Iterable<Participant> allParticipanti = server.findAllParticipants();
        return new Response.Builder().type(ResponseType.OK).data(allParticipanti).build();
    }

    private Response handleFIND_PARTICIPANT(Request request){
        Long id = (Long) request.data();
        Optional<Participant> participant = server.findParticipant(id);
        return new Response.Builder().type(ResponseType.OK).data(participant.orElse(null)).build();
    }

    private Response handleFIND_ACCOUNT(Request request){
        String usernameAndPassword = (String) request.data();
        String[] tokens = usernameAndPassword.split(" ");
        Optional<Arbitru> account = server.findAccount(tokens[0], tokens[1]);
        return new Response.Builder().type(ResponseType.OK).data(account.orElse(null)).build();
    }

    private Response handleLOGOUT(Request request){
        System.out.println("Logout request...");

        Arbitru arbitru = (Arbitru) request.data();
        try {
            server.logout(arbitru);
            connected=false;
            return okResponse;

        } catch (TriatlonException e) {
            return new Response.Builder().type(ResponseType.ERROR).data(e.getMessage()).build();
        }
    }


    private Response handleFIND_ALL_ARBITRI(Request request){
        Iterable<Arbitru> allArbitri = server.findAllArbitri();
        return new Response.Builder().type(ResponseType.OK).data(allArbitri).build();
    }

    /*private Response handleFIND_ACCOUNT(Request request){
        String usernameAndPassword = (String) request.data();
        String[] tokens = usernameAndPassword.split(" ");
        Optional<Arbitru> account = server.findAccount(tokens[0], tokens[1]);
        if (account.isPresent()) {
            return new Response.Builder().type(ResponseType.OK).data(account.get()).build();
        } else {
            return new Response.Builder().type(ResponseType.ERROR).data("Account not found").build();
        }
    }*/

    private Response handleUPDATE_PARTICIPANT(Request request){
        Participant participant = (Participant) request.data();
        server.updateParticipant(participant);
        // Fetch the updated Participant from the server
        Iterable<Participant> updatedParticipanti = server.findAllParticipants();
        // Return the updated Participant in the response
        return new Response.Builder().type(ResponseType.OK).data(updatedParticipanti).build();
    }

    private Response handleADD_REZULTAT(Request request){
        Rezultat rezultat = (Rezultat) request.data();
        server.addRezultat(rezultat.getIdparticipant(), rezultat.getIdproba(), rezultat.getPuncte());
        return okResponse;
    }

    private Response handleFIND_ALL_REZULTATE(Request request){
        Iterable<Rezultat> allRezultate = server.findAllRezultate();
        return new Response.Builder().type(ResponseType.OK).data(allRezultate).build();
    }

    private Response handleUPDATE_REZULTAT(Request request){
        String[] tokens = ((String) request.data()).split(" ");
        Long idparticipant = Long.parseLong(tokens[0]);
        Long idproba = Long.parseLong(tokens[1]);
        int puncte = Integer.parseInt(tokens[2]);
        server.updateRezultat(idparticipant, idproba, puncte);

        // Fetch the updated results from the server
        Iterable<Rezultat> updatedRezultate = server.findAllRezultate();

        // Return the updated results in the response
        return new Response.Builder().type(ResponseType.OK).data(updatedRezultate).build();
    }


    private Response readResponse() throws TriatlonException {
        Response response = null;
        try {
            response = (Response) input.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return response;
    }
}