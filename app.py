import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="EcoRenováveis Pro - Engenharia Global", page_icon="🌍", layout="wide")

st.title("🌍 EcoRenováveis Pro: Engenharia Global")
st.write("Plataforma completa: Renováveis, Elétrica, Civil, Automação e Indústria.")

# Criando as 24 abas (TODAS FUNCIONAIS E PREENCHIDAS)
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16, tab17, tab18, tab19, tab20, tab21, tab22, tab23, tab24 = st.tabs([
    "🌟 Guia Automático", "📍 Mapa", "☀️ Solar (Manual)", "🌡️ Térmica", "🌬️ Eólica", "💧 Hídrica", 
    "🚰 Bombeamento", "🌱 Biomassa", "⚡ Eletrotécnica", "🚗 Mobilidade EV", "🤖 Automação", 
    "🏗️ Eng. Civil", "🛣️ Estradas", "💡 Iluminação", "🏭 Indústria", "⚙️ Mecânica", 
    "🔋 Baterias", "🔌 Inversores", "⚙️ Geradores", "🛠️ Manutenção", "📚 Guia Técnico", 
    "🔧 Executivo", "💼 Negócio", "🇦🇴 Governo/Investimento"
])

if 'latitude' not in st.session_state: st.session_state.latitude = -8.8390
if 'longitude' not in st.session_state: st.session_state.longitude = 13.2894

