
namespace WinFormsApp3
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.stergereButton = new System.Windows.Forms.Button();
            this.dataGridView_Carte = new System.Windows.Forms.DataGridView();
            this.dataGridView_Recenzie = new System.Windows.Forms.DataGridView();
            this.titluTextBox = new System.Windows.Forms.TextBox();
            this.descriereTextBox = new System.Windows.Forms.TextBox();
            this.titluCarteLabel = new System.Windows.Forms.Label();
            this.descriereLabel = new System.Windows.Forms.Label();
            this.idCarteTextBox = new System.Windows.Forms.TextBox();
            this.autorTextBox = new System.Windows.Forms.TextBox();
            this.pozitivTextBox = new System.Windows.Forms.TextBox();
            this.continutTextBox = new System.Windows.Forms.RichTextBox();
            this.idCarteLabel = new System.Windows.Forms.Label();
            this.autorLabel = new System.Windows.Forms.Label();
            this.pozitivLabel = new System.Windows.Forms.Label();
            this.continutLabel = new System.Windows.Forms.Label();
            this.carteIdLabel = new System.Windows.Forms.Label();
            this.carteIdTextBox = new System.Windows.Forms.TextBox();
            this.actualizareButton = new System.Windows.Forms.Button();
            this.messageToUser = new System.Windows.Forms.Label();
            this.adaugareButton = new System.Windows.Forms.Button();
            this.idRecenzieTextBox = new System.Windows.Forms.TextBox();
            this.idRecenzieLabel = new System.Windows.Forms.Label();
            this.anAparitieTextBox = new System.Windows.Forms.TextBox();
            this.idEdituraTextBox = new System.Windows.Forms.TextBox();
            this.anAparitieLabel = new System.Windows.Forms.Label();
            this.idEdituraLabel = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView_Carte)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView_Recenzie)).BeginInit();
            this.SuspendLayout();
            // 
            // stergereButton
            // 
           
            this.stergereButton.Location = new System.Drawing.Point(1052, 73);
            this.stergereButton.Margin = new System.Windows.Forms.Padding(4);
            this.stergereButton.Name = "stergereButton";
            this.stergereButton.Size = new System.Drawing.Size(152, 38);
            this.stergereButton.TabIndex = 0;
            this.stergereButton.Text = "Șterge recenzie";
            this.stergereButton.UseVisualStyleBackColor = true;
            this.stergereButton.Click += new System.EventHandler(this.stergereButton_Click);
            // 
            // dataGridView_Carte
            // 
            this.dataGridView_Carte.BackgroundColor = System.Drawing.SystemColors.InactiveBorder;
            this.dataGridView_Carte.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView_Carte.Location = new System.Drawing.Point(39, 57);
            this.dataGridView_Carte.Margin = new System.Windows.Forms.Padding(4);
            this.dataGridView_Carte.Name = "dataGridView_Carte";
            this.dataGridView_Carte.RowHeadersWidth = 51;
            this.dataGridView_Carte.Size = new System.Drawing.Size(456, 185);
            this.dataGridView_Carte.TabIndex = 1;
            this.dataGridView_Carte.CellClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridView_Carte_CellClick);
            // 
            // dataGridView_Recenzie
            // 
            this.dataGridView_Recenzie.BackgroundColor = System.Drawing.SystemColors.InactiveBorder;
            this.dataGridView_Recenzie.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView_Recenzie.Location = new System.Drawing.Point(589, 57);
            this.dataGridView_Recenzie.Margin = new System.Windows.Forms.Padding(4);
            this.dataGridView_Recenzie.Name = "dataGridView_Recenzie";
            this.dataGridView_Recenzie.RowHeadersWidth = 51;
            this.dataGridView_Recenzie.Size = new System.Drawing.Size(456, 185);
            this.dataGridView_Recenzie.TabIndex = 2;
            this.dataGridView_Recenzie.CellClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridView_Recenzie_CellClick);
            // 
            // titluTextBox
            // 
            this.titluTextBox.Location = new System.Drawing.Point(215, 304);
            this.titluTextBox.Margin = new System.Windows.Forms.Padding(4);
            this.titluTextBox.Name = "titluTextBox";
            this.titluTextBox.Size = new System.Drawing.Size(164, 22);
            this.titluTextBox.TabIndex = 3;
            // 
            // descriereTextBox
            // 
            this.descriereTextBox.Location = new System.Drawing.Point(215, 334);
            this.descriereTextBox.Margin = new System.Windows.Forms.Padding(4);
            this.descriereTextBox.Name = "descriereTextBox";
            this.descriereTextBox.Size = new System.Drawing.Size(164, 22);
            this.descriereTextBox.TabIndex = 4;
            // 
            // titluCarteLabel
            // 
            this.titluCarteLabel.AutoSize = true;
            this.titluCarteLabel.Location = new System.Drawing.Point(111, 307);
            this.titluCarteLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.titluCarteLabel.Name = "titluCarteLabel";
            this.titluCarteLabel.Size = new System.Drawing.Size(126, 17);
            this.titluCarteLabel.TabIndex = 5;
            this.titluCarteLabel.Text = "Titlu carte";
            // 
            // descriereLabel
            // 
            this.descriereLabel.AutoSize = true;
            this.descriereLabel.Location = new System.Drawing.Point(117, 336);
            this.descriereLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.descriereLabel.Name = "descriereLabel";
            this.descriereLabel.Size = new System.Drawing.Size(90, 17);
            this.descriereLabel.TabIndex = 6;
            this.descriereLabel.Text = "Descriere";
            // TextBox pentru anul apariției
            this.anAparitieTextBox.Location = new System.Drawing.Point(215, 364);
            this.anAparitieTextBox.Margin = new System.Windows.Forms.Padding(4);
            this.anAparitieTextBox.Name = "anAparitieTextBox";
            this.anAparitieTextBox.Size = new System.Drawing.Size(164, 22);
            this.anAparitieTextBox.TabIndex = 10;

            // TextBox pentru ID-ul editurii
            this.idEdituraTextBox.Location = new System.Drawing.Point(215, 394);
            this.idEdituraTextBox.Margin = new System.Windows.Forms.Padding(4);
            this.idEdituraTextBox.Name = "idEdituraTextBox";
            this.idEdituraTextBox.Size = new System.Drawing.Size(164, 22);
            this.idEdituraTextBox.TabIndex = 11;

            // Label pentru anul apariției
            this.anAparitieLabel.AutoSize = true;
            this.anAparitieLabel.Location = new System.Drawing.Point(117, 367);
            this.anAparitieLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.anAparitieLabel.Name = "anAparitieLabel";
            this.anAparitieLabel.Size = new System.Drawing.Size(90, 17);
            this.anAparitieLabel.TabIndex = 12;
            this.anAparitieLabel.Text = "An apariție";

            // Label pentru ID-ul editurii
            this.idEdituraLabel.AutoSize = true;
            this.idEdituraLabel.Location = new System.Drawing.Point(117, 397);
            this.idEdituraLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.idEdituraLabel.Name = "idEdituraLabel";
            this.idEdituraLabel.Size = new System.Drawing.Size(64, 17);
            this.idEdituraLabel.TabIndex = 13;
            this.idEdituraLabel.Text = "ID editură";
            // 
            // idCarteTextBox
            // 
            this.idCarteTextBox.Location = new System.Drawing.Point(779, 296);
            this.idCarteTextBox.Margin = new System.Windows.Forms.Padding(4);
            this.idCarteTextBox.Name = "idCarteTextBox";
            this.idCarteTextBox.Size = new System.Drawing.Size(164, 22);
            this.idCarteTextBox.TabIndex = 7;
            // 
            // autorTextBox
            // 
            this.autorTextBox.Location = new System.Drawing.Point(779, 327);
            this.autorTextBox.Margin = new System.Windows.Forms.Padding(4);
            this.autorTextBox.Name = "autorTextBox";
            this.autorTextBox.Size = new System.Drawing.Size(164, 22);
            this.autorTextBox.TabIndex = 8;
            // 
            // pozitivTextBox
            // 
            this.pozitivTextBox.Location = new System.Drawing.Point(779, 357);
            this.pozitivTextBox.Margin = new System.Windows.Forms.Padding(4);
            this.pozitivTextBox.Name = "pozitivTextBox";
            this.pozitivTextBox.Size = new System.Drawing.Size(164, 22);
            this.pozitivTextBox.TabIndex = 9;
            // 
            // continutTextBox
            // 
            this.continutTextBox.Location = new System.Drawing.Point(779, 417);
            this.continutTextBox.Margin = new System.Windows.Forms.Padding(4);
            this.continutTextBox.Name = "continutTextBox";
            this.continutTextBox.Size = new System.Drawing.Size(164, 67);
            this.continutTextBox.TabIndex = 11;
            this.continutTextBox.Text = "";
            // 
            // idCarteLabel
            // 
            this.idCarteLabel.AutoSize = true;
            this.idCarteLabel.Location = new System.Drawing.Point(693, 299);
            this.idCarteLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.idCarteLabel.Name = "idCarteLabel";
            this.idCarteLabel.Size = new System.Drawing.Size(78, 17);
            this.idCarteLabel.TabIndex = 12;
            this.idCarteLabel.Text = "ID Carte";
            // 
            // autorLabel
            // 
            this.autorLabel.AutoSize = true;
            this.autorLabel.Location = new System.Drawing.Point(700, 330);
            this.autorLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.autorLabel.Name = "autorLabel";
            this.autorLabel.Size = new System.Drawing.Size(96, 17);
            this.autorLabel.TabIndex = 13;
            this.autorLabel.Text = "Autor";
            // 
            // pozitivLabel
            // 
            this.pozitivLabel.AutoSize = true;
            this.pozitivLabel.Location = new System.Drawing.Point(655, 360);
            this.pozitivLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.pozitivLabel.Name = "pozitivLabel";
            this.pozitivLabel.Size = new System.Drawing.Size(116, 17);
            this.pozitivLabel.TabIndex = 14;
            this.pozitivLabel.Text = "Pozitiv/Negativ";
            
            // 
            // continutLabel
            // 
            this.continutLabel.AutoSize = true;
            this.continutLabel.Location = new System.Drawing.Point(699, 443);
            this.continutLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.continutLabel.Name = "continutLabel";
            this.continutLabel.Size = new System.Drawing.Size(72, 17);
            this.continutLabel.TabIndex = 16;
            this.continutLabel.Text = "Continut";
            // 
            // carteIdLabel
            // 
            this.carteIdLabel.AutoSize = true;
            this.carteIdLabel.Location = new System.Drawing.Point(130, 278);
            this.carteIdLabel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.carteIdLabel.Name = "carteIdLabel";
            this.carteIdLabel.Size = new System.Drawing.Size(78, 17);
            this.carteIdLabel.TabIndex = 17;
            this.carteIdLabel.Text = "ID Carte";
            // 
            // carteIdTextBox
            // 
            this.carteIdTextBox.Location = new System.Drawing.Point(215, 275);
            this.carteIdTextBox.Name = "carteIdTextBox";
            this.carteIdTextBox.Size = new System.Drawing.Size(164, 22);
            this.carteIdTextBox.TabIndex = 18;
            // 
            // actualizareButton
            // 
            
            this.actualizareButton.Location = new System.Drawing.Point(1052, 184);
            this.actualizareButton.Name = "actualizareButton";
            this.actualizareButton.Size = new System.Drawing.Size(152, 38);
            this.actualizareButton.TabIndex = 19;
            this.actualizareButton.Text = "Actualizează recenzie";
            this.actualizareButton.UseVisualStyleBackColor = true;
            this.actualizareButton.Click += new System.EventHandler(this.actualizareButton_Click);
            // 
            // messageToUser
            // 
            this.messageToUser.AutoSize = true;
            this.messageToUser.Location = new System.Drawing.Point(13, 477);
            this.messageToUser.Name = "messageToUser";
            this.messageToUser.Size = new System.Drawing.Size(0, 17);
            this.messageToUser.TabIndex = 20;
            // 
            // adaugareButton
            // 
            
            this.adaugareButton.Location = new System.Drawing.Point(1052, 128);
            this.adaugareButton.Name = "adaugareButton";
            this.adaugareButton.Size = new System.Drawing.Size(152, 38);
            this.adaugareButton.TabIndex = 21;
            this.adaugareButton.Text = "Adaugă recenzie";
            this.adaugareButton.UseVisualStyleBackColor = true;
            this.adaugareButton.Click += new System.EventHandler(this.adaugareButton_Click);
            // 
            // idRecenzieTextBox
            // 
            this.idRecenzieTextBox.BackColor = System.Drawing.SystemColors.Window;
            this.idRecenzieTextBox.Location = new System.Drawing.Point(779, 263);
            this.idRecenzieTextBox.Name = "idRecenzieTextBox";
            this.idRecenzieTextBox.Size = new System.Drawing.Size(164, 22);
            this.idRecenzieTextBox.TabIndex = 22;
            // 
            // idRecenzieLabel
            // 
            this.idRecenzieLabel.AutoSize = true;
            this.idRecenzieLabel.Location = new System.Drawing.Point(700, 266);
            this.idRecenzieLabel.Name = "idRecenzieLabel";
            this.idRecenzieLabel.Size = new System.Drawing.Size(73, 17);
            this.idRecenzieLabel.TabIndex = 23;
            this.idRecenzieLabel.Text = "ID Recenzie";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
          
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(1219, 536);
            this.Controls.Add(this.idRecenzieLabel);
            this.Controls.Add(this.idRecenzieTextBox);
            this.Controls.Add(this.adaugareButton);
            this.Controls.Add(this.messageToUser);
            this.Controls.Add(this.actualizareButton);
            this.Controls.Add(this.carteIdTextBox);
            this.Controls.Add(this.carteIdLabel);
            this.Controls.Add(this.continutLabel);
            this.Controls.Add(this.pozitivLabel);
            this.Controls.Add(this.autorLabel);
            this.Controls.Add(this.idCarteLabel);
            this.Controls.Add(this.continutTextBox);
            this.Controls.Add(this.pozitivTextBox);
            this.Controls.Add(this.autorTextBox);
            this.Controls.Add(this.idCarteTextBox);
            this.Controls.Add(this.descriereLabel);
            this.Controls.Add(this.titluCarteLabel);
            this.Controls.Add(this.descriereTextBox);
            this.Controls.Add(this.titluTextBox);
            this.Controls.Add(this.dataGridView_Recenzie);
            this.Controls.Add(this.dataGridView_Carte);
            this.Controls.Add(this.stergereButton);
            this.Controls.Add(this.anAparitieTextBox);
            this.Controls.Add(this.idEdituraTextBox);
            this.Controls.Add(this.anAparitieLabel);
            this.Controls.Add(this.idEdituraLabel);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form1";
            this.Text = "Biblioteca";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView_Carte)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView_Recenzie)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button stergereButton;
        private System.Windows.Forms.DataGridView dataGridView_Carte;
        private System.Windows.Forms.DataGridView dataGridView_Recenzie;
        private System.Windows.Forms.TextBox titluTextBox;
        private System.Windows.Forms.TextBox descriereTextBox;
        private System.Windows.Forms.Label titluCarteLabel;
        private System.Windows.Forms.Label descriereLabel;
        private System.Windows.Forms.TextBox idCarteTextBox;
        private System.Windows.Forms.TextBox autorTextBox;
        private System.Windows.Forms.TextBox pozitivTextBox;
        private System.Windows.Forms.RichTextBox continutTextBox;
        private System.Windows.Forms.Label idCarteLabel;
        private System.Windows.Forms.Label autorLabel;
        private System.Windows.Forms.Label pozitivLabel;
        private System.Windows.Forms.Label continutLabel;
        private System.Windows.Forms.Label carteIdLabel;
        private System.Windows.Forms.TextBox carteIdTextBox;
        private System.Windows.Forms.Button actualizareButton;
        private System.Windows.Forms.Label messageToUser;
        private System.Windows.Forms.Button adaugareButton;
        private System.Windows.Forms.TextBox idRecenzieTextBox;
        private System.Windows.Forms.Label idRecenzieLabel;
        private System.Windows.Forms.TextBox anAparitieTextBox;
        private System.Windows.Forms.TextBox idEdituraTextBox;
        private System.Windows.Forms.Label anAparitieLabel;
        private System.Windows.Forms.Label idEdituraLabel;

    }
}

