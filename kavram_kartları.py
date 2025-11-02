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