# ==========================================
# ABA 1: GUIA AUTOMÁTICO
# ==========================================
with tab1:
    st.subheader("🌟 Assistente de Criação de Projeto (Tudo-em-Um)")
    tipo_sistema = st.selectbox("Selecione o Tipo de Sistema para Dimensionar", [
        "☀️ Solar Fotovoltaico", "⚡ Eletrotécnica", "🚰 Bombeamento Solar", "🤖 Automação Industrial",
        "🏗️ Engenharia Civil (Betão)", "🛣️ Estradas (Asfalto)", "💡 Iluminação Pública", 
        "🌡️ Energia Térmica", "🌬️ Energia Eólica", "💧 Energia Hídrica", "🌱 Biomassa", "🏭 Indústria"
    ], key="t1_main")
    st.divider()

    if tipo_sistema == "☀️ Solar Fotovoltaico":
        col1, col2, col3 = st.columns(3)
        with col1:
            c_sol = st.number_input("Consumo Mensal (kWh)", value=300.0, key="g_sol_c")
            irr_sol = st.number_input("Irradiação (kWh/m²/dia)", value=5.5, key="g_sol_i")
        with col2:
            tp_painel = st.selectbox("Tipo de Painel", ["Monocristalino", "Policristalino", "Filme Fino"], key="g_sol_tp")
            pot_painel = st.number_input("Potência do Painel (W)", value=550, key="g_sol_pp")
        with col3:
            tp_bat = st.selectbox("Tipo de Bateria", ["Lítio (DoD 90%)", "Chumbo-Ácido (DoD 50%)"], key="g_sol_tb")
            dias_aut = st.number_input("Dias de Autonomia", 1, 5, 1, key="g_sol_da")
        if st.button("Calcular Solar", key="b_g_sol"):
            kwp = (c_sol/30) / (irr_sol * 0.8)
            num_p = math.ceil((kwp*1000)/pot_painel)
            dod = 0.9 if "Lítio" in tp_bat else 0.5
            num_b = math.ceil(((c_sol/30*1000*dias_aut)/(48*dod))/200)
            st.success("✅ Resultado:")
            c1, c2 = st.columns(2)
            c1.metric("Painéis Necessários", f"{num_p} un.")
            c2.metric("Baterias Necessárias", f"{num_b} un.")

    elif tipo_sistema == "⚡ Eletrotécnica":
        col1, col2 = st.columns(2)
        with col1:
            p_ele = st.number_input("Potência (W)", value=1000.0, key="g_ele_p")
            v_ele = st.number_input("Tensão (V)", value=220.0, key="g_ele_v")
        with col2:
            fase_ele = st.selectbox("Fase", ["Monofásico", "Bifásico", "Trifásico"], key="g_ele_f")
            fp_ele = st.number_input("Fator de Potência", value=0.8, key="g_ele_fp")
        if st.button("Calcular Elétrica", key="b_g_ele"):
            if "Trifásico" in fase_ele: i = p_ele / (math.sqrt(3) * v_ele * fp_ele)
            elif "Bifásico" in fase_ele: i = p_ele / (2 * v_ele * fp_ele)
            else: i = p_ele / (v_ele * fp_ele)
            r = v_ele / i if i > 0 else 0
            st.success("✅ Resultado (5 Grandezas):")
            c1, c2, c3, c4, c5 = st.columns(5)
            c1.metric("Potência", f"{p_ele:.0f} W")
            c2.metric("Tensão", f"{v_ele:.0f} V")
            c3.metric("Corrente", f"{i:.2f} A")
            c4.metric("Resistência", f"{r:.2f} Ω")
            c5.metric("Frequência", "50 Hz")

    elif tipo_sistema == "🚰 Bombeamento Solar":
        col1, col2 = st.columns(2)
        with col1:
            prof = st.number_input("Profundidade (m)", value=50.0, key="g_b_p")
            alt = st.number_input("Altura Tanque (m)", value=10.0, key="g_b_a")
        with col2:
            vol = st.number_input("Volume (m³/dia)", value=20.0, key="g_b_v")
            ef = st.slider("Eficiência Bomba (%)", 30, 80, 50, key="g_b_e") / 100
        if st.button("Calcular Bombeamento", key="b_g_bomb"):
            hmt = (prof + alt) * 1.1
            pot = (1000 * 9.81 * (vol/(24*3600)) * hmt) / ef
            st.metric("HMT", f"{hmt:.1f} m")
            st.metric("Potência Solar Necessária", f"{(pot/(1000*0.8)):.2f} kWp")

    elif tipo_sistema == "🤖 Automação Industrial":
        col1, col2 = st.columns(2)
        with col1:
            p_rob = st.number_input("Potência (W)", value=1500.0, key="g_a_p")
            h_rob = st.number_input("Horas/Dia", value=16.0, key="g_a_h")
        with col2:
            n_rob = st.number_input("Quantidade", value=4, key="g_a_n")
            tem_vfd = st.selectbox("Inclui VFD?", ["Sim", "Não"], key="g_a_vfd")
        if st.button("Calcular Automação", key="b_g_aut"):
            cons = (p_rob * h_rob * n_rob) / 1000
            st.metric("Consumo Diário", f"{cons:.1f} kWh")
            if tem_vfd == "Sim": st.info("⚠️ VFDs exigem cabos blindados e energia estável.")

    elif tipo_sistema == "🏗️ Engenharia Civil (Betão)":
        col1, col2 = st.columns(2)
        with col1:
            comp = st.number_input("Comprimento (m)", value=5.0, key="g_civ_c")
            larg = st.number_input("Largura (m)", value=4.0, key="g_civ_l")
        with col2:
            alt = st.number_input("Altura/Espessura (m)", value=0.15, key="g_civ_a")
            traco = st.selectbox("Traço", ["1:2:3", "1:3:3"], key="g_civ_t")
        if st.button("Calcular Betão", key="b_g_civ"):
            vol = comp * larg * alt
            sacos = math.ceil(vol * (7 if "1:2:3" in traco else 5))
            st.metric("Volume de Betão", f"{vol:.2f} m³")
            st.metric("Sacos de Cimento", f"{sacos} un.")

    elif tipo_sistema == "🛣️ Estradas (Asfalto)":
        col1, col2 = st.columns(2)
        with col1:
            km = st.number_input("Comprimento (km)", value=1.0, key="g_est_km")
            larg = st.number_input("Largura (m)", value=7.0, key="g_est_l")
        with col2:
            base = st.number_input("Base (m)", value=0.20, key="g_est_b")
            asf = st.number_input("Asfalto (m)", value=0.05, key="g_est_a")
        if st.button("Calcular Estrada", key="b_g_est"):
            v_b = km * 1000 * larg * base
            v_a = km * 1000 * larg * asf
            st.metric("Volume Base", f"{v_b:,.0f} m³")
            st.metric("Volume Asfalto", f"{v_a:,.0f} m³")
            st.metric("Toneladas Asfalto", f"{(v_a*2.4):,.0f} t")

    elif tipo_sistema == "💡 Iluminação Pública":
        comp = st.number_input("Comprimento (m)", value=1000, key="g_ilu_c")
        esp = st.number_input("Espaçamento (m)", value=30, key="g_ilu_e")
        pot = st.number_input("Potência LED (W)", value=100, key="g_ilu_p")
        if st.button("Calcular Iluminação", key="b_g_ilu"):
            n = math.ceil(comp / esp) + 1
            st.metric("Nº Postes", f"{n} un.")
            st.metric("Carga Total", f"{(n*pot)/1000:.2f} kW")

    elif tipo_sistema == "🌡️ Energia Térmica":
        v = st.number_input("Volume Água (L/dia)", value=200, key="g_t_v")
        tp = st.selectbox("Coletor", ["Plano", "Tubo a Vácuo"], key="g_t_tp")
        if st.button("Calcular Térmica", key="b_g_t"):
            ef = 0.60 if "Plano" in tp else 0.75
            st.metric("Área de Coletores", f"{((v * 1.16 * 40) / 1000) / (5.5 * ef):.1f} m²")

    elif tipo_sistema == "🌬️ Energia Eólica":
        v = st.number_input("Vento (m/s)", value=6.0, key="g_e_v")
        r = st.number_input("Raio Pás (m)", value=2.0, key="g_e_r")
        tp = st.selectbox("Turbina", ["Eixo Horizontal", "Eixo Vertical"], key="g_e_tp")
        if st.button("Calcular Eólica", key="b_g_e"):
            cp = 0.40 if "Horizontal" in tp else 0.25
            st.metric("Potência", f"{0.5 * 1.225 * (math.pi * r**2) * (v**3) * cp:.0f} W")

    elif tipo_sistema == "💧 Energia Hídrica":
        q = st.number_input("Vazão (m³/s)", value=10.0, key="g_h_q")
        h = st.number_input("Queda (m)", value=20.0, key="g_h_h")
        tp = st.selectbox("Turbina", ["Pelton", "Francis", "Kaplan"], key="g_h_tp")
        if st.button("Calcular Hídrica", key="b_g_h"):
            ef = 0.90 if "Pelton" in tp else (0.92 if "Francis" in tp else 0.94)
            st.metric("Potência", f"{(1000 * 9.81 * q * h * ef)/1000:.1f} kW")

    elif tipo_sistema == "🌱 Biomassa":
        m = st.number_input("Massa Resíduo (kg/dia)", value=1000.0, key="g_bio_m")
        tp = st.selectbox("Processo", ["Combustão (25%)", "Gaseificação (35%)", "Biodigestor (65%)"], key="g_bio_tp")
        if st.button("Calcular Biomassa", key="b_g_bio"):
            ef = 0.25 if "Combustão" in tp else (0.35 if "Gaseificação" in tp else 0.65)
            st.metric("Potência Contínua", f"{((m * 15 * ef) / 3.6) / 24:.1f} kW")

    elif tipo_sistema == "🏭 Indústria":
        prod = st.number_input("Produção Diária", value=10, key="g_ind_p")
        en = st.number_input("Energia/Unidade (kWh)", value=150.0, key="g_ind_e")
        if st.button("Calcular Indústria", key="b_g_ind"):
            st.metric("Consumo Diário", f"{(prod * en):,} kWh")

