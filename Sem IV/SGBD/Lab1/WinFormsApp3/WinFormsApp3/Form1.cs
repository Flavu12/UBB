using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace WinFormsApp3
{
    public partial class Form1 : Form
    {
        SqlConnection connection = new SqlConnection(@"Data Source=DESKTOP-OHC70B4;Database=Biblioteca;Integrated Security=true");
        SqlDataAdapter dataAdapterCarte = new SqlDataAdapter(); //obiect intermediar intre baza de date si dataset pt Carte
        DataSet dataSetCarte = new DataSet(); //container in memorie pentru datele din Carte
        SqlDataAdapter dataAdapterRecenzie = new SqlDataAdapter();
        DataSet dataSetRecenzie = new DataSet();//container in memorie pentru datele din Recenzii

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                dataAdapterCarte.SelectCommand = new SqlCommand("SELECT * FROM Carti", connection);
                dataSetCarte.Clear();
                dataAdapterCarte.Fill(dataSetCarte);
                dataGridView_Carte.DataSource = dataSetCarte.Tables[0];
            }
            catch (Exception ex)
            {
                messageToUser.Text += ex.Message;
                connection.Close();
            }

            stergereButton.Visible = false;
            actualizareButton.Visible = false;
            adaugareButton.Visible = false;
            carteIdTextBox.Enabled = false; titluTextBox.Enabled = false; descriereTextBox.Enabled = false; anAparitieTextBox.Enabled = false;
            idEdituraTextBox.Enabled = false;
            idRecenzieTextBox.Enabled = false; idCarteTextBox.Enabled = false;
        }

        //Afiseaza recenziile unei carti
        private void dataGridView_Carte_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            stergereButton.Visible = false;
            actualizareButton.Visible = false;
            adaugareButton.Visible = true;
            pozitivTextBox.Enabled = true;
            messageToUser.Text = "";
            idRecenzieTextBox.Text = ""; autorTextBox.Text = ""; pozitivTextBox.Text = ""; continutTextBox.Text = "";

            try
            {
                if (dataGridView_Carte.Rows[e.RowIndex].Cells[e.ColumnIndex].Value != null)
                {
                    dataGridView_Carte.CurrentRow.Selected = true;

                    carteIdTextBox.Text = dataGridView_Carte.Rows[e.RowIndex].Cells["id"].FormattedValue.ToString();
                    titluTextBox.Text = dataGridView_Carte.Rows[e.RowIndex].Cells["titlu"].FormattedValue.ToString();
                    descriereTextBox.Text = dataGridView_Carte.Rows[e.RowIndex].Cells["descriere"].FormattedValue.ToString();
                    anAparitieTextBox.Text = dataGridView_Carte.Rows[e.RowIndex].Cells["an_aparitie"].FormattedValue.ToString();
                    idEdituraTextBox.Text = dataGridView_Carte.Rows[e.RowIndex].Cells["id_editura"].FormattedValue.ToString();

                    idCarteTextBox.Text = carteIdTextBox.Text;

                    dataAdapterRecenzie.SelectCommand = new SqlCommand("SELECT * FROM Recenzii WHERE id_carte = @id", connection);
                    dataAdapterRecenzie.SelectCommand.Parameters.AddWithValue("@id", carteIdTextBox.Text);
                    dataSetRecenzie.Clear();
                    dataAdapterRecenzie.Fill(dataSetRecenzie);
                    dataGridView_Recenzie.DataSource = dataSetRecenzie.Tables[0];
                }
            }
            catch (Exception ex)
            {
                connection.Close();
                messageToUser.Text = ex.Message;
            }
        }

        //Afiseaza detaliite unei recenzii
        private void dataGridView_Recenzie_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            messageToUser.Text = "";
            adaugareButton.Visible = false;
            stergereButton.Visible = true;
            actualizareButton.Visible = true;

            try
            {
                if (dataGridView_Recenzie.Rows[e.RowIndex].Cells[e.ColumnIndex].Value != null)
                {
                    dataGridView_Recenzie.CurrentRow.Selected = true;

                    idRecenzieTextBox.Text = dataGridView_Recenzie.Rows[e.RowIndex].Cells["id"].FormattedValue.ToString();
                    idCarteTextBox.Text = dataGridView_Recenzie.Rows[e.RowIndex].Cells["id_carte"].FormattedValue.ToString();
                    autorTextBox.Text = dataGridView_Recenzie.Rows[e.RowIndex].Cells["autor"].FormattedValue.ToString();
                    pozitivTextBox.Text = dataGridView_Recenzie.Rows[e.RowIndex].Cells["pozitiv"].FormattedValue.ToString();
                   
                    continutTextBox.Text = dataGridView_Recenzie.Rows[e.RowIndex].Cells["continut"].FormattedValue.ToString();
                }
            }
            catch (Exception ex)
            {
                messageToUser.Text = ex.Message;
            }
        }


        //Functie de stergere a unei recenzii
        private void stergereButton_Click(object sender, EventArgs e)
        {
            try
            {
                string idRecenzie = dataGridView_Recenzie.SelectedRows[0].Cells["id"].FormattedValue.ToString();

                dataAdapterRecenzie.DeleteCommand = new SqlCommand("DELETE FROM Recenzii WHERE id = @id", connection);
                dataAdapterRecenzie.DeleteCommand.Parameters.AddWithValue("@id", idRecenzie);

                connection.Open();
                dataAdapterRecenzie.DeleteCommand.ExecuteNonQuery();
                connection.Close();

                messageToUser.Text = "Recenzie stearsa cu succes!";

                dataSetRecenzie.Clear();
                dataAdapterRecenzie.Fill(dataSetRecenzie);
            }
            catch (Exception ex)
            {
                connection.Close();
                messageToUser.Text = ex.Message;
            }
        }

        //Functie de actualizare a unei recenzii
        private void actualizareButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (autorTextBox.Text == "")
                {
                    throw new Exception("Actualizarea nu s-a putut efectua!");
                }

                dataAdapterRecenzie.UpdateCommand = new SqlCommand("UPDATE Recenzii SET continut = @continut, autor = @autor, pozitiv = @pozitiv" +
                    " WHERE id = @id", connection);
                dataAdapterRecenzie.UpdateCommand.Parameters.AddWithValue("@autor", autorTextBox.Text);
                dataAdapterRecenzie.UpdateCommand.Parameters.AddWithValue("@id", idRecenzieTextBox.Text);
                dataAdapterRecenzie.UpdateCommand.Parameters.AddWithValue("@continut", continutTextBox.Text);
                dataAdapterRecenzie.UpdateCommand.Parameters.AddWithValue("@pozitiv", pozitivTextBox.Text);
             

                connection.Open();
                dataAdapterRecenzie.UpdateCommand.ExecuteNonQuery();
                connection.Close();

                dataSetRecenzie.Clear();
                dataAdapterRecenzie.Fill(dataSetRecenzie);

                messageToUser.Text = "Recenzie actualizata cu succes!";
            }
            catch (Exception ex)
            {
                connection.Close();
                messageToUser.Text = ex.Message;
            }
        }

        //Functie de adaugare a unei recenzii
        private void adaugareButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (autorTextBox.Text == "" || pozitivTextBox.Text == "")
                {
                    throw new Exception("Adaugarea nu s-a putut efectua!");
                }

                dataAdapterRecenzie.InsertCommand = new SqlCommand("INSERT INTO Recenzii( continut, autor, pozitiv, id_carte) " +
                    "VALUES ( @continut, @autor, @pozitiv, @id_carte)", connection);
                dataAdapterRecenzie.InsertCommand.Parameters.AddWithValue("@id_carte", idCarteTextBox.Text);
                dataAdapterRecenzie.InsertCommand.Parameters.AddWithValue("@autor", autorTextBox.Text);
                dataAdapterRecenzie.InsertCommand.Parameters.AddWithValue("@pozitiv", pozitivTextBox.Text);
                dataAdapterRecenzie.InsertCommand.Parameters.AddWithValue("@continut", continutTextBox.Text);

                connection.Open();
                dataAdapterRecenzie.InsertCommand.ExecuteNonQuery();
                connection.Close();

                dataSetRecenzie.Clear();
                dataAdapterRecenzie.Fill(dataSetRecenzie);

                messageToUser.Text = "Recenzie adăugata cu succes!";
            }
            catch (Exception ex)
            {
                connection.Close();
                messageToUser.Text = ex.Message;
            }
        }
    }
}
