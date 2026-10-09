import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Backend imports
from CLSanalysis import clsAnalysis
from CLSpatient import clsPatient
from CLSsymptoms import clsSymptoms
from CLSParameter import clsParameters 

# UI Import for Report
from ReportPreview import ReportPreviewWindow

class FrmAnalysis:
    def __init__(self, root):
        self.root = root
        
        # Yellow Header Styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", 
                        background="#fbc531", 
                        foreground="black", 
                        font=("Segoe UI", 10, "bold"))

        self.selected_id = None
        self.vPatientID = 0 

        # Main Container
        self.main_container = tk.Frame(self.root, bg="#f5f6fa")
        self.main_container.pack(fill="both", expand=True)

        # ---------- Layout ----------
        self.left_frame = tk.LabelFrame(self.main_container, text=" Analysis Master ", font=("Segoe UI", 12, "bold"), bg="#f5f6fa", padx=10, pady=10)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        self.right_frame = tk.Frame(self.main_container, bg="#f5f6fa")
        self.right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

        # ================== LEFT UI (Form & Table) ==================
        form = tk.Frame(self.left_frame, bg="#f5f6fa")
        form.pack(pady=10)

        lbl_s = {"bg": "#f5f6fa", "font": ("Segoe UI", 10)}
        tk.Label(form, text="Date", **lbl_s).grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.txtDate = DateEntry(form, width=18, date_pattern='yyyy-mm-dd')
        self.txtDate.grid(row=0, column=1)

        tk.Label(form, text="Patient", **lbl_s).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.cmbPatient = ttk.Combobox(form, width=22, state="readonly")
        self.cmbPatient.grid(row=1, column=1)
        self.cmbPatient.bind("<<ComboboxSelected>>", self.on_patient_select)

        tk.Label(form, text="Symptoms", **lbl_s).grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.cmbSymptoms = ttk.Combobox(form, width=22, state="readonly")
        self.cmbSymptoms.grid(row=2, column=1)
        self.cmbSymptoms.bind("<<ComboboxSelected>>", self.on_symptom_change)

        # CRUD Buttons + Export Report Button
        btn_f = tk.Frame(self.left_frame, bg="#f5f6fa")
        btn_f.pack(pady=15)
        btn_s = {"width": 10, "fg": "white", "font": ("Segoe UI", 9, "bold")}
        
        tk.Button(btn_f, text="Save", bg="#27ae60", command=self.save, **btn_s).grid(row=0, column=0, padx=2)
        tk.Button(btn_f, text="Update", bg="#2980b9", command=self.update, **btn_s).grid(row=0, column=1, padx=2)
        tk.Button(btn_f, text="Delete", bg="#c0392b", command=self.delete, **btn_s).grid(row=0, column=2, padx=2)
        tk.Button(btn_f, text="New", bg="#7f8c8d", command=self.clear, **btn_s).grid(row=0, column=3, padx=2)
        
        # Export Button (Purple)
        tk.Button(btn_f, text="Export Report", bg="#8e44ad", command=self.open_report_preview, **btn_s).grid(row=0, column=4, padx=2)

        # History Table (Left)
        self.tbl = ttk.Treeview(self.left_frame, columns=("id", "date", "sname"), show="headings", height=12)
        self.tbl.heading("id", text="ID"); self.tbl.heading("date", text="Date"); self.tbl.heading("sname", text="Symptoms Name")
        self.tbl.column("id", width=40, anchor="center"); self.tbl.column("date", width=100); self.tbl.column("sname", width=250)
        self.tbl.pack(fill="both", expand=True)
        self.tbl.bind("<<TreeviewSelect>>", self.on_select)

        # ================== RIGHT UI ==================
        self.top_diag = tk.LabelFrame(self.right_frame, text=" Diagnosis (Current Symptom) ", font=("Segoe UI", 10, "bold"), bg="#f5f6fa", fg="#e67e22")
        self.top_diag.pack(fill="both", expand=True, pady=(0, 10))

        self.tblDiag = ttk.Treeview(self.top_diag, columns=("sno", "disease"), show="headings")
        self.tblDiag.heading("sno", text="S.No"); self.tblDiag.heading("disease", text="Predicted Disease Name")
        self.tblDiag.column("sno", width=50, anchor="center"); self.tblDiag.pack(fill="both", expand=True, padx=5, pady=5)

        self.bottom_diag = tk.LabelFrame(self.right_frame, text=" Diagnosis (Based on Most Symptoms Match) ", font=("Segoe UI", 10, "bold"), bg="#f5f6fa", fg="#27ae60")
        self.bottom_diag.pack(fill="both", expand=True)

        self.tblHistoryDiag = ttk.Treeview(self.bottom_diag, columns=("sno", "disease"), show="headings")
        self.tblHistoryDiag.heading("sno", text="S.No"); self.tblHistoryDiag.heading("disease", text="Predicted Disease Name")
        self.tblHistoryDiag.column("sno", width=50, anchor="center"); self.tblHistoryDiag.pack(fill="both", expand=True, padx=5, pady=5)

        self.load_patient(); self.load_symptoms(); self.load_data()

    # --- Methods ---
    def open_report_preview(self):
        if not self.vPatientID:
            messagebox.showwarning("Warning", "Please select a patient first.")
            return

        all_patients = clsPatient.getAllPatientInformation()
        p_data = next((p for p in all_patients if str(p[0]) == str(self.vPatientID)), None)

        if p_data:
            # Match Results from 2nd Table (tblHistoryDiag)
            match_results = []
            for item in self.tblHistoryDiag.get_children():
                diagnosis_text = self.tblHistoryDiag.item(item)['values'][1]
                match_results.append(diagnosis_text)

            if not match_results:
                messagebox.showwarning("No Results", "No matching diagnosis found to export.")
                return

            # Symptoms list from current patient session
            all_symptoms = [self.tbl.item(i)['values'][2] for i in self.tbl.get_children()]

            # Package data (Email index is 7 based on your SQL schema)
            data_to_send = {
                "name": p_data[1],
                "email": p_data[7], 
                "date": self.txtDate.get(),
                "age": p_data[3],
                "height": p_data[4],
                "weight": p_data[5],
                "blood": p_data[6],
                "symptoms": all_symptoms if all_symptoms else [self.cmbSymptoms.get()],
                "predictions": match_results 
            }
            ReportPreviewWindow(self.root, data_to_send)

    def on_patient_select(self, event):
        pname = self.cmbPatient.get()
        self.vPatientID = self.patient_map.get(pname, 0)
        self.load_data()
        self.load_history_diagnosis(self.vPatientID)

    def on_symptom_change(self, event):
        sname = self.cmbSymptoms.get()
        sid = self.symptom_map.get(sname, 0)
        self.load_current_diagnosis(sid)

    def load_current_diagnosis(self, sid):
        self.tblDiag.delete(*self.tblDiag.get_children())
        if sid == 0: return
        rows = clsParameters.getDiseasesBySymptom(sid)
        for i, dname in enumerate(rows, 1):
            self.tblDiag.insert("", "end", values=(i, dname))

    def load_history_diagnosis(self, pid):
        self.tblHistoryDiag.delete(*self.tblHistoryDiag.get_children())
        if pid == 0: return
        rows = clsParameters.getDiseasesByPatientHistory(pid)
        for i, row in enumerate(rows, 1):
            self.tblHistoryDiag.insert("", "end", values=(i, f"{row[0]} ({row[1]} symptoms matched)"))

    def load_data(self):
        self.tbl.delete(*self.tbl.get_children())
        rows = clsAnalysis.getAllAnalysisInformation()
        for r in rows:
            if self.vPatientID == 0 or str(r[2]) == str(self.vPatientID):
                self.tbl.insert("", "end", values=(r[0], r[1], r[5]))

    def on_select(self, event):
        selected = self.tbl.focus()
        if not selected: return
        v = self.tbl.item(selected, "values")
        self.selected_id = v[0]
        self.txtDate.set_date(v[1])
        self.cmbSymptoms.set(v[2])
        self.on_symptom_change(None)

    def save(self):
        pn, sn = self.cmbPatient.get(), self.cmbSymptoms.get()
        if not pn or not sn: return
        obj = clsAnalysis()
        obj.setAnalysisID(0)
        obj.setAnalysisDate(self.txtDate.get())
        obj.setPatientID(self.patient_map[pn])
        obj.setSymptomsID(self.symptom_map[sn])
        clsAnalysis.addNewAnalysis(obj)
        messagebox.showinfo("Success", "Analysis entry saved!")
        self.clear()

    def update(self):
        if not self.selected_id: return
        pn, sn = self.cmbPatient.get(), self.cmbSymptoms.get()
        obj = clsAnalysis()
        obj.setAnalysisID(self.selected_id)
        obj.setAnalysisDate(self.txtDate.get())
        obj.setPatientID(self.patient_map[pn])
        obj.setSymptomsID(self.symptom_map[sn])
        clsAnalysis.updateAnalysis(obj)
        messagebox.showinfo("Success", "Analysis entry updated!")
        self.clear()

    def delete(self):
        if not self.selected_id: return
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this entry?"):
            obj = clsAnalysis()
            obj.setAnalysisID(self.selected_id)
            clsAnalysis.deleteAnalysis(obj)
            self.clear()

    def clear(self):
        self.selected_id = None
        self.cmbPatient.set("")
        self.cmbSymptoms.set("")
        self.vPatientID = 0
        self.load_data()
        self.tblDiag.delete(*self.tblDiag.get_children())
        self.tblHistoryDiag.delete(*self.tblHistoryDiag.get_children())

    def load_patient(self):
        rows = clsPatient.getAllPatientInformation()
        self.cmbPatient["values"] = [r[1] for r in rows]
        self.patient_map = {r[1]: r[0] for r in rows}

    def load_symptoms(self):
        rows = clsSymptoms.getAllSymptomInformation()
        self.cmbSymptoms["values"] = [r[1] for r in rows]
        self.symptom_map = {r[1]: r[0] for r in rows}

if __name__ == "__main__":
    root = tk.Tk()
    FrmAnalysis(root)
    root.mainloop()
