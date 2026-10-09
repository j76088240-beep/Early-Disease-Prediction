import customtkinter as ctk

# === ERROR BYPASS CLASS ===
class SafeFrame(ctk.CTkFrame):
    def title(self, *args): pass
    def geometry(self, *args): pass

# === MAIN DASHBOARD ===
class MedicalDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Disease AI - Clinical Intelligence")
        self.geometry("1200x750")
        
        # Colors based on your prototype
        self.bg_color = "#f4f7f6"
        self.sidebar_color = "#ffffff"
        self.primary_blue = "#0052cc"
        self.text_dark = "#172b4d"
        self.text_muted = "#6b778c"
        
        ctk.set_appearance_mode("light")
        self.configure(fg_color=self.bg_color)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ==================== SIDEBAR ====================
        self.sidebar = ctk.CTkFrame(self, width=240, corner_radius=0, fg_color=self.sidebar_color)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo = ctk.CTkLabel(self.sidebar, text="Disease AI", 
                               font=ctk.CTkFont(size=22, weight="bold"), text_color=self.primary_blue)
        self.logo.pack(pady=(30, 0), padx=20, anchor="w")
        
        self.sub_logo = ctk.CTkLabel(self.sidebar, text="CLINICAL INTELLIGENCE", 
                                   font=ctk.CTkFont(size=10, weight="bold"), text_color=self.text_muted)
        self.sub_logo.pack(pady=(0, 40), padx=20, anchor="w")

        # Nav Buttons
        nav_items = ["Symptoms", "Diseases", "Parameters", "Patients", "Analysis"]
        for item in nav_items:
            btn = ctk.CTkButton(self.sidebar, text=item, height=40, corner_radius=8,
                               fg_color="transparent", text_color=self.text_dark,
                               hover_color="#ebecf0", anchor="w", font=ctk.CTkFont(size=14))
            btn.pack(fill="x", padx=15, pady=5)

        # User Profile at Bottom
        self.profile = ctk.CTkLabel(self.sidebar, text="RS   Rida Shaikh\n        Chief Pathologist", 
                                  justify="left", font=ctk.CTkFont(size=12), text_color=self.text_dark)
        self.profile.pack(side="bottom", pady=30, padx=20, anchor="w")

        # ==================== MAIN CONTENT ====================
        self.main_view = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_view.grid(row=0, column=1, sticky="nsew", padx=40, pady=30)
        self.main_view.grid_columnconfigure((0, 1, 2), weight=1)

        # Header Text
        self.breadcrumb = ctk.CTkLabel(self.main_view, text="Dashboard > Overview", text_color=self.text_muted)
        self.breadcrumb.grid(row=0, column=0, sticky="w", pady=(0, 20))

        self.title_lbl = ctk.CTkLabel(self.main_view, text="Clinical Overview", 
                                    font=ctk.CTkFont(size=36, weight="bold"), text_color=self.text_dark)
        self.title_lbl.grid(row=1, column=0, columnspan=3, sticky="w")

        self.subtitle_lbl = ctk.CTkLabel(self.main_view, text="Welcome back, Dr. Shaikh. Your diagnostic pipeline is optimized with the latest predictive cohorts.", 
                                       font=ctk.CTkFont(size=14), text_color=self.text_muted)
        self.subtitle_lbl.grid(row=2, column=0, columnspan=3, sticky="w", pady=(5, 40))

        # ==================== CARDS SECTION ====================
        
        # Card 1: Patient Records (White)
        card1 = ctk.CTkFrame(self.main_view, height=220, fg_color="#ffffff", corner_radius=15)
        card1.grid(row=3, column=0, sticky="nsew", padx=(0, 10))
        card1.pack_propagate(False)
        ctk.CTkLabel(card1, text="Patient Records", font=ctk.CTkFont(size=18, weight="bold"), text_color=self.text_dark).pack(anchor="w", padx=20, pady=(30, 10))
        ctk.CTkLabel(card1, text="Securely manage and view comprehensive clinical histories of active patients.", wraplength=200, justify="left", text_color=self.text_muted).pack(anchor="w", padx=20)
        ctk.CTkLabel(card1, text="View Records →", font=ctk.CTkFont(weight="bold"), text_color=self.primary_blue).pack(anchor="w", padx=20, pady=(30, 0))

        # Card 2: Predict Disease (BLUE Highlight)
        card2 = ctk.CTkFrame(self.main_view, height=220, fg_color=self.primary_blue, corner_radius=15)
        card2.grid(row=3, column=1, sticky="nsew", padx=10)
        card2.pack_propagate(False)
        ctk.CTkLabel(card2, text="Predict Disease", font=ctk.CTkFont(size=18, weight="bold"), text_color="#ffffff").pack(anchor="w", padx=20, pady=(30, 10))
        ctk.CTkLabel(card2, text="Leverage AI models to analyze symptoms and parameters for diagnostic support.", wraplength=200, justify="left", text_color="#e6f0ff").pack(anchor="w", padx=20)
        btn_run = ctk.CTkButton(card2, text="Run Diagnostic", fg_color="#ffffff", text_color=self.primary_blue, hover_color="#f4f7f6", corner_radius=20)
        btn_run.pack(anchor="w", padx=20, pady=(25, 0))

        # Card 3: Analysis (White)
        card3 = ctk.CTkFrame(self.main_view, height=220, fg_color="#ffffff", corner_radius=15)
        card3.grid(row=3, column=2, sticky="nsew", padx=(10, 0))
        card3.pack_propagate(False)
        ctk.CTkLabel(card3, text="Analysis", font=ctk.CTkFont(size=18, weight="bold"), text_color=self.text_dark).pack(anchor="w", padx=20, pady=(30, 10))
        ctk.CTkLabel(card3, text="Deep dive into data trends, outcomes, and predictive accuracy across patient cohorts.", wraplength=200, justify="left", text_color=self.text_muted).pack(anchor="w", padx=20)
        ctk.CTkLabel(card3, text="Explore Insights →", font=ctk.CTkFont(weight="bold"), text_color=self.text_dark).pack(anchor="w", padx=20, pady=(30, 0))

if __name__ == "__main__":
    app = MedicalDashboard()
    app.mainloop()
