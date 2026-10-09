import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

class ReportPreviewWindow(ctk.CTkToplevel):
    def __init__(self, master, report_data):
        super().__init__(master)
        
        self.title("📄 Clinical Diagnosis Report Preview")
        self.geometry("750x900")
        self.report_data = report_data 
        
        self.grab_set()
        self.focus_set()

        self.main_scroll = ctk.CTkScrollableFrame(self, fg_color="#f5f6fa", corner_radius=0)
        self.main_scroll.pack(fill="both", expand=True)

        self.paper = ctk.CTkFrame(self.main_scroll, fg_color="white", corner_radius=2, border_width=1, border_color="#dcdde1")
        self.paper.pack(fill="both", expand=True, padx=60, pady=40)

        self.create_header()
        self.create_patient_section()
        self.create_diagnosis_section()
        self.create_disclaimer_section()

        # --- Action Button ---
        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(fill="x", pady=20)

        self.btn_export = ctk.CTkButton(btn_frame, text="💾 Save PDF & Send Email to Patient", 
                                        font=("Segoe UI", 13, "bold"),
                                        fg_color="#27ae60", hover_color="#219150", 
                                        height=45, command=self.process_report)
        self.btn_export.pack(pady=10)

    def create_header(self):
        header = ctk.CTkFrame(self.paper, fg_color="#2c3e50", corner_radius=0, height=100)
        header.pack(fill="x", side="top")
        ctk.CTkLabel(header, text="DISEASE AI - MEDICAL REPORT", font=("Segoe UI", 24, "bold"), text_color="white").pack(pady=(20, 0))
        ctk.CTkLabel(header, text="Symptom-Based Health Screening | Diagnostic Analysis", font=("Segoe UI", 10), text_color="#bdc3c7").pack(pady=(0, 15))

    def create_patient_section(self):
        section = ctk.CTkFrame(self.paper, fg_color="transparent")
        section.pack(fill="x", padx=45, pady=30)
        ctk.CTkLabel(section, text="PATIENT CLINICAL RECORD", font=("Segoe UI", 14, "bold"), text_color="#2c3e50").pack(anchor="w")
        ctk.CTkFrame(section, fg_color="#ecf0f1", height=2).pack(fill="x", pady=5)
        
        grid = ctk.CTkFrame(section, fg_color="transparent")
        grid.pack(fill="x", pady=10)
        details = [
            ("Patient Name:", self.report_data.get('name', 'N/A')),
            ("Report Date:", self.report_data.get('date', 'N/A')),
            ("Age / Gender:", f"{self.report_data.get('age', 'N/A')} Years"),
            ("Blood Group:", self.report_data.get('blood', 'N/A')),
            ("Height:", f"{self.report_data.get('height', 'N/A')} cm"),
            ("Weight:", f"{self.report_data.get('weight', 'N/A')} kg")
        ]
        for i, (lbl, val) in enumerate(details):
            r, c = i // 2, i % 2
            f = ctk.CTkFrame(grid, fg_color="transparent")
            f.grid(row=r, column=c, sticky="w", padx=10, pady=8)
            ctk.CTkLabel(f, text=lbl, font=("Segoe UI", 11, "bold"), text_color="black", width=110, anchor="w").pack(side="left")
            ctk.CTkLabel(f, text=str(val), font=("Segoe UI", 11), text_color="#34495e").pack(side="left")

    def create_diagnosis_section(self):
        section = ctk.CTkFrame(self.paper, fg_color="transparent")
        section.pack(fill="both", expand=True, padx=45, pady=10)
        ctk.CTkLabel(section, text="SYMPTOMS ANALYZED", font=("Segoe UI", 13, "bold"), text_color="#2c3e50").pack(anchor="w")
        syms = ", ".join(self.report_data.get('symptoms', []))
        ctk.CTkLabel(section, text=syms, font=("Segoe UI", 11), text_color="#34495e", wraplength=500, justify="left").pack(anchor="w", pady=(5, 20))
        ctk.CTkLabel(section, text="FINAL ANALYTICAL MATCHES", font=("Segoe UI", 13, "bold"), text_color="#c0392b").pack(anchor="w")
        pred_box = ctk.CTkFrame(section, fg_color="#fff5f5", border_width=1, border_color="#feb2b2")
        pred_box.pack(fill="x", pady=10)
        for d in self.report_data.get('predictions', []):
            color = "#b91c1c" if "High Match" in str(d) else "#2d3436"
            ctk.CTkLabel(pred_box, text=f"● {d}", font=("Segoe UI", 12, "bold"), text_color=color, anchor="w").pack(padx=20, pady=6)

    def create_disclaimer_section(self):
        footer = ctk.CTkFrame(self.paper, fg_color="#fdfdfd", corner_radius=5, border_width=1, border_color="#f1f2f6")
        footer.pack(fill="x", padx=45, pady=40, side="bottom")
        # Yahan UI ke liye emoji theek hai
        txt = "IMPORTANT: AI-generated screening report based on symptom mapping. Not a clinical diagnosis."
        ctk.CTkLabel(footer, text=txt, font=("Segoe UI", 9, "italic"), text_color="#7f8c8d", wraplength=500).pack(pady=15)

    # ================== PDF & EMAIL LOGIC ==================
    def process_report(self):
        filename = f"Report_{self.report_data['name'].replace(' ', '_')}.pdf"
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile=filename)
        
        if file_path:
            try:
                self.generate_pdf_file(file_path)
                self.send_email_with_attachment(file_path)
                messagebox.showinfo("Success", f"Report saved and emailed to {self.report_data.get('email', 'Patient')}")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Process Failed: {str(e)}")

    def generate_pdf_file(self, path):
        pdf = FPDF(orientation='P', unit='mm', format='A4') 
        pdf.add_page()
        
        # Header Blue Bar
        pdf.set_fill_color(44, 62, 80)
        pdf.rect(0, 0, 210, 45, 'F')
        pdf.set_text_color(255, 255, 255)
        pdf.set_font("Arial", 'B', 20)
        pdf.cell(190, 15, "DISEASE AI - MEDICAL REPORT", ln=True, align='C')
        pdf.set_font("Arial", size=10)
        pdf.cell(190, 5, "Symptom-Based Health Screening", ln=True, align='C')
        
        # Patient Data
        pdf.ln(30); pdf.set_text_color(0, 0, 0); pdf.set_font("Arial", 'B', 12)
        pdf.cell(190, 10, "PATIENT INFORMATION", ln=True)
        pdf.line(10, 60, 200, 60)
        
        pdf.ln(5); pdf.set_font("Arial", size=11)
        pdf.cell(95, 8, f"Name: {self.report_data['name']}"); pdf.cell(95, 8, f"Date: {self.report_data['date']}", ln=1)
        pdf.cell(95, 8, f"Age: {self.report_data['age']} Years"); pdf.cell(95, 8, f"Blood: {self.report_data['blood']}", ln=1)
        
        # Symptoms & Predictions
        pdf.ln(10); pdf.set_font("Arial", 'B', 12); pdf.cell(190, 10, "SYMPTOMS ANALYZED", ln=True)
        pdf.set_font("Arial", size=11); pdf.multi_cell(0, 7, txt=", ".join(self.report_data['symptoms']))
        
        pdf.ln(5); pdf.set_font("Arial", 'B', 12); pdf.set_text_color(192, 57, 43)
        pdf.cell(190, 10, "FINAL ANALYTICAL RESULTS", ln=True)
        pdf.set_text_color(0, 0, 0); pdf.set_font("Arial", 'B', 11)
        for d in self.report_data['predictions']:
            pdf.cell(190, 8, f"- {d}", ln=True)

        # --- Fix: Removed Emoji to avoid latin-1 error ---
        pdf.ln(20) 
        pdf.set_font("Arial", 'I', 9)
        pdf.set_text_color(100, 100, 100) 
        disclaimer_text = "IMPORTANT: AI-generated screening report based on symptom mapping. Not a clinical diagnosis. Please consult a qualified doctor for professional medical advice."
        pdf.multi_cell(190, 5, txt=disclaimer_text, align='C')
            
        pdf.output(path)

    def send_email_with_attachment(self, file_path):
        sender_email = "disease.aiprediction@gmail.com" 
        app_password = "etck vaas hgbf dqgx" 
        receiver_email = self.report_data.get('email')

        if not receiver_email or "@" not in str(receiver_email):
            raise Exception("Invalid patient email address.")

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"Medical Diagnosis Report - {self.report_data['name']}"

        body = f"""

Dear {self.report_data['name']},

Thank you for visiting and using our Disease AI screening system. We hope you are doing well.

Please find attached your professional diagnostic screening report. This report analyzes the symptoms you provided to help monitor your health trends.

We appreciate your trust in our digital tool. We wish you a very speedy recovery and great health.


Best Regards,
Medical Analysis Team

        """


        msg.attach(MIMEText(body, 'plain'))

        with open(file_path, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(file_path)}")
            msg.attach(part)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
