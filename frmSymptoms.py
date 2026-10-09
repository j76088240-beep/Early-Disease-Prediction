import tkinter as tk
from tkinter import ttk, messagebox

from CLSsymptoms import clsSymptoms
from DLSsymptoms import dlsSymptoms
from DBManager import QueryExecutor


class FrmSymptomsNew:

    def __init__(self, root):
        self.root = root
        self.root.title("Symptoms Master")
        self.root.geometry("700x450")

        self.selected_id = None

        # ---------- Title ----------
        tk.Label(
            root,
            text="Symptoms Master",
            font=("Segoe UI", 18, "bold")
        ).pack(pady=10)

        # ---------- Form Frame ----------
        form = tk.Frame(root)
        form.pack(pady=10)

        tk.Label(form, text="Symptom Name:", font=("Segoe UI", 11)).grid(row=0, column=2, padx=10, pady=5, sticky="e")
        self.txtSymptomNm = tk.Entry(form, width=20, font=("Segoe UI", 11))
        self.txtSymptomNm.grid(row=0, column=3, pady=5)        

        # ---------- Buttons ----------
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame, text="Save", width=12,
            bg="#27ae60", fg="white", activebackground="#2ecc71", command=self.save
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame, text="Update", width=12,
            bg="#2980b9", fg="white", command=self.update
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            btn_frame, text="Delete", width=12,
            bg="#c0392b", fg="white", command=self.delete
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            btn_frame, text="New", width=12, 
            bg="#7f8c8d", fg="white", command=self.clear
        ).grid(row=0, column=3, padx=5)

        # ---------- Table ----------
        table_frame = tk.Frame(root)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tbl = ttk.Treeview(
            table_frame,
            columns=("id", "name"),
            show="headings"
        )
        self.tbl.heading("id", text="Symptom ID")
        self.tbl.heading("name", text="Symptom Name")


        self.tbl.column("id", width=120, anchor="center")
        self.tbl.column("name", width=300,anchor="center")
        
        self.tbl.pack(fill="both", expand=True)

        self.tbl.bind("<<TreeviewSelect>>", self.on_select)

        self.load_data()

    # ---------- Load Data ----------
    def load_data(self):

        self.tbl.delete(*self.tbl.get_children())

        rows = clsSymptoms.getAllSymptomInformation()

        #print("Debug rows:", rows)
        #print("Debug rows type:", type(rows))
        #print("Debug first element type:", type(rows[0]))

        for row in rows:
            self.tbl.insert(
                "",
                "end",
                values=row   # tuple maps directly to columns
            )


    # ---------- Save ----------
    def save(self):
        name = self.txtSymptomNm.get().strip()
        if not name:
            messagebox.showwarning("Validation", "Enter Symptoms Name")
            return

        obj = clsSymptoms()
        obj.setSymptomsID(0)
        obj.setSymptomsName(name)

        clsSymptoms.addNewSymptom(obj)
        

        #qb = QueryExecutor()
        #qb.execute(dls.insert(obj))

        messagebox.showinfo("Success", "Symptom Saved")
        self.clear()
        self.load_data()

    # ---------- Update ----------
    def update(self):
        if self.selected_id is None:
            messagebox.showwarning("Selection", "Select record to update")
            return

        name = self.txtSymptomNm.get().strip()
        if not name:
            messagebox.showwarning("Validation", "Enter Symptoms Name")
            return


        obj = clsSymptoms()
        obj.setSymptomsID(self.selected_id)
        obj.setSymptomsName(name)

        clsSymptoms.updateSymptom(obj)

        #qb = QueryExecutor()
        #qb.execute(DlsCrimeType.update(obj))

        messagebox.showinfo("Success", "Symptom Updated")
        self.clear()
        self.load_data()

    # ---------- Delete ----------
    def delete(self):
        if self.selected_id is None:
            messagebox.showwarning("Selection", "Select record to delete")
            return

        name = self.txtSymptomNm.get().strip()
        if not name:
            messagebox.showwarning("Validation", "Enter Symptoms Name")
            return

        if not messagebox.askyesno("Confirm", "Are you sure to delete?"):
            return

        obj = clsSymptoms()
        obj.setSymptomsID(self.selected_id)
        obj.setSymptomsName(name)

        clsSymptoms.deleteSymptom(obj)

        #qb = QueryExecutor()
        #qb.execute(dlsCrimeType.delete(self.selected_id))

        messagebox.showinfo("Deleted", "Symptom Deleted")
        self.clear()
        self.load_data()

    # ---------- Select Row ----------
    def on_select(self, event):
        selected = self.tbl.focus()
        if not selected:
            return

        values = self.tbl.item(selected, "values")

        print("Table Values ........................ ",values)
        self.selected_id = values[0]

        self.txtSymptomNm.delete(0, tk.END)
        self.txtSymptomNm.insert(0, values[1])


    # ---------- Clear ----------
    def clear(self):
        self.selected_id = None
        self.txtSymptomNm.delete(0, tk.END)


# ---------- Run ----------
if __name__ == "__main__":
    root = tk.Tk()
    FrmSymptomsNew(root)
    root.mainloop()
