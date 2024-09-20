# Web Kriptografi by Joshua Abbel Rakaditya

Sebuah web sederhana yang mengimplementasikan 3 cipher kriptografi: **Vigenere Cipher**, **Playfair Cipher**, dan **Hill Cipher**. Web ini memungkinkan pengguna untuk melakukan enkripsi dan dekripsi pesan teks menggunakan kunci dengan panjang minimal 12 karakter.

## Fitur
- **Metode Input**: Pengguna dapat mengetikkan pesan secara langsung atau mengunggah file `.txt`.
- **Cipher yang Tersedia**: 
  - Vigenere Cipher
  - Playfair Cipher
  - Hill Cipher (hanya mendukung matriks 2x2)
- **Persyaratan Key**: Key minimal 12 karakter.
- **Enkripsi/Dekripsi**: Pengguna dapat memilih untuk mengenkripsi atau mendekripsi pesan yang diinput.
- **Dukungan File**: Dapat memproses file `.txt` yang diunggah.
- **Tanpa Spasi**: Segala jenis spasi akan dihapus tepat setelah pengguna melakukan aksi.
- **Capslock Otomatis**: Hasil output akan otomatis capslock.

## Instalasi

### Prasyarat
- Python 3.6
- Flask (untuk framework web)

1. **Clone repository**:
    ```bash
    git clone https://github.com/JoshuaAbbelR/Kriptografi-Joshua-Abbel-Rakaditya
    cd Kriptografi-Joshua-Abbel-Rakaditya
    ```

2. **Instalasi Flask**:
    ```bash
    pip install flask
    ```

3. **Menjalankan aplikasi Flask**:
    ```bash
    python app.py
    ```

4. **Akses aplikasi**:
    Buka browser dan akses `http://127.0.0.1:5000/`.

## Petunjuk Penggunaan

1. **Input Teks**: Masukkan pesan yang ingin dienkripsi atau didekripsi di area teks yang tersedia atau unggah file `.txt`.
2. **Key**: Masukkan key dengan panjang minimal 12 karakter.
3. **Pilih Cipher**: Pilih salah satu cipher yang tersedia (Vigenere, Playfair, atau Hill).
4. **Pilih Aksi**: Klik tombol **Encrypt** atau **Decrypt** untuk melakukan aksi.
5. **Hasil**: Hasil enkripsi atau dekripsi akan ditampilkan di area hasil setelah proses selesai.

## Tampilan GUI
![Screenshot (685)](https://github.com/user-attachments/assets/e78874ff-d634-4d3b-80fb-ff6a05514175)

## Contoh
### Input
- **Pesan**: `KRIPTOSERULHO`
- **Kunci**: `AKUCINTAILKOM`
- **Cipher**: Vigenere Cipher
- **Aksi**: Enkripsi

### Output
- **Pesan Terenkripsi**: `KBCRBBLEZFVVA`

## Struktur Proyek
```plaintext
.
├── app.py                # File aplikasi utama (Flask)
├── static/
│   └── style.css         # CSS untuk antarmuka web
├── templates/
│   └── index.html        # Template HTML untuk halaman utama
├── vigenere.py           # Implementasi cipher Vigenere
├── playfair.py           # Implementasi cipher Playfair
├── hill.py               # Implementasi cipher Hill
└── README.md             # File ini
