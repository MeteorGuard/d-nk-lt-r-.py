import streamlit as st

st.set_page_config(page_title="Din Kültürü Eşleştirme Etkinlikleri", layout="wide")
st.title("🧩 Din Kültürü Eşleştirme Etkinlikleri – 10. Sınıf")
st.markdown("Ayetlerle bilgi eşleştirme, bilgi türü eşleştirme ve Allah-Alem ilişkisi üzerine interaktif etkinlikler seni bekliyor!")

# 1️⃣ Ayet – Bilgi Eşleştirme
st.header("📘 Etkinlik 1 – Ayetlerle Bilgi Eşleştirme")

ayet_sorular = [
    {
        "soru": "“Hiç bilenlerle bilmeyenler bir olur mu?” ayeti hangi bilgi türüne işaret eder?",
        "secenekler": ["Dini Bilgi", "Sanat Bilgisi", "Gündelik Bilgi", "Selim Akıl"],
        "dogru": "Selim Akıl"
    },
    {
        "soru": "“Ey insanlar! Siz Allah’a muhtaçsınız…” ayeti neyi vurgular?",
        "secenekler": ["Kadim Bilgi", "İnsan Bilgisi", "İslam", "Hadis Bilgisi"],
        "dogru": "İslam"
    },
    {
        "soru": "“Yeryüzünde yürüyen bütün canlıların rızkı ancak Allah’a aittir…” ayeti neyi anlatır?",
        "secenekler": ["Allah’ın yaratması", "Allah’ın rızık vericiliği", "İnsan aklı", "Sanat bilgisi"],
        "dogru": "Allah’ın rızık vericiliği"
    }
]

ayet_cevaplar = []
for i, soru in enumerate(ayet_sorular):
    secim = st.radio(f"{i+1}. {soru['soru']}", soru["secenekler"], key=f"ayet_{i}")
    ayet_cevaplar.append(secim)

# 2️⃣ Bilgi Türü – Tanım Eşleştirme
st.header("📗 Etkinlik 2 – Bilgi Türü Eşleştirme")

bilgi_sorular = [
    {
        "soru": "“Kur’an’daki emirler” hangi bilgi türüne girer?",
        "secenekler": ["Beşerî Bilgi", "Dini Bilgi", "Deneysel Bilgi", "Sezgisel Bilgi"],
        "dogru": "Dini Bilgi"
    },
    {
        "soru": "“Su döngüsü gözlemi” hangi bilgi türüdür?",
        "secenekler": ["Dini Bilgi", "Beşerî Bilgi", "Deneysel Bilgi", "Sanat Bilgisi"],
        "dogru": "Deneysel Bilgi"
    },
    {
        "soru": "“İlhamla gelen fikir” hangi bilgi türüne girer?",
        "secenekler": ["Sezgisel Bilgi", "Dini Bilgi", "Kadim Bilgi", "Gündelik Bilgi"],
        "dogru": "Sezgisel Bilgi"
    }
]

bilgi_cevaplar = []
for i, soru in enumerate(bilgi_sorular):
    secim = st.radio(f"{i+1}. {soru['soru']}", soru["secenekler"], key=f"bilgi_{i}")
    bilgi_cevaplar.append(secim)

# 3️⃣ Allah-Alem İlişkisi – Ayet Eşleştirme
st.header("📕 Etkinlik 3 – Allah-Alem İlişkisi Eşleştirme")

alem_sorular = [
    {
        "soru": "“O, gökleri ve yeri yoktan var edendir.” ayeti neyi anlatır?",
        "secenekler": ["Allah’ın yaratıcı olması", "İnsan aklı", "Doğa kanunları", "Sanat bilgisi"],
        "dogru": "Allah’ın yaratıcı olması"
    },
    {
        "soru": "“Güneşi bir aydınlatıcı, ayı ise bir ışık yapmıştır.” ayeti neyi vurgular?",
        "secenekler": ["Allah’ın düzen kuruculuğu", "İnsan bilgisi", "Beşerî bilgi", "Kadim bilgi"],
        "dogru": "Allah’ın düzen kuruculuğu"
    },
    {
        "soru": "“Her şeyi bir ölçüye göre yarattık.” ayeti neyi ifade eder?",
        "secenekler": ["Allah’ın kudreti", "İnsan aklı", "Sanat bilgisi", "Deneysel bilgi"],
        "dogru": "Allah’ın kudreti"
    }
]

alem_cevaplar = []
for i, soru in enumerate(alem_sorular):
    secim = st.radio(f"{i+1}. {soru['soru']}", soru["secenekler"], key=f"alem_{i}")
    alem_cevaplar.append(secim)

# 🔍 Sonuç Butonu
if st.button("Etkinliği Tamamla", key="tamamla_eslestirme"):
    dogru_sayisi = 0
    st.subheader("✅ Sonuçlar")

    for i, secim in enumerate(ayet_cevaplar):
        if secim == ayet_sorular[i]["dogru"]:
            st.success(f"Ayet {i+1}: Doğru ({secim})")
            dogru_sayisi += 1
        else:
            st.error(f"Ayet {i+1}: Yanlış. Doğru cevap: {ayet_sorular[i]['dogru']}")

    for i, secim in enumerate(bilgi_cevaplar):
        if secim == bilgi_sorular[i]["dogru"]:
            st.success(f"Bilgi {i+1}: Doğru ({secim})")
            dogru_sayisi += 1
        else:
            st.error(f"Bilgi {i+1}: Yanlış. Doğru cevap: {bilgi_sorular[i]['dogru']}")

    for i, secim in enumerate(alem_cevaplar):
        if secim == alem_sorular[i]["dogru"]:
            st.success(f"Alem {i+1}: Doğru ({secim})")
            dogru_sayisi += 1
        else:
            st.error(f"Alem {i+1}: Yanlış. Doğru cevap: {alem_sorular[i]['dogru']}")

    toplam_soru = len(ayet_sorular) + len(bilgi_sorular) + len(alem_sorular)
    st.info(f"🔢 Toplam doğru: {dogru_sayisi} / {toplam_soru}")
