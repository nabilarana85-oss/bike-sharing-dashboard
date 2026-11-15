
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

# Ringkasan Statistik
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

# Informasi dataset
st.subheader("Data Penyewaan Sepeda")
st.write("Data penyewaan per jam:")
st.dataframe(hour_df.head())

st.write("Data penyewaan per hari:")
st.dataframe(day_df.head())

# Visualisasi 1: Pertanyaan Bisnis 1
st.subheader(
    "1. Perbandingan Rata-rata Penyewaan Sepeda per Jam "
    "antara Hari Kerja dan Bukan Hari Kerja"
)

hourly_data = hour_df.groupby(
    ['hr', 'workingday']
)['cnt'].mean().reset_index()

hourly_data['workingday'] = hourly_data['workingday'].map({
    0: 'Bukan Hari Kerja',
    1: 'Hari Kerja'
})

fig, ax = plt.subplots(figsize=(12, 6))

sns.lineplot(
    data=hourly_data,
    x='hr',
    y='cnt',
    hue='workingday',
    marker='o',
    ax=ax
)

ax.set_xlabel("Jam (00.00–23.00)")
ax.set_ylabel("Rata-rata Jumlah Penyewaan Sepeda")
ax.set_title(
    "Perbandingan Rata-rata Penyewaan Sepeda per Jam "
    "pada Hari Kerja dan Bukan Hari Kerja (2011–2012)"
)
ax.set_xticks(range(24))
ax.legend(title="Kategori Hari")
ax.grid(axis='y', alpha=0.3)

st.pyplot(fig)
plt.close(fig)

# Visualisasi 2: Pertanyaan Bisnis 2
st.subheader(
    "2. Rata-rata Penyewaan Sepeda Berdasarkan Musim "
    "dan Kondisi Cuaca"
)

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
    1: 'Clear',
    2: 'Cloudy',
    3: 'Light Rain/Snow',
    4: 'Heavy Rain/Snow'
})

fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(
    data=season_weather_data,
    x='season',
    y='cnt',
    hue='weathersit',
    order=['Spring', 'Summer', 'Fall', 'Winter'],
    hue_order=['Clear', 'Cloudy', 'Light Rain/Snow'],
    ax=ax
)

ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Jumlah Penyewaan Sepeda per Hari")
ax.set_title(
    "Rata-rata Penyewaan Sepeda Berdasarkan Musim "
    "dan Kondisi Cuaca (2011–2012)"
)
ax.legend(title="Kondisi Cuaca")
ax.grid(axis='y', alpha=0.3)

st.pyplot(fig)
plt.close(fig)
