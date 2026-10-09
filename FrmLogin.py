import customtkinter as ctk
from tkinter import messagebox
from CLSUser import clsUser

# Theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class FrmLogin(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.logged_in = False

        self.title("Login - Disease AI")
        self.geometry("450x500")
        self.resizable(False, False)

        # Frame
        self.login_frame = ctk.CTkFrame(self, corner_radius=20)
        self.login_frame.pack(expand=True, padx=30, pady=30)

        # Title
        ctk.CTkLabel(
            self.login_frame,
            text="🩺 Disease AI",
            font=ctk.CTkFont(size=28, weight="bold")
        ).pack(pady=(20, 10))

        ctk.CTkLabel(
            self.login_frame,
            text="Login to continue"
        ).pack(pady=(0, 20))

        # Username
        self.txtUser = ctk.CTkEntry(
            self.login_frame,
            placeholder_text="Username",
            width=250,
            height=40
        )
        self.txtUser.pack(pady=10)

        # Password
        self.txtPass = ctk.CTkEntry(
            self.login_frame,
            placeholder_text="Password",
            show="*",
            width=250,
            height=40
        )
        self.txtPass.pack(pady=10)

        # Show Password
        self.show_var = ctk.BooleanVar()
        ctk.CTkCheckBox(
            self.login_frame,
            text="Show Password",
            variable=self.show_var,
            command=self.toggle_password
        ).pack(pady=5)

        # Button
        ctk.CTkButton(
            self.login_frame,
            text="Login",
            width=250,
            height=40,
            command=self.login
        ).pack(pady=20)

    def toggle_password(self):
        if self.show_var.get():
            self.txtPass.configure(show="")
        else:
            self.txtPass.configure(show="*")

    def login(self):
        username = self.txtUser.get()
        password = self.txtPass.get()

        if username == "" or password == "":
            messagebox.showwarning("Error", "Enter Username & Password")
            return

        obj = clsUser()
        obj.setUsername(username)
        obj.setPassword(password)

        if clsUser.checkLogin(obj):
            messagebox.showinfo("Success", "Login Successful")

            self.logged_in = True
            self.destroy()  # close login window

        else:
            messagebox.showerror("Error", "Invalid Username or Password")


# RUN APP
if __name__ == "__main__":
    app = FrmLogin()
    app.mainloop()
