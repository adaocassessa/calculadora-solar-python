import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="EcoRenováveis Pro - Engenharia Global", page_icon="🌍", layout="wide")

st.title("🌍 EcoRenováveis Pro: Engenharia Global")
st.write("Plataforma completa: Renováveis, Elétrica, Civil, Mobilidade, Automação e Indústria.")

# Criando as 20 abas
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16, tab17, tab18, tab19, tab20 = st.tabs([
    "🌟 Guia Automático", "📍 Mapa", "☀️ Solar", "🌡️ Térmica", "🌬️ Eólica", "💧 Hídrica", 
    "🚰 Bombeamento", "🌱 Biomassa", "⚡ Eletrotécnica", "🚗 Mobilidade EV", "🤖 Automação", 
    "🏗️ Engenharia Civil", "🏭 Indústria/Fabrico", "⚙️ Mecânica", "🔋 Baterias", "🔌 Inversores", 
    "⚙️ Geradores", "🛠️ Manutenção", "🔧 Executivo", "💼 Negócio"
])

if 'latitude' not in st.session_state: st.session_state.latitude = -8.8390
if 'longitude' not in st.session_state: st.session_state.longitude = 13.2894

# ==========================================
# ABA 1: GUIA AUTOMÁTICO (Com Indústria)
# ==========================================
with tab1:
    st.subheader("🌟 Assistente de Criação de Projeto (Tudo-em-Um)")
    tipo_sistema_guia = st.selectbox("Selecione o Tipo de Sistema", [
        "Solar Fotovoltaico", "Bombeamento Solar", "Instalação Elétrica", "Mecânica", 
        "Mobilidade Elétrica (Carros)", "Automação (Drones/Robôs)", "Engenharia Civil (Betão)",
        "Estudo de Viabilidade (Obras)", "Fábrica de Carros (Indústria)"
    ], key="t1_tipo")
    
    if tipo_sistema_guia == "Fábrica de Carros (Indústria)":
        st.markdown("### Planeamento de Fábrica Automóvel")
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            carros_mes = st.number_input("Produção Desejada (Carros/Mês)", value=100, key="t1_f_carros")
            tipo_carro = st.selectbox("Tipo de Veículo", ["Combustão (Gasolina/Diesel)", "Elétrico (EV)", "Híbrido"], key="t1_f_tipo")
        with col_f2:
            area_terreno = st.number_input("Área do Terreno da Fábrica (m²)", value=10000, key="t1_f_area")
            investimento_disp = st.number_input("Investimento Inicial (USD)", value=500000.0, key="t1_f_inv")
        
        if st.button("Calcular Fábrica", key="btn_auto_fabrica"):
            # Estimativas de materiais por carro
            aco_por_carro = 1.2 # toneladas
            plastico_por_carro = 0.2 # toneladas
            litio_por_carro = 0.01 # toneladas (apenas EV)
            
            total_aco = carros_mes * aco_por_carro
            total_plastico = carros_mes * plastico_por_carro
            total_litio = carros_mes * litio_por_carro if "Elétrico" in tipo_carro else 0
            
            # Energia da Fábrica (robôs de solda e linha de montagem)
            consumo_kwh_carro = 500 if "Elétrico" in tipo_carro else 300
            energia_mensal = carros_mes * consumo_kwh_carro
            
            st.markdown("---")
            st.markdown("### 🏭 Resumo da Fábrica e Matérias-Primas")
            st.metric("Produção Anual", f"{(carros_mes * 12):,} carros")
            st.metric("Energia Necessária (Mês)", f"{energia_mensal:,} kWh")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("Aço Necessário (Mês)", f"{total_aco:.1f} Toneladas")
            c2.metric("Plástico (Mês)", f"{total_plastico:.1f} Toneladas")
            if "Elétrico" in tipo_carro:
                c3.metric("Lítio (Baterias)", f"{total_litio:.2f} Toneladas")
            
            st.info("💡 **Nota:** Esta energia da fábrica pode ser complementada com os cálculos da aba Solar.")

    elif tipo_sistema_guia == "Solar Fotovoltaico":
        col1, col2, col3 = st.columns(3)
        with col1:
            c_auto = st.number_input("Consumo Mensal (kWh)", value=300.0, key="t1_c")
            i_auto = st.number_input("Irradiação (kWh/m²/dia)", value=5.5, key="t1_i")
        with col2:
            s_auto = st.slider("Sombreamento (%)", 0, 50, 10, key="t1_s")
            pp_auto = st.number_input("Potência do Painel (W)", value=550, key="t1_pp")
        with col3:
            carga_auto = st.number_input("Carga de Pico (W)", value=3000, key="t1_carga")
            tb_auto = st.selectbox("Bateria", ["Lítio", "Chumbo-Ácido"], key="t1_tb")
        
        if st.button("Calcular Solar", key="btn_auto_solar"):
            pr = 0.8 * (1 - s_auto/100)
            kwp = (c_auto/30) / (i_auto * pr)
            p_num = math.ceil((kwp*1000)/pp_auto)
            inv = carga_auto * 1.25
            bat = math.ceil(((c_auto/30*1000*1)/(48*(0.9 if tb_auto=='Lítio' else 0.5)))/200)
            st.markdown("---")
            c1, c2, c3 = st.columns(3)
            c1.metric("Painéis", f"{p_num} un.")
            c2.metric("Inversor", f"{inv/1000:.1f} kW")
            c3.metric("Baterias", f"{bat} un.")

    # (As outras opções do Guia Automático: Bombeamento, EV, Civil, Viabilidade mantêm-se, omitidas aqui para focar no novo)
    elif tipo_sistema_guia == "Estudo de Viabilidade (Obras)":
        st.info("Análise de solo, topografia e infraestrutura (Veja a aba Engenharia Civil).")

