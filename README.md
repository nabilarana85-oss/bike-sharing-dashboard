# Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda berdasarkan hari kerja, jam penyewaan, musim, dan kondisi cuaca selama tahun 2011–2012.

## Pertanyaan Bisnis
1. Bagaimana perbedaan rata-rata jumlah penyewaan sepeda pada setiap jam antara hari kerja dan bukan hari kerja?
2. Bagaimana perbedaan rata-rata penyewaan sepeda berdasarkan musim dan kondisi cuaca?

## Struktur File
- `dashboard.py`: File dashboard Streamlit.
- `hour.csv`: Dataset penyewaan sepeda per jam.
- `day.csv`: Dataset penyewaan sepeda per hari.
- `requirements.txt`: Daftar library yang dibutuhkan.
- `Copy_of_Proyek_Analisis_Data (2).ipynb`: Notebook analisis data.

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
streamlit run dashboard.py
```

Dashboard akan terbuka melalui browser pada alamat:

`http://localhost:8501`

## Fitur Dashboard
- Filter data berdasarkan tahun 2011 dan 2012.
- Visualisasi rata-rata penyewaan sepeda berdasarkan jam dan kategori hari.
- Visualisasi rata-rata penyewaan sepeda berdasarkan musim dan kondisi cuaca.

## Link Dashboard
https://bike-sharing-dashboard-asxf8ypawqdd6neykppkxr.streamlit.app
