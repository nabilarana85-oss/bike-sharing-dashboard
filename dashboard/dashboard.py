import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

st.set_page_config(page_title="Bike Sharing Dashboard", page_icon="🚲", layout="wide")

st.title("🚲 Bike Sharing Dashboard")
st.markdown(
    "Analisis penyewaan sepeda berdasarkan hari kerja, musim, dan kondisi cuaca."
)


@st.cache_data
def load_data():
    csv_path = Path(__file__).resolve().parent / "main_data.csv"
    df = pd.read_csv(csv_path)
    df["dteday"] = pd.to_datetime(df["dteday"])

    hour_df = df[df["data_type"] == "hour"].copy()
    day_df = df[df["data_type"] == "day"].copy()

    # Jika baris data harian tidak ada, buat dari data per jam
    if day_df.empty:
        day_df = (
            hour_df.groupby("dteday")
            .agg(
                season=("season", "first"),
                yr=("yr", "first"),
                weathersit=("weathersit", lambda s: s.mode().iloc[0]),
                workingday=("workingday", "first"),
                cnt=("cnt", "sum"),
            )
            .reset_index()
        )
    return hour_df, day_df


hour_df, day_df = load_data()

# Filter tahun
st.sidebar.header("Filter Dashboard")
selected_year = st.sidebar.selectbox("Pilih Tahun", options=[2011, 2012], index=0)
year_code = 0 if selected_year == 2011 else 1

hour_filtered = hour_df[hour_df["yr"] == year_code].copy()
day_filtered = day_df[day_df["yr"] == year_code].copy()

st.subheader(f"Ringkasan Penyewaan Tahun {selected_year}")

col1, col2, col3 = st.columns(3)
col1.metric("Total Penyewaan per Jam", f"{int(hour_filtered['cnt'].sum()):,}")
col2.metric("Total Penyewaan Harian", f"{int(day_filtered['cnt'].sum()):,}")
col3.metric("Rata-rata Penyewaan Harian", f"{day_filtered['cnt'].mean():,.2f}")

st.divider()

# Pertanyaan Bisnis 1
st.subheader(
    "1. Perbandingan Rata-rata Penyewaan Sepeda per Jam "
    "antara Hari Kerja dan Bukan Hari Kerja"
)

hourly_avg = (
    hour_filtered.groupby(["hr", "workingday"])["cnt"].mean().reset_index()
)

fig1, ax1 = plt.subplots(figsize=(12, 5))
sns.lineplot(
    data=hourly_avg, x="hr", y="cnt", hue="workingday", marker="o", ax=ax1
)
ax1.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
ax1.set_xlabel("Jam")
ax1.set_ylabel("Rata-rata Jumlah Penyewaan")
ax1.set_xticks(range(24))
ax1.grid(alpha=0.3)
ax1.legend(title="Jenis Hari")
st.pyplot(fig1)
plt.close(fig1)

st.markdown(
    "Grafik menunjukkan pola rata-rata penyewaan sepeda per jam "
    "pada hari kerja dan bukan hari kerja."
)

st.divider()

# Pertanyaan Bisnis 2
st.subheader(
    "2. Analisis Rata-rata Penyewaan Sepeda Berdasarkan Musim dan Kondisi Cuaca"
)

season_weather_avg = (
    day_filtered.groupby(["season", "weathersit"])["cnt"].mean().reset_index()
)

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(
    data=season_weather_avg, x="season", y="cnt", hue="weathersit", ax=ax2
)
ax2.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim dan Cuaca")
ax2.set_xlabel("Musim")
ax2.set_ylabel("Rata-rata Jumlah Penyewaan")
ax2.grid(axis="y", alpha=0.3)
ax2.legend(title="Kondisi Cuaca")
st.pyplot(fig2)
plt.close(fig2)

st.markdown(
    "Grafik membandingkan rata-rata penyewaan sepeda "
    "berdasarkan musim dan kondisi cuaca."
)

st.caption("Sumber data: Bike Sharing Dataset — data hasil cleaning notebook.")
