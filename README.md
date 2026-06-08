# 📄 MarkItDown Web Converter (AI Prompt Optimizer)

Sebuah aplikasi web ringan untuk mengonversi berbagai jenis dokumen berat (Word, PDF, Excel, PowerPoint) menjadi teks **Markdown (.md)** murni secara instan. 

Aplikasi ini sangat cocok digunakan sebagai *tool* pendamping bagi kamu yang sering bekerja dengan AI (ChatGPT, Claude, Gemini, dll) atau developer yang menggunakan API LLM.

---

## 🤖 Mengapa Harus Convert ke Markdown untuk AI?

Jika kamu sering mengunggah file PDF atau Word langsung ke prompt AI, kamu sebenarnya sedang **membuang-buang banyak token**. 

Dokumen mentah mengandung sangat banyak metadata, *styling* tersembunyi, dan struktur kompleks yang membuat AI harus bekerja ekstra keras (dan memakan banyak token) hanya untuk membacanya. 

Dengan mengubahnya menjadi `.md` terlebih dahulu melalui alat ini:
1. **Pangkas Token Drastis (Hemat Kuota/Biaya):** File `.md` menghapus semua "sampah" visual dan hanya menyisakan teks murni dengan struktur semantik (Heading, List, Tabel). Ini adalah bahasa asli yang paling dipahami oleh LLM.
2. **Respon AI Lebih Cepat & Akurat:** Karena teksnya sudah bersih, AI tidak perlu lagi memecah format dokumen yang rumit. Konteks prompt kamu menjadi lebih padat, mengurangi risiko halusinasi, dan AI bisa langsung fokus pada isi konten.
3. **Bypass Limit File:** File PDF berukuran besar sering ditolak oleh platform AI. Teks `.md` ukurannya sangat kecil (hitungan Kilobyte), sehingga kamu bisa memasukkan lebih banyak informasi ke dalam satu prompt.

---

## ✨ Fitur Utama

- **Multi-Format Support:** Mendukung konversi dari `.docx`, `.pdf`, `.xlsx`, `.pptx`, dan `.txt`.
- **Ekstraksi Cerdas:** Mengubah tabel, *heading*, dan paragraf dokumen asli menjadi struktur Markdown yang rapi tanpa merusak konteks.
- **One-Click Download:** Tombol unduh otomatis untuk menyimpan hasil ekstraksi langsung ke file `.md`.
- **Arsitektur Serverless:** Backend ringan berbasis Python Flask yang dirancang khusus untuk berjalan cepat di Vercel.
- **Clean UI:** Antarmuka yang bersih, responsif, modern, dan sangat mudah digunakan baik di PC maupun *smartphone*.

---

## 🛠️ Teknologi yang Digunakan

- **Core Engine:** `markitdown[all]` (Teknologi ekstraksi dari Microsoft)
- **Backend:** Python 3, Flask
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Deployment:** Vercel (Serverless Functions)

---

## 📁 Struktur Direktori

```text
📦 alat-markitdown
 ┣ 📂 api
 ┃ ┗ 📜 index.py          # Logika backend Flask & Vercel Serverless Function
 ┣ 📜 index.html          # Tampilan antarmuka utama (Frontend)
 ┣ 📜 requirements.txt    # Daftar dependensi Python
 ┣ 📜 vercel.json         # Konfigurasi routing Vercel
 ┗ 📜 README.md           # Dokumentasi proyek
