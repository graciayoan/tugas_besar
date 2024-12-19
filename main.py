# Data penyimpanan akun pengguna dan soal (disimpan dalam memori)
data_pengguna = {
    "admin": {"password": "saya adalah admin", "role": "admin"}  # Default akun admin
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

# Fungsi untuk login
def login():
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    if username in data_pengguna and data_pengguna[username]['password'] == password:
        print("Login berhasil!")
        return username
    else:
        print("Username atau password salah!")
        return None

# Fungsi untuk mendaftar akun
def signup():
    print("\n=== SIGN UP ===")
    username = input("Username: ")
    if username in data_pengguna:
        print("Username sudah terdaftar!")
        return None
    password = input("Password: ")
    data_pengguna[username] = {"password": password, "role": "user"}  # Default role nya user
    print(f"Akun {username} berhasil dibuat!")
    return username

# Fungsi untuk menjalankan kuis
def take_quiz(username):
    print("\n=== KUIS ===")
    score = 0
    for i, question in enumerate(data_kuis, 1):
        print(f"\nSoal {i}: {question['question']}")
        for j, option in enumerate(question['options'], 1):
            print(f"{j}. {option}")
        
        # Validasi input pilihan jawaban
        while True:
            try:
                answer = int(input("Pilih jawaban (1-3): "))
                if answer < 1 or answer > 3:
                    raise ValueError("Pilihan harus antara 1 dan 3.")
                break
            except ValueError as e:
                print(f"Input salah: {e}")
        
        if question['options'][answer - 1] == question['answer']:
            score += question['points']
    
    print(f"\nSkor Anda: {score}")
    
    # Simpan skor pengguna
    data_pengguna[username]['score'] = score
    
    # Pilihan untuk mengulang kuis atau keluar
    while True:
        choice = input("\nIngin mengulang kuis? (y/n): ").lower()
        if choice == 'y':
            take_quiz(username)
        elif choice == 'n':
            print("Terima kasih telah mengikuti kuis!")
            break
        else:
            print("Pilihan kamu tidak vali!")

# Fungsi untuk tampilan admin
def admin_menu():
    print("\n=== ADMIN MENU ===")
    while True:
        print("\n1. Tambah Soal")
        print("2. Edit Soal")
        print("3. Hapus Soal")
        print("4. Atur Poin Soal")
        print("5. Kembali ke Login")
        
        # Validasi input pilihan menu admin
        while True:
            try:
                choice = int(input("Pilih menu: "))
                if choice < 1 or choice > 5:
                    raise ValueError("Pilihan harus antara 1 dan 5.")
                break
            except ValueError as e:
                print(f"Input salah: {e}")
        
        if choice == 1:
            add_question()
        elif choice == 2:
            edit_question()
        elif choice == 3:
            delete_question()
        elif choice == 4:
            set_question_points()
        elif choice == 5:
            break

# Fungsi untuk menambah soal
def add_question():
    question = input("\nMasukkan soal baru: ")
    options = [input("Pilihan 1: "), input("Pilihan 2: "), input("Pilihan 3: ")]
    answer = input("Jawaban yang benar: ")
    
    # Validasi poin
    while True:
        try:
            points = int(input("Poin soal: "))
            if points <= 0:
                raise ValueError("Poin harus lebih besar dari 0.")
            break
        except ValueError as e:
            print(f"Input salah: {e}")
    
    data_kuis.append({"question": question, "options": options, "answer": answer, "points": points})
    print("Soal berhasil ditambahkan!")

# Fungsi untuk mengedit soal
def edit_question():
    list_questions()
    
    # Validasi input nomor soal
    while True:
        try:
            question_index = int(input("\nPilih nomor soal yang ingin diedit: ")) - 1
            if question_index < 0 or question_index >= len(data_kuis):
                raise ValueError("Nomor soal tidak valid!")
            break
        except ValueError as e:
            print(f"Input salah: {e}")
    
    question = input("Masukkan soal baru: ")
    options = [input("Pilihan 1: "), input("Pilihan 2: "), input("Pilihan 3: ")]
    answer = input("Jawaban yang benar: ")
    
    # Validasi poin
    while True:
        try:
            points = int(input("Poin soal: "))
            if points <= 0:
                raise ValueError("Poin harus lebih besar dari 0.")
            break
        except ValueError as e:
            print(f"Input salah: {e}")
    
    data_kuis[question_index] = {"question": question, "options": options, "answer": answer, "points": points}
    print("Soal berhasil diubah!")

# Fungsi untuk menghapus soal
def delete_question():
    list_questions()
    
    # Validasi input nomor soal
    while True:
        try:
            question_index = int(input("\nPilih nomor soal yang ingin dihapus: ")) - 1
            if question_index < 0 or question_index >= len(data_kuis):
                raise ValueError("Nomor soal tidak valid!")
            break
        except ValueError as e:
            print(f"Input salah: {e}")
    
    data_kuis.pop(question_index)
    print("Soal berhasil dihapus!")

# Fungsi untuk mengatur poin soal
def set_question_points():
    list_questions()
    
    # Validasi input nomor soal
    while True:
        try:
            question_index = int(input("\nPilih nomor soal yang ingin diubah poinnya: ")) - 1
            if question_index < 0 or question_index >= len(data_kuis):
                raise ValueError("Nomor soal tidak valid!")
            break
        except ValueError as e:
            print(f"Input salah: {e}")
    
    while True:
        try:
            points = int(input("Masukkan jumlah poin baru: "))
            if points <= 0:
                raise ValueError("Poin harus lebih besar dari 0.")
            break
        except ValueError:
            print(f"Input salah: harus angka dan lebih besar dari 0")
    
    data_kuis[question_index]['points'] = points
    print("Poin soal berhasil diubah!")

# Fungsi untuk menampilkan daftar soal
def list_questions():
    print("\nDaftar Soal:")
    for idx, question in enumerate(data_kuis, 1):
        print(f"{idx}. {question['question']}")

# Menu utama
def main():
    print("Selamat datang di sistem kuis!")
    while True:
        print("\n1. Login")
        print("2. Sign Up")
        print("3. Keluar")
        
        # Validasi input pilihan menu
        while True:
            try:
                choice = int(input("Pilih menu: "))
                if choice < 1 or choice > 3:
                    raise ValueError("Pilihan haru antsara 1 dan 3.")
                break
            except ValueError:
                print(f"Input salah: harus angka dan pilihan harus antara 1 dan 3")
        
        if choice == 1:
            username = login()
            if username:
                if data_pengguna[username]['role'] == "admin":
                    admin_menu()
                else:
                    take_quiz(username)
        elif choice == 2:
            username = signup()
            if username:
                print("Akun berhasil dibuat, silakan login!")
        elif choice == 3:
            print("Terima kasih, sampai jumpa!")
            break

import tkinter as tk
from tkinter import messagebox

# Data penyimpanan akun pengguna dan soal
data_pengguna = {
    "admin": {"password": "saya adalah admin", "role": "admin"}  # Default akun admin
}
data_kuis = [
    {"question": "Apa ibu kota Indonesia?", "options": ["Jakarta", "Bandung", "Surabaya"], "answer": "Jakarta", "points": 10},
    {"question": "Berapa banyak planet di tata surya?", "options": ["7", "8", "9"], "answer": "8", "points": 10},
]

# Fungsi untuk login
def login_gui():
    def login_action():
        username = entry_username.get()
        password = entry_password.get()
        if username in data_pengguna and data_pengguna[username]['password'] == password:
            messagebox.showinfo("Login", "Login berhasil!")
            root_login.destroy()
            if data_pengguna[username]['role'] == "admin":
                admin_menu_gui()
            else:
                take_quiz_gui(username)
        else:
            messagebox.showerror("Login", "Username atau password salah!")

    root_login = tk.Tk()
    root_login.title("Login")
    
    tk.Label(root_login, text="Username:").pack()
    entry_username = tk.Entry(root_login)
    entry_username.pack()
    
    tk.Label(root_login, text="Password:").pack()
    entry_password = tk.Entry(root_login, show="*")
    entry_password.pack()

    tk.Button(root_login, text="Login", command=login_action).pack()
    tk.Button(root_login, text="Sign Up", command=signup_gui).pack()

    root_login.mainloop()

# Fungsi untuk signup
def signup_gui():
    def signup_action():
        username = entry_username.get()
        password = entry_password.get()
        if username in data_pengguna:
            messagebox.showerror("Sign Up", "Username sudah terdaftar!")
        else:
            data_pengguna[username] = {"password": password, "role": "user"}
            messagebox.showinfo("Sign Up", f"Akun {username} berhasil dibuat!")
            root_signup.destroy()
            login_gui()

    root_signup = tk.Tk()
    root_signup.title("Sign Up")
    
    tk.Label(root_signup, text="Username:").pack()
    entry_username = tk.Entry(root_signup)
    entry_username.pack()
    
    tk.Label(root_signup, text="Password:").pack()
    entry_password = tk.Entry(root_signup, show="*")
    entry_password.pack()

    tk.Button(root_signup, text="Sign Up", command=signup_action).pack()
    tk.Button(root_signup, text="Back to Login", command=lambda: [root_signup.destroy(), login_gui()]).pack()

    root_signup.mainloop()

# Fungsi untuk menjalankan kuis dengan GUI
def take_quiz_gui(username):
    current_question_index = 0
    score = 0
    var_answers = []

    def next_question():
        nonlocal current_question_index
        if current_question_index < len(data_kuis) - 1:
            current_question_index += 1
            display_question()

    def prev_question():
        nonlocal current_question_index
        if current_question_index > 0:
            current_question_index -= 1
            display_question()

    def submit_quiz():
        nonlocal score
        for idx, question in enumerate(data_kuis):
            selected_option = var_answers[idx].get()
            if selected_option == question['answer']:
                score += question['points']
        
        messagebox.showinfo("Skor Kuis", f"Skor Anda: {score}")
        data_pengguna[username]['score'] = score
        if messagebox.askyesno("Ulang Kuis", "Ingin mengulang kuis?"):
            take_quiz_gui(username)
        else:
            root_quiz.destroy()

    def display_question():
        question = data_kuis[current_question_index]
        for widget in root_quiz.winfo_children():
            widget.destroy()

        tk.Label(root_quiz, text=f"Soal {current_question_index + 1}: {question['question']}").pack()

        var_answer = tk.StringVar(value="")
        var_answers.append(var_answer)
        for option in question['options']:
            tk.Radiobutton(root_quiz, text=option, variable=var_answer, value=option).pack()

        tk.Button(root_quiz, text="Next", command=next_question).pack(side="left", padx=10)
        tk.Button(root_quiz, text="Prev", command=prev_question).pack(side="right", padx=10)
        tk.Button(root_quiz, text="Submit", command=submit_quiz).pack(side="right", padx=10)

    root_quiz = tk.Tk()
    root_quiz.title("Kuis")

    display_question()
    root_quiz.mainloop()

# Fungsi untuk menu admin dengan GUI
def admin_menu_gui():
    def add_question_gui():
        def add_question_action():
            question = entry_question.get()
            options = [entry_option1.get(), entry_option2.get(), entry_option3.get()]
            answer = entry_answer.get()
            try:
                points = int(entry_points.get())
                if points <= 0:
                    raise ValueError("Poin harus lebih besar dari 0.")
                data_kuis.append({"question": question, "options": options, "answer": answer, "points": points})
                messagebox.showinfo("Admin Menu", "Soal berhasil ditambahkan!")
                root_add_question.destroy()
            except ValueError as e:
                messagebox.showerror("Admin Menu", str(e))

        root_add_question = tk.Tk()
        root_add_question.title("Tambah Soal")

        tk.Label(root_add_question, text="Masukkan soal:").pack()
        entry_question = tk.Entry(root_add_question)
        entry_question.pack()
        
        tk.Label(root_add_question, text="Pilihan 1:").pack()
        entry_option1 = tk.Entry(root_add_question)
        entry_option1.pack()

        tk.Label(root_add_question, text="Pilihan 2:").pack()
        entry_option2 = tk.Entry(root_add_question)
        entry_option2.pack()

        tk.Label(root_add_question, text="Pilihan 3:").pack()
        entry_option3 = tk.Entry(root_add_question)
        entry_option3.pack()

        tk.Label(root_add_question, text="Jawaban yang benar:").pack()
        entry_answer = tk.Entry(root_add_question)
        entry_answer.pack()

        tk.Label(root_add_question, text="Poin soal:").pack()
        entry_points = tk.Entry(root_add_question)
        entry_points.pack()

        tk.Button(root_add_question, text="Tambah Soal", command=add_question_action).pack()
        root_add_question.mainloop()

    def admin_menu_action():
        root_admin_menu = tk.Tk()
        root_admin_menu.title("Menu Admin")

        tk.Button(root_admin_menu, text="Tambah Soal", command=add_question_gui).pack()
        tk.Button(root_admin_menu, text="Keluar", command=root_admin_menu.destroy).pack()

        root_admin_menu.mainloop()

    admin_menu_action()

# Menu utama
def main_gui():
    root = tk.Tk()
    root.title("Selamat Datang di Sistem Kuis")

    tk.Button(root, text="Login", command=login_gui).pack()
    tk.Button(root, text="Sign Up", command=signup_gui).pack()
    tk.Button(root, text="Keluar", command=root.destroy).pack()

    root.mainloop()

# Jalankan aplikasi GUI
if __name__ == "__main__":
    main_gui()
