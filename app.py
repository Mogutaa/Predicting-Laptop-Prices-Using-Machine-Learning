import streamlit as st
import joblib
import numpy as np

model = joblib.load("rf_model.pkl")

# Configuração inicial da página
st.set_page_config(page_title="Previsão de Preços de Notebooks", page_icon="💻")

# CSS personalizado
st.markdown("""
    <style>
    .main {background-color: #F5F5F5;}
    h1 {color: #2F4F4F;}
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 24px;
    }
    .stNumberInput {padding: 10px;}
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho
st.title("💻 Previsão de Preços de Notebooks")
st.markdown("**Precifique seu notebook de forma inteligente!**")

# Divisor visual
st.markdown("---")

# Descrição
st.markdown("""
🔍 **Como funciona:**  
Preencha as especificações técnicas do notebook abaixo e clique no botão para receber 
uma estimativa de preço em dólares (USD). Ideal para quem quer comprar ou vender notebooks usados!
""")

# Seção de inputs usando colunas
with st.container():
    st.subheader("📝 Especificações Técnicas")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        processor_speed = st.number_input(
            "Velocidade do Processador (GHz)",
            min_value=1.0,
            max_value=5.0,
            value=2.5,
            step=0.5,
            help="Ex: 2.4 GHz, 3.0 GHz"
        )
        
    with col2:
        ram_size = st.number_input(
            "Memória RAM (GB)",
            min_value=4,
            max_value=64,
            value=16,
            step=8,
            format="%d",
            help="Ex: 8GB, 16GB"
        )
        
    with col3:
        storage_capacity = st.number_input(
            "Armazenamento (GB)",
            min_value=128,
            max_value=4096,
            value=512,
            step=256,
            format="%d",
            help="Ex: 256GB, 1TB = 1024GB"
        )

# Divisor visual
st.markdown("---")

# Botão de previsão centralizado
col_btn1, col_btn2, col_btn3 = st.columns([1,2,1])
with col_btn2:
    prediction = st.button("🚀 Calcular Preço Estimado", use_container_width=True)

# Seção de resultados
if prediction:
    st.balloons()
    x1 = np.array([processor_speed, ram_size, storage_capacity])
    prediction = model.predict([x1])
    
    with st.container():
        st.markdown("---")
        st.subheader("📊 Resultado da Estimativa")
        st.markdown(f"""
        <div style="background-color:#E8F5E9; padding:20px; border-radius:10px;">
            <h3 style="color:#2E7D32; margin:0;">Preço Estimado:</h3>
            <p style="font-size:36px; color:#1B5E20; margin:10px 0; font-weight:bold;">
                US$ {float(prediction):,.2f}
            </p>
            <p style="color:#616161; margin:0;">* Valor de referência em dólares americanos (USD)</p>
        </div>
        """, unsafe_allow_html=True)
        
else:
    st.markdown("""
    <div style="text-align:center; color:#616161; margin-top:50px;">
        👆 Clique no botão acima para calcular o preço
    </div>
    """, unsafe_allow_html=True)