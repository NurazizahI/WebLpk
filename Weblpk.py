import streamlit as st
from streamlit_option_menu import option_menu 

# navigasi sidebar
with st.sidebar :
    selected = option_menu ('Perhitungan Analisis Titrimetri',
    ['Hitung Nilai Normalitas',
    'Hitung Nilai Molaritas',
    'Hitung Nilai PPM'],
    default_index=0)
    
# halaman hitung nilai normalitas 
if (selected == 'Hitung Nilai Normalitas') :
    st.title('Hitung Nilai Normalitas')
    
    Massa = st.number_input('Masukan Nilai Massa')
    Volume = st.number_input('Masukan Nilai Volume')
    BE = st.number_input('Masukan Nilai BE')
    
    tombol = st.button('Hitung Nilai Normalitas')
    
    if tombol:
        nilai_normalitas = Massa/(BE*Volume)
        st.success(f'Nilai Normalitas adalah {nilai_normalitas}')
        
# halaman hitung nilai molaritas 
if (selected == 'Hitung Nilai Molaritas') :
    st.title('Hitung Nilai Molaritas')
    
    Massa = st.number_input('Masukan Nilai Massa')
    Volume = st.number_input('Masukan Nilai Volume')
    Mr = st.number_input('Masukan Nilai Mr')
    
    tombol = st.button('Hitung Nilai Molaritas')
    
    if tombol:
        nilai_normalitas = Massa/(Mr*Volume)
        st.success(f'Nilai Normalitas adalah {nilai_Molaritas}')