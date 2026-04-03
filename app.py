import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Analisis Keselamatan Berkendara", layout="centered")

st.title("🚗 Analisis Kecepatan & Keselamatan Berkendara")
st.write("Aplikasi ini membantu memahami hubungan kecepatan dengan tingkat bahaya saat berkendara.")

# PILIH KENDARAAN
kendaraan = st.selectbox("Pilih Jenis Kendaraan", ["Motor", "Mobil", "Truk"])

# MASSA OTOMATIS
if kendaraan == "Motor":
    m = 150
elif kendaraan == "Mobil":
    m = 1200
elif kendaraan == "Truk":
    m = 5000

st.write(f"Massa rata-rata kendaraan: {m} kg")

# INPUT KECEPATAN
v_kmh = st.number_input("Kecepatan (km/jam)", min_value=0.0)

# KONVERSI KE m/s
v = v_kmh / 3.6

if st.button("Analisis"):
    Ek = 0.5 * m * v**2
    
    st.subheader("Hasil Perhitungan")
    st.success(f"Energi kinetik = {Ek:.2f} Joule")
    
    st.write("Rumus: Ek = ½ m v²")

    # INDIKATOR BAHAYA
    if Ek < 5000:
        st.info("🟢 Risiko rendah (relatif aman)")
    elif Ek < 20000:
        st.warning("🟡 Risiko sedang (perlu waspada)")
    else:
        st.error("🔴 Risiko tinggi (berbahaya)")

    # GRAFIK
    v_range = np.linspace(0, v, 50)
    Ek_range = 0.5 * m * v_range**2

    fig, ax = plt.subplots()
    ax.plot(v_range * 3.6, Ek_range)  # balik ke km/jam biar familiar
    ax.set_xlabel("Kecepatan (km/jam)")
    ax.set_ylabel("Energi Kinetik (J)")
    ax.set_title("Grafik Energi Kinetik vs Kecepatan")

    st.pyplot(fig)

    # ANALISIS
    st.subheader("Analisis")
    st.write(
        "Energi kinetik meningkat sangat cepat seiring bertambahnya kecepatan. "
        "Artinya, sedikit peningkatan kecepatan dapat menyebabkan peningkatan risiko kecelakaan yang signifikan. "
        "Oleh karena itu, berkendara dengan kecepatan tinggi sangat berbahaya."
    )
