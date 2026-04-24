using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Configuration;
using System.Security.Cryptography;
using System.Globalization;



namespace lab1
{
    public partial class Form1 : Form
    {
        

        static string con = ConfigurationManager.ConnectionStrings["connection"].ConnectionString;
        static string parentName = ConfigurationManager.AppSettings["ParentControls"];
        static string childName = ConfigurationManager.AppSettings["ChildControls"];
        static int childNumberOfColumns = int.Parse(ConfigurationManager.AppSettings["ChildNumberOfColumns"]);
        static string insertQuerry = ConfigurationManager.AppSettings["ChildInsertQUERY"];
        static string deleteQuerry = ConfigurationManager.AppSettings["ChildDeleteQUERY"];
        static string updateQuerry = ConfigurationManager.AppSettings["ChildUpdateQUERY"];
        static string childArr = ConfigurationManager.AppSettings["ChildArr"];
        static string childColumnNames = ConfigurationManager.AppSettings["ChildColumnNames"];
        static string childColumnTypes = ConfigurationManager.AppSettings["ChildColumnTypes"];
        static string childToParentID = ConfigurationManager.AppSettings["ChildToParentID"];

        SqlConnection cs = new SqlConnection(con);
        SqlDataAdapter dataAdapter = new SqlDataAdapter();
        BindingSource bindingSourceP = new BindingSource();
        BindingSource bindingSourceC = new BindingSource();
        DataSet dataSetP = new DataSet();
        DataSet dataSetC = new DataSet();

        TextBox[] textBoxes = new TextBox[childNumberOfColumns];
        Label[] labels = new Label[childNumberOfColumns];

        public Form1()
        {
            InitializeComponent();
            string[] names = childColumnNames.Split(", ");
            for (int i = 0; i < childNumberOfColumns; i++)
            {
                labels[i] = new Label();
                textBoxes[i] = new TextBox();
                labels[i].Text = names[i];
                labels[i].Location = new Point(40, i * 30 + 120);
                textBoxes[i].Text = "";
                textBoxes[i].Width = 200;
                textBoxes[i].Location = new Point(150, i * 30 + 120);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            for (int i = 0; i < childNumberOfColumns; i++)
            {
                this.Controls.Add(labels[i]);
                this.Controls.Add(textBoxes[i]);
            }
            dataAdapter.SelectCommand = new SqlCommand("SELECT * FROM " + parentName, cs);
            dataSetP.Clear();
            dataAdapter.Fill(dataSetP);
            dataGridViewParent.DataSource = dataSetP.Tables[0];
            bindingSourceC.DataSource = dataSetP.Tables[0];
            bindingSourceP.MoveLast();
        }

        /**
        private void buttonConnect_Click(object sender, EventArgs e)
        {
            dataAdapter.SelectCommand = new SqlCommand("SELECT * FROM " + parentName, cs);
            dataSetP.Clear();
            dataAdapter.Fill(dataSetP);
            dataGridViewParent.DataSource = dataSetP.Tables[0];
            bindingSourceC.DataSource = dataSetP.Tables[0];
            bindingSourceP.MoveLast();
        }*/

        private void dataGridViewParent_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            if (dataGridViewParent.Rows[e.RowIndex].Cells[e.ColumnIndex].Value == null)
                return;


            string id = dataGridViewParent.Rows[e.RowIndex].Cells[0].Value.ToString();


            dataAdapter.SelectCommand = new SqlCommand("SELECT * from " + childName +
                    " where " + childName + "." + childToParentID + "=" + id + "; ", cs);
            dataSetC.Clear();
            dataAdapter.Fill(dataSetC);
            dataGridViewChild.DataSource = dataSetC.Tables[0];
            bindingSourceC.DataSource = dataSetC.Tables[0];
        }