# ==========================================
# ABA 2: MAPA
# ==========================================
with tab2:
    lat = st.number_input("Latitude", value=st.session_state.latitude, key="t2_lat")
    lon = st.number_input("Longitude", value=st.session_state.longitude, key="t2_lon")
    st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}), zoom=12)

# ==========================================
# ABA 3: SOLAR MANUAL
# ==========================================
with tab3:
    st.subheader("☀️ Solar Fotovoltaico (Manual)")
    col1, col2 = st.columns(2)
    with col1:
        c = st.number_input("Consumo (kWh)", value=300.0, key="t3_c")
        irr = st.number_input("Irradiação", value=5.5, key="t3_i")
        sombra = st.slider("Sombreamento (%)", 0, 50, 10, key="t3_s")
    with col2:
        tp = st.selectbox("Tipo de Painel", ["Monocristalino", "Policristalino", "Filme Fino"], key="t3_tp")
        pp = st.number_input("Potência Painel (W)", value=550, key="t3_pp")
    if st.button("Calcular Solar Manual", key="b_t3"):
        pr = 0.8 * (1 - sombra/100)
        kwp = (c/30) / (irr * pr)
        st.metric("Painéis Necessários", f"{math.ceil((kwp*1000)/pp)} un.")

# ==========================================
# ABA 4: TÉRMICA MANUAL
# ==========================================
with tab4:
    st.subheader("🌡️ Energia Térmica (Manual)")
    v = st.number_input("Volume Água (L/dia)", value=200, key="t4_v")
    dt = st.number_input("Aumento Temp (°C)", value=40, key="t4_dt")
    tp = st.selectbox("Tipo de Coletor", ["Plano", "Tubo a Vácuo"], key="t4_tp")
    ef = 0.60 if "Plano" in tp else 0.75
    st.metric("Área Coletores", f"{((v * 1.16 * dt) / 1000) / (5.5 * ef):.1f} m²")

