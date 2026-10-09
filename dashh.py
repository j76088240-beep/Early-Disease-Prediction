import customtkinter as ctk
from PIL import Image
import os

# --- Import your modules here ---
# from frmSymptoms import FrmSymptoms
# from frmPatient import FrmPatient

# --- Constants & Configuration ---
APP_NAME = "Disease AI"
PRIMARY_COLOR = "#1a73e8"
BG_LIGHT = "#f8f9fa"
BG_DARK = "#121212"
CARD_BG_LIGHT = "#ffffff"
CARD_BG_DARK = "#1e1e1e"

# Error Bypass for title/geometry in sub-files
class SafeFrame(ctk.CTkFrame):
    def title(self, *args): pass
    def geometry(self, *args): pass

class MedicalDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Setup ---
        self.title(f"{APP_NAME} - Early Disease Prediction")
        self.geometry("1440x900")
        self.configure(fg_color=(BG_LIGHT, BG_DARK))
        
        self.appearance_mode = "light"
        ctk.set_appearance_mode(self.appearance_mode)

        # --- Grid Configuration ---
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Sidebar ---
        self.sidebar_frame = ctk.CTkFrame(self, width=280, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text=APP_NAME, 
                                     font=ctk.CTkFont(size=26, weight="bold"), 
                                     text_color=PRIMARY_COLOR)
        self.logo_label.pack(pady=(30, 10), padx=20)
        
        self.sub_logo = ctk.CTkLabel(self.sidebar_frame, text="CLINICAL INTELLIGENCE", 
                                   font=ctk.CTkFont(size=10, weight="bold"), text_color="grey")
        self.sub_logo.pack(pady=(0, 40))

        # Navigation
        nav_items = ["Symptoms", "Diseases", "Parameters", "Patients", "Analysis"]
        for item in nav_items:
            btn = ctk.CTkButton(self.sidebar_frame, text=item, height=45, corner_radius=10,
                               fg_color="transparent", text_color=("black", "white"),
                               hover_color=PRIMARY_COLOR, anchor="w",
                               command=lambda t=item: self.on_nav_click(t))
            btn.pack(fill="x", padx=20, pady=5)

        # --- Main Layout ---
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.grid(row=0, column=1, sticky="nsew", padx=30, pady=20)
        self.main_container.grid_rowconfigure(1, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        # Header
        self.header = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.header.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        
        self.breadcrumb = ctk.CTkLabel(self.header, text="Dashboard / Overview", font=ctk.CTkFont(size=16))
        self.breadcrumb.pack(side="left")

        self.theme_switch = ctk.CTkSwitch(self.header, text="Dark Mode", command=self.toggle_theme)
        self.theme_switch.pack(side="right", padx=10)

        # Dynamic Content Area (Where your forms load)
        self.dynamic_area = ctk.CTkFrame(self.main_container, corner_radius=15, fg_color=(CARD_BG_LIGHT, CARD_BG_DARK))
        self.dynamic_area.grid(row=1, column=0, sticky="nsew")

        self.show_welcome()

    def show_welcome(self):
        # Default welcome screen
        lbl = ctk.CTkLabel(self.dynamic_area, text="Welcome, Rida!\nSelect a module to begin clinical analysis.",
                          font=ctk.CTkFont(size=20))
        lbl.pack(expand=True)

    def on_nav_click(self, title):
        self.breadcrumb.configure(text=f"Dashboard / {title}")
        for widget in self.dynamic_area.winfo_children():
            widget.destroy()
        
        # Here you will load your frames, for example:
        # if title == "Symptoms":
        #    container = SafeFrame(self.dynamic_area)
        #    container.pack(fill="both", expand=True)
        #    FrmSymptoms(container)

    def toggle_theme(self):
        if self.appearance_mode == "light":
            self.appearance_mode = "dark"
        else:
            self.appearance_mode = "light"
        ctk.set_appearance_mode(self.appearance_mode)

if __name__ == "__main__":
    app = MedicalDashboard()
    app.mainloop()
