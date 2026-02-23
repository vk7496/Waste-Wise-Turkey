import streamlit as st
import pandas as pd
import plotly.express as px
from translations import lang_dict

# تنظیمات اصلی
st.set_page_config(page_title="AI Waste Tracker", layout="wide")

# انتخاب زبان در بالای سایدبار
lang_choice = st.sidebar.selectbox("Select Language / Dil Seçin", ["English", "Turkish"])
t = lang_dict[lang_choice]

# تیتر و هدر
st.title(t["title"])
st.markdown(f"#### {t['header']}")

# تولید دیتای فرضی
df = pd.DataFrame({
    'Food': ['Adana Kebap', 'Pilav', 'Salads', 'Baklava', 'Bread'],
    'Loss_TRY': [25000, 8000, 4500, 12000, 3000]
})

# نمایش متریک‌ها
m1, m2, m3 = st.columns(3)
m1.metric(t["metrics"][0], "52,500 TRY", "-8%")
m2.metric(t["metrics"][1], "420 Kg", "+2%")
m3.metric(t["metrics"][2], "9,450 TRY", delta_color="normal")

st.divider()

# نمودارها
fig = px.bar(df, x='Food', y='Loss_TRY', color='Food', title=t["chart_title"])
st.plotly_chart(fig, use_container_width=True)

# بخش هوش مصنوعی
st.info(t["ai_note"])
if lang_choice == "Turkish":
    st.write("- **Kebap** atığı hafta sonları %15 daha fazla. Üretim planını optimize edin.")
else:
    st.write("- **Kebap** waste increases by 15% on weekends. Optimize production planning.")

# بخش آپلود (برای دمو)
st.subheader(t["upload_msg"])
st.file_uploader("", type=['jpg', 'png'])

if st.button(t["cta"]):
    st.success("Report Generated!")