# ==========================================
# ABA 5: EÓLICA MANUAL
# ==========================================
with tab5:
    st.subheader("🌬️ Energia Eólica (Manual)")
    v = st.number_input("Vento (m/s)", value=6.0, key="t5_v")
    r = st.number_input("Raio Pás (m)", value=2.0, key="t5_r")
    tp = st.selectbox("Tipo de Turbina", ["Eixo Horizontal", "Eixo Vertical"], key="t5_tp")
    cp = 0.40 if "Horizontal" in tp else 0.25
    st.metric("Potência", f"{0.5 * 1.225 * (math.pi * r**2) * (v**3) * cp:.0f} W")

# ==========================================
# ABA 6: HÍDRICA MANUAL
# ==========================================
with tab6:
    st.subheader("💧 Energia Hídrica (Manual)")
    q = st.number_input("Vazão (m³/s)", value=10.0, key="t6_q")
    h = st.number_input("Queda (m)", value=20.0, key="t6_h")
    tp = st.selectbox("Tipo de Turbina", ["Pelton", "Francis", "Kaplan"], key="t6_tp")
    ef = 0.90 if "Pelton" in tp else (0.92 if "Francis" in tp else 0.94)
    st.metric("Potência", f"{(1000 * 9.81 * q * h * ef)/1000:.1f} kW")

# ==========================================
# ABA 7: BOMBEAMENTO MANUAL
# ==========================================
with tab7:
    st.subheader("🚰 Bombeamento (Manual)")
    prof = st.number_input("Profundidade (m)", value=50.0, key="t7_p")
    alt = st.number_input("Altura Tanque (m)", value=10.0, key="t7_a")
    st.metric("HMT", f"{(prof + alt) * 1.1:.1f} m")

# ==========================================
# ABA 8: BIOMASSA MANUAL (Corrigida)
# ==========================================
with tab8:
    st.subheader("🌱 Biomassa (Manual)")
    m = st.number_input("Massa Resíduo (kg/dia)", value=1000.0, key="t8_m")
    p = st.number_input("Poder Calorífico (MJ/kg)", value=15.0, key="t8_p")
    tp = st.selectbox("Tipo de Processo", ["Combustão Direta", "Gaseificação", "Biodigestor"], key="t8_tp")
    ef = 0.25 if "Combustão" in tp else (0.35 if "Gaseificação" in tp else 0.65)
    st.metric("Potência Contínua", f"{((m * p * ef) / 3.6) / 24:.1f} kW")

# ==========================================
# ABA 9: ELETROTÉCNICA (Manual Completa)
# ==========================================
with tab9:
    st.subheader("⚡ Eletrotécnica (Manual)")
    p = st.number_input("Potência (W)", value=1000.0, key="t9_p")
    v = st.number_input("Tensão (V)", value=220.0, key="t9_v")
    tp = st.selectbox("Tipo de Instalação", ["Monofásico", "Bifásico", "Trifásico"], key="t9_tp")
    if "Trifásico" in tp: i = p / (math.sqrt(3) * v * 0.8)
    elif "Bifásico" in tp: i = p / (2 * v * 0.8)
    else: i = p / (v * 0.8)
    st.metric("Corrente (A)", f"{i:.2f} A")
    st.metric("Resistência (Ω)", f"{(v/i if i>0 else 0):.2f} Ω")

# ==========================================
# ABA 10: MOBILIDADE EV
# ==========================================
with tab10:
    st.subheader("🚗 Mobilidade Elétrica (Manual)")
    n = st.number_input("Nº Carregadores", value=5, key="t10_n")
    pot = st.number_input("Potência (kW)", value=22.0, key="t10_p")
    st.metric("Potência Total", f"{n * pot:.1f} kW")

# ==========================================
# ABA 11: AUTOMAÇÃO
# ==========================================
with tab11:
    st.subheader("🤖 Automação (Manual)")
    p = st.number_input("Potência Robô (W)", value=1500.0, key="t11_p")
    h = st.number_input("Horas", value=16.0, key="t11_h")
    st.metric("Consumo Diário", f"{(p * h)/1000:.1f} kWh")

# ==========================================
# ABA 12: ENGENHARIA CIVIL
# ==========================================
with tab12:
    st.subheader("🏗️ Engenharia Civil (Manual)")
    comp = st.number_input("Comprimento (m)", value=5.0, key="t12_c")
    larg = st.number_input("Largura (m)", value=4.0, key="t12_l")
    alt = st.number_input("Altura (m)", value=0.15, key="t12_a")
    st.metric("Volume Betão", f"{comp * larg * alt:.2f} m³")