# ==========================================
# ABA 2: MAPA
# ==========================================
with tab2:
    lat = st.number_input("Latitude", value=st.session_state.latitude, key="t2_lat")
    lon = st.number_input("Longitude", value=st.session_state.longitude, key="t2_lon")
    st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}), zoom=12)

# ==========================================
# ABAS 3 a 8: MANUAIS (Solar, Térmica, Eólica, Hídrica, Bombeamento, Biomassa)
# ==========================================
with tab3:
    st.subheader("☀️ Solar Fotovoltaico (Manual)")
    c = st.number_input("Consumo (kWh)", value=300.0, key="t3_c")
    i = st.number_input("Irradiação", value=5.5, key="t3_i")
    st.metric("Painéis Necessários", f"{math.ceil(((c/30)/(i*0.8)*1000)/550)} un.")

with tab4:
    st.subheader("🌡️ Térmica (Manual)")
    v = st.number_input("Volume Água (L/dia)", value=200, key="t4_v")
    st.metric("Área de Coletores", f"{((v * 1.16 * 40) / 1000) / (5.5 * 0.6):.1f} m²")

with tab5:
    st.subheader("🌬️ Eólica (Manual)")
    vento = st.number_input("Vento (m/s)", value=6.0, key="t5_v")
    raio = st.number_input("Raio Pás (m)", value=2.0, key="t5_r")
    st.metric("Potência Gerada", f"{0.5 * 1.225 * (math.pi * raio**2) * (vento**3) * 0.40:.0f} W")

with tab6:
    st.subheader("💧 Hídrica (Manual)")
    q = st.number_input("Vazão (m³/s)", value=10.0, key="t6_q")
    h = st.number_input("Queda (m)", value=20.0, key="t6_h")
    st.metric("Potência Gerada", f"{(1000 * 9.81 * q * h * 0.9)/1000:.1f} kW")

with tab7:
    st.subheader("🚰 Bombeamento (Manual)")
    prof = st.number_input("Profundidade (m)", value=50.0, key="t7_p")
    alt = st.number_input("Altura Tanque (m)", value=10.0, key="t7_a")
    st.metric("HMT", f"{(prof + alt) * 1.1:.1f} m")

with tab8:
    st.subheader("🌱 Biomassa (Manual)")
    m = st.number_input("Massa Resíduo (kg/dia)", value=1000.0, key="t8_m")
    st.metric("Potência Contínua", f"{((m * 15 * 0.25) / 3.6) / 24:.1f} kW")

# ==========================================
# ABA 9: ELETROTÉCNICA
# ==========================================
with tab9:
    st.subheader("⚡ Eletrotécnica")
    p = st.number_input("Potência (W)", value=1000.0, key="t9_p")
    v = st.number_input("Tensão (V)", value=220.0, key="t9_v")
    st.metric("Corrente", f"{(p/v):.2f} A")
    st.metric("Resistência da Carga", f"{(v/(p/v)):.2f} Ω")

# ==========================================
# ABA 10: MOBILIDADE EV (MANUAL)
# ==========================================
with tab10:
    st.subheader("🚗 Mobilidade Elétrica (Manual)")
    n = st.number_input("Nº Carregadores", value=5, key="t10_n")
    pot = st.number_input("Potência (kW)", value=22.0, key="t10_p")
    st.metric("Potência Total", f"{n * pot:.1f} kW")

# ==========================================
# ABA 11: AUTOMAÇÃO (MANUAL)
# ==========================================
with tab11:
    st.subheader("🤖 Automação (Manual)")
    p_robo = st.number_input("Potência (W)", value=500.0, key="t11_p")
    h_robo = st.number_input("Horas", value=8.0, key="t11_h")
    st.metric("Consumo Diário", f"{(p_robo * h_robo)/1000:.1f} kWh")

