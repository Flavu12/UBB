package ro.mpp2024;

import ro.mpp2024.Repo.Utils.ParticipantRepository;
import ro.mpp2024.Repo.Utils.ProbaRepository;
import ro.mpp2024.Repo.Utils.ArbitruRepository;
import ro.mpp2024.Repo.Utils.RezultatRepository;
import ro.mpp2024.utils.AbstractServer;
import ro.mpp2024.utils.TriatlonRpcConcurrentServer;

import java.io.IOException;
import java.rmi.ServerException;
import java.util.Properties;

public class StartRcpServer {
    private static int defaultPort = 55555;

    public static void main(String[] args) {
        Properties serverProps = new Properties();
        try {
            serverProps.load(StartRcpServer.class.getResourceAsStream("/bd.properties"));
            System.out.println("Server properties set. ");
            serverProps.list(System.out);

            // Get database connection details
            String url = serverProps.getProperty("jdbc.url");
            String username = serverProps.getProperty("jdbc.username");
            String password = serverProps.getProperty("jdbc.password");

            // Initialize repositories
            ParticipantRepository participantRepository = new ParticipantRepository(url, username, password);
            ProbaRepository probaRepository = new ProbaRepository(url, username, password);
            ArbitruRepository arbitruRepository = new ArbitruRepository(url, username, password);
            RezultatRepository rezultatRepository = new RezultatRepository(url, username, password);

            // Initialize service
            ITriatlonServices triatlonServices = new TriatlonServicesImpl(participantRepository, probaRepository, arbitruRepository, rezultatRepository);

            int serverPort = defaultPort;
            try {
                serverPort = Integer.parseInt(serverProps.getProperty("ro.mpp2024.port"));
            } catch (NumberFormatException nef) {
                System.err.println("Wrong Port Number" + nef.getMessage());
                System.err.println("Using default port " + defaultPort);
            }
            System.out.println("Starting server on port: " + serverPort);

            AbstractServer server = new TriatlonRpcConcurrentServer(serverPort, triatlonServices);
            try{
                try {
                    server.start();
                } catch (ro.mpp2024.utils.ServerException e) {
                    throw new RuntimeException(e);
                }
            } finally {
                try {
                    server.stop();
                } catch (ro.mpp2024.utils.ServerException e) {
                    throw new RuntimeException(e);
                }
            }
        } catch (IOException e) {
            System.err.println("Cannot find bd.properties " + e);
            return;
        }
    }
}