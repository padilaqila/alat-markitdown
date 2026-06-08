# 📄 MarkItDown Web Converter

Sebuah aplikasi web ringan untuk mengonversi berbagai jenis dokumen (Word, PDF, Excel, PowerPoint) menjadi teks **Markdown (.md)** secara instan. 

Aplikasi ini menggunakan teknologi ekstraksi [Microsoft MarkItDown](https://github.com/microsoft/markitdown) di sisi *backend* dan dibungkus dengan antarmuka pengguna (UI) modern berbasis **PAPIC OS Design System**. Sangat cocok di-deploy secara gratis menggunakan infrastruktur Serverless Vercel.

---

## ✨ Fitur Utama

- **Multi-Format Support:** Mendukung konversi dari `.docx`, `.pdf`, `.xlsx`, `.pptx`, dan `.txt`.
- **Ekstraksi Cerdas:** Mengubah tabel, heading, dan format teks dokumen asli menjadi struktur Markdown yang rapi.
- **One-Click Download:** Tombol unduh otomatis untuk menyimpan hasil ekstraksi langsung ke file `.md`.
- **Desain Modern (PAPIC OS):** Antarmuka yang bersih, responsif, dilengkapi *custom file picker*, dan ramah perangkat seluler.
- **Arsitektur Serverless:** Backend berbasis Python Flask yang dirancang khusus untuk berjalan di Vercel Serverless Functions.

---

## 🛠️ Teknologi yang Digunakan

- **Frontend:** HTML5, CSS3 (PAPIC OS / Stacks Design System), Vanilla JavaScript.
- **Backend:** Python 3, Flask.
- **Core Engine:** `markitdown[all]` (Microsoft).
- **Deployment:** Vercel.

---

## 📁 Struktur Direktori

```text
📦 nama-repositori-kamu
 ┣ 📂 api
 ┃ ┗ 📜 index.py          # Logika backend Flask & Vercel Serverless Function
 ┣ 📜 index.html          # Tampilan antarmuka utama (Frontend)
 ┣ 📜 requirements.txt    # Daftar dependensi Python
 ┗ 📜 README.md           # Dokumentasi proyek