# ==========================================
# ABA 13: ESTRADAS
# ==========================================
with tab13:
    st.subheader("🛣️ Estradas (Manual)")
    km = st.number_input("Comprimento (km)", value=1.0, key="t13_km")
    st.metric("Volume Asfalto (5cm)", f"{(km * 1000 * 7 * 0.05):,.0f} m³")

# ==========================================
# ABA 14: ILUMINAÇÃO
# ==========================================
with tab14:
    st.subheader("💡 Iluminação (Manual)")
    comp = st.number_input("Comprimento (m)", value=1000, key="t14_c")
    st.metric("Nº Postes (30m)", f"{math.ceil(comp / 30) + 1} un.")

# ==========================================
# ABA 15: INDÚSTRIA (Corrigida e Expandida)
# ==========================================
with tab15:
    st.subheader("🏭 Indústria e Fabrico (Manual)")
    st.write("Cálculo de carga elétrica e consumo para linhas de produção.")
    col1, col2 = st.columns(2)
    with col1:
        prod = st.number_input("Produção Diária (Unidades)", value=10, key="t15_p")
        en = st.number_input("Energia/Unidade (kWh)", value=150.0, key="t15_e")
    with col2:
        maq = st.number_input("Potência das Máquinas (kW)", value=50.0, key="t15_m")
        horas = st.number_input("Horas de Operação/Dia", value=8.0, key="t15_h")
    
    st.metric("Consumo Diário (Produção)", f"{(prod * en):,} kWh")
    st.metric("Consumo Diário (Máquinas)", f"{(maq * horas):,} kWh")
    st.metric("Carga Total Instalada (Máquinas)", f"{maq:.1f} kW")

# ==========================================
# ABA 16: MECÂNICA
# ==========================================
with tab16:
    st.subheader("⚙️ Mecânica (Manual)")
    pot = st.number_input("Potência Motor (kW)", value=10.0, key="t16_p")
    rpm = st.number_input("Rotação (RPM)", value=1500.0, key="t16_r")
    torque = (pot * 1000) / ((rpm * 2 * math.pi) / 60)
    st.metric("Torque", f"{torque:.1f} N.m")

# ==========================================
# ABA 17: BATERIAS MANUAL
# ==========================================
with tab17:
    st.subheader("🔋 Baterias (Manual)")
    tp = st.selectbox("Tipo de Bateria", ["Lítio", "Chumbo-Ácido"], key="t17_tp")
    c = st.number_input("Consumo (kWh)", value=300.0, key="t17_c")
    dod = 0.9 if tp == "Lítio" else 0.5
    st.metric("Baterias de 200Ah", f"{math.ceil(((c/30*1000)/(48*dod))/200)} un.")

# ==========================================
# ABA 18: INVERSORES MANUAL
# ==========================================
with tab18:
    st.subheader("🔌 Inversores (Manual)")
    tp = st.selectbox("Tipo de Inversor", ["Híbrido", "Off-Grid", "On-Grid"], key="t18_tp")
    carga = st.number_input("Carga (W)", value=2000.0, key="t18_c")
    st.metric("Inversor", f"{carga * 1.25:.0f} W")

# ==========================================
# ABA 19: GERADORES MANUAL
# ==========================================
with tab19:
    st.subheader("⚙️ Geradores (Manual)")
    tp = st.selectbox("Tipo de Gerador", ["Diesel", "Gasolina", "Gás"], key="t19_tp")
    p = st.number_input("Carga Pico (kW)", value=5.0, key="t19_p")
    st.metric("Gerador", f"{(p * 1.25) / 0.8:.1f} kVA")