# ==========================================
# ABA 12: ENGENHARIA CIVIL (MANUAL)
# ==========================================
with tab12:
    st.subheader("🏗️ Engenharia Civil (Manual)")
    comp = st.number_input("Comprimento (m)", value=5.0, key="t12_comp")
    larg = st.number_input("Largura (m)", value=4.0, key="t12_larg")
    alt_pilar = st.number_input("Altura da Coluna/Pilar (m)", value=3.0, key="t12_alt")
    
    if st.button("Calcular Volume de Betão e Materiais", key="btn_civil"):
        vol_pilar = comp * larg * alt_pilar
        sacos = math.ceil(vol_pilar * 7)
        st.metric("Volume Total de Betão", f"{vol_pilar:.2f} m³")
        c1, c2, c3 = st.columns(3)
        c1.metric("Cimento (50kg)", f"{sacos} sacos")
        c2.metric("Areia", f"{vol_pilar * 0.5:.1f} m³")
        c3.metric("Brita", f"{vol_pilar * 0.8:.1f} m³")

# ==========================================
# ABA 13: INDÚSTRIA E FABRICO (MANUAL)
# ==========================================
with tab13:
    st.subheader("🏭 Indústria e Fabrico (Engenharia de Produção)")
    st.write("Planeamento de linhas de montagem e matérias-primas.")
    
    col_fab1, col_fab2 = st.columns(2)
    with col_fab1:
        prod_diaria = st.number_input("Produção Diária (Unidades)", value=10, key="t13_prod")
        custo_materia = st.number_input("Custo Matéria-Prima por Unidade (USD)", value=5000.0, key="t13_custo")
    with col_fab2:
        energia_unidade = st.number_input("Energia por Unidade (kWh)", value=150.0, key="t13_energia")
        horas_turno = st.number_input("Horas de Turno", value=8.0, key="t13_turno")
    
    energia_diaria_fab = prod_diaria * energia_unidade
    custo_diario_fab = prod_diaria * custo_materia
    
    st.markdown("---")
    st.metric("Consumo Diário da Fábrica", f"{energia_diaria_fab:,} kWh")
    st.metric("Potência Necessária (Demanda Média)", f"{(energia_diaria_fab / horas_turno):.1f} kW")
    st.metric("Custo Diário de Matéria-Prima", f"$ {custo_diario_fab:,.2f}")
    st.info("💡 **Nota:** Para alimentar esta fábrica, o sistema solar (ou gerador) tem de ser dimensionado para a Demanda Média calculada acima.")

# ==========================================
# ABA 14 A 17: MECÂNICA, BATERIAS, INVERSORES, GERADORES
# ==========================================
with tab14:
    st.subheader("⚙️ Mecânica")
    st.metric("Torque", f"{((10 * 1000) / ((1500 * 2 * math.pi) / 60)):.1f} N.m")

with tab15:
    st.subheader("🔋 Baterias")
    st.metric("Baterias (300kWh/mês)", "5 un. de 200Ah")

with tab16:
    st.subheader("🔌 Inversores")
    st.metric("Inversor (2000W)", "2500 W")

with tab17:
    st.subheader("⚙️ Geradores")
    st.metric("Gerador (5kW)", "7.8 kVA")

# ==========================================
# ABA 18: MANUTENÇÃO
# ==========================================
with tab18:
    st.subheader("🛠️ Manutenção")
    st.checkbox("Inspeção visual", key="m1")
    st.checkbox("Limpeza", key="m2")

# ==========================================
# ABA 19: PROJETO EXECUTIVO
# ==========================================
with tab19:
    st.subheader("🔧 Projeto Executivo")
    st.selectbox("Sistema", ["Solar", "Bombeamento", "EV", "Civil", "Indústria"], key="t19_sel")
    st.info("Detalhes técnicos de instalação, segurança e proteções.")

# ==========================================
# ABA 20: NEGÓCIO
# ==========================================
with tab20:
    st.subheader("💼 Meu Negócio")
    st.metric("Faturamento Estimado (Ano 1)", "$ 3.000,00")
    st.info("💡 **Estratégia Modular:** Venda o software completo ou apenas os módulos que o cliente precisa (Ex: Módulo de Fábrica para Investidores).")

# --- BARRA LATERAL ---
st.sidebar.title("EcoRenováveis Pro")
st.sidebar.info(
    "Desenvolvido por **Adão Cassessa**.\n\n"
    "Engenharia Total: Renováveis, Elétrica, Civil, Mecânica e Indústria.\n\n"
    "Contacto: +244 946 419 656"
)
st.sidebar.caption("© 2026 EcoRenováveis. Todos os direitos reservados.")
