import streamlit as st

st.set_page_config(page_title="Dashboard Kimia Dasar", layout="wide")
st.title("🔬 Dashboard Interaktif: Kimia Dasar")

# === Tiga kolom ===
col1, col2, col3 = st.columns(3)

# =======================
# KOLOM 1: KALKULATOR
# =======================
with col1:
    st.header("🧮 Kalkulator Kimia")
    st.markdown("Gunakan kalkulator ini untuk menghitung *massa, **mol, atau **Mr*.")

    pilihan = st.radio("Pilih yang ingin dihitung:", ["Massa", "Mol", "Mr"])

    if pilihan == "Massa":
        mol = st.number_input("Masukkan jumlah mol (mol):", min_value=0.0, format="%.4f")
        mr = st.number_input("Masukkan Mr (g/mol):", min_value=0.0, format="%.4f")
        if st.button("Hitung Massa"):
            massa = mol * mr
            st.success(f"📘 Massa = {massa:.4f} gram")

    elif pilihan == "Mol":
        massa = st.number_input("Masukkan massa (gram):", min_value=0.0, format="%.4f")
        mr = st.number_input("Masukkan Mr (g/mol):", min_value=0.0, format="%.4f")
        if st.button("Hitung Mol"):
            if mr != 0:
                mol = massa / mr
                st.success(f"📘 Mol = {mol:.4f} mol")
            else:
                st.error("Mr tidak boleh nol!")

    elif pilihan == "Mr":
        massa = st.number_input("Masukkan massa (gram):", min_value=0.0, format="%.4f")
        mol = st.number_input("Masukkan jumlah mol (mol):", min_value=0.0, format="%.4f")
        if st.button("Hitung Mr"):
            if mol != 0:
                mr = massa / mol
                st.success(f"📘 Mr = {mr:.4f} g/mol")
            else:
                st.error("Mol tidak boleh nol!")

# =======================
# KOLOM 2: RUMUS KIMIA DASAR
# =======================
with col2:
    st.header("📚 Rumus Kimia Dasar")
    st.markdown("""
    *1. Massa = Mol × Mr*  
    *2. Mol = Massa / Mr*  
    *3. Mr = Massa / Mol*  
    *4. Hukum Avogadro:* 1 mol = 6.022 × 10²³ partikel  
    *5. Volume Gas Ideal (STP):* 1 mol gas = 22.4 L pada STP
    """)

# =======================
# KOLOM 3: CONTOH SOAL
# =======================
with col3:
    st.header("📝 Contoh Soal dan Pembahasan")
    st.markdown("""
    *Soal 1:*  
    Berapa massa 2 mol air (H₂O)?  
    Mr = (2×1) + 16 = 18  
    Massa = 2 × 18 = *36 gram*

    *Soal 2:*  
    Massa NaCl = 58.5 g, Mr = 58.5  
    Mol = 58.5 / 58.5 = *1 mol*

    *Soal 3:*  
    Mr Ca(OH)₂ = 40 + 2×(16+1) = *74 g/mol*
    """)

st.markdown("---")
st.caption("📘 Dibuat dengan Streamlit | Materi: Kimia Dasar untuk SMP/SMA")
