import tkinter as tk
from tkinter import ttk, messagebox


# Data penyimpanan pengguna dan soal
data_pengguna = {
    "1": {"password": "1", "role": "admin"}
}
data_kuis = [
    {"question": "Apa planet terbesar dalam tata surya kita?", "options": ["Mars", "Jupiter", "Pluto", "Saturnus"], "answer": "Jupiter", "points": 10},
    {"question": "Sungai terpanjang di Indonesia terletak di pulau?", "options": ["Kalimantan", "Sumatra", "Jawa", "Sulawesi"], "answer": "Kalimantan", "points": 10},
    {"question": "Berapa jumlah hari pada tahun kabisat?", "options": ["144 hari", "256 hari", "366 hari", "401 hari"], "answer": "366 hari", "points": 10},
    {"question": "Arah jam 09.00 sama dengan arah?", "options": ["Barat", "Timur", "Selatan", "Barat Daya"], "answer": "Barat", "points": 10},
    {"question": "Berapa jumlah kotak tempat bidak pada papan catur?", "options": ["54", "62", "64", "56"], "answer": "64", "points": 10},
    {"question": "Hewan nasional Australia adalah...", "options": ["Koala", "Kanguru", "Platipus", "Gajah"], "answer": "Kanguru", "points": 10},
    {"question": "Bunga nasional Jepang adalah...", "options": ["Sakura", "Tulip", "Mawar", "Melati"], "answer": "Sakura", "points": 10},
    {"question": "Umar Wirahadikusuma adalah wakil presiden Indonesia ke?", "options": ["5", "3", "2", "4"], "answer": "4", "points": 10},
    {"question": "Benua apa yang disebut dengan benua kuning?", "options": ["Asia", "Afrika", "Eropa", "Australia"], "answer": "Asia", "points": 10},
    {"question": "Patung Sphinx banyak dijumpai di negara?", "options": ["Mesir", "Swiss", "Indonesia", "India"], "answer": "Mesir", "points": 10},
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
        admin_window.geometry("600x400")
        admin_window.configure(bg="#f0f0f0")
        
        frame = ttk.Frame(admin_window, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Menu Admin", style='Header.TLabel').pack(pady=20)
        
        def open_question_manager():
            self.manage_questions(admin_window)
        
        ttk.Button(frame, text="Kelola Soal", command=open_question_manager).pack(pady=10)
        ttk.Button(frame, text="Kembali ke Menu Utama", command=self.main_menu).pack(pady=10)
        
        self.center_window(admin_window)

    def manage_questions(self, parent_window):
        question_window = tk.Toplevel(parent_window)
        question_window.title("Kelola Soal")
        question_window.geometry("700x500")
        question_window.configure(bg="#f0f0f0")
        
        def refresh_question_list():
            for widget in question_list_frame.winfo_children():
                widget.destroy()
            for idx, question in enumerate(data_kuis):
                ttk.Label(question_list_frame, text=f"{idx + 1}. {question['question']}").pack(anchor="w")
                ttk.Button(question_list_frame, text="Edit", command=lambda i=idx: edit_question(i)).pack(side="right")
                ttk.Button(question_list_frame, text="Hapus", command=lambda i=idx: delete_question(i)).pack(side="right")
        
        def add_question():
            def save_question():
                new_question = question_entry.get()
                new_options = [opt1_entry.get(), opt2_entry.get(), opt3_entry.get(), opt4_entry.get()]
                new_answer = answer_entry.get()
                new_points = points_entry.get()
                if not (new_question and all(new_options) and new_answer and new_points):
                    messagebox.showerror("Error", "Semua kolom harus diisi!")
                    return
                data_kuis.append({
                    "question": new_question,
                    "options": new_options,
                    "answer": new_answer,
                    "points": int(new_points)
                })
                refresh_question_list()
                add_window.destroy()
            
            add_window = tk.Toplevel(question_window)
            add_window.title("Tambah Soal")
            add_window.geometry("400x400")
            add_window.configure(bg="#f0f0f0")

            frame = ttk.Frame(add_window, padding="20")
            frame.pack(fill=tk.BOTH, expand=True)

            ttk.Label(frame, text="Tambah Soal", style='Header.TLabel').pack(pady=10)

            ttk.Label(frame, text="Pertanyaan:").pack(anchor="w", pady=5)
            question_entry = ttk.Entry(frame, width=50)
            question_entry.pack(pady=5)

            ttk.Label(frame, text="Opsi Jawaban:").pack(anchor="w", pady=5)
            opt1_entry = ttk.Entry(frame, width=50)
            opt1_entry.pack(pady=5)
            opt2_entry = ttk.Entry(frame, width=50)
            opt2_entry.pack(pady=5)
            opt3_entry = ttk.Entry(frame, width=50)
            opt3_entry.pack(pady=5)
            opt4_entry = ttk.Entry(frame, width=50)
            opt4_entry.pack(pady=5)

            ttk.Label(frame, text="Jawaban Benar:").pack(anchor="w", pady=5)
            answer_entry = ttk.Entry(frame, width=50)
            answer_entry.pack(pady=5)

            ttk.Label(frame, text="Poin:").pack(anchor="w", pady=5)
            points_entry = ttk.Entry(frame, width=20)
            points_entry.pack(pady=5)

            ttk.Button(frame, text="Simpan", command=save_question).pack(pady=10)

            self.center_window(add_window)

        def edit_question(index):
            def save_edited_question():
                edited_question = question_entry.get()
                edited_options = [opt1_entry.get(), opt2_entry.get(), opt3_entry.get(), opt4_entry.get()]
                edited_answer = answer_entry.get()
                edited_points = points_entry.get()
                if not (edited_question and all(edited_options) and edited_answer and edited_points):
                    messagebox.showerror("Error", "Semua kolom harus diisi!")
                    return
                data_kuis[index] = {
                    "question": edited_question,
                    "options": edited_options,
                    "answer": edited_answer,
                    "points": int(edited_points)
                }
                refresh_question_list()
                edit_window.destroy()

            question_data = data_kuis[index]

            edit_window = tk.Toplevel(question_window)
            edit_window.title("Edit Soal")
            edit_window.geometry("400x400")
            edit_window.configure(bg="#f0f0f0")

            frame = ttk.Frame(edit_window, padding="20")
            frame.pack(fill=tk.BOTH, expand=True)

            ttk.Label(frame, text="Edit Soal", style='Header.TLabel').pack(pady=10)

            ttk.Label(frame, text="Pertanyaan:").pack(anchor="w", pady=5)
            question_entry = ttk.Entry(frame, width=50)
            question_entry.insert(0, question_data["question"])
            question_entry.pack(pady=5)

            ttk.Label(frame, text="Opsi Jawaban:").pack(anchor="w", pady=5)
            opt1_entry = ttk.Entry(frame, width=50)
            opt1_entry.insert(0, question_data["options"][0])
            opt1_entry.pack(pady=5)
            opt2_entry = ttk.Entry(frame, width=50)
            opt2_entry.insert(0, question_data["options"][1])
            opt2_entry.pack(pady=5)
            opt3_entry = ttk.Entry(frame, width=50)
            opt3_entry.insert(0, question_data["options"][2])
            opt3_entry.pack(pady=5)
            opt4_entry = ttk.Entry(frame, width=50)
            opt4_entry.insert(0, question_data["options"][3])
            opt4_entry.pack(pady=5)

            ttk.Label(frame, text="Jawaban Benar:").pack(anchor="w", pady=5)
            answer_entry = ttk.Entry(frame, width=50)
            answer_entry.insert(0, question_data["answer"])
            answer_entry.pack(pady=5)

            ttk.Label(frame, text="Poin:").pack(anchor="w", pady=5)
            points_entry = ttk.Entry(frame, width=20)
            points_entry.insert(0, question_data["points"])
            points_entry.pack(pady=5)

            ttk.Button(frame, text="Simpan", command=save_edited_question).pack(pady=10)

            self.center_window(edit_window)

        def delete_question(index):
            confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus soal ini?")
            if confirm:
                del data_kuis[index]
                refresh_question_list()

        ttk.Label(question_window, text="Kelola Soal", style='Header.TLabel').pack(pady=10)

        question_list_frame = ttk.Frame(question_window, padding="10")
        question_list_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Button(question_window, text="Tambah Soal", command=add_question).pack(pady=10)

        refresh_question_list()
        self.center_window(question_window)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = QuizApp()
    app.run()
