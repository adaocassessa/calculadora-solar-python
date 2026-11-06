import streamlit as st
import math
import pandas as pd

# Configuração da página (O Streamlit vai gerir as cores automaticamente)
st.set_page_config(page_title="EcoRenováveis Pro - Engenharia", page_icon="🌍", layout="wide")

st.title("🌍 EcoRenováveis Pro: Engenharia de Precisão")
st.write("Plataforma avançada com geolocalização, cálculo de inclinação solar e gestão de sistemas.")

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs([
    "📍 Mapa e Localização", 
    "☀️ Solar Fotovoltaico", 
    "🌬️ Energia Eólica", 
    "💧 Hídrica", 
    "🌱 Biomassa",
    "⚡ Eletrotécnica",
    "🔋 Baterias",
    "🔌 Inversores",
    "🛠️ Manutenção",
    "📚 Guia do Técnico",
    "💼 Meu Negócio"
])

if 'latitude' not in st.session_state: st.session_state.latitude = -8.8390
if 'longitude' not in st.session_state: st.session_state.longitude = 13.2894
if 'consumo_mensal' not in st.session_state: st.session_state.consumo_mensal = 300.0

with tab1:
    st.subheader("📍 Geolocalização do Projeto")
    col_geo1, col_geo2, col_geo3 = st.columns(3)
    with col_geo1:
        lat = st.number_input("Latitude", min_value=-90.0, max_value=90.0, value=st.session_state.latitude, format="%.4f")
    with col_geo2:
        lon = st.number_input("Longitude", min_value=-180.0, max_value=180.0, value=st.session_state.longitude, format="%.4f")
    with col_geo3:
        altitude = st.number_input("Altitude (m)", min_value=0, value=50, step=10)
    
    st.session_state.latitude = lat
    st.session_state.longitude = lon

    st.markdown("### 🗺️ Mapa da Instalação")
    try:
        df_mapa = pd.DataFrame({'lat': [lat], 'lon': [lon]})
        st.map(df_mapa, zoom=12)
    except Exception as e:
        st.warning("O mapa interativo não pôde ser carregado.")
    
    link_google_maps = f"https://www.google.com/maps?q={lat},{lon}"
    st.link_button("📍 Abrir localização no GPS", link_google_maps)

    st.divider()
    angulo_otimo = abs(lat) + 5 if lat < 0 else abs(lat) - 5
    direcao = "Norte" if lat < 0 else "Sul"
    col_ang1, col_ang2 = st.columns(2)
    col_ang1.metric("Ângulo de Inclinação Ideal", f"{angulo_otimo:.1f}°")
    col_ang2.metric("Direção do Painel", direcao)

with tab2:
    st.subheader("Dimensionamento Solar")
    col1, col2, col3 = st.columns(3)
    with col1:
        consumo_mensal = st.number_input("Consumo mensal (kWh)", min_value=1.0, value=300.0, step=10.0)
        st.session_state.consumo_mensal = consumo_mensal
    with col2:
        irradiacao = st.number_input("Irradiação solar", min_value=1.0, value=5.5, step=0.1)
    with col3:
        sombreamento = st.slider("Sombreamento (%)", min_value=0, max_value=50, value=10, step=5)

    tipo_painel = st.selectbox("Tecnologia do Painel", ["Monocristalino", "Policristalino", "Filme Fino"])
    col4, col5 = st.columns(2)
    with col4:
        potencia_painel = st.number_input("Potência do painel (W)", min_value=100, value=550, step=10)
    with col5:
        area_painel = st.number_input("Área (m²)", min_value=0.5, value=2.6, step=0.1)

    fator_sombreamento = 1 - (sombreamento / 100)
    performance_ratio = 0.80 * fator_sombreamento
    consumo_diario = consumo_mensal / 30
    potencia_kwp = consumo_diario / (irradiacao * performance_ratio)
    numero_paineis = math.ceil((potencia_kwp * 1000) / potencia_painel)
    
    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("Potência", f"{potencia_kwp:.2f} kWp")
    c2.metric("Painéis", f"{numero_paineis} un.")
    c3.metric("Área Total", f"{(numero_paineis * area_painel):.1f} m²")

with tab3:
    st.subheader("Eólico")
    tipo_turbina = st.selectbox("Tipo de Turbina", ["Eixo Horizontal", "Eixo Vertical"])
    col6, col7 = st.columns(2)
    with col6:
        velocidade_vento = st.number_input("Vento (m/s)", min_value=1.0, value=6.0, step=0.5)
        raio_turbina = st.number_input("Raio das pás (m)", min_value=0.5, value=2.0, step=0.1)
    with col7:
        eficiencia_turbina = st.slider("Eficiência (Cp)", min_value=0.20, max_value=0.59, value=0.40, step=0.01)
    area_varredura = math.pi * (raio_turbina ** 2)
    potencia_eolica_w = 0.5 * 1.225 * area_varredura * (velocidade_vento ** 3) * eficiencia_turbina
    st.metric("Potência", f"{potencia_eolica_w:.0f} W")

