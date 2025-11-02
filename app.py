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

import streamlit as st

st.set_page_config(page_title="Din Kültürü Doğru–Yanlış Soruları", layout="wide")
st.title("✅ Din Kültürü – 1. Ünite Doğru–Yanlış Etkinliği")
st.markdown("Aşağıdaki ifadeleri değerlendir: Doğru mu, yanlış mı? Bilgi kaynakları, türleri ve Allah-âlem ilişkisi konularında cyber doğruluk testi başlıyor!")

# Sorular: ifade, doğru mu?
sorular = [
    {"ifade": "1. İslam’da bilgi sadece ahiret için önemlidir.", "dogru": False},
    {"ifade": "2. Vahiy, bilgiye ulaşma yollarından biridir.", "dogru": True},
    {"ifade": "3. Duyular bilgi üretmez, sadece eğlence sağlar.", "dogru": False},
    {"ifade": "4. Akıl, doğru ile yanlışı ayırma yeteneğidir.", "dogru": True},
    {"ifade": "5. İçtihat, vahyin doğrudan bir parçasıdır.", "dogru": False},
    {"ifade": "6. Sezgisel bilgi kalbe doğan bilgidir.", "dogru": True},
    {"ifade": "7. Deneysel bilgi gözlem ve deneyle elde edilir.", "dogru": True},
    {"ifade": "8. Beşerî bilgi vahiy kaynaklıdır.", "dogru": False},
    {"ifade": "9. Kur’an’da bilgiye vurgu yapılmaz.", "dogru": False},
    {"ifade": "10. Hz. Muhammed ilim öğrenmeyi teşvik etmiştir.", "dogru": True},
    {"ifade": "11. Allah’ın yaratması süreklidir.", "dogru": True},
    {"ifade": "12. Allah’ın yasaları değişebilir.", "dogru": False},
    {"ifade": "13. İnsan Allah’a muhtaç değildir.", "dogru": False},
    {"ifade": "14. Allah bütün canlılara rızık verir.", "dogru": True},
    {"ifade": "15. İslam’da bilgi öğrenmek ibadet sayılır.", "dogru": True},
    {"ifade": "16. Gündelik bilgi sınırsız ve kutsaldır.", "dogru": False},
    {"ifade": "17. Sanat bilgisi hayal gücüne dayanır.", "dogru": True},
    {"ifade": "18. Dini bilgi sadece bilimsel yöntemle elde edilir.", "dogru": False},
    {"ifade": "19. Akıl, İslam’da bilgiye ulaşma yollarındandır.", "dogru": True},
    {"ifade": "20. İçtihat, yorum yaparak bilgi üretmektir.", "dogru": True},
    {"ifade": "21. Vahiy, Allah’ın peygamber aracılığıyla bildirdiği buyruklardır.", "dogru": True},
    {"ifade": "22. Duyular, gözlem yapmaya yardımcı olur.", "dogru": True},
    {"ifade": "23. Allah âlemlerin Rabbidir.", "dogru": True},
    {"ifade": "24. Bilgi sahibi olmak sorumluluk getirir.", "dogru": True},
    {"ifade": "25. Kur’an’da bilgiye hiç yer verilmez.", "dogru": False},
    {"ifade": "26. Sezgisel bilgi tamamen bilimsel temellidir.", "dogru": False},
    {"ifade": "27. Beşerî bilgi insan üretimidir.", "dogru": True},
    {"ifade": "28. Allah’ın yaratması tesadüfîdir.", "dogru": False},
    {"ifade": "29. İslam’da bilgi sadece alimlere mahsustur.", "dogru": False},
    {"ifade": "30. Bilgi, hem bireysel hem toplumsal sorumluluk doğurur.", "dogru": True}
]

cevaplar = []
for i, soru in enumerate(sorular):
    secim = st.radio(soru["ifade"], ["Doğru", "Yanlış"], key=f"dy_{i}")
    cevaplar.append(secim)

# Sonuç butonu
if st.button("Etkinliği Tamamla", key="tamamla_dy"):
    dogru_sayisi = 0
    st.subheader("✅ Sonuçlar")
    for i, secim in enumerate(cevaplar):
        dogru_mu = "Doğru" if sorular[i]["dogru"] else "Yanlış"
        if secim == dogru_mu:
            st.success(f"{i+1}. ✅ Doğru ({secim})")
            dogru_sayisi += 1
        else:
            st.error(f"{i+1}. ❌ Yanlış. Doğru cevap: {dogru_mu}")
    st.info(f"🔢 Toplam doğru: {dogru_sayisi} / {len(sorular)}")

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

import streamlit as st

st.set_page_config(page_title="Bilgi Kavram Kartları", layout="wide")
st.title(" Din Kültürü – Bilgi Kaynakları")
st.markdown("İslam’da bilgiye ulaşma yollarını tanıtan kartlar:")

# Kart verileri
kartlar = [
    {
        "baslik": "📖 Vahiy",
        "aciklama": "Allah’ın peygamber aracılığıyla bildirdiği buyruklardır. En temel bilgi kaynağıdır.",
        "renk": "#f9f5ff"
    },
    {
        "baslik": "🧠 Selim Akıl",
        "aciklama": "Doğru ile yanlışı ayırabilen, ön yargılardan arınmış, sağlıklı düşünme yeteneğidir.",
        "renk": "#e0f7fa"
    },
    {
        "baslik": "👁️ Salim Duyular",
        "aciklama": "Beş duyu organının sağlıklı ve güvenilir şekilde çalışmasıyla elde edilen bilgi kaynağıdır.",
        "renk": "#fff3e0"
    }
]

# Kartları göster
for kart in kartlar:
    st.markdown(f"""
    <div style="background-color:{kart['renk']}; padding:15px; border-radius:10px; margin-bottom:10px">
        <h3>{kart['baslik']}</h3>
        <p>{kart['aciklama']}</p>
    </div>
    """, unsafe_allow_html=True)
