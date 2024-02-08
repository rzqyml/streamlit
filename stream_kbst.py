import streamlit as st
import joblib

# Load the Naive Bayes model
model = joblib.load(open('kbst_model.sav', 'rb'))

# Function to make predictions
def predict(input_data):
    # Placeholder for the actual prediction logic based on your model
    # Modify this part according to your model's input requirements
    prediction = model.predict([input_data])[0]
    return prediction

# Streamlit app
def main():
    st.title("Aplikasi Prediksi Stunting Keluarga")

    # Input data
    st.header("Input Data")
    
    sumber_air_minum_buruk = st.sidebar.number_input("Apakah Sumber Air Minum Buruk?", min_value=0, max_value=1)
    sanitasi_buruk = st.sidebar.number_input("Apakah Sanitasi Buruk?", min_value=0, max_value=1)
    terlalu_muda_istri = st.sidebar.number_input("Apakah Istri Terlalu Muda?", min_value=0, max_value=1)
    terlalu_tua_istri = st.sidebar.number_input("Apakah Istri Terlalu Tua?", min_value=0, max_value=1)
    terlalu_dekat_umur = st.sidebar.number_input("Apakah Umur Suami & Istri Terlalu Dekat?", min_value=0, max_value=1)
    terlalu_banyak_anak = st.sidebar.number_input("Apakah Memiliki Banyak Anak?", min_value=0, max_value=1)
    
    input_data = [sumber_air_minum_buruk, sanitasi_buruk, terlalu_muda_istri, terlalu_tua_istri, terlalu_dekat_umur, terlalu_banyak_anak]

    # Predict button
    if st.button("Prediksi"):
        result = predict(input_data)

        # Display result
        st.header("Hasil Prediksi")
        if result == 0:
            st.write("Keluarga Tidak Beresiko Stunting")
        else:
            st.write("Keluarga Beresiko Stunting")

if __name__ == "__main__":
    main()
