package ro.mpp2024.triatlonclientfxx.gui;

import javafx.application.Platform;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.concurrent.Task;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.control.*;
import javafx.stage.Stage;
import ro.mpp2024.*;

import java.io.IOException;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

public class AppController implements ITriatlonObserver {

    private ITriatlonServices server;

    private Arbitru loggedInArbitru;

    @FXML
    private ListView<String> participantListView;

    @FXML
    private ListView<String> arbitruListView;

    @FXML
    private Label loggedInArbitruLabel;

    @FXML
    private TextField pointsTextField;


    @FXML
    private Label pointsLabel;


    @FXML
    private ListView<String> probaListView;

    @FXML
    private Button closeButton;

    public void loadProbaData() {
        Platform.runLater(() -> {
            Long probaId = loggedInArbitru.getProbaId();
            var participants = StreamSupport.stream(server.findAllRezultate().spliterator(), false) // get all results
                    .filter(r -> r.getIdproba().equals(probaId)) // filter results by probaId
                    .map(r -> {
                        Participant p = server.findParticipant(r.getIdparticipant()).orElseThrow(() -> new RuntimeException("Participant not found"));
                        return p.getId() + " - " + p.getNume() + " - " + r.getPuncte();
                    })
                    .sorted(Comparator.comparing(s -> Integer.parseInt(((String) s).split(" - ")[2])).reversed()) // sort by points in descending order
                    .collect(Collectors.toList());
            probaListView.getItems().clear();
            probaListView.getItems().addAll(participants);
        });
    }

    public void loadData() {
        // load participants and points
        var participants = StreamSupport.stream(server.findAllParticipants().spliterator(), false)
                .sorted(Comparator.comparing(Participant::getNume))
                .map(p -> p.getId() + " - " + p.getNume() + " - " + p.getPuncte())
                .collect(Collectors.toList());
        participantListView.getItems().setAll(participants);

        var arbitri = StreamSupport.stream(server.findAllArbitri().spliterator(), false)
                .sorted(Comparator.comparing(Arbitru::getNume))
                .map(Arbitru::getNume)
                .collect(Collectors.toList());
        arbitruListView.getItems().setAll(arbitri);
    }

    public void setLoggedInArbitru(Arbitru arbitru) {
        this.loggedInArbitru = arbitru;
        loggedInArbitruLabel.setText("Logged in as: " + loggedInArbitru.getNume() + ", responsible for proba: " + loggedInArbitru.getProbaId());
        initialize(arbitru);
    }

    public void initialize(Arbitru arbitru) {
        this.loggedInArbitru = arbitru;
        loadData();
        loadProbaData();
    }

    public void setServer(ITriatlonServices server) {
        this.server = server;
    }


    @FXML
    public void addResult(ActionEvent actionEvent){
        Task<Void> task = new Task<Void>() {
            @Override
            protected Void call() throws Exception {
                String selectedParticipant = participantListView.getSelectionModel().getSelectedItem();
                String points = pointsTextField.getText();
                if (selectedParticipant == null || points.isEmpty()) {
                    throw new RuntimeException("Please select a participant and fill in the points field!");
                }

                String[] parts = selectedParticipant.split(" - ");
                Long participantId = Long.parseLong(parts[0]);
                Long probaId = loggedInArbitru.getProbaId(); // get probaId from loggedInArbitru

                try {
                    int pointsValue = Integer.parseInt(points);
                    server.addRezultat(participantId, probaId, pointsValue);
                } catch (NumberFormatException e) {
                    throw new RuntimeException("Invalid number format for points!");
                } catch (Exception e) {
                    throw new RuntimeException("Failed to add result: " + e.getMessage());
                }
                return null;
            }
        };

        task.setOnSucceeded(e -> {
            loadData();
            loadProbaData();
        });

        task.setOnFailed(e -> {
            Throwable exception = task.getException();
            System.out.println("Add result error " + exception);
        });

        new Thread(task).start();
    }

    @FXML
    public void modifyPoints(ActionEvent actionEvent) {
        Task<Void> task = new Task<Void>() {
            @Override
            protected Void call() throws Exception {
                System.out.println("ModifyPoints: Starting task");
                String selectedParticipant = probaListView.getSelectionModel().getSelectedItem();
                String points = pointsTextField.getText();
                if (selectedParticipant == null || points.isEmpty()) {
                    throw new RuntimeException("Please select a participant and fill in the points field!");
                }

                String[] parts = selectedParticipant.split(" - ");
                Long participantId = Long.parseLong(parts[0]);
                Long probaId = loggedInArbitru.getProbaId(); // get probaId from loggedInArbitru

                try {
                    int pointsValue = Integer.parseInt(points);
                    System.out.println("ModifyPoints: Modifying points for participantId: " + participantId + ", probaId: " + probaId + ", points: " + pointsValue);
                    server.updateRezultat(participantId, probaId, pointsValue);
                } catch (Exception e) {
                    System.out.println("Exception occurred during update: " + e.getMessage());
                    e.printStackTrace();
                }
                return null;
            }
        };

        task.setOnSucceeded(e -> {
            System.out.println("ModifyPoints: Task succeeded");
            loadData();
            loadProbaData();
        });

        task.setOnFailed(e -> {
            Throwable exception = task.getException();
            System.out.println("Modify points error " + exception);
        });

        new Thread(task).start();
    }

    @FXML
    private void Logout(ActionEvent actionEvent) {
        Task<Void> task = new Task<Void>() {
            @Override
            protected Void call() throws Exception {
                try {
                    server.logout(loggedInArbitru);
                } catch (TriatlonException e) {
                    throw new RuntimeException(e);
                }
                return null;
            }
        };

        task.setOnSucceeded(e -> {

            Node src = (Node) actionEvent.getSource();
            Stage stage = (Stage) src.getScene().getWindow();
            stage.close();
            MessageAlert.showMessage(null, Alert.AlertType.INFORMATION, "Logout successful!");
        });

        task.setOnFailed(e -> {
            Throwable exception = task.getException();
            System.out.println("Logout error " + exception);
        });

        new Thread(task).start();
    }



    @Override
    public void updatedParticipant(Iterable<Participant> allParticipanti) {
        Platform.runLater(() -> {
            loadData();
            loadProbaData();
        });
    }

    @Override
    public void updatedRezultate(Iterable<Rezultat> updatedRezultate) throws TriatlonException {
        Platform.runLater(() -> {
            loadData();
            loadProbaData();
        });
    }


    public void logout() {
        try {
            server.logout(loggedInArbitru);
        } catch (TriatlonException e) {
            throw new RuntimeException(e);
        }
    }

}
