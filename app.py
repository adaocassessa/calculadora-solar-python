import streamlit as st
import math

st.set_page_config(page_title="Calculadora Solar Profissional", page_icon="☀️", layout="centered")

st.title("☀️ Calculadora de Dimensionamento Fotovoltaico")
st.write("Preencha os dados abaixo para estimar o sistema solar necessário e o retorno do investimento.")

# Criando abas para organizar a tela
tab1, tab2 = st.tabs(["⚙️ Dimensionamento Técnico", "💰 Economia e Retorno"])

with tab1:
    st.subheader("Dados do Consumo e Equipamentos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        consumo_mensal = st.number_input("Consumo mensal de energia (kWh)", min_value=1.0, value=300.0, step=10.0)
        irradiacao = st.number_input("Irradiação solar média local (kWh/m²/dia)", min_value=1.0, value=5.5, step=0.1, help="Em Luanda, fica em torno de 5 a 6.")
        performance_ratio = st.slider("Performance Ratio (eficiência do sistema)", min_value=0.60, max_value=0.90, value=0.80, step=0.01)
        
    with col2:
        potencia_painel = st.number_input("Potência de cada painel (W)", min_value=100, value=550, step=10)
        area_painel = st.number_input("Área de cada painel (m²)", min_value=0.5, value=2.6, step=0.1)

    # Cálculos Técnicos
    consumo_diario = consumo_mensal / 30
    potencia_kwp = consumo_diario / (irradiacao * performance_ratio)
    numero_paineis = math.ceil((potencia_kwp * 1000) / potencia_painel)
    area_necessaria = numero_paineis * area_painel
    geracao_mensal = potencia_kwp * irradiacao * performance_ratio * 30

    st.divider()
    st.subheader("📊 Resultado da estimativa técnica")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Potência", f"{potencia_kwp:.2f} kWp")
    c2.metric("Painéis", f"{numero_paineis} un.")
    c3.metric("Área", f"{area_necessaria:.1f} m²")
    c4.metric("Geração", f"{geracao_mensal:.0f} kWh")

with tab2:
    st.subheader("Dados Financeiros (para Payback)")
    
    col3, col4 = st.columns(2)
    with col3:
        preco_kwh = st.number_input("Preço do kWh na sua região (ex: AOA, USD, R$)", min_value=0.01, value=150.0, step=10.0, help="Em Angola, verifique a tarifa média da sua distribuidora.")
    with col4:
        custo_kwp = st.number_input("Custo estimado do sistema por kWp (na sua moeda)", min_value=100.0, value=1500.0, step=100.0, help="Quanto custa instalar 1 kWp na sua região?")

    # Cálculos Financeiros
    custo_total_sistema = potencia_kwp * custo_kwp
    economia_mensal = consumo_mensal * preco_kwh
    payback_meses = custo_total_sistema / economia_mensal
    payback_anos = payback_meses / 12

    st.divider()
    st.subheader("💰 Resultado Financeiro")
    
    f1, f2, f3 = st.columns(3)
    f1.metric("Custo Estimado", f"{custo_total_sistema:,.0f}")
    f2.metric("Economia Mensal", f"{economia_mensal:,.0f}")
    f3.metric("Tempo de Retorno", f"{payback_anos:.1f} anos", f"{payback_meses:.0f} meses", delta_color="inverse")

st.info("Aviso: Esta é uma estimativa inicial para pré-dimensionamento. Para um projeto real, é necessário avaliar sombreamento, inclinação, estrutura e normas locais.")