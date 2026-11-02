import streamlit as st
import math

# Configuração da página
st.set_page_config(page_title="EcoRenováveis Pro - Engenharia", page_icon="🌍", layout="wide")

st.title("🌍 EcoRenováveis Pro: Plataforma de Engenharia")
st.write("Ferramenta completa para dimensionamento de sistemas fotovoltaicos, eólicos e eletrotécnica básica.")

# Criando as abas
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "☀️ Solar Fotovoltaico", 
    "🌬️ Energia Eólica", 
    "⚡ Eletrotécnica (Lei de Ohm)", 
    "🔋 Equipamentos e Baterias",
    "📚 Guia do Técnico"
])

with tab1:
    st.subheader("1. Dados do Consumo e Localização")
    col1, col2, col3 = st.columns(3)
    with col1:
        consumo_mensal = st.number_input("Consumo mensal (kWh)", min_value=1.0, value=300.0, step=10.0)
    with col2:
        irradiacao = st.number_input("Irradiação solar (kWh/m²/dia)", min_value=1.0, value=5.5, step=0.1)
    with col3:
        performance_ratio = st.slider("Performance Ratio (eficiência)", min_value=0.60, max_value=0.95, value=0.80, step=0.01)

    st.subheader("2. Escolha do Painel Solar")
    col4, col5 = st.columns(2)
    with col4:
        potencia_painel = st.number_input("Potência do painel (W)", min_value=100, value=550, step=10)
    with col5:
        area_painel = st.number_input("Área do painel (m²)", min_value=0.5, value=2.6, step=0.1)

    # Cálculos Solares
    consumo_diario = consumo_mensal / 30
    potencia_kwp = consumo_diario / (irradiacao * performance_ratio)
    numero_paineis = math.ceil((potencia_kwp * 1000) / potencia_painel)
    area_necessaria = numero_paineis * area_painel

    st.divider()
    st.subheader("📊 Resultado do Arranjo Fotovoltaico")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Potência Necessária", f"{potencia_kwp:.2f} kWp")
    c2.metric("Número de Painéis", f"{numero_paineis} un.")
    c3.metric("Área Requerida", f"{area_necessaria:.1f} m²")
    c4.metric("Consumo Diário", f"{consumo_diario:.1f} kWh/dia")

with tab2:
    st.subheader("Dimensionamento de Turbina Eólica")
    st.info("Fórmula baseada na densidade do ar e velocidade do vento. A potência eólica cresce ao cubo da velocidade.")
    
    col6, col7 = st.columns(2)
    with col6:
        velocidade_vento = st.number_input("Velocidade média do vento (m/s)", min_value=1.0, value=6.0, step=0.5)
        raio_turbina = st.number_input("Raio das pás da turbina (metros)", min_value=0.5, value=2.0, step=0.1)
    with col7:
        eficiencia_turbina = st.slider("Eficiência da turbina (Coeficiente Cp)", min_value=0.20, max_value=0.59, value=0.40, step=0.01, help="O limite de Betz é 0.59 (59%). Na prática usamos 0.35 a 0.45.")
    
    # Cálculo Eólico: P = 0.5 * densidade_ar * Area * v^3 * Cp
    densidade_ar = 1.225 # kg/m3 ao nível do mar
    area_varredura = math.pi * (raio_turbina ** 2)
    potencia_eolica_w = 0.5 * densidade_ar * area_varredura * (velocidade_vento ** 3) * eficiencia_turbina
    
    st.divider()
    st.subheader("🌬️ Potência Estimada da Turbina")
    st.metric("Potência Elétrica Gerada", f"{potencia_eolica_w:.0f} W")
    st.caption(f"Área de varredura das pás: {area_varredura:.1f} m²")

