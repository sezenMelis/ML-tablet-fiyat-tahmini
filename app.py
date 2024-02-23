import streamlit as st
import joblib
import numpy as np

model_path = "gradient_boosting_regresyon_model2.pkl"
# Eğer model daha önce eğitilmediyse eğit
if "model" not in st.session_state:
    st.session_state.model = joblib.load(model_path)

# Marka seçenekleri
marka_options = {
    "Apple": 0,
    "Lenovo": 5,
    "Samsung": 6,
    "Diger": 1,
    "Huawei": 4,
    "HONOR": 2,
    "Hometech": 3,
    "Xiaomi": 8,
    "TCL": 7,
}

islemci_cikirdek_options = {
    "Sekiz Çekirdekli İşlemci": 6,
    "Dört Çekirdekli İşlemci": 4,
    "Yok": 1,
    "Altı Çekirdekli İşlemci": 5,
    "Çift Çekirdekli İşlemci": 3,
    "Tek Çekirdekli İşlemci": 2,
}


# İşletim sistemi tabanı seçenekleri
isletim_sistemi_options = {
    "Android": 0,
    "iOS": 1,
    "HarmonyOS": 2,
    "Windows": 3,
    "Snapdragon": 4,
    "EMUI": 5,
}

ekrancozunurluk_options = {
    "2000 x 1200": 4,
    "1920 x 1200": 3,
    "1280 x 800": 1,
    "2360 x 1640": 7,
    "Diger": 9,
    "1340 x 800": 2,
    "2160 x 1620": 5,
    "2560 x 1600": 8,
    "2200 x 1440": 6,
    "1024 x 600": 0,
}

ekran_modeli_options = {
    "IPS Ekran": 4,
    "TFT": 12,
    "LCD": 6,
    "HD IPS": 3,
    "HD Ekran": 2,
    "Liquid Retina Ekran": 7,
    "WQXGA Ekran": 13,
    "Kapasitif Ekran": 5,
    "AMOLED": 0,
    "TDDI": 11,
    "WUXGA": 14,
    "Liquid Retina XDR Ekran": 8,
    "Retina Ekran": 10,
    "OLED Ekran": 9,
    "E-Mürekkep Ekran": 1,
}

# Streamlit uygulamasını oluştur
st.title("Ürün Fiyat Tahmini")

# Kullanıcıdan giriş verilerini al
marka = st.selectbox("Marka", list(marka_options.keys()))
pil = st.number_input("Pil Kapasitesi", min_value=0, max_value=10000, value=3000)
ekrancozunurluk = st.selectbox("Ekran Çözünürlüğü", list(ekrancozunurluk_options.keys()))
kalem = st.checkbox("Kalem Desteği Var mı?")
ram = st.number_input("RAM Miktarı (GB)", min_value=1, max_value=64, value=8)
isletimsistemitabani = st.selectbox("İşletim Sistemi/Tabanı", list(isletim_sistemi_options.keys()))
islemcicekirdek = st.selectbox("İşlemci Çekirdek", list(islemci_cikirdek_options.keys()))
ekranboyutu = st.number_input("Ekran Boyutu (inç)", min_value=1, max_value=100, value=14)
diskkapasitesi = st.number_input("Disk Kapasitesi (GB)", min_value=1, max_value=10000, value=256)
ekran_modeli = st.selectbox("Ekran Modeli", list(ekran_modeli_options.keys()))
# Seçilen marka ve işletim sistemi tabanını sayısal değere dönüştür
marka_numeric = marka_options[marka]
isletim_sistemi_numeric = isletim_sistemi_options[isletimsistemitabani]
ekrancozunurluk_numeric = ekrancozunurluk_options[ekrancozunurluk]
ekran_modeli_numeric = ekran_modeli_options[ekran_modeli]
islemci_cikirdek_numeric = islemci_cikirdek_options[islemcicekirdek]

# Tahmin fonksiyonu
def make_prediction(marka, pil, ekrancozunurluk, kalem, ram, isletimsistemitabani, islemcicekirdek, ekranboyutu, diskkapasitesi, EkranModeli):
    input_data = np.array([[marka, pil, ekrancozunurluk, int(kalem), ram, isletimsistemitabani, islemcicekirdek, ekranboyutu, diskkapasitesi, EkranModeli]])
    prediction = st.session_state.model.predict(input_data)
    return prediction

# Tahmini yap ve sonucu göster
if st.button("Fiyat Tahmini Yap"):
    result = make_prediction(marka_numeric, pil, ekrancozunurluk_numeric, kalem, ram, isletim_sistemi_numeric, islemci_cikirdek_numeric, ekranboyutu, diskkapasitesi, ekran_modeli_numeric)
    st.success(f"Tahmin Edilen Ürün Fiyatı: {result[0]:.2f} TL")