# ==========================================
# ABA 20: MANUTENÇÃO (Com Tipos e Checklists Reais)
# ==========================================
with tab20:
    st.subheader("🛠️ Gestão de Manutenção Sincronizada")
    sist = st.selectbox("Selecione o Sistema Alvo", [
        "Solar Fotovoltaico", "Térmica", "Eólica", "Hídrica", "Bombeamento", "Biomassa", 
        "Eletrotécnica", "Mobilidade EV", "Automação", "Engenharia Civil", "Estradas", 
        "Iluminação", "Indústria", "Mecânica", "Baterias", "Inversores", "Geradores"
    ], key="t20_s")
    
    st.markdown(f"### 📋 Checklist: {sist}")
    
    if sist == "Solar Fotovoltaico":
        tp = st.selectbox("Tecnologia do Painel", ["Monocristalino", "Policristalino", "Filme Fino"], key="m_sol_tp")
        st.checkbox("Limpeza dos painéis (remoção de pó)", key="m_sol1")
        if tp == "Monocristalino": st.checkbox("Verificar Hot Spots (Pontos Quentes)", key="m_sol2")
        elif tp == "Policristalino": st.checkbox("Verificar micro-fissuras", key="m_sol3")
        else: st.checkbox("Verificar delaminação do filme", key="m_sol4")
    elif sist == "Baterias":
        tp = st.selectbox("Tecnologia", ["Lítio", "Chumbo-Ácido"], key="m_bat_tp")
        st.checkbox("Verificar tensão de cada bateria", key="m_bat1")
        if tp == "Lítio": st.checkbox("Verificar BMS", key="m_bat2")
        else: st.checkbox("Verificar nível de água destilada", key="m_bat3")
    elif sist == "Eletrotécnica":
        st.checkbox("Aperto de terminais e testes de continuidade", key="m_ele1")
        st.checkbox("Teste de Haste de Terra (< 10 Ω)", key="m_ele2")
        st.checkbox("Verificação de Disjuntores e DPS", key="m_ele3")
    elif sist == "Automação":
        st.checkbox("Calibração de Sensores", key="m_aut1")
        st.checkbox("Backup do programa do PLC/HMI", key="m_aut2")
        st.checkbox("Verificação de ruído elétrico nos VFDs", key="m_aut3")
        st.checkbox("Lubrificação de braços robóticos", key="m_aut4")
    elif sist == "Térmica":
        tp = st.selectbox("Tecnologia do Coletor", ["Plano", "Tubo a Vácuo"], key="m_term_tp")
        st.checkbox("Limpeza dos vidros", key="m_term1")
        if tp == "Plano": st.checkbox("Verificar isolamento da caixa", key="m_term2")
        else: st.checkbox("Verificar tubos de vácuo partidos", key="m_term3")
    elif sist == "Eólica":
        tp = st.selectbox("Tecnologia", ["Eixo Horizontal", "Eixo Vertical"], key="m_eol_tp")
        st.checkbox("Lubrificação do multiplicador", key="m_eol1")
        if tp == "Eixo Horizontal": st.checkbox("Verificar sistema de orientação (Yaw)", key="m_eol2")
    elif sist == "Hídrica":
        tp = st.selectbox("Tecnologia", ["Pelton", "Francis", "Kaplan"], key="m_hid_tp")
        st.checkbox("Limpeza das grades", key="m_hid1")
        if tp == "Pelton": st.checkbox("Verificar desgaste das colheres", key="m_hid2")
    elif sist == "Bombeamento":
        st.checkbox("Verificar proteção contra funcionamento a seco", key="m_bomb1")
    elif sist == "Biomassa":
        st.checkbox("Limpeza da fuligem/caldeira", key="m_bio1")
    elif sist == "Mobilidade EV":
        st.checkbox("Verificar cabos de carregamento", key="m_ev1")
    elif sist == "Engenharia Civil":
        st.checkbox("Inspeção de fissuras", key="m_civ1")
    elif sist == "Estradas":
        st.checkbox("Verificação de buracos e fissuras", key="m_est1")
    elif sist == "Iluminação":
        st.checkbox("Teste de acendimento dos LED", key="m_ilu1")
    elif sist == "Indústria":
        st.checkbox("Manutenção preventiva das máquinas", key="m_ind1")
    elif sist == "Mecânica":
        st.checkbox("Alinhamento e lubrificação", key="m_mec1")
    elif sist == "Inversores":
        st.checkbox("Limpeza do dissipador de calor", key="m_inv1")
    elif sist == "Geradores":
        st.checkbox("Verificar óleo e água", key="m_ger1")

