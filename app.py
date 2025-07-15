# kalkulator_fisika_streamlit.py
# Aplikasi Streamlit untuk menghitung kinematika, dinamika, dan konversi satuan

import streamlit as st

st.set_page_config(page_title="Kalkulator Fisika", layout="centered")
st.title("🧮 Kalkulator Fisika Web")
st.markdown("Gunakan tab di bawah ini untuk menghitung kinematika, dinamika, atau konversi satuan.")

# Tab untuk fitur
tab1, tab2, tab3 = st.tabs(["Kinematika", "Dinamika", "Konversi Satuan"])

# ==============================
# KINEMATIKA
# ==============================
with tab1:
    st.header("Kalkulator Kinematika")
    mode = st.selectbox("Pilih yang ingin dihitung:", ["Jarak (s)", "Kecepatan (v)", "Waktu (t)", "Percepatan (a)"])

    if mode == "Jarak (s)":
        v = st.number_input("Kecepatan (m/s)", step=0.1)
        t = st.number_input("Waktu (s)", step=0.1)
        if st.button("Hitung Jarak"):
            st.success(f"Jarak = {v * t:.2f} meter")

    elif mode == "Kecepatan (v)":
        s = st.number_input("Jarak (m)", step=0.1)
        t = st.number_input("Waktu (s)", step=0.1)
        if t != 0 and st.button("Hitung Kecepatan"):
            st.success(f"Kecepatan = {s / t:.2f} m/s")

    elif mode == "Waktu (t)":
        s = st.number_input("Jarak (m)", step=0.1)
        v = st.number_input("Kecepatan (m/s)", step=0.1)
        if v != 0 and st.button("Hitung Waktu"):
            st.success(f"Waktu = {s / v:.2f} detik")

    elif mode == "Percepatan (a)":
        v1 = st.number_input("Kecepatan awal v1 (m/s)", step=0.1)
        v2 = st.number_input("Kecepatan akhir v2 (m/s)", step=0.1)
        t = st.number_input("Waktu (s)", step=0.1)
        if t != 0 and st.button("Hitung Percepatan"):
            st.success(f"Percepatan = {(v2 - v1) / t:.2f} m/s²")


# ==============================
# DINAMIKA
# ==============================
with tab2:
    st.header("Kalkulator Dinamika")
    mode = st.selectbox("Pilih yang ingin dihitung:", ["Gaya (F)", "Tekanan (P)", "Energi Kinetik (Ek)"])

    if mode == "Gaya (F)":
        m = st.number_input("Massa (kg)", step=0.1)
        a = st.number_input("Percepatan (m/s²)", step=0.1)
        if st.button("Hitung Gaya"):
            st.success(f"Gaya = {m * a:.2f} Newton")

    elif mode == "Tekanan (P)":
        F = st.number_input("Gaya (N)", step=0.1)
        A = st.number_input("Luas (m²)", step=0.01)
        if A != 0 and st.button("Hitung Tekanan"):
            st.success(f"Tekanan = {F / A:.2f} Pascal")

    elif mode == "Energi Kinetik (Ek)":
        m = st.number_input("Massa (kg)", step=0.1)
        v = st.number_input("Kecepatan (m/s)", step=0.1)
        if st.button("Hitung Energi Kinetik"):
            st.success(f"Energi Kinetik = {0.5 * m * v**2:.2f} Joule")


# ==============================
# KONVERSI SATUAN
# ==============================
with tab3:
    st.header("Konversi Satuan Fisika")
    jenis = st.selectbox("Jenis yang ingin dikonversi:", ["Energi", "Tekanan"])

    val = st.number_input("Nilai yang ingin dikonversi:", step=0.1)
    satuan_from = st.selectbox("Dari satuan:", [])
    satuan_to = st.selectbox("Ke satuan:", [])

    energi_satuan = {"joule":1, "kjoule":1e3, "kwh":3.6e6, "kalori":4.184}
    tekanan_satuan = {"pa":1, "kpa":1e3, "bar":1e5, "atm":101325, "mmhg":133.322}

    if jenis == "Energi":
        satuan_from = st.selectbox("Dari satuan:", list(energi_satuan.keys()), key="from_energy")
        satuan_to = st.selectbox("Ke satuan:", list(energi_satuan.keys()), key="to_energy")
        faktor = energi_satuan
    elif jenis == "Tekanan":
        satuan_from = st.selectbox("Dari satuan:", list(tekanan_satuan.keys()), key="from_pressure")
        satuan_to = st.selectbox("Ke satuan:", list(tekanan_satuan.keys()), key="to_pressure")
        faktor = tekanan_satuan

    if st.button("Konversi"):
        try:
            hasil = val * faktor[satuan_from] / faktor[satuan_to]
            st.success(f"Hasil: {hasil:.4f} {satuan_to}")
        except:
            st.error("Terjadi kesalahan dalam konversi.")
