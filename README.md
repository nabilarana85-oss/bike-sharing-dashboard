
# Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi Proyek
Proyek ini merupakan analisis data penyewaan sepeda (*Bike Sharing Dataset*) pada periode tahun 2011–2012. Analisis dilakukan untuk mengetahui pola penyewaan sepeda berdasarkan hari kerja, musim, kondisi cuaca, dan waktu penyewaan.

Hasil analisis dibuat dalam bentuk visualisasi dan dashboard interaktif menggunakan Streamlit.

## Pertanyaan Bisnis
1. Bagaimana perbedaan rata-rata jumlah penyewaan sepeda per jam antara hari kerja dan bukan hari kerja selama tahun 2011–2012?
2. Bagaimana perbedaan rata-rata jumlah penyewaan sepeda per hari berdasarkan musim dan kondisi cuaca selama tahun 2011–2012?

## Dataset
Dataset yang digunakan dalam proyek ini adalah:
- `hour.csv`: berisi data penyewaan sepeda berdasarkan jam.
- `day.csv`: berisi data penyewaan sepeda berdasarkan hari.

Kedua dataset mencakup periode tahun 2011–2012.

## Tahapan Analisis Data

1. **Gathering Data**

   Memuat dataset `hour.csv` dan `day.csv` yang digunakan untuk proses analisis.

2. **Assessing Data**

   Memeriksa kondisi dataset, seperti jumlah data, tipe data, nilai kosong, dan data duplikat.

3. **Cleaning Data**

   Melakukan pemeriksaan dan penyesuaian data yang diperlukan agar data siap digunakan dalam analisis.

4. **Exploratory Data Analysis (EDA)**

   Mengeksplorasi data untuk mengetahui pola penyewaan sepeda berdasarkan hari kerja, musim, kondisi cuaca, dan jam.

5. **Explanatory Analysis**

   Membuat visualisasi untuk menjawab pertanyaan bisnis dan menyampaikan hasil analisis.

## Hasil Analisis

Berdasarkan hasil analisis, diperoleh beberapa temuan berikut:

- Rata-rata penyewaan sepeda per jam pada hari kerja sebesar 193,21, sedangkan pada bukan hari kerja sebesar 181,41.
- Pada hari kerja, penyewaan sepeda mencapai puncak sekitar pukul 08.00 dan 17.00.
- Pada bukan hari kerja, penyewaan sepeda cenderung mencapai puncak sekitar pukul 13.00.
- Berdasarkan musim dan kondisi cuaca, rata-rata penyewaan harian tertinggi terdapat pada musim gugur (*Fall*) dengan kondisi cuaca cerah.
- Kondisi cuaca yang lebih baik cenderung diikuti oleh jumlah penyewaan sepeda yang lebih tinggi.

## Dashboard

Dashboard dibuat menggunakan Streamlit untuk menampilkan hasil analisis data secara lebih mudah. Dashboard memiliki beberapa fitur, yaitu:

- Filter data berdasarkan tahun 2011 dan 2012.
- Menampilkan total penyewaan sepeda.
- Menampilkan rata-rata penyewaan per jam dan per hari.
- Membandingkan rata-rata penyewaan pada hari kerja dan bukan hari kerja.
- Menampilkan rata-rata penyewaan berdasarkan musim dan kondisi cuaca.
- Menampilkan pola penyewaan sepeda berdasarkan jam.

## Cara Menjalankan Dashboard

Pastikan Python sudah terpasang di komputer.

1. Simpan file `dashboard.py`, `hour.csv`, dan `day.csv` dalam satu folder.
2. Buka terminal atau Command Prompt pada folder tersebut.
3. Install library yang dibutuhkan dengan perintah:

   `pip install -r requirements.txt`

4. Jalankan dashboard menggunakan perintah:

   `streamlit run dashboard.py`

5. Setelah berhasil dijalankan, buka alamat lokal yang muncul di terminal. Biasanya dashboard dapat diakses melalui:

   `http://localhost:8501`

## Library yang Digunakan

- Pandas
- Matplotlib
- Seaborn
- Streamlit
