import streamlit as st

st.set_page_config(page_title="Din Kültürü Eşleştirme Soruları", layout="wide")
st.title("🧩 Din Kültürü – Bilgi Kaynakları Eşleştirme Etkinliği")
st.markdown("Aşağıdaki kavramları doğru tanımlarla eşleştir. Bilgi kaynakları konusunu etkinliklerle test et!")

# Kavramlar ve doğru tanımları
eslestirme_sorular = [
    {
        "kavram": "Vahiy",
        "dogru": "Allah’ın peygamber aracılığıyla bildirdiği buyruklardır.",
        "yanlis": "Gözlem ve deneyle elde edilen bilgi"
    },
    {
        "kavram": "Akıl",
        "dogru": "Doğru ile yanlışı ayırma yeteneği",
        "yanlis": "Kalbe doğan sezgisel bilgi"
    },
    {
        "kavram": "Duyular",
        "dogru": "Beş duyu ile elde edilen bilgi",
        "yanlis": "Yorum yaparak fıkıh üretme yöntemi"
    
    },
    {
        "kavram": "Sezgi",
        "dogru": "Kalbe doğan sezgisel bilgi",
        "yanlis": "Deneysel gözlemle elde edilen bilgi"
    }
]

cevaplar = []
for i, soru in enumerate(eslestirme_sorular):
    st.write(f"**{i+1}. {soru['kavram']}**")
    secenekler = [soru["dogru"], soru["yanlis"]]
    secim = st.radio("Tanımı seç:", secenekler, key=f"es_{i}")
    cevaplar.append(secim)

# Sonuç butonu
if st.button("Eşleştirmeyi Kontrol Et", key="kontrol_eslestirme"):
    dogru_sayisi = 0
    st.subheader("✅ Sonuçlar")
    for i, secim in enumerate(cevaplar):
        if secim == eslestirme_sorular[i]["dogru"]:
            st.success(f"{i+1}. ✅ Doğru eşleşme")
            dogru_sayisi += 1
        else:
            st.error(f"{i+1}. ❌ Yanlış. Doğru tanım: {eslestirme_sorular[i]['dogru']}")
    st.info(f"🔢 Toplam doğru eşleşme: {dogru_sayisi} / {len(eslestirme_sorular)}")
