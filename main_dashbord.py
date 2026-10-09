import customtkinter as ctk
import tkinter as tk
from PIL import Image
import os

# File connections
from frmSymptoms import FrmSymptomsNew as FrmSymptoms
from frmDiseases import FrmDiseases
from frmParameter import FrmParameter
from frmPatient import FrmPatient
from frmAnalysis import FrmAnalysis
import FrmLogin
    

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  


class SafeFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
    def title(self, *args): pass 
    def geometry(self, *args): pass 

class DiseasePredictionDashbord(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Disease AI - Early Prediction System")
        self.geometry("1150x700") 
        self.minsize(1100, 650)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ================= SIDEBAR =================
        self.sidebar_frame = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1) 

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="🩺 Disease AI", font=ctk.CTkFont(size=24, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 30))

        self.btn_overview = self.create_sidebar_btn("📊 Overview", "overview", 1)
        self.btn_symptoms = self.create_sidebar_btn("🧠 Symptoms", "symptoms", 2)
        self.btn_diseases = self.create_sidebar_btn("🦠 Diseases", "diseases", 3)
        self.btn_parameters = self.create_sidebar_btn("⚙ Parameters", "parameters", 4)
        self.btn_patients = self.create_sidebar_btn("👤 Patients", "patients", 5)
        self.btn_analysis = self.create_sidebar_btn("📈 Analysis & Predict", "analysis", 6)
        self.btn_about = self.create_sidebar_btn("ℹ About Us", "about", 7)

        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=11, column=0, padx=20, pady=(10, 20))

        # ================= MAIN AREA =================
        self.main_container = ctk.CTkFrame(self, corner_radius=15, fg_color="transparent")
        self.main_container.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.main_container.grid_rowconfigure(1, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        self.header_label = ctk.CTkLabel(self.main_container, text="Dashboard / Overview", font=ctk.CTkFont(size=24, weight="bold"))
        self.header_label.grid(row=0, column=0, sticky="nw", pady=(0, 20))

        self.dynamic_frame = ctk.CTkFrame(self.main_container, corner_radius=10)
        self.dynamic_frame.grid(row=1, column=0, sticky="nsew")

        self.select_frame("overview")

    def create_sidebar_btn(self, text, name, row):
        btn = ctk.CTkButton(self.sidebar_frame, text=text, anchor="w", fg_color="transparent", text_color=("black", "white"), command=lambda: self.select_frame(name))
        btn.grid(row=row, column=0, padx=20, pady=5, sticky="ew")
        return btn

    def change_appearance_mode_event(self, mode):
        ctk.set_appearance_mode(mode)

    def select_frame(self, frame_name):
        active_bg, active_text = "#1a73e8", "white"
        default_bg, default_text = "transparent", ("black", "white")

        buttons = {"overview": self.btn_overview, "symptoms": self.btn_symptoms, "diseases": self.btn_diseases, 
                   "parameters": self.btn_parameters, "patients": self.btn_patients, "analysis": self.btn_analysis, "about": self.btn_about}

        for name, btn in buttons.items():
            btn.configure(fg_color=active_bg if name == frame_name else default_bg, text_color=active_text if name == frame_name else default_text)

        for widget in self.dynamic_frame.winfo_children(): widget.destroy()
        safe_container = SafeFrame(self.dynamic_frame, fg_color="transparent")
        safe_container.pack(fill="both", expand=True)

        if frame_name == "overview":
            self.header_label.configure(text="Dashboard / Overview")
            self.render_overview(safe_container)
        elif frame_name == "about":
            self.header_label.configure(text="Dashboard / About Us")
            self.render_about_us(safe_container)
        elif frame_name == "symptoms": FrmSymptoms(safe_container)
        elif frame_name == "diseases": FrmDiseases(safe_container)
        elif frame_name == "parameters": FrmParameter(safe_container)
        elif frame_name == "patients": FrmPatient(safe_container)
        elif frame_name == "analysis": FrmAnalysis(safe_container)

    def render_overview(self, parent):
        container = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=20, pady=10)
        
        # 1. Banner
        banner = ctk.CTkFrame(container, fg_color=("#3b82f6", "#1e3a8a"), height=160, corner_radius=20)
        banner.pack(fill="x", pady=(0, 30))
        banner.pack_propagate(False)
        ctk.CTkLabel(banner, text="Disease AI: Early Prediction System", font=ctk.CTkFont(size=28, weight="bold"), text_color="white").pack(pady=(40, 5), padx=40, anchor="w")
        ctk.CTkLabel(banner, text="Helping healthcare with AI-driven symptom analysis.", font=ctk.CTkFont(size=14), text_color="#dbeafe").pack(padx=40, anchor="w")
        
        # 2. Stat Cards Section (CENTERED)
        cards_outer_container = ctk.CTkFrame(container, fg_color="transparent")
        cards_outer_container.pack(fill="x", pady=10)
        
        # Center alignment
        cards_outer_container.grid_columnconfigure((0, 4), weight=1) # Side gaps
        
        self.create_stat_card(cards_outer_container, "Total Symptoms", "133", "#3b82f6", 1)
        self.create_stat_card(cards_outer_container, "Mapped Diseases", "41", "#10b981", 2)
        self.create_stat_card(cards_outer_container, "Predictions Done", "150+", "#f59e0b", 3)

        # 3. Activity Table
        ctk.CTkLabel(container, text="Recent Diagnostic Activity", font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", pady=(50, 15))
        
        table_frame = ctk.CTkFrame(container, fg_color=("white", "#212121"), corner_radius=15, border_width=1, border_color="#dcdde1")
        table_frame.pack(fill="both", expand=True, pady=(0, 30))
        
        h_frame = ctk.CTkFrame(table_frame, fg_color=("#f8f9fa", "#2d2d2d"), height=45, corner_radius=10)
        h_frame.pack(fill="x", padx=10, pady=10)
        headers = ["Patient Name", "Predicted Disease", "Confidence", "Status"]
        for i, h in enumerate(headers):
            ctk.CTkLabel(h_frame, text=h, font=ctk.CTkFont(size=13, weight="bold"), text_color="gray").place(relx=0.05 + (i*0.25), rely=0.5, anchor="w")

        log_data = [("Zain Khan", "Pneumonia", "92% High", "Email Sent"), ("Ishwari Patil", "Hemorrhoids", "75% Mid", "Saved"), ("Kuldeep Saindane", "Common Cold", "98% High", "Email Sent")]
        for pat, dis, conf, stat in log_data:
            row = ctk.CTkFrame(table_frame, fg_color="transparent", height=45)
            row.pack(fill="x", padx=15)
            ctk.CTkLabel(row, text=pat, font=ctk.CTkFont(size=13)).place(relx=0.04, rely=0.5, anchor="w")
            ctk.CTkLabel(row, text=dis, font=ctk.CTkFont(size=13)).place(relx=0.29, rely=0.5, anchor="w")
            c_color = "#27ae60" if "High" in conf else "#e67e22"
            ctk.CTkLabel(row, text=conf, text_color=c_color, font=ctk.CTkFont(weight="bold")).place(relx=0.54, rely=0.5, anchor="w")
            ctk.CTkLabel(row, text=stat, font=ctk.CTkFont(size=12), text_color="gray").place(relx=0.79, rely=0.5, anchor="w")
            ctk.CTkFrame(table_frame, fg_color=("#e0e0e0", "#333333"), height=1).pack(fill="x", padx=20)

    def render_about_us(self, parent):
        container = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=20, pady=10)
        banner = ctk.CTkFrame(container, fg_color=("#3b82f6", "#1e3a8a"), height=160, corner_radius=20)
        banner.pack(fill="x", pady=(0, 20))
        banner.pack_propagate(False)
        ctk.CTkLabel(banner, text="Disease AI - Early Prediction System", font=ctk.CTkFont(size=28, weight="bold"), text_color="white").pack(pady=(35, 5), padx=40, anchor="w")
        ctk.CTkLabel(banner, text="Providing fast, automated diagnostic screening reports.", font=ctk.CTkFont(size=14), text_color="#dbeafe").pack(padx=40, anchor="w")
        ctk.CTkLabel(container, text="Project Developed By:", font=ctk.CTkFont(size=22, weight="bold")).pack(pady=(5, 20))

        cards_outer = ctk.CTkFrame(container, fg_color="transparent")
        cards_outer.pack(expand=True)
        self.create_dev_card(cards_outer, "Janhavi Jagtap", "#3b82f6", 0)
        self.create_dev_card(cards_outer, "Gaurav Nikam", "#10b981", 1)
        self.create_dev_card(cards_outer, "Devika Chaudhari", "#9b59b6", 2)
        self.create_dev_card(cards_outer, "Suvarna Borse", "#e74c3c",3)

        ctk.CTkLabel(container, text="RCPIT Collage of Engineering Shirpur", font=ctk.CTkFont(size=14), text_color="gray").pack(pady=50)

    def create_stat_card(self, parent, title, value, color, col):
        card = ctk.CTkFrame(parent, width=280, height=170, corner_radius=20, border_width=2, border_color=color)
        card.grid(row=0, column=col, padx=10, pady=10)
        card.pack_propagate(False)
        ctk.CTkLabel(card, text="📊", font=ctk.CTkFont(size=45)).pack(pady=(25, 10))
        ctk.CTkLabel(card, text=value, font=ctk.CTkFont(size=32, weight="bold")).pack()
        ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=14), text_color="gray").pack()

    def create_dev_card(self, parent, name, color, col):
        card = ctk.CTkFrame(parent, width=280, height=220, corner_radius=20, border_width=2, border_color=color)
        card.grid(row=0, column=col, padx=15, pady=10)
        card.pack_propagate(False)
        ctk.CTkLabel(card, text="👤", font=ctk.CTkFont(size=60)).pack(pady=(25, 10))
        ctk.CTkLabel(card, text=name, font=ctk.CTkFont(size=18, weight="bold"), text_color=color).pack()
        ctk.CTkLabel(card, text="Developer", font=ctk.CTkFont(size=13), text_color="gray").pack()
        
if __name__ == "__main__":
    dash_cls = globals().get("DiseasePredictionDashbord") or globals().get("DiseasePredictionDashboard")

    login = FrmLogin.FrmLogin()
    login.mainloop()

    if login.logged_in:
        app = dash_cls()
        app.mainloop()