# ==========================================
# ABA 21: GUIA TÉCNICO
# ==========================================
with tab21:
    st.subheader("📚 Guia Técnico e Boas Práticas")
    with st.expander("☀️ Solar Fotovoltaico"): st.write("**Fórmulas:** Potência (kWp) = Consumo Diário / (Irradiação × PR). Evite sombreamento.")
    with st.expander("🌡️ Térmica"): st.write("Use tubos a vácuo em climas frios e coletores planos em climas quentes.")
    with st.expander("🌬️ Eólica"): st.write("A potência cresce ao cubo da velocidade do vento. Altura mínima de 10m.")
    with st.expander("💧 Hídrica"): st.write("Pelton (Alta queda), Francis (Média), Kaplan (Baixa queda).")
    with st.expander("🚰 Bombeamento"): st.write("Verifique sempre a HMT (Altura Manométrica Total) para não queimar a bomba.")
    with st.expander("🌱 Biomassa"): st.write("Biodigestores requerem temperatura constante e resíduos orgânicos.")
    with st.expander("⚡ Eletrotécnica"): st.write("Cabo dimensionado por queda de tensão máx 3%. Haste de terra obrigatória (< 10 Ω).")
    with st.expander("🚗 Mobilidade EV"): st.write("Carregadores rápidos (DC) exigem transformadores dedicados.")
    with st.expander("🤖 Automação"): st.write("Robôs industriais exigem energia estabilizada e aterramento rigoroso.")
    with st.expander("🏗️ Engenharia Civil"): st.write("Estudo de solo é obrigatório. Betão 1:2:3 para alta resistência.")
    with st.expander("🛣️ Estradas"): st.write("Base de brita 0.20m, asfalto 0.05m (tráfego leve). Compactação é essencial.")
    with st.expander("💡 Iluminação"): st.write("Postes solares devem ter autonomia de 2-3 dias de chuva.")
    with st.expander("🏭 Indústria"): st.write("1 carro consome ~1.2t de aço. Fábricas precisam de energia trifásica.")
    with st.expander("⚙️ Mecânica"): st.write("Alinhamento de eixos com tolerância máx 0.05mm.")
    with st.expander("🔋 Baterias"): st.write("Lítio (DoD 90%) vs Chumbo (DoD 50%).")
    with st.expander("🔌 Inversores"): st.write("Fator de segurança de 1.25. Motores exigem pico de 3x.")
    with st.expander("⚙️ Geradores"): st.write("Manutenção a cada 250h. Nunca ligue à rede sem ATS.")
    
    st.divider()
    st.markdown("### 🇦🇴 Oportunidades de Investimento (Governo)")
    with st.expander("Reativação de Fábricas (ZEE)"): st.write("Textang II, Inducamar, Sidurex.")
    with st.expander("Mineração (Lítio, Ouro)"): st.write("Energia para minas e refinarias.")
    with st.expander("Robótica e Automação"): st.write("Drones Agrícolas e Robótica Médica.")

# ==========================================
# ABA 22: PROJETO EXECUTIVO (Instruções Detalhadas)
# ==========================================
with tab22:
    st.subheader("🔧 Projeto Executivo e Detalhamento de Campo")
    exec_sist = st.selectbox("Selecione o Sistema para Execução", [
        "Solar Fotovoltaico", "Térmica", "Eólica", "Hídrica", "Bombeamento", "Biomassa", 
        "Eletrotécnica", "Mobilidade EV", "Automação", "Engenharia Civil", "Estradas", 
        "Iluminação", "Indústria", "Mecânica", "Baterias", "Inversores", "Geradores"
    ], key="t22_sel")
    
    st.info(f"📋 **Instruções de Execução para {exec_sist}:**")
    
    if exec_sist == "Solar Fotovoltaico":
        st.success("**String:** Máximo de 10 painéis em série. **Cabo DC:** 6mm².")
        st.error("**Segurança:** Haste de Terra (< 10 Ω).")
    elif exec_sist == "Térmica":
        st.success("**Tubagem:** Cobre 22mm. **Vaso de Expansão:** 18L.")
        st.error("**Segurança:** Válvula de segurança 6 bar.")
    elif exec_sist == "Eólica":
        st.success("**Cabo DC:** Proteção UV. **Controlador:** Dumpload.")
        st.error("**Segurança:** Haste de terra na torre.")
    elif exec_sist == "Hídrica":
        st.success("**Cabo AC:** Trifásico 380V. **Regulador:** AVR.")
        st.error("**Segurança:** Haste de terra no gerador.")
    elif exec_sist == "Bombeamento":
        st.success("**Controlador:** VFD (Variador). **Cabo submersível:** 4mm².")
        st.error("**Segurança:** Proteção contra funcionamento a seco.")
    elif exec_sist == "Biomassa":
        st.success("**Gás:** Tubo PEAD. **Filtro:** H2S.")
        st.error("**Segurança:** Válvula corta-fogo.")
    elif exec_sist == "Eletrotécnica":
        st.success("**Quadro:** Disjuntor Geral, DPS, Identificação de circuitos.")
        st.warning("**Motores:** Instalar relés térmicos e contactores. Quadro ATS para geradores.")
        st.error("**Segurança:** Haste de terra (< 10 Ω).")
    elif exec_sist == "Mobilidade EV":
        st.success("**Cabos:** Dimensionados para alta corrente. **Transformador:** Dedicado.")
        st.error("**Segurança:** Proteção contra surtos (DPS).")
    elif exec_sist == "Automação":
        st.success("**Cabos:** Blindados para sinais analógicos. **Sensores:** Calibrados.")
        st.warning("**VFDs:** Instalar filtros de linha (chokes) para reduzir harmónicos.")
        st.error("**Segurança:** Botão de emergência (cogumelo) e paragem de emergência no PLC.")
    elif exec_sist == "Engenharia Civil":
        st.success("**Betão:** Traço 1:2:3. **Cura:** Molhar por 7 dias.")
        st.error("**Segurança:** EPIs obrigatórios (capacete, botas).")
    elif exec_sist == "Estradas":
        st.success("**Base:** Brita compactada. **Asfalto:** Aplicar entre 140-160°C.")
        st.error("**Segurança:** Sinalização de trânsito na obra.")
    elif exec_sist == "Iluminação":
        st.success("**Postes:** Espaçamento 30m. **Cabo:** 16mm².")
        st.error("**Segurança:** Disjuntor diferencial no quadro.")
    elif exec_sist == "Indústria":
        st.success("**Energia:** Trifásico 380V. **Manutenção:** Preventiva mensal.")
        st.error("**Segurança:** Aterramento rigoroso.")
    elif exec_sist == "Mecânica":
        st.success("**Alinhamento:** Tolerância 0.05mm. **Lubrificação:** Massa grafitada.")
        st.error("**Segurança:** Carenagem de proteção nas correias.")
    elif exec_sist == "Baterias":
        st.success("**Instalação:** Local ventilado. **Conexão:** Cabos grossos.")
        st.error("**Segurança:** Extintor de incêndio classe C por perto.")
    elif exec_sist == "Inversores":
        st.success("**Instalação:** Local fresco. **Limpeza:** Dissipador a cada 6 meses.")
        st.error("**Segurança:** Desligar antes de intervir.")
    elif exec_sist == "Geradores":
        st.success("**Óleo:** Trocar a cada 250h. **Combustível:** Filtrar.")
        st.error("**Segurança:** Chaminé de exaustão para o exterior.")

