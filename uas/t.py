import sqlite3
import datetime

# Koneksi ke database
conn = sqlite3.connect('tugas.db')
cursor = conn.cursor()

# Buat tabel tugas jika belum ada
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tugas (
        id INTEGER PRIMARY KEY,
        nama TEXT,
        tanggal DATE,
        waktu TIME,
        prioritas TEXT
    )
""")

# Tambah jadwal/tugas
def tambah_tugas():
    nama = input("Masukkan nama tugas: ")
    tanggal = input("Masukkan tanggal tugas (YYYY-MM-DD): ")
    waktu = input("Masukkan waktu tugas (HH:MM): ")
    prioritas = input("Masukkan prioritas tugas (Tinggi, Moderat, Rendah): ")
    cursor.execute("INSERT INTO tugas (nama, tanggal, waktu, prioritas) VALUES (?, ?, ?, ?)", (nama, tanggal, waktu, prioritas))
    conn.commit()
    print("Tugas berhasil ditambahkan!")

# Notifikasi atau pengingat tugas yang mendekati tenggat
def notifikasi_tugas():
    tanggal_sekarang = datetime.datetime.now()
    cursor.execute("SELECT * FROM tugas WHERE tanggal <= ? AND waktu <= ?", (tanggal_sekarang.strftime("%Y-%m-%d"), tanggal_sekarang.strftime("%H:%M")))
    tugas_list = cursor.fetchall()
    for tugas in tugas_list:
        print(f"Notifikasi: Tugas '{tugas[1]}' akan segera jatuh tempo pada tanggal {tugas[2]} jam {tugas[3]}")

# Filter tugas berdasarkan prioritas
def filter_tugas():
    prioritas = input("Masukkan prioritas tugas (Tinggi, Moderat, Rendah): ")
    cursor.execute("SELECT * FROM tugas WHERE prioritas = ?", (prioritas,))
    tugas_list = cursor.fetchall()
    for tugas in tugas_list:
        print(f"Tugas '{tugas[1]}' dengan prioritas '{tugas[4]}' pada tanggal {tugas[2]} jam {tugas[3]}")

# Main program
def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Notifikasi Tugas")
        print("3. Filter Tugas")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tambah_tugas()
        elif pilihan == "2":
            notifikasi_tugas()
        elif pilihan == "3":
            filter_tugas()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()