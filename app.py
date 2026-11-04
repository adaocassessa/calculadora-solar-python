import streamlit as st
import math
import pandas as pd

# Configuração da página
st.set_page_config(page_title="EcoRenováveis Pro - Global", page_icon="🌍", layout="wide")

# --- CÓDIGO CSS PARA MELHORAR O DESIGN (Menos robótico) ---
st.markdown("""
<style>
    /* Fundo geral */
    .stApp {
        background: linear-gradient(135deg, #f0fdf4 0%, #e0f2fe 100%);
    }
    /* Títulos mais fortes */
    h1, h2, h3 {
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
        color: #0f172a;
    }
    /* Botões e métricas */
    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
        font-weight: bold;
        color: #047857;
    }
    /* Caixas de input */
    .stTextInput>div>div>input, .stNumberInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #10b981;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌍 EcoRenováveis Pro: Engenharia de Precisão")
st.write("Plataforma avançada com geolocalização, cálculo de inclinação solar e gestão de sistemas.")

# Criando as abas
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs([
    "📍 Localização e Mapa", 
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

# Variáveis globais
if 'latitude' not in st.session_state: st.session_state.latitude = -8.8390
if 'longitude' not in st.session_state: st.session_state.longitude = 13.2894
if 'consumo_mensal' not in st.session_state: st.session_state.consumo_mensal = 300.0

with tab1:
    st.subheader("📍 Geolocalização do Projeto")
    st.write("Insira as coordenadas do local da instalação para calcular o ângulo solar ideal.")
    
    col_geo1, col_geo2, col_geo3 = st.columns(3)
    with col_geo1:
        lat = st.number_input("Latitude (Ex: -8.83 para Luanda)", min_value=-90.0, max_value=90.0, value=st.session_state.latitude, format="%.4f")
    with col_geo2:
        lon = st.number_input("Longitude (Ex: 13.28 para Luanda)", min_value=-180.0, max_value=180.0, value=st.session_state.longitude, format="%.4f")
    with col_geo3:
        altitude = st.number_input("Altitude (metros)", min_value=0, value=50, step=10)
    
    st.session_state.latitude = lat
    st.session_state.longitude = lon

    # Mapa Interativo
    df_mapa = pd.DataFrame({'lat': [lat], 'lon': [lon]})
    st.map(df_mapa, zoom=10)

    # Cálculo do Ângulo Ótimo
    st.divider()
    st.subheader("📐 Otimização do Ângulo de Inclinação")
    
    # Fórmula simplificada: No hemisfério sul, o ângulo é a latitude + 5 a 10 graus.
    angulo_otimo = abs(lat) + 5 if lat < 0 else abs(lat) - 5
    direcao = "Norte" if lat < 0 else "Sul"
    
    col_ang1, col_ang2 = st.columns(2)
    col_ang1.metric("Ângulo de Inclinação Ideal", f"{angulo_otimo:.1f}°")
    col_ang2.metric("Direção do Painel", direcao)
    st.info(f"💡 Para maximizar a captação, os painéis devem estar inclinados a {angulo_otimo:.1f}° e virados para o {direcao}.")

with tab2:
    st.subheader("Dimensionamento Solar com Perdas por Sombreamento")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        consumo_mensal = st.number_input("Consumo mensal (kWh)", min_value=1.0, value=300.0, step=10.0)
        st.session_state.consumo_mensal = consumo_mensal
    with col2:
        irradiacao = st.number_input("Irradiação solar local (kWh/m²/dia)", min_value=1.0, value=5.5, step=0.1)
    with col3:
        sombreamento = st.slider("Perda por Sombreamento (%)", min_value=0, max_value=50, value=10, step=5, help="Árvores, prédios ou nuvens reduzem a geração.")

    st.subheader("Escolha do Painel Solar")
    tipo_painel = st.selectbox("Tecnologia do Painel", [
        "Monocristalino (Alta Eficiência - 20%)", 
        "Policristalino (Custo-benefício - 15%)", 
        "Filme Fino (Flexível - 10%)"
    ])

    eficiencia_painel = 0.20 if "Monocristalino" in tipo_painel else (0.15 if "Policristalino" in tipo_painel else 0.10)

    col4, col5 = st.columns(2)
    with col4:
        potencia_painel = st.number_input("Potência do painel (W)", min_value=100, value=550, step=10)
    with col5:
        area_painel = st.number_input("Área de cada painel (m²)", min_value=0.5, value=2.6, step=0.1)

    # Cálculos considerando o sombreamento
    fator_sombreamento = 1 - (sombreamento / 100)
    performance_ratio = 0.80 * fator_sombreamento # PR base de 80% menos sombreamento
    
    consumo_diario = consumo_mensal / 30
    potencia_kwp = consumo_diario / (irradiacao * performance_ratio)
    numero_paineis = math.ceil((potencia_kwp * 1000) / potencia_painel)
    geracao_real_estimada = potencia_kwp * irradiacao * performance_ratio * 30
    
    st.divider()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Potência Necessária", f"{potencia_kwp:.2f} kWp")
    c2.metric("Número de Painéis", f"{numero_paineis} un.")
    c3.metric("Área Total", f"{(numero_paineis * area_painel):.1f} m²")
    c4.metric("Geração Mensal Estimada", f"{geracao_real_estimada:.0f} kWh")

    # GRÁFICO DE EFICIÊNCIA
    st.subheader("📊 Curva de Geração Diária (Estimada)")
    # Simulação simples de uma curva de sino para o sol
    horas = list(range(6, 19))
    geracao_hora = [max(0, (potencia_kwp * irradiacao / 6) * math.sin((h - 6) * math.pi / 12)) for h in horas]
    df_grafico = pd.DataFrame({"Hora do Dia": horas, "Geração (kW)": geracao_hora})
    st.line_chart(df_grafico.set_index("Hora do Dia"), color="#10b981")

with tab3:
    st.subheader("Dimensionamento Eólico")
    tipo_turbina = st.selectbox("Tipo de Turbina Eólica", ["Eixo Horizontal (Hélice)", "Eixo Vertical (Ventos fracos)"])
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

with tab4:
    st.subheader("Energia Hídrica")
    tipo_hidro = st.selectbox("Tipo de Turbina Hídrica", ["Pelton (Alta Queda)", "Francis (Média)", "Kaplan (Baixa Queda)"])
    col12, col13 = st.columns(2)
    with col12:
        vazao = st.number_input("Vazão de água (m³/s)", min_value=0.01, value=500.0, step=10.0)
        queda = st.number_input("Altura da queda (metros)", min_value=0.5, value=100.0, step=1.0)
    with col13:
        eficiencia_hidrica = st.slider("Eficiência", min_value=0.50, max_value=0.95, value=0.85, step=0.01)
    potencia_hidrica_w = 1000 * 9.81 * vazao * queda * eficiencia_hidrica
    potencia_hidrica_mw = potencia_hidrica_w / 1_000_000
    st.divider()
    st.metric("Potência Gerada", f"{potencia_hidrica_mw:.2f} MW" if potencia_hidrica_mw > 1 else f"{potencia_hidrica_w:.0f} W")

with tab5:
    st.subheader("Biomassa")
    tipo_biomassa = st.selectbox("Tipo de Processo", ["Combustão Direta", "Gaseificação", "Biodigestor"])
    col14, col15 = st.columns(2)
    with col14:
        massa_residuo = st.number_input("Massa de resíduo por dia (kg)", min_value=1.0, value=1000.0, step=100.0)
        poder_calorifico = st.number_input("Poder Calorífico (MJ/kg)", min_value=1.0, value=15.0, step=1.0)
    with col15:
        eficiencia_biomassa = st.slider("Eficiência", min_value=0.15, max_value=0.40, value=0.25, step=0.01)
    energia_diaria_kwh = (massa_residuo * poder_calorifico * eficiencia_biomassa) / 3.6
    potencia_biomassa_kw = energia_diaria_kwh / 24
    st.divider()
    st.metric("Potência Contínua Gerada", f"{potencia_biomassa_kw:.1f} kW")

with tab6:
    st.subheader("Eletrotécnica Básica")
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

with tab7:
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
    st.metric("Baterias Necessárias", f"{numero_baterias} un.")

with tab8:
    st.subheader("🔌 Inversores")
    tipo_inversor = st.selectbox("Tipo de Inversor", ["Híbrido (Rede + Baterias)", "Off-Grid", "On-Grid"])
    col10, col11 = st.columns(2)
    with col10:
        carga_total = st.number_input("Carga contínua total (W)", min_value=100, value=2000, step=100)
    with col11:
        tem_motores = st.selectbox("Tem motores? (Geleira/Bomba)", ["Sim", "Não"])
    fator = 1.25
    p_continua = carga_total * fator
    p_pico = carga_total * 3.0 if tem_motores == "Sim" else p_continua
    st.divider()
    i1, i2 = st.columns(2)
    i1.metric("Potência Contínua", f"{p_continua:.0f} W")
    i2.metric("Potência de Pico", f"{p_pico:.0f} W")

with tab9:
    st.subheader("🛠️ Manutenção")
    tipo_manutencao = st.selectbox("Tipo de Manutenção", ["Preventiva", "Corretiva", "Preditiva"])
    st.markdown("### Checklist")
    st.checkbox("Limpeza dos painéis (remoção de pó)")
    st.checkbox("Verificação de cabos e conectores")
    st.checkbox("Inspeção do inversor")

with tab10:
    st.subheader("📚 Guia do Técnico")
    st.info("O ângulo de inclinação ideal depende da latitude. Em Angola, os painéis devem apontar para o Norte e ter uma inclinação igual à latitude + 5°.")

with tab11:
    st.subheader("💼 Meu Negócio")
    st.metric("Faturamento Projetado (Ano 1)", "$ 3.000,00")

st.sidebar.title("EcoRenováveis Pro")
st.sidebar.info("Desenvolvido por **Adão Cassessa**.\n\nEngenharia de Precisão e Gestão.")
