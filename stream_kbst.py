import joblib
import streamlit as st

# MEMBACA MODEL
model = joblib.load(open('kbst_model.sav', 'rb'))

#TITLE WEB
st.title('SISTEM PREDIKSI KELUARGA BERESIKO STUNTING')

# fUNGSI PREDIKSI
def predict(input_data):
    prediction = model.predict([input_data])[0]
    return prediction

def main():
    st.title("Aplikasi Prediksi Stunting Keluarga")

    #Input Data
    st.header("Input Data")

    sumber_air_minum_buruk = st.sidebar.number_input("Apakah Sumber Air Minum Buruk?", min_value=0, max_value=1)
    sanitasi_buruk = st.sidebar.number_input("Apakah Sanitasi Buruk?", min_value=0, max_value=1)
    terlalu_muda_istri = st.sidebar.number_input("Apakah Istri Terlalu Muda?", min_value=0, max_value=1)
    terlalu_tua_istri = st.sidebar.number_input("Apakah Istri Terlalu Tua?", min_value=0, max_value=1)
    terlalu_dekat_umur = st.sidebar.number_input("Apakah Umur Suami & Istri Terlalu Dekat?", min_value=0, max_value=1)
    terlalu_banyak_anak = st.sidebar.number_input("Apakah Memiliki Banyak Anak?", min_value=0, max_value=1)

    input_data = [sumber_air_minum_buruk, sanitasi_buruk, terlalu_muda_istri, terlalu_tua_istri, terlalu_dekat_umur, terlalu_banyak_anak]

    #Button Prediksi
    if st.button("Test Prediksi"):
        result = predict(input_data)

        #Tampilan Hasil Prediksi
        st.header("Hasil Prediksi")
        if result == 0:
            st.write("Keluarga Tidak Beresiko Stunting")
        else:
            st.write("Keluarga Beresiko Stunting")

if __name__ == "__main__":
    main()
