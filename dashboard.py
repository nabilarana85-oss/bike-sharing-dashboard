
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

# Judul dashboard
st.title("🚲 Bike Sharing Dashboard")
st.write("Dashboard Analisis Data Penyewaan Sepeda Tahun 2011–2012")

# Memuat dataset
@st.cache_data
def load_data():
    hour_df = pd.read_csv("hour.csv")
    day_df = pd.read_csv("day.csv")
    return hour_df, day_df

hour_df, day_df = load_data()

# Filter tahun
st.subheader("Filter Tahun")

year_options = {
    "Semua Tahun": None,
    "2011": 0,
    "2012": 1
}

selected_year = st.selectbox(
    "Pilih Tahun:",
    options=list(year_options.keys())
)

if year_options[selected_year] is not None:
    hour_df = hour_df[hour_df['yr'] == year_options[selected_year]]
    day_df = day_df[day_df['yr'] == year_options[selected_year]]

# Ringkasan Statistik (KPI)

st.subheader("Ringkasan Penyewaan Sepeda")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Penyewaan",
        value=f"{hour_df['cnt'].sum():,}"
    )

with col2:
    st.metric(
        label="Rata-rata Penyewaan per Jam",
        value=f"{hour_df['cnt'].mean():.2f}"
    )

with col3:
    st.metric(
        label="Rata-rata Penyewaan per Hari",
        value=f"{day_df['cnt'].mean():.2f}"
    )

# Menampilkan informasi dataset
st.subheader("Data Penyewaan Sepeda")
st.write("Dataset berhasil dimuat.")

st.write("Data penyewaan per jam:")
st.dataframe(hour_df.head())

st.write("Data penyewaan per hari:")
st.dataframe(day_df.head())

# Visualisasi 1: Hari Kerja vs Bukan Hari Kerja

st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Jam")

hourly_workingday = filtered_hour.groupby(
    ['hr', 'workingday']
)['cnt'].mean().reset_index()

hourly_workingday['Kategori Hari'] = hourly_workingday['workingday'].map({
    0: 'Bukan Hari Kerja',
    1: 'Hari Kerja'
})

fig, ax = plt.subplots(figsize=(12, 6))

sns.lineplot(
    data=hourly_workingday,
    x='hr',
    y='cnt',
    hue='Kategori Hari',
    marker='o',
    ax=ax
)

ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.set_xticks(range(24))
ax.set_title("Pola Penyewaan Sepeda per Jam")
st.pyplot(fig)

# Visualisasi 2: Musim dan Kondisi Cuaca

st.subheader("2. Rata-rata Penyewaan Berdasarkan Musim dan Cuaca")

season_weather_data = day_df.groupby(
    ['season', 'weathersit']
)['cnt'].mean().reset_index()

season_weather_data['season'] = season_weather_data['season'].map({
    1: 'Spring',
    2: 'Summer',
    3: 'Fall',
    4: 'Winter'
})

season_weather_data['weathersit'] = season_weather_data['weathersit'].map({
    1: 'Cerah',
    2: 'Berawan',
    3: 'Hujan Ringan',
    4: 'Hujan Lebat'
})

fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(
    data=season_weather_data,
    x='season',
    y='cnt',
    hue='weathersit',
    ax=ax
)

ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Penyewaan Sepeda per Hari")
ax.set_title("Rata-rata Penyewaan Berdasarkan Musim dan Kondisi Cuaca")
ax.legend(title="Kondisi Cuaca")

st.pyplot(fig)

plt.close(fig)

# Visualisasi 3: Pola Penyewaan Berdasarkan Jam

st.subheader("3. Pola Penyewaan Sepeda Berdasarkan Jam")

hourly_data = hour_df.groupby(
    ['hr', 'workingday']
)['cnt'].mean().reset_index()

hourly_data['workingday'] = hourly_data['workingday'].map({
    0: 'Bukan Hari Kerja',
    1: 'Hari Kerja'
})

fig, ax = plt.subplots(figsize=(10, 5))

sns.lineplot(
    data=hourly_data,
    x='hr',
    y='cnt',
    hue='workingday',
    marker='o',
    ax=ax
)

ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.set_title("Pola Penyewaan Sepeda Berdasarkan Jam")
ax.set_xticks(range(0, 24))
ax.legend(title="Kategori Hari")

st.pyplot(fig)

plt.close(fig)