with tab3:
    st.subheader("Eletrotécnica Básica e Dimensionamento de Cabos")
    
    col8, col9 = st.columns(2)
    with col8:
        tensao = st.number_input("Tensão do sistema (Volts - V)", min_value=12.0, value=220.0, step=12.0)
        potencia_equipamento = st.number_input("Potência do equipamento (Watts - W)", min_value=1.0, value=1000.0, step=100.0)
    with col9:
        distancia_cabo = st.number_input("Distância do cabo (metros)", min_value=1.0, value=20.0, step=1.0)
        material_cabo = st.selectbox("Material do cabo", ["Cobre (Resistividade 0.0172)", "Alumínio (Resistividade 0.0282)"])
    
    # Cálculo de Corrente (Lei de Ohm: I = P / V)
    corrente = potencia_equipamento / tensao
    
    # Queda de tensão (Fórmula para CC e CA monofásico: Delta V = (2 * resistividade * distancia * corrente) / Area)
    # Para acharmos a área do cabo ideal (Queda de tensão máxima de 3%): Area = (2 * resistividade * distancia * corrente) / (tensao * 0.03)
    resistividade = 0.0172 if "Cobre" in material_cabo else 0.0282
    queda_maxima = tensao * 0.03 # 3%
    area_cabo_mm2 = (2 * resistividade * distancia_cabo * corrente) / queda_maxima
    
    st.divider()
    st.subheader("⚡ Resultados Elétricos (Lei de Ohm)")
    e1, e2, e3 = st.columns(3)
    e1.metric("Corrente (I)", f"{corrente:.2f} A")
    e2.metric("Resistência do Circuito", f"{(tensao / corrente):.2f} Ω" if corrente > 0 else "0 Ω")
    e3.metric("Cabo Mínimo Recomendado", f"{area_cabo_mm2:.2f} mm²")
    st.caption("O cálculo de cabo acima considera uma queda de tensão máxima de 3% (padrão de segurança).")

with tab4:
    st.subheader("Dimensionamento de Baterias")
    st.info("Escolha o tipo de bateria para ajustar a Profundidade de Descarga (DoD).")
    
    tipo_bateria = st.selectbox("Tipo de Bateria", ["Lítio (DoD 90% - Longa vida)", "Chumbo-Ácido (DoD 50% - Comum)"])
    dias_autonomia = st.number_input("Dias de autonomia (sem sol/vento)", min_value=1, max_value=5, value=1, step=1)
    tensao_sistema = st.selectbox("Tensão do sistema de baterias (V)", [12, 24, 48], index=2)
    
    col10, col11 = st.columns(2)
    with col10:
        capacidade_bateria = st.number_input("Capacidade de cada bateria (Ah)", min_value=50, value=200, step=50)
    with col11:
        fator_potencia_inversor = st.slider("Fator de segurança do Inversor", min_value=1.1, max_value=1.5, value=1.25, step=0.05)

    # Reutilizando o consumo diário calculado na aba 1
    dod = 0.90 if "Lítio" in tipo_bateria else 0.50
    energia_bateria_necessaria_wh = (consumo_diario * 1000) * dias_autonomia
    capacidade_total_ah = energia_bateria_necessaria_wh / (tensao_sistema * dod)
    numero_baterias = math.ceil(capacidade_total_ah / capacidade_bateria)
    potencia_inversor_w = (potencia_kwp * 1000) * fator_potencia_inversor

    st.divider()
    st.subheader("🔌 Equipamentos Sugeridos")
    b1, b2 = st.columns(2)
    b1.metric("Inversor Necessário", f"{potencia_inversor_w:.0f} W")
    b2.metric("Número de Baterias", f"{numero_baterias} un. de {capacidade_bateria}Ah")

with tab5:
    st.subheader("📚 Guia Técnico Prático")
    st.markdown("""
    **1. Por que a Eólica é diferente da Solar?**
    Na solar, a potência cresce linearmente com o sol. Na eólica, a potência cresce ao **cubo** da velocidade do vento (se o vento dobra, a potência multiplica por 8). Por isso, torres eólicas precisam de altura e ventos constantes.
    
    **2. Lei de Ohm e Cabos (O erro mais comum)**
    Muitos sistemas falham porque o cabo é fino demais. A fórmula da corrente é `I = P / V`. Se a tensão for muito baixa (12V) e a potência alta (2000W), a corrente será de 166 Amperes! Isso derrete cabos finos. Por isso, sistemas maiores usam 48V: a corrente cai e o cabo pode ser mais fino e barato.
    
    **3. Baterias de Lítio vs Chumbo-Ácido**
    As de Chumbo só podem descarregar 50% (senão viciam). As de Lítio descarregam 90%. Se o cliente tem dinheiro, o Lítio dura 3x mais e precisa de menos baterias para o mesmo sistema.
    """)

st.sidebar.title("Sobre o Software")
st.sidebar.info("Desenvolvido por **Adão Cassessa**.\n\nEngenheiro de Energias Renováveis e Desenvolvedor Python. Uma plataforma completa para técnicos, empresas e estudantes.")
