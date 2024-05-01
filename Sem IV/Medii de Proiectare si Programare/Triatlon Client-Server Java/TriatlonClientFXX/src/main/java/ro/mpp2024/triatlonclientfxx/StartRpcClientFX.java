package ro.mpp2024.triatlonclientfxx;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import ro.mpp2024.ITriatlonServices;
import ro.mpp2024.rpcprotocol.TriatlonServicesRpcProxy;
import ro.mpp2024.triatlonclientfxx.gui.AppController;
import ro.mpp2024.triatlonclientfxx.gui.LoginController;


import java.io.IOException;
import java.util.Properties;

public class StartRpcClientFX extends Application {
    private Stage primaryStage;

    private static int defaultContestPort = 55555;
    private static String defaultServer = "localhost";


    @Override
    public void start(Stage primaryStage) throws Exception {
        System.out.println("In start");
        Properties clientProps = new Properties();
        try {
            clientProps.load(StartRpcClientFX.class.getResourceAsStream("/ro/mpp2024/triatlonclientfxx/bd.properties"));
            System.out.println("Client properties set. ");
            clientProps.list(System.out);
        } catch (IOException e) {
            System.err.println("Cannot find bd.properties " + e);
            return;
        }
        String serverIP = clientProps.getProperty("ro.mpp2024.host", defaultServer);
        int serverPort = defaultContestPort;

        try {
            serverPort = Integer.parseInt(clientProps.getProperty("ro.mpp2024.port"));
        } catch (NumberFormatException ex) {
            System.err.println("Wrong port number " + ex.getMessage());
            System.out.println("Using default port: " + defaultContestPort);
        }
        System.out.println("Using server IP " + serverIP);
        System.out.println("Using server port " + serverPort);

        ITriatlonServices server = new TriatlonServicesRpcProxy(serverIP, serverPort);

        FXMLLoader loginLoader = new FXMLLoader(getClass().getClassLoader().getResource("ro/mpp2024/triatlonclientfxx/login-table.fxml"));
        Parent loginRoot = loginLoader.load();

        LoginController loginCtrl = loginLoader.<LoginController>getController();
        loginCtrl.setServer(server);
        loginCtrl.setupLoginController(); // Call the setupLoginController method here


        FXMLLoader mainLoader = new FXMLLoader(getClass().getClassLoader().getResource("ro/mpp2024/triatlonclientfxx/main-table.fxml"));
        Parent mainContestParent = mainLoader.load();

        AppController appCtrl = mainLoader.<AppController>getController();
        appCtrl.setServer(server);

        loginCtrl.setParent(mainContestParent);
        loginCtrl.setAppController(appCtrl); // Ensure AppController is set before login attempt

        primaryStage.setTitle("Triatlon");
        primaryStage.setScene(new Scene(loginRoot, 600, 600));
        primaryStage.show();
    }
}
