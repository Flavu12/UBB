using System.Diagnostics;
using System.Windows.Forms;

namespace lab1
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            dataGridViewChild = new DataGridView();
            dataGridViewParent = new DataGridView();
            buttonUpdate = new Button();
            buttonAdd = new Button();
            buttonDelete = new Button();
            labelTitle = new Label();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            ((System.ComponentModel.ISupportInitialize)dataGridViewChild).BeginInit();
            ((System.ComponentModel.ISupportInitialize)dataGridViewParent).BeginInit();
            SuspendLayout();
            // 
            // dataGridViewChild
            // 
            dataGridViewChild.AllowUserToAddRows = false;
            dataGridViewChild.BackgroundColor = Color.White;
            dataGridViewChild.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridViewChild.Location = new Point(459, 332);
            dataGridViewChild.Margin = new Padding(3, 2, 3, 2);
            dataGridViewChild.Name = "dataGridViewChild";
            dataGridViewChild.ReadOnly = true;
            dataGridViewChild.RowHeadersWidth = 51;
            dataGridViewChild.RowTemplate.Height = 29;
            dataGridViewChild.Size = new Size(393, 181);
            dataGridViewChild.TabIndex = 9;
            // 
            // dataGridViewParent
            // 
            dataGridViewParent.AllowUserToAddRows = false;
            dataGridViewParent.AllowUserToDeleteRows = false;
            dataGridViewParent.BackgroundColor = Color.White;
            dataGridViewParent.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridViewParent.Location = new Point(459, 110);
            dataGridViewParent.Margin = new Padding(3, 2, 3, 2);
            dataGridViewParent.MultiSelect = false;
            dataGridViewParent.Name = "dataGridViewParent";
            dataGridViewParent.ReadOnly = true;
            dataGridViewParent.RowHeadersWidth = 51;
            dataGridViewParent.RowTemplate.Height = 29;
            dataGridViewParent.Size = new Size(393, 181);
            dataGridViewParent.TabIndex = 8;
            dataGridViewParent.CellClick += dataGridViewParent_CellClick;
            // 
            // buttonUpdate
            // 
            buttonUpdate.BackColor = Color.White;
            buttonUpdate.FlatAppearance.MouseOverBackColor = Color.SandyBrown;
            buttonUpdate.Font = new Font("Verdana", 11.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            buttonUpdate.ForeColor = SystemColors.ControlText;
            buttonUpdate.Location = new Point(142, 468);
            buttonUpdate.Margin = new Padding(3, 2, 3, 2);
            buttonUpdate.Name = "buttonUpdate";
            buttonUpdate.Size = new Size(115, 45);
            buttonUpdate.TabIndex = 16;
            buttonUpdate.Text = "Update";
            buttonUpdate.UseVisualStyleBackColor = false;
            buttonUpdate.Click += buttonUpdate_Click;
            // 
            // buttonAdd
            // 
            buttonAdd.BackColor = Color.White;
            buttonAdd.FlatAppearance.MouseOverBackColor = Color.SandyBrown;
            buttonAdd.Font = new Font("Verdana", 11.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            buttonAdd.Location = new Point(3, 468);
            buttonAdd.Margin = new Padding(3, 2, 3, 2);
            buttonAdd.Name = "buttonAdd";
            buttonAdd.Size = new Size(122, 45);
            buttonAdd.TabIndex = 7;
            buttonAdd.Text = "Adauga";
            buttonAdd.UseVisualStyleBackColor = false;
            buttonAdd.Click += buttonAdd_Click;
            // 
            // buttonDelete
            // 
            buttonDelete.BackColor = Color.FloralWhite;
            buttonDelete.FlatAppearance.MouseOverBackColor = Color.SandyBrown;
            buttonDelete.Font = new Font("Verdana", 11.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            buttonDelete.Location = new Point(282, 468);
            buttonDelete.Margin = new Padding(3, 2, 3, 2);
            buttonDelete.Name = "buttonDelete";
            buttonDelete.Size = new Size(131, 45);
            buttonDelete.TabIndex = 7;
            buttonDelete.Text = "Sterge";
            buttonDelete.UseVisualStyleBackColor = false;
            buttonDelete.Click += buttonDelete_Click;
            // 
            // labelTitle
            // 
            labelTitle.Location = new Point(0, 0);
            labelTitle.Name = "labelTitle";
            labelTitle.Size = new Size(100, 23);
            labelTitle.TabIndex = 0;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Myanmar Text", 36F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label1.ForeColor = Color.Black;
            label1.Location = new Point(13, 9);
            label1.Name = "label1";
            label1.Size = new Size(244, 85);
            label1.TabIndex = 17;
            label1.Text = "Biblioteca";
            label1.Click += label1_Click;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Verdana", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label2.ForeColor = Color.Black;
            label2.Location = new Point(376, 193);
            label2.Name = "label2";
            label2.Size = new Size(77, 23);
            label2.TabIndex = 18;
            label2.Text = "parinte";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Verdana", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label3.ForeColor = Color.Black;
            label3.Location = new Point(397, 413);
            label3.Name = "label3";
            label3.Size = new Size(56, 23);
            label3.TabIndex = 19;
            label3.Text = "copil";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.White;
            ClientSize = new Size(864, 524);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(buttonUpdate);
            Controls.Add(buttonAdd);
            Controls.Add(buttonDelete);
            Controls.Add(dataGridViewChild);
            Controls.Add(dataGridViewParent);
            Margin = new Padding(3, 2, 3, 2);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ((System.ComponentModel.ISupportInitialize)dataGridViewChild).EndInit();
            ((System.ComponentModel.ISupportInitialize)dataGridViewParent).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        //private Button buttonConnect;
        private Button buttonDelete;
        private Button buttonAdd;
        private Button buttonUpdate;
        private Label labelTitle;
        private Label label2;
        private Label label3;
        private DataGridView dataGridViewChild;
        private DataGridView dataGridViewParent;
        private Label label1;
    }
}