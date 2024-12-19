import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font

# Data storage remains the same
data_pengguna = {
    "admin": {"password": "saya adalah admin", "role": "admin"}
}
data_kuis = [
    {"question": "Apa planet terbesar dalam tata surya kita?", "options": ["Mars", "Jupiter", "Pluto", "Saturnus"], "answer": "Jupiter", "points": 10},
    {"question": "Sungai terpanjang di indonesia terletak di pulau", "options": ["Kalimantan", "Sumatra", "Jawa", "Sulawesi"], "answer": "Kalimantan", "points": 10},
    {"question": "Berapa jumlah hari pada tahun kabisat?", "options": ["144 hari", "256 hari", "366 hari", "401 hari"], "answer": "366 hari", "points": 10},
    {"question": "Arah jam 09.00 sama dengan arah?", "options": ["Barat", "Timur", "Selatan", "Barat Daya"], "answer": "Barat", "points": 10},
    {"question": "Berapa jumlah kotak kotak tempat bidak pada papan catur?", "options": ["54", "62", "64", "56"], "answer": "64", "points": 10},
    {"question": "Hewan nasional Australia adalah...", "options": ["Koala", "Kanguru", "Platipus", "Gajah"], "answer": "Kanguru", "points": 10},
    {"question": "Bunga nasional Jepang adalah...", "options": ["Sakura", "Tulip", "Mawar", "Melati"], "answer": "Sakura", "points": 10},
    {"question": "Umar Wirahadikusuma adalah wakil presiden Indonesia ke", "options": ["5", "3", "2", "4"], "answer": "4", "points": 10},
    {"question": "Benua apa yang disebut dengan benua kuning? ", "options": ["Asia", "Afrika", "Eropa", "Australia"], "answer": "Asia", "points": 10},
    {"question": "Patung Sphinx banyak dijumpai di negara", "options": ["Mesir", "Swiss", "Indonesia", "India"], "answer": "Mesir", "points": 10},
]

class QuizApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistem Kuis")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TButton', padding=10, font=('Helvetica', 10))
        self.style.configure('TLabel', font=('Helvetica', 11), background="#f0f0f0")
        self.style.configure('Header.TLabel', font=('Helvetica', 16, 'bold'), background="#f0f0f0")
        
        self.main_menu()
        
    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')

    def create_frame(self):
        frame = ttk.Frame(self.root, padding="20")
        frame.place(relx=0.5, rely=0.5, anchor="center")
        return frame

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        frame = self.create_frame()
        
        ttk.Label(frame, text="Selamat Datang di Sistem Kuis", 
                 style='Header.TLabel').pack(pady=20)
        
        ttk.Button(frame, text="Login", command=self.login_window, 
                  width=30).pack(pady=10)
        ttk.Button(frame, text="Sign Up", command=self.signup_window, 
                  width=30).pack(pady=10)
        ttk.Button(frame, text="Keluar", command=self.root.quit, 
                  width=30).pack(pady=10)
        
        self.center_window(self.root)

    def login_window(self):
        login_window = tk.Toplevel(self.root)
        login_window.title("Login")
        login_window.geometry("400x300")
        login_window.configure(bg="#f0f0f0")
        
        frame = ttk.Frame(login_window, padding="20")
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        ttk.Label(frame, text="Login", style='Header.TLabel').pack(pady=20)
        
        ttk.Label(frame, text="Username:").pack()
        username_entry = ttk.Entry(frame, width=30)
        username_entry.pack(pady=5)
        
        ttk.Label(frame, text="Password:").pack()
        password_entry = ttk.Entry(frame, show="*", width=30)
        password_entry.pack(pady=5)
        
        def login_action():
            username = username_entry.get()
            password = password_entry.get()
            if username in data_pengguna and data_pengguna[username]['password'] == password:
                login_window.destroy()
                if data_pengguna[username]['role'] == "admin":
                    self.admin_menu()
                else:
                    self.take_quiz(username)
            else:
                messagebox.showerror("Error", "Username atau password salah!")
        
        ttk.Button(frame, text="Login", command=login_action, 
                  width=30).pack(pady=10)
        
        self.center_window(login_window)

    def signup_window(self):
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Sign Up")
        signup_window.geometry("400x300")
        signup_window.configure(bg="#f0f0f0")
        
        frame = ttk.Frame(signup_window, padding="20")
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        ttk.Label(frame, text="Sign Up", style='Header.TLabel').pack(pady=20)
        
        ttk.Label(frame, text="Username:").pack()
        username_entry = ttk.Entry(frame, width=30)
        username_entry.pack(pady=5)
        
        ttk.Label(frame, text="Password:").pack()
        password_entry = ttk.Entry(frame, show="*", width=30)
        password_entry.pack(pady=5)
        
        def signup_action():
            username = username_entry.get()
            password = password_entry.get()
            if username in data_pengguna:
                messagebox.showerror("Error", "Username sudah terdaftar!")
            else:
                data_pengguna[username] = {"password": password, "role": "user"}
                messagebox.showinfo("Success", f"Akun {username} berhasil dibuat!")
                signup_window.destroy()
        
        ttk.Button(frame, text="Sign Up", command=signup_action, 
                  width=30).pack(pady=10)
        
        self.center_window(signup_window)

    def take_quiz(self, username):
        quiz_window = tk.Toplevel(self.root)
        quiz_window.title("Kuis")
        quiz_window.geometry("600x400")
        quiz_window.configure(bg="#f0f0f0")
        
        current_question = {'value': 0}
        answers = []
        score = {'value': 0}
        
        main_frame = ttk.Frame(quiz_window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        question_frame = ttk.Frame(main_frame)
        question_frame.pack(fill=tk.BOTH, expand=True)
        
        def display_question():
            for widget in question_frame.winfo_children():
                widget.destroy()
                
            question = data_kuis[current_question['value']]
            
            ttk.Label(question_frame, 
                     text=f"Soal {current_question['value'] + 1} dari {len(data_kuis)}", 
                     style='Header.TLabel').pack(pady=10)
            
            ttk.Label(question_frame, 
                     text=question['question'],
                     wraplength=500).pack(pady=10)
            
            answer_var = tk.StringVar(value="")
            answers.append(answer_var)
            
            for option in question['options']:
                ttk.Radiobutton(question_frame, 
                              text=option,
                              variable=answer_var,
                              value=option).pack(pady=5)
        
        def next_question():
            if current_question['value'] < len(data_kuis) - 1:
                current_question['value'] += 1
                display_question()
        
        def prev_question():
            if current_question['value'] > 0:
                current_question['value'] -= 1
                display_question()
        
        def submit_quiz():
            score['value'] = 0
            for idx, question in enumerate(data_kuis):
                if answers[idx].get() == question['answer']:
                    score['value'] += question['points']
            
            data_pengguna[username]['score'] = score['value']
            messagebox.showinfo("Hasil", f"Skor Anda: {score['value']}")
            
            if messagebox.askyesno("Ulangi", "Ingin mengulang kuis?"):
                quiz_window.destroy()
                self.take_quiz(username)
            else:
                quiz_window.destroy()
        
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="< Sebelumnya", command=prev_question).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Selanjutnya >", command=next_question).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Selesai", command=submit_quiz).pack(side=tk.LEFT, padx=5)
        
        display_question()
        self.center_window(quiz_window)

    def admin_menu(self):
        admin_window = tk.Toplevel(self.root)
        admin_window.title("Admin Menu")
        admin_window.geometry("500x400")
        admin_window.configure(bg="#f0f0f0")
        
        frame = ttk.Frame(admin_window, padding="20")
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        ttk.Label(frame, text="Menu Admin", style='Header.TLabel').pack(pady=20)
        
        def add_question_window():
            add_window = tk.Toplevel(admin_window)
            add_window.title("Tambah Soal")
            add_window.geometry("500x500")
            add_window.configure(bg="#f0f0f0")
            
            frame = ttk.Frame(add_window, padding="20")
            frame.place(relx=0.5, rely=0.5, anchor="center")
            
            ttk.Label(frame, text="Tambah Soal Baru", style='Header.TLabel').pack(pady=20)
            
            entries = {}
            for field in ['question', 'option1', 'option2', 'option3', 'answer', 'points']:
                ttk.Label(frame, text=field.capitalize() + ":").pack()
                entry = ttk.Entry(frame, width=40)
                entry.pack(pady=5)
                entries[field] = entry
            
            def save_question():
                try:
                    points = int(entries['points'].get())
                    if points <= 0:
                        raise ValueError("Poin harus lebih dari 0")
                    
                    options = [entries['option1'].get(), 
                             entries['option2'].get(), 
                             entries['option3'].get()]
                    
                    data_kuis.append({
                        "question": entries['question'].get(),
                        "options": options,
                        "answer": entries['answer'].get(),
                        "points": points
                    })
                    messagebox.showinfo("Success", "Soal berhasil ditambahkan!")
                    add_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Poin harus berupa angka positif!")
            
            ttk.Button(frame, text="Simpan", command=save_question, 
                      width=30).pack(pady=10)
            
            self.center_window(add_window)
        
        ttk.Button(frame, text="Tambah Soal", command=add_question_window, 
                  width=30).pack(pady=10)
        ttk.Button(frame, text="Kembali", command=admin_window.destroy, 
                  width=30).pack(pady=10)
        
        self.center_window(admin_window)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = QuizApp()
    app.run()
