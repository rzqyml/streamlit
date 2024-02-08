import pickle
import streamlit as st

# MEMBACA MODEL
model = pickle.load(open('kbst_model.sav', 'rb'))

#TITLE WEB
st.title('SISTEM PREDIKSI KELUARGA BERESIKO STUNTING')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    sumber_air_minum_buruk = st.text_input ('Apakah Sumber Air Minum Buruk?')

with col2 :
    sanitasi_buruk = st.text_input ('Apakah Sanitasi Buruk?')

with col1 :
    terlalu_muda_istri = st.text_input ('Apakah Istri Terlalu Muda?')

with col2 :
    terlalu_tua_istri = st.text_input ('Apakah Istri Terlalu Tua?')

with col1 :
    terlalu_dekat_umur = st.text_input ('Apakah Umur Suami & Istri Terlalu Dekat?')

with col2 :
    terlalu_banyak_anak = st.text_input ('Apakah Memiliki Banyak Anak?')

# code untuk prediksi
diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    prediksi = diabetes_model.predict([[sumber_air_minum_buruk, sanitasi_buruk, terlalu_muda_istri, terlalu_tua_istri, terlalu_dekat_umur, terlalu_banyak_anak]])

    if(prediksi[0] == 1):
        diagnosis = 'Pasien terkena Diabetes'
    else:
        diagnosis = 'Pasien tidak terkena Diabetes'
st.success(diagnosis)