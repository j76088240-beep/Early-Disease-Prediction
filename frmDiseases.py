import tkinter as tk
from tkinter import ttk, messagebox

from CLSdiseases import clsDiseases


class FrmDiseases:

    def __init__(self, root):
        self.root = root
        self.root.title("Diseases Master")
        self.root.geometry("950x550")

        self.selected_id = None

        # ---------- Title ----------
        tk.Label(root, text="Diseases Master", font=("Segoe UI", 18, "bold")).pack(pady=10)

        # ---------- Form ----------
        form = tk.Frame(root)
        form.pack(pady=10)

        tk.Label(form, text="Disease Name").grid(row=0, column=0, padx=10, pady=5)
        self.txtName = tk.Entry(form, width=30)
        self.txtName.grid(row=0, column=1, padx=10)

        # ---------- Buttons ----------
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Save", width=12,
                  bg="#27ae60", fg="white",
                  command=self.save).grid(row=0, column=0, padx=5)

        tk.Button(btn_frame, text="Update", width=12,
                  bg="#2980b9", fg="white",
                  command=self.update).grid(row=0, column=1, padx=5)

        tk.Button(btn_frame, text="Delete", width=12,
                  bg="#c0392b", fg="white",
                  command=self.delete).grid(row=0, column=2, padx=5)

        tk.Button(btn_frame, text="New", width=12,
                  bg="#7f8c8d", fg="white",
                  command=self.clear).grid(row=0, column=3, padx=5)

        # ---------- Table ----------
        table_frame = tk.Frame(root)
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tbl = ttk.Treeview(
            table_frame,
            columns=("id", "name"),
            show="headings"
        )
        self.tbl.heading("id", text="Disease ID")
        self.tbl.heading("name", text="Disease Name")
        self.tbl.column("id", width=120, anchor="center")
        self.tbl.column("name", width=500)

        scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tbl.yview)
        self.tbl.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        self.tbl.pack(fill="both", expand=True)

        self.tbl.bind("<<TreeviewSelect>>", self.on_select)

        self.load_data()

    # ---------- Load Table ----------
    def load_data(self):
        self.tbl.delete(*self.tbl.get_children())

        rows = clsDiseases.getAllDiseaseInformation()

        for row in rows:
            self.tbl.insert("", "end", values=(row[0], row[1]))

    # ---------- Save ----------
    def save(self):
        name = self.txtName.get().strip()

        if not name:
            messagebox.showwarning("Error", "Enter disease name")
            return

        obj = clsDiseases()
        obj.setDiseasesID(0)
        obj.setDiseasesName(name)

        clsDiseases.addNewDiseases(obj)

        messagebox.showinfo("Saved", "Record Saved")
        self.clear()
        self.load_data()

    # ---------- Update ----------
    def update(self):
        if self.selected_id is None:
            messagebox.showwarning("Select", "Select record")
            return

        name = self.txtName.get().strip()

        if not name:
            messagebox.showwarning("Error", "Enter disease name")
            return

        obj = clsDiseases()
        obj.setDiseasesID(self.selected_id)
        obj.setDiseasesName(name)

        clsDiseases.updateDiseases(obj)

        messagebox.showinfo("Updated", "Record Updated")
        self.clear()
        self.load_data()

    # ---------- Delete ----------
    def delete(self):
        if self.selected_id is None:
            messagebox.showwarning("Select", "Select record")
            return

        if not messagebox.askyesno("Confirm", "Delete this disease?"):
            return

        obj = clsDiseases()
        obj.setDiseasesID(self.selected_id)

        clsDiseases.deleteDiseases(obj)

        messagebox.showinfo("Deleted", "Record Deleted")
        self.clear()
        self.load_data()

    # ---------- Select ----------
    def on_select(self, event):
        selected = self.tbl.focus()
        if not selected:
            return

        values = self.tbl.item(selected, "values")

        self.selected_id = values[0]
        self.txtName.delete(0, tk.END)
        self.txtName.insert(0, values[1])

    # ---------- Clear ----------
    def clear(self):
        self.selected_id = None
        self.txtName.delete(0, tk.END)


# ---------- Run ----------
if __name__ == "__main__":
    root = tk.Tk()
    FrmDiseases(root)
    root.mainloop()