# ==========================================
# ABA 23: NEGÓCIO
# ==========================================
with tab23:
    st.subheader("💼 Meu Negócio")
    st.metric("Faturamento Estimado (Ano 1)", "$ 3.000,00 (Exemplo base)")
    st.info("💡 **Estratégia Modular:** Venda a plataforma completa ou módulos por setor (Governo, Mineração, Civil).")

# ==========================================
# ABA 24: GOVERNO/INVESTIMENTO
# ==========================================
with tab24:
    st.subheader("🇦🇴 Catálogo de Soluções e Oportunidades de Angola")
    st.write("A plataforma está preparada para resolver desafios de todas as áreas da engenharia angolana.")
    st.markdown("### 🏭 Reativação de Fábricas Paradas")
    with st.expander("Ver Fábricas (ZEE, Têxteis)"):
        st.markdown("*   **Textang II:** Energia para máquinas e irrigação para algodão.\n*   **Inducamar (Pneus):** Potência de fornos e solda.\n*   **Sidurex (Aço):** Alta tensão para laminação.")
    st.markdown("### ⛏️ Mineração (35 dos 45 minerais)")
    with st.expander("Ver Soluções para Mineração"):
        st.markdown("*   **Lítio e Níquel:** Fábricas de processamento de baterias.\n*   **Diamantes e Ouro:** Energia para minas e refinarias.\n*   **Terras Raras:** Automação de separadores magnéticos.")


# --- BARRA LATERAL (Com Aviso Legal) ---
st.sidebar.title("EcoRenováveis Pro")
st.sidebar.info(
    "Desenvolvido por **Adão Cassessa**.\n\n"
    "Engenharia Total: Renováveis, Elétrica, Civil, Mecânica Automação e Indústria.\n\n"
    "Contacto: +244 946 419 656"
)
st.sidebar.caption("© 2026 EcoRenováveis. Todos os direitos reservados.")

st.sidebar.markdown("---")
st.sidebar.warning(
    "⚠️ **AVISO LEGAL:** O **EcoRenováveis Pro** é uma ferramenta de pré-dimensionamento baseada em normas IEC/IEEE. Os resultados gerados **não substituem** a vistoria local e a assinatura de um engenheiro inscrito na **Ordem dos Engenheiros de Angola (OEA)**. O desenvolvedor não se responsabiliza por danos decorrentes da execução sem supervisão técnica."
)
