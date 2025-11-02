import streamlit as st

st.set_page_config(page_title="Din Kültürü Seçmeli Boşluk Doldurma", layout="wide")
st.title(" Din Kültürü – 1. Ünite Seçmeli Boşluk Doldurma Etkinliği")
st.markdown("Her cümlede boşluğu dolduracak doğru kelimeyi seç. Bilgi kaynakları, türleri ve Allah-âlem ilişkisi konularında cyber test başlıyor!")

# Sorular: cümle, doğru cevap, yanlış cevap
sorular = [
    {"cumle": "İslam’da bilgiye ulaşmanın en temel yolu ___________’dir.", "dogru": "vahiy", "yanlis": "rüya"},
    {"cumle": "Gözlemle elde edilen bilgi ___________ bilgidir.", "dogru": "deneysel", "yanlis": "dini"},
    {"cumle": "Kur’an ve sünnet ___________ bilgi kaynağına örnektir.", "dogru": "vahiy", "yanlis": "akıl"},
    {"cumle": "Mantık yürütme ile elde edilen bilgi ___________ ile sağlanır.", "dogru": "akıl", "yanlis": "duyular"},
    {"cumle": "Kalbe doğan bilgi ___________ bilgidir.", "dogru": "sezgisel", "yanlis": "beşerî"},
    {"cumle": "Allah’ın yaratması ___________ bir süreçtir.", "dogru": "sürekli", "yanlis": "tesadüfi"},
    {"cumle": "Allah’ın yasalarında ___________ olmaz.", "dogru": "değişiklik", "yanlis": "kararsızlık"},
    {"cumle": "İnsan ___________ Allah’a muhtaçtır.", "dogru": "her zaman", "yanlis": "bazen"},
    {"cumle": "Bilgi hem ___________ hem ahiret için önemlidir.", "dogru": "dünya", "yanlis": "mal"},
    {"cumle": "Fıkıh yorumları ___________ yoluyla elde edilir.", "dogru": "içtihat", "yanlis": "duyular"}
]

cevaplar = []
for i, soru in enumerate(sorular):
    secenekler = [soru["dogru"], soru["yanlis"]]
    st.write(f"{i+1}. {soru['cumle']}")
    secim = st.radio("Seçimin:", secenekler, key=f"soru_{i}")
    cevaplar.append(secim)

# Sonuç butonu
if st.button("Etkinliği Tamamla", key="tamamla_secimli"):
    dogru_sayisi = 0
    st.subheader("✅ Sonuçlar")
    for i, secim in enumerate(cevaplar):
        if secim == sorular[i]["dogru"]:
            st.success(f"{i+1}. Doğru ({secim})")
            dogru_sayisi += 1
        else:
            st.error(f"{i+1}. Yanlış. Doğru cevap: {sorular[i]['dogru']}")
    st.info(f"🔢 Toplam doğru: {dogru_sayisi} / {len(sorular)}")