with tab4:
    st.subheader("Hídrica")
    tipo_hidro = st.selectbox("Tipo de Turbina", ["Pelton", "Francis", "Kaplan"])
    vazao = st.number_input("Vazão (m³/s)", min_value=0.01, value=500.0, step=10.0)
    queda = st.number_input("Queda (m)", min_value=0.5, value=100.0, step=1.0)
    eficiencia_hidrica = st.slider("Eficiência", min_value=0.50, max_value=0.95, value=0.85, step=0.01)
    potencia_hidrica_w = 1000 * 9.81 * vazao * queda * eficiencia_hidrica
    st.metric("Potência", f"{(potencia_hidrica_w / 1_000_000):.2f} MW")

with tab5:
    st.subheader("Biomassa")
    tipo_biomassa = st.selectbox("Processo", ["Combustão Direta", "Gaseificação", "Biodigestor"])
    massa_residuo = st.number_input("Resíduo (kg/dia)", min_value=1.0, value=1000.0)
    poder_calorifico = st.number_input("Poder Calorífico (MJ/kg)", min_value=1.0, value=15.0)
    eficiencia_biomassa = st.slider("Eficiência", min_value=0.15, max_value=0.40, value=0.25)
    st.metric("Potência", f"{((massa_residuo * poder_calorifico * eficiencia_biomassa) / 3.6) / 24:.1f} kW")

with tab6:
    st.subheader("Eletrotécnica")
    tensao = st.number_input("Tensão (V)", min_value=12.0, value=220.0)
    potencia_equipamento = st.number_input("Potência (W)", min_value=1.0, value=1000.0)
    distancia_cabo = st.number_input("Cabo (m)", min_value=1.0, value=20.0)
    material_cabo = st.selectbox("Material", ["Cobre", "Alumínio"])
    corrente = potencia_equipamento / tensao
    resistividade = 0.0172 if material_cabo == "Cobre" else 0.0282
    area_cabo_mm2 = (2 * resistividade * distancia_cabo * corrente) / (tensao * 0.03)
    st.metric("Cabo Mínimo", f"{area_cabo_mm2:.2f} mm²")

with tab7:
    st.subheader("Baterias")
    tipo_bateria = st.selectbox("Tipo", ["Lítio", "Chumbo-Ácido"])
    tensao_sistema = st.selectbox("Tensão (V)", [12, 24, 48], index=2)
    capacidade_bateria = st.number_input("Capacidade (Ah)", min_value=50, value=200)
    dias_autonomia = st.number_input("Dias", min_value=1, max_value=5, value=1)
    dod = 0.90 if "Lítio" in tipo_bateria else 0.50
    numero_baterias = math.ceil(((st.session_state.consumo_mensal / 30 * 1000 * dias_autonomia) / (tensao_sistema * dod)) / capacidade_bateria)
    st.metric("Baterias", f"{numero_baterias} un.")

with tab8:
    st.subheader("Inversores")
    tipo_inversor = st.selectbox("Tipo", ["Híbrido", "Off-Grid", "On-Grid"])
    carga_total = st.number_input("Carga (W)", min_value=100, value=2000)
    tem_motores = st.selectbox("Tem motores?", ["Sim", "Não"])
    p_pico = carga_total * 3.0 if tem_motores == "Sim" else carga_total * 1.25
    st.metric("Pico", f"{p_pico:.0f} W")

with tab9:
    st.subheader("Manutenção")
    tipo_manutencao = st.selectbox("Tipo", ["Preventiva", "Corretiva", "Preditiva"])
    st.checkbox("Limpeza dos painéis")
    st.checkbox("Verificação de cabos")

with tab10:
    st.subheader("Guia")
    st.info("Em Angola, os painéis apontam para o Norte com inclinação igual à latitude + 5°.")

with tab11:
    st.subheader("Meu Negócio")
    st.metric("Faturamento Estimado (Ano 1)", "$ 3.000,00")

st.sidebar.title("EcoRenováveis Pro")
st.sidebar.title("EcoRenováveis Pro")
st.sidebar.info("Desenvolvido por **Adão Cassessa**.\n\nTécnico em Energias Renováveis e Desenvolvedor Python.\n\nContacto: +244 946 419 656")
st.sidebar.caption("© 2026 EcoRenováveis. Todos os direitos reservados.")
