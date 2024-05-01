package ro.mpp2024.triatlonclientfxx.gui;

import javafx.scene.control.Alert;
import javafx.stage.Stage;

public class MessageAlert
{
    public static void showMessage(Stage Owner, Alert.AlertType type, String text){
        Alert message=new Alert(type);
        message.initOwner(Owner);
        message.setTitle("Mesaj");
        message.setContentText(text);
        message.showAndWait();
    }
    public static void showErrorMessage(Stage Owner, String text){
        Alert message=new Alert(Alert.AlertType.ERROR);
        message.initOwner(Owner);
        message.setTitle("Mesaj eroare");
        message.setContentText(text);
        message.showAndWait();
    }
}
