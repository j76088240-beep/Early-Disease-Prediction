import tkinter as tk
from tkinter import ttk, messagebox
from CLSsymptoms import clsSymptoms
from CLSdiseases import clsDiseases
from CLSParameter import clsParameters

class FrmParameter:
    def __init__(self, root):
        self.root = root
        self.root.title("Symptoms Diseases Master")
        self.root.geometry("900x550")
        
        self.selected_id = None
        self.vDiseaseID = 0
        self.vSymptomID = 0

        tk.Label(root, text="Symptoms Diseases Master", font=("Segoe UI", 18, "bold")).pack(pady=10)
        ttk.Separator(root, orient="horizontal").pack(fill="x", padx=20, pady=5)

        form = tk.Frame(root)
        form.pack(pady=10)

        # Labels & Comboboxes
        tk.Label(form, text="Diseases:", font=("Segoe UI", 11)).grid(row=0, column=0, padx=10, sticky="e")
        self.cmbDiseases = ttk.Combobox(form, width=25, font=("Segoe UI", 11), state="readonly")
        self.cmbDiseases.grid(row=0, column=1, pady=5)
        self.cmbDiseases.bind("<<ComboboxSelected>>", self.on_disease_select)

        tk.Label(form, text="Symptoms:", font=("Segoe UI", 11)).grid(row=0, column=2, padx=10, sticky="e")
        self.cmbSymptoms = ttk.Combobox(form, width=35, font=("Segoe UI", 11), state="readonly")
        self.cmbSymptoms.grid(row=0, column=3, pady=5)
        self.cmbSymptoms.bind("<<ComboboxSelected>>", self.on_symptom_select)

        self.cmbSymptoms["values"] = clsSymptoms.getAllSymptomsNames()
        self.cmbDiseases["values"] = clsDiseases.getAllDiseasesNames()

        # Buttons (Commands linked now)
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Save", width=12, bg="#27ae60", fg="white", command=self.save).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update", width=12, bg="#2980b9", fg="white", command=self.update).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete", width=12, bg="#c0392b", fg="white", command=self.delete).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="New", width=12, bg="#7f8c8d", fg="white", command=self.new).grid(row=0, column=3, padx=5)

        # Table
        table_frame = tk.Frame(root)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.tbl = ttk.Treeview(table_frame, columns=("id", "sid", "sname", "did", "dname"), show="headings")
        self.tbl.heading("id", text="Record ID")
        self.tbl.heading("sname", text="Symptom Name")
        self.tbl.heading("dname", text="Disease Name")
        
        # Show name to User, hide IDs 
        self.tbl.config(displaycolumns=("id", "sname", "dname"))
        self.tbl.pack(fill="both", expand=True)
        self.tbl.bind("<<TreeviewSelect>>", self.on_select)

        self.load_data()

    def on_disease_select(self, event):
        self.vDiseaseID = clsDiseases.getIDFromName(self.cmbDiseases.get())
        self.load_data() # Filter by disease

    def on_symptom_select(self, event):
        self.vSymptomID = clsSymptoms.getIDFromName(self.cmbSymptoms.get())

    def save(self):
        if self.vSymptomID == 0 or self.vDiseaseID == 0:
            messagebox.showwarning("Error", "Select both Disease and Symptom")
            return
        obj = clsParameters()
        obj.setSymptomID(self.vSymptomID)
        obj.setDiseaseID(self.vDiseaseID)
        clsParameters.addNewParameter(obj)
        messagebox.showinfo("Saved", "Mapping Saved")
        self.load_data()

    def update(self):
        if not self.selected_id: return
        obj = clsParameters()
        obj.setParameterID(self.selected_id)
        obj.setSymptomID(self.vSymptomID)
        obj.setDiseaseID(self.vDiseaseID)
        clsParameters.updateParameter(obj)
        messagebox.showinfo("Updated", "Mapping Updated")
        self.load_data()

    def delete(self):
        if not self.selected_id: return
        if messagebox.askyesno("Confirm", "Delete this record?"):
            obj = clsParameters()
            obj.setParameterID(self.selected_id)
            clsParameters.deleteParameter(obj)
            self.load_data(); self.new()

    def new(self):
        self.selected_id = None
        self.cmbSymptoms.set(""); self.cmbDiseases.set("")
        self.vSymptomID = 0; self.vDiseaseID = 0
        self.load_data()

    def load_data(self):
        self.tbl.delete(*self.tbl.get_children())
        # vDiseaseID filter 
        rows = clsParameters.getAllParameterInformationExtracted(self.vDiseaseID)
        for row in rows:
            self.tbl.insert("", "end", values=row)

    def on_select(self, event):
        selected = self.tbl.focus()
        if not selected: return
        v = self.tbl.item(selected, "values")
        self.selected_id = v[0]
        self.vSymptomID = v[1]
        self.vDiseaseID = v[3]
        self.cmbSymptoms.set(v[2])
        self.cmbDiseases.set(v[4])

if __name__ == "__main__":
    root = tk.Tk(); FrmParameter(root); root.mainloop()
