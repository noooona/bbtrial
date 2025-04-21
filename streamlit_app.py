import streamlit as st

# Judul aplikasi
st.title("🐄 Perhitungan Bobot Badan Sapi")

# Deskripsi
st.markdown("""
Aplikasi ini digunakan untuk memperkirakan bobot badan sapi berdasarkan ukuran tubuh menggunakan rumus:
**(Lingkar Dada² × Panjang Badan) / 10838**
""")

# Input pengguna
panjang_badan = st.number_input("Masukkan Panjang Badan (cm)", min_value=0.0, format="%.2f")
lingkar_dada = st.number_input("Masukkan Lingkar Dada (cm)", min_value=0.0, format="%.2f")

# Tombol untuk menghitung
if st.button("Hitung Bobot Badan"):
    if panjang_badan > 0 and lingkar_dada > 0:
        bobot = (lingkar_dada ** 2 * panjang_badan) / 10838
        st.success(f"Perkiraan Bobot Badan: {bobot:.2f} kg")
    else:
        st.warning("Masukkan nilai panjang badan dan lingkar dada yang valid.")

# Footer
st.markdown("---")
st.caption("Dibuat oleh Noona")