        private void buttonAdd_Click(object sender, EventArgs e)
        {
            dataAdapter.InsertCommand = new SqlCommand(insertQuerry, cs);
            dataAdapter.InsertCommand.Parameters.Add("@id", SqlDbType.Int).Value = dataSetP.Tables[dataGridViewParent.CurrentCell.ColumnIndex].Rows[dataGridViewParent.CurrentCell.RowIndex][0];

            string[] args = childArr.Split(", ");
            string[] types = childColumnTypes.Split(", ");

            try
            {
                for (int i = 0; i < childNumberOfColumns; i++)
                {
                    switch (types[i])
                    {
                        case "string":
                            dataAdapter.InsertCommand.Parameters.Add(args[i + 1], SqlDbType.VarChar).Value = textBoxes[i].Text;
                            break;
                        case "int":
                            dataAdapter.InsertCommand.Parameters.Add(args[i + 1], SqlDbType.Int).Value = int.Parse(textBoxes[i].Text);
                            break;
                        case "float":
                            dataAdapter.InsertCommand.Parameters.Add(args[i + 1], SqlDbType.Float).Value = float.Parse(textBoxes[i].Text);
                            break;
                        case "date":
                            dataAdapter.InsertCommand.Parameters.Add(args[i + 1], SqlDbType.Date).Value = textBoxes[i].Text;
                            break;
                    }
                }

                cs.Open();
                dataAdapter.InsertCommand.ExecuteNonQuery();
                cs.Close();
                dataSetC.Clear();
                dataAdapter.Fill(dataSetC);
            }
            catch
            {
                MessageBox.Show("Wrong input!");
            }
        }

        private void buttonDelete_Click(object sender, EventArgs e)
        {
            if (dataGridViewChild.SelectedCells.Count == 0)
            {
                MessageBox.Show("O linie in copil trebuie selectata!");
                return;
            }
            else if (dataGridViewChild.SelectedCells.Count > 1)
            {
                MessageBox.Show("O singura linie in copil trebuie selectata!");
                return;
            }

            dataAdapter.DeleteCommand = new SqlCommand(deleteQuerry, cs);

            dataAdapter.DeleteCommand.Parameters.Add("@id",
                SqlDbType.Int).Value = dataSetC.Tables[0].Rows[dataGridViewChild.CurrentCell.RowIndex][0];

            cs.Open();
            dataAdapter.DeleteCommand.ExecuteNonQuery();
            cs.Close();
            dataSetC.Clear();
            dataAdapter.Fill(dataSetC);
        }

        private void buttonUpdate_Click(object sender, EventArgs e)
        {
            if (dataGridViewChild.SelectedCells.Count == 0)
            {
                MessageBox.Show("O linie în copil trebuie să fie selectată!");
                return;
            }
            else if (dataGridViewChild.SelectedCells.Count > 1)
            {
                MessageBox.Show("O singură linie în copil trebuie să fie selectată!");
                return;
            }

            int x;
            dataAdapter.UpdateCommand = new SqlCommand(updateQuerry, cs);

            dataAdapter.UpdateCommand.Parameters.Add("@id",
                SqlDbType.Int).Value = dataSetC.Tables[0].Rows[dataGridViewChild.CurrentCell.RowIndex]["id"];

            string[] args = childArr.Split(", ");
            string[] types = childColumnTypes.Split(", ");

            try
            {
                for (int i = 0; i < childNumberOfColumns; i++)
                {
                    switch (types[i])
                    {
                        case "string":
                            dataAdapter.UpdateCommand.Parameters.Add(args[i + 1], SqlDbType.VarChar).Value = textBoxes[i].Text;
                            break;
                        case "int":
                            dataAdapter.UpdateCommand.Parameters.Add(args[i + 1], SqlDbType.Int).Value = int.Parse(textBoxes[i].Text);
                            break;
                        case "float":
                            dataAdapter.UpdateCommand.Parameters.Add(args[i + 1], SqlDbType.Float).Value = float.Parse(textBoxes[i].Text);
                            break;
                        case "date":
                            dataAdapter.UpdateCommand.Parameters.Add(args[i + 1], SqlDbType.Date).Value = textBoxes[i].Text;
                            break;
                    }
                }

                cs.Open();
                x = dataAdapter.UpdateCommand.ExecuteNonQuery();
                cs.Close();
                dataSetC.Clear();
                dataAdapter.Fill(dataSetC);

                if (x >= 1)
                    MessageBox.Show("The record has been updated");
            }

            catch
            {
                MessageBox.Show("Wrong input!");
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}