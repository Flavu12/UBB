package ro.mpp2024.triatlonclientfxx.gui;

import javafx.application.Platform;
import javafx.concurrent.Task;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.stage.Stage;
import javafx.stage.WindowEvent;
import ro.mpp2024.*;
import ro.mpp2024.triatlonclientfxx.gui.AppController;

import java.io.IOException;
import java.util.Optional;

public class LoginController implements ITriatlonObserver {
    private ITriatlonServices server;
    private AppController appController;
    private Arbitru loggedInArbitru;
    Parent mainContestParent;

    @FXML
    private TextField usernameField;

    @FXML
    private PasswordField passwordField;

    public void setServer(ITriatlonServices s){
        if (s == null) {
            throw new IllegalArgumentException("Server cannot be null");
        }
        server=s;
    }

    public void setLoggedInArbitru(Arbitru arbitru) {
        this.loggedInArbitru = arbitru;
    }

    public void setParent(Parent p){
        mainContestParent=p;
    }

    @Override
    public void updatedParticipant(Iterable<Participant> allParticipanti) throws TriatlonException {
        // do nothing
    }

    @Override
    public void updatedRezultate(Iterable<Rezultat> updatedRezultate) throws TriatlonException {
        // do nothing
    }

    public void setupLoginController() {
        // Create the AppController
        AppController appController = new AppController();
        // Set the server for the AppController
        appController.setServer(server);

        // Create the LoginController
        LoginController loginController = new LoginController();
        // Set the server and AppController for the LoginController
        loginController.setServer(server);
        loginController.setAppController(appController);

        // Now when the login button is clicked, the AppController should be properly initialized
    }

    @FXML
    private void LoginButton(ActionEvent event) {
        String username = usernameField.getText();
        String password = passwordField.getText();
        loggedInArbitru = new Arbitru(username, password);

        Task<Void> task = new Task<Void>() {
            @Override
            protected Void call() throws Exception {
                try {
                    loggedInArbitru = server.login(loggedInArbitru, appController); // Use the returned Arbitru object


                } catch (TriatlonException e) {
                    throw new RuntimeException(e);
                }
                return null;
            }
        };

        task.setOnSucceeded(e -> {
            Stage stage = new Stage();
            stage.setTitle("Bine ai venit, " + loggedInArbitru.getUsername() + "!");
            stage.setScene(new Scene(mainContestParent));

            stage.setOnCloseRequest(new EventHandler<WindowEvent>() {
                @Override
                public void handle(WindowEvent event) {
                    appController.logout();
                    System.exit(0);
                }
            });

            stage.show();
            appController.setLoggedInArbitru(loggedInArbitru); // Pass the loggedInArbitru to the AppController
            ((Node)(event.getSource())).getScene().getWindow().hide();
        });

        task.setOnFailed(e -> {
            Throwable exception = task.getException();
            Alert alert = new Alert(Alert.AlertType.INFORMATION);
            alert.setTitle("MPP chat");
            alert.setHeaderText("Authentication failure");
            alert.setContentText("Failed to login: " + exception.getMessage());
            alert.showAndWait();
        });

        new Thread(task).start();
    }

    public void setAppController(AppController appController) {
        this.appController = appController;
    }


}