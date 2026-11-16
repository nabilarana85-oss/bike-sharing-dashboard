# Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda berdasarkan hari kerja, jam penyewaan, musim, dan kondisi cuaca selama tahun 2011–2012.

## Pertanyaan Bisnis
1. Bagaimana perbedaan rata-rata jumlah penyewaan sepeda pada setiap jam antara hari kerja dan bukan hari kerja?
2. Bagaimana perbedaan rata-rata penyewaan sepeda berdasarkan musim dan kondisi cuaca?

## Struktur File
```
submission/
├── dashboard/
│   ├── main_data.csv
│   └── dashboard.py
├── data/
│   ├── hour.csv
│   └── day.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

- `dashboard/dashboard.py`: File dashboard Streamlit.
- `dashboard/main_data.csv`: Data hasil pembersihan yang dibaca oleh dashboard.
- `data/hour.csv`: Dataset mentah penyewaan sepeda per jam.
- `data/day.csv`: Dataset mentah penyewaan sepeda per hari.
- `notebook.ipynb`: Notebook analisis data.
- `requirements.txt`: Daftar library yang dibutuhkan.
- `url.txt`: Tautan dashboard Streamlit.

## Persiapan Environment

1. Pastikan Python sudah terinstal.
2. Download atau clone repository ini.
3. Buka terminal atau Command Prompt pada folder proyek.
4. Buat virtual environment:

   ```bash
   python -m venv .venv
   ```

5. Aktifkan virtual environment.

   Windows:
   ```bash
   .venv\Scripts\activate
   ```

   Mac/Linux:
   ```bash
   source .venv/bin/activate
   ```

## Instalasi Library

Jalankan perintah berikut:

```bash
pip install -r requirements.txt
```

## Menjalankan Dashboard

Jalankan perintah:

```bash
streamlit run dashboard/dashboard.py
```

Dashboard akan terbuka melalui browser pada alamat:

`http://localhost:8501`

## Fitur Dashboard
- Filter data berdasarkan tahun 2011 dan 2012.
- Visualisasi rata-rata penyewaan sepeda berdasarkan jam dan kategori hari.
- Visualisasi rata-rata penyewaan sepeda berdasarkan musim dan kondisi cuaca.

## Link Dashboard
https://bike-sharing-dashboard-6oppenu3es8pvanxqfxc8d.streamlit.app
