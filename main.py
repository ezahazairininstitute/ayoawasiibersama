import streamlit as st
import math

st.write("""
# Ini adalah Aplikasi Sederhana Penghitungan Jumlah Sampling Dalam Verifikasi Partai Politik Pemilu Tahun 2024""")

chikuadrat = 3.84
populasi = st.number_input("Masukan Populasi",format="%.0f")
galatpendugaan = 0.05
proporsi = 0.5
sampel = st.button("Hitung Sampel")
interval = st.button ("Lihat Interval")


# results = st.write('hasil')

if (bool(populasi)):
    results = (chikuadrat * populasi * proporsi * (1-proporsi)) / ((populasi - 1) * (galatpendugaan**2) + chikuadrat * proporsi *(1-proporsi))
    st.write("Jumlah Sampel Verifikasi Faktualnya adalah", round(results))
    
elif(populasi == 0):
  st.write("Populasi Masih kosong")
else:
    st.write("Data gagal diproses")

# Interval = st.write('hasil')

if interval: 
    interval = populasi / results
    st.write("Intervalnya adalah", round(interval,2))
