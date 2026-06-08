from flask import Flask, request, jsonify
from markitdown import MarkItDown
import os
import tempfile

app = Flask(__name__)
markitdown = MarkItDown()

# Endpoint Utama untuk memanggil index.html di dalam folder static
@app.route('/')
def home():
    return app.send_static_file('index.html')

# Endpoint untuk memproses konversi file
@app.route('/convert', methods=['POST'])
def convert_file():
    if 'file' not in request.files:
        return jsonify({"error": "Tidak ada file yang diunggah"}), 400
        
    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return jsonify({"error": "Nama file belum dipilih"}), 400

    try:
        # Buat file sementara di server
        suffix = os.path.splitext(uploaded_file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
            uploaded_file.save(temp_file.name)
            temp_path = temp_file.name

        # Jalankan mesin konversi Microsoft MarkItDown
        result = markitdown.convert(temp_path)
        
        # Hapus kembali file sementara agar server tidak penuh
        os.remove(temp_path)

        # Kirim teks markdown kembali ke Frontend
        return jsonify({
            "filename": uploaded_file.filename,
            "markdown": result.text_content
        })

    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return jsonify({"error": str(e)}), 500