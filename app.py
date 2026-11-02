import streamlit as st
import math

st.set_page_config(page_title="EcoRenováveis Pro - Global", page_icon="🌍", layout="wide")

st.title("🌍 EcoRenováveis Pro: Engenharia Global")
st.write("Plataforma de dimensionamento de sistemas, grandes barragens e estimativa de potencial energético regional.")

# Criando as abas
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "☀️ Solar Fotovoltaico", 
    "🌬️ Energia Eólica", 
    "💧 Hídrica (Micro e Grandes)",
    "🌱 Biomassa",
    "⚡ Eletrotécnica",
    "🔋 Baterias",
    "🗺️ Potencial Macroeconómico",
    "📚 Guia do Técnico"
])

# Variáveis globais
if 'consumo_mensal' not in st.session_state:
    st.session_state.consumo_mensal = 300.0

with tab1:
    st.subheader("Dimensionamento Solar Residencial/Comercial")
    col1, col2, col3 = st.columns(3)
    with col1:
        consumo_mensal = st.number_input("Consumo mensal (kWh)", min_value=1.0, value=300.0, step=10.0)
        st.session_state.consumo_mensal = consumo_mensal
    with col2:
        irradiacao = st.number_input("Irradiação solar (kWh/m²/dia)", min_value=1.0, value=5.5, step=0.1)
    with col3:
        performance_ratio = st.slider("Performance Ratio", min_value=0.60, max_value=0.95, value=0.80, step=0.01)

    st.subheader("Escolha do Painel Solar")
    
    # NOVIDADE AQUI: Seletor de Tecnologia do Painel
    tipo_painel = st.selectbox("Tecnologia do Painel", [
        "Monocristalino (Alta Eficiência - Telhados pequenos)", 
        "Policristalino (Custo-benefício - Telhados grandes)", 
        "Filme Fino (Flexível - Grandes áreas)"
    ])

    # Avisos dinâmicos baseados no tipo de painel
    if "Monocristalino" in tipo_painel:
        st.success("💡 Dica: É o melhor para aproveitar pouco espaço. A eficiência média é de 18% a 22%.")
    elif "Policristalino" in tipo_painel:
        st.warning("💡 Dica: Mais económico, mas ocupa cerca de 20% mais área no telhado do que o Monocristalino.")
    else:
        st.info("💡 Dica: Use apenas se o cliente tiver uma área gigante ou um telhado curvo. A eficiência é baixa (7% a 12%).")

    col4, col5 = st.columns(2)
    with col4:
        potencia_painel = st.number_input("Potência do painel (W)", min_value=100, value=550, step=10)
    with col5:
        area_painel = st.number_input("Área de cada painel (m²)", min_value=0.5, value=2.6, step=0.1)

    consumo_diario = consumo_mensal / 30
    potencia_kwp = consumo_diario / (irradiacao * performance_ratio)
    numero_paineis = math.ceil((potencia_kwp * 1000) / potencia_painel)
    
    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("Potência Necessária", f"{potencia_kwp:.2f} kWp")
    c2.metric("Número de Painéis", f"{numero_paineis} un.")
    c3.metric("Área Total Requerida", f"{(numero_paineis * area_painel):.1f} m²")

with tab2:
    st.subheader("Dimensionamento Eólico")
    col6, col7 = st.columns(2)
    with col6:
        velocidade_vento = st.number_input("Velocidade do vento (m/s)", min_value=1.0, value=6.0, step=0.5)
        raio_turbina = st.number_input("Raio das pás (m)", min_value=0.5, value=2.0, step=0.1)
    with col7:
        eficiencia_turbina = st.slider("Eficiência (Cp)", min_value=0.20, max_value=0.59, value=0.40, step=0.01)
    
    area_varredura = math.pi * (raio_turbina ** 2)
    potencia_eolica_w = 0.5 * 1.225 * area_varredura * (velocidade_vento ** 3) * eficiencia_turbina
    
    st.divider()
    st.metric("Potência Elétrica Gerada", f"{potencia_eolica_w:.0f} W")

with tab3:
    st.subheader("Energia Hídrica (Micro a Grandes Barragens)")
    col12, col13 = st.columns(2)
    with col12:
        vazao = st.number_input("Vazão de água (m³/s)", min_value=0.01, value=500.0, step=10.0)
        queda = st.number_input("Altura da queda (metros)", min_value=0.5, value=100.0, step=1.0)
    with col13:
        eficiencia_hidrica = st.slider("Eficiência (Turbina + Gerador)", min_value=0.50, max_value=0.95, value=0.85, step=0.01)
    
    potencia_hidrica_w = 1000 * 9.81 * vazao * queda * eficiencia_hidrica
    potencia_hidrica_mw = potencia_hidrica_w / 1_000_000
    
    st.divider()
    if potencia_hidrica_mw > 1:
        st.metric("Potência Gerada (Grande Escala)", f"{potencia_hidrica_mw:.2f} MW")
    else:
        st.metric("Potência Gerada (Micro Escala)", f"{potencia_hidrica_w:.0f} W")

with tab4:
    st.subheader("Biomassa (Biogás e Resíduos)")
    col14, col15 = st.columns(2)
    with col14:
        massa_residuo = st.number_input("Massa de resíduo por dia (kg)", min_value=1.0, value=1000.0, step=100.0)
        poder_calorifico = st.number_input("Poder Calorífico (MJ/kg)", min_value=1.0, value=15.0, step=1.0)
    with col15:
        eficiencia_biomassa = st.slider("Eficiência do gerador", min_value=0.15, max_value=0.40, value=0.25, step=0.01)
    
    energia_diaria_kwh = (massa_residuo * poder_calorifico * eficiencia_biomassa) / 3.6
    potencia_biomassa_kw = energia_diaria_kwh / 24
    
    st.divider()
    st.metric("Potência Contínua Gerada", f"{potencia_biomassa_kw:.1f} kW")

with tab5:
    st.subheader("Eletrotécnica Básica e Cabos")
    col8, col9 = st.columns(2)
    with col8:
        tensao = st.number_input("Tensão (V)", min_value=12.0, value=220.0, step=12.0)
        potencia_equipamento = st.number_input("Potência (W)", min_value=1.0, value=1000.0, step=100.0)
    with col9:
        distancia_cabo = st.number_input("Distância do cabo (m)", min_value=1.0, value=20.0, step=1.0)
        material_cabo = st.selectbox("Material", ["Cobre", "Alumínio"])
    
    corrente = potencia_equipamento / tensao
    resistividade = 0.0172 if material_cabo == "Cobre" else 0.0282
    area_cabo_mm2 = (2 * resistividade * distancia_cabo * corrente) / (tensao * 0.03)
    
    st.divider()
    e1, e2, e3 = st.columns(3)
    e1.metric("Corrente", f"{corrente:.2f} A")
    e2.metric("Resistência", f"{(tensao / corrente):.2f} Ω" if corrente > 0 else "0")
    e3.metric("Cabo Mínimo", f"{area_cabo_mm2:.2f} mm²")

with tab6:
    st.subheader("Baterias")
    tipo_bateria = st.selectbox("Tipo", ["Lítio (DoD 90%)", "Chumbo-Ácido (DoD 50%)"])
    tensao_sistema = st.selectbox("Tensão das baterias (V)", [12, 24, 48], index=2)
    capacidade_bateria = st.number_input("Capacidade unitária (Ah)", min_value=50, value=200, step=50)
    dias_autonomia = st.number_input("Dias de autonomia", min_value=1, max_value=5, value=1, step=1)
    
    dod = 0.90 if "Lítio" in tipo_bateria else 0.50
    consumo_diario_bat = st.session_state.consumo_mensal / 30
    capacidade_total_ah = (consumo_diario_bat * 1000 * dias_autonomia) / (tensao_sistema * dod)
    numero_baterias = math.ceil(capacidade_total_ah / capacidade_bateria)
    
    st.divider()
    st.metric("Número de Baterias Necessárias", f"{numero_baterias} un.")

with tab7:
    st.subheader("🗺️ Potencial Macroeconómico (Países)")
    area_pais = st.number_input("Área da região/país (km²)", min_value=100.0, value=1246700.0, step=10000.0)
    
    st.markdown("### 1. Potencial Solar Teórico")
    irradiacao_media_pais = st.number_input("Irradiação solar média (kWh/m²/dia)", min_value=1.0, value=5.5, step=0.1)
    potencial_solar_twh = (area_pais * 1_000_000 * irradiacao_media_pais * 365 * 0.20) / 1_000_000_000
    st.metric("Potencial Solar Teórico", f"{potencial_solar_twh:,.0f} TWh/ano")

    st.markdown("### 2. Potencial Eólico Teórico")
    densidade_eolica = st.number_input("Densidade eólica média (W/m²)", min_value=10.0, value=150.0, step=10.0)
    potencial_eolico_twh = (area_pais * 1_000_000 * densidade_eolica * 0.01 * 8760) / 1_000_000_000
    st.metric("Potencial Eólico Viável (1% do território)", f"{potencial_eolico_twh:,.0f} TWh/ano")

with tab8:
    st.subheader("📚 Guia do Engenheiro Consultor")
    st.markdown("""
    **1. Diferença entre Painéis (Solar):**
    *   **Monocristalino:** Células de silício puro. Cor preta uniforme. Eficiência alta (18-22%). Melhor escolha para telhados residenciais onde o espaço é limitado.
    *   **Policristalino:** Silício com impurezas. Cor azulada. Eficiência média (13-16%). Bom para grandes instalações no solo onde a área não é problema e o custo é o foco.
    *   **Filme Fino:** Não usa silício cristalino. É flexível. Eficiência baixa (7-12%), precisa de muita área, mas funciona bem com pouca luz e altas temperaturas.

    **2. Grandes Barragens vs. Micro-Hídrica**
    A física é a mesma. A diferença está na escala. Uma grande barragem requer estudos geológicos e de impacto ambiental.

    **3. Potencial Teórico vs. Técnico**
    Na aba Macroeconómica, calculamos o Potencial Teórico. Na vida real, precisamos de cidades, florestas e agricultura. Mesmo assim, 1% desse potencial é suficiente para alimentar um país.
    """)

st.sidebar.title("EcoRenováveis Pro")
st.sidebar.info("Desenvolvido por **Adão Cassessa**.\n\nEngenheiro de Energias Renováveis e Desenvolvedor Python.")
