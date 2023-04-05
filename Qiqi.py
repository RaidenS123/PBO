import tkinter as tk

class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        # buat user dan pass dengan widgets
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        # buat tombol login
        self.login_button = tk.Button(self, text="Masuk", command=self.login)
        self.login_button.pack()

    def login(self):
        # Masuk id dan pass
        username = self.username_entry.get()
        password = self.password_entry.get()

        # cek id dan pass benar
        if username == "Carlos" and password == "123456":
            print("Berhasil masuk")
        else:
            print("User dan pass tidak sesuai")

# buat window
root = tk.Tk()
login_frame = LoginFrame(root)
login_frame.pack()

# memulai aplikasi
root.mainloop()
