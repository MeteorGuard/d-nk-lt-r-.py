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
