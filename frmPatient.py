import tkinter as tk
from tkinter import ttk, messagebox

from CLSpatient import clsPatient

class FrmPatient:

    def __init__(self, root):
        self.root = root
        self.root.title("Patient Master")
        self.root.geometry("1100x650") #height spacing

        self.selected_id = None

        # ---------- Title ----------
        tk.Label(
            root,
            text="Patient Master",
            font=("Segoe UI", 20, "bold")
        ).pack(pady=(20, 10)) #20px gap

        # ---------- Form Frame ----------
        form = tk.Frame(root)
        form.pack(pady=15) # Form gap

        # Common Spacing Variables
        row_p = 10  #row gap
        col_p = 10  # Label & Entry gap

        # Row 1
        tk.Label(form, text="Patient Name", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="e", pady=row_p)
        self.txtName = tk.Entry(form, width=30)
        self.txtName.grid(row=0, column=1, padx=col_p, pady=row_p, ipady=3) # ipady se box look "tall"

        tk.Label(form, text="Age", font=("Segoe UI", 10)).grid(row=0, column=2, sticky="e", pady=row_p)
        self.txtAge = tk.Entry(form, width=15)
        self.txtAge.grid(row=0, column=3, padx=col_p, pady=row_p, ipady=3)

        # Row 2
        tk.Label(form, text="Contact No", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="e", pady=row_p)
        self.txtContact = tk.Entry(form, width=30)
        self.txtContact.grid(row=1, column=1, padx=col_p, pady=row_p, ipady=3)

        tk.Label(form, text="City", font=("Segoe UI", 10)).grid(row=1, column=2, sticky="e", pady=row_p)
        self.txtCity = tk.Entry(form, width=15)
        self.txtCity.grid(row=1, column=3, padx=col_p, pady=row_p, ipady=3)

        # Row 3
        tk.Label(form, text="Height (cm)", font=("Segoe UI", 10)).grid(row=2, column=0, sticky="e", pady=row_p)
        self.txtHeight = tk.Entry(form, width=30)
        self.txtHeight.grid(row=2, column=1, padx=col_p, pady=row_p, ipady=3)

        tk.Label(form, text="Weight", font=("Segoe UI", 10)).grid(row=2, column=2, sticky="e", pady=row_p)
        self.txtWeight = tk.Entry(form, width=15)
        self.txtWeight.grid(row=2, column=3, padx=col_p, pady=row_p, ipady=3)

        # Row 4
        tk.Label(form, text="Blood Group", font=("Segoe UI", 10)).grid(row=3, column=0, sticky="e", pady=row_p)
        self.cmbBlood = ttk.Combobox(form, values=["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], width=28)
        self.cmbBlood.grid(row=3, column=1, padx=col_p, pady=row_p)

        # Row 5 - Email (Span)
        tk.Label(form, text="Email", font=("Segoe UI", 10)).grid(row=4, column=0, sticky="e", pady=row_p)
        self.txtEmail = tk.Entry(form, width=60)
        self.txtEmail.grid(row=4, column=1, columnspan=3, padx=col_p, pady=row_p, sticky="w", ipady=3)

        # Row 6 - Address (Span)
        tk.Label(form, text="Address", font=("Segoe UI", 10)).grid(row=5, column=0, sticky="ne", pady=row_p)
        self.txtAddress = tk.Text(form, width=60, height=3, font=("Segoe UI", 9))
        self.txtAddress.grid(row=5, column=1, columnspan=3, padx=col_p, pady=row_p, sticky="w")

        # ---------- Buttons ----------
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=(20, 10)) # Address box 20px door, table 10px

        btn_w = 14 # buttons width
        tk.Button(btn_frame, text="Save", width=btn_w, bg="#27ae60", fg="white", font=("Segoe UI", 9, "bold"), command=self.save).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Update", width=btn_w, bg="#2980b9", fg="white", font=("Segoe UI", 9, "bold"), command=self.update).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Delete", width=btn_w, bg="#c0392b", fg="white", font=("Segoe UI", 9, "bold"), command=self.delete).grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="New", width=btn_w, bg="#7f8c8d", fg="white", font=("Segoe UI", 9, "bold"), command=self.clear).grid(row=0, column=3, padx=10)

        # ---------- Table ----------
        # Table frame remains exactly as you had it
        table_frame = tk.Frame(root)
        table_frame.pack(fill="both", expand=True, padx=15, pady=10)

        self.tbl = ttk.Treeview(
            table_frame,
            columns=("id","name","contact","age","height","weight","blood","email","city","address"),
            show="headings"
        )

        headings = ["ID","Name","Contact","Age","Height","Weight","Blood","Email","City","Address"]

        for i, h in enumerate(headings):
            self.tbl.heading(i, text=h)
            self.tbl.column(i, width=100, anchor="center")

        self.tbl.pack(fill="both", expand=True)
        self.tbl.bind("<<TreeviewSelect>>", self.on_select)

        self.load_data()

    # ---------- Methods (Keep these exactly the same) ----------
    def load_data(self):
        self.tbl.delete(*self.tbl.get_children())
        rows = clsPatient.getAllPatientInformation()
        for row in rows:
            self.tbl.insert("", "end", values=row)

    def save(self):
        obj = clsPatient()
        obj.setPatientID(0)
        obj.setPatientName(self.txtName.get())
        obj.setContactNo(self.txtContact.get())
        obj.setAge(self.txtAge.get())
        obj.setHeight(self.txtHeight.get())
        obj.setWeight(self.txtWeight.get())
        obj.setBloodGroup(self.cmbBlood.get())
        obj.setEmailID(self.txtEmail.get())
        obj.setCity(self.txtCity.get())
        obj.setAddress(self.txtAddress.get("1.0", tk.END).strip())
        clsPatient.addNewPatient(obj)
        messagebox.showinfo("Success", "Patient Saved")
        self.clear()
        self.load_data()

    def update(self):
        if self.selected_id is None:
            messagebox.showwarning("Select", "Select record")
            return
        obj = clsPatient()
        obj.setPatientID(self.selected_id)
        obj.setPatientName(self.txtName.get())
        obj.setContactNo(self.txtContact.get())
        obj.setAge(self.txtAge.get())
        obj.setHeight(self.txtHeight.get())
        obj.setWeight(self.txtWeight.get())
        obj.setBloodGroup(self.cmbBlood.get())
        obj.setEmailID(self.txtEmail.get())
        obj.setCity(self.txtCity.get())
        obj.setAddress(self.txtAddress.get("1.0", tk.END).strip())
        clsPatient.updatePatient(obj)
        messagebox.showinfo("Updated", "Patient Updated")
        self.clear()
        self.load_data()

    def delete(self):
        if self.selected_id is None:
            messagebox.showwarning("Select", "Select record")
            return
        obj = clsPatient()
        obj.setPatientID(self.selected_id)
        clsPatient.deletePatient(obj)
        messagebox.showinfo("Deleted", "Patient Deleted")
        self.clear()
        self.load_data()

    def on_select(self, event):
        selected = self.tbl.focus()
        if not selected: return
        values = self.tbl.item(selected, "values")
        self.selected_id = values[0]
        self.txtName.delete(0, tk.END); self.txtName.insert(0, values[1])
        self.txtContact.delete(0, tk.END); self.txtContact.insert(0, values[2])
        self.txtAge.delete(0, tk.END); self.txtAge.insert(0, values[3])
        self.txtHeight.delete(0, tk.END); self.txtHeight.insert(0, values[4])
        self.txtWeight.delete(0, tk.END); self.txtWeight.insert(0, values[5])
        self.cmbBlood.set(values[6])
        self.txtEmail.delete(0, tk.END); self.txtEmail.insert(0, values[7])
        self.txtCity.delete(0, tk.END); self.txtCity.insert(0, values[8])
        self.txtAddress.delete("1.0", tk.END); self.txtAddress.insert("1.0", values[9])

    def clear(self):
        self.selected_id = None
        self.txtName.delete(0, tk.END); self.txtContact.delete(0, tk.END)
        self.txtAge.delete(0, tk.END); self.txtHeight.delete(0, tk.END)
        self.txtWeight.delete(0, tk.END); self.cmbBlood.set("")
        self.txtEmail.delete(0, tk.END); self.txtCity.delete(0, tk.END)
        self.txtAddress.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    FrmPatient(root)
    root.mainloop()
