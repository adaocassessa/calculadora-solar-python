import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="EcoRenováveis Pro - Engenharia", page_icon="🌍", layout="wide")

st.title("🌍 EcoRenováveis Pro: Engenharia de Precisão")
st.write("Plataforma global de engenharia para dimensionamento de sistemas renováveis.")

# Criando as 14 abas
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14 = st.tabs([
    "🌟 Guia Automático", 
    "📍 Mapa", 
    "☀️ Solar (Manual)", 
    "🌡️ Térmica",
    "🌬️ Eólica", 
    "💧 Hídrica", 
    "🌱 Biomassa",
    "⚡ Eletrotécnica",
    "🔋 Baterias",
    "🔌 Inversores",
    "⚙️ Geradores",
    "🛠️ Manutenção",
    "🔧 Executivo Completo",
    "💼 Negócio"
])

if 'latitude' not in st.session_state: st.session_state.latitude = -8.8390
if 'longitude' not in st.session_state: st.session_state.longitude = 13.2894

# ==========================================
# ABA 1: GUIA AUTOMÁTICO
# ==========================================
with tab1:
    st.subheader("🌟 Assistente de Criação de Projeto (Tudo-em-Um)")
    tipo_sistema_guia = st.selectbox("Selecione o Tipo de Sistema a Dimensionar", ["Solar Fotovoltaico", "Energia Eólica", "Energia Hídrica", "Energia Térmica", "Biomassa"], key="t1_tipo")
    
    if tipo_sistema_guia == "Solar Fotovoltaico":
        col1, col2, col3 = st.columns(3)
        with col1:
            c_auto = st.number_input("Consumo Mensal (kWh)", value=300.0, key="t1_c")
            i_auto = st.number_input("Irradiação (kWh/m²/dia)", value=5.5, key="t1_i")
        with col2:
            s_auto = st.slider("Sombreamento (%)", 0, 50, 10, key="t1_s")
            tp_auto = st.selectbox("Tipo de Painel", ["Monocristalino", "Policristalino", "Filme Fino"], key="t1_tp")
            pp_auto = st.number_input("Potência do Painel (W)", value=550, key="t1_pp")
        with col3:
            carga_auto = st.number_input("Carga de Pico (W)", value=3000, key="t1_carga")
            mot_auto = st.selectbox("Tem motores?", ["Não", "Sim"], key="t1_mot")
            tb_auto = st.selectbox("Bateria", ["Lítio", "Chumbo-Ácido"], key="t1_tb")
        
        if st.button("Calcular Projeto", key="btn_auto_solar"):
            pr = 0.8 * (1 - s_auto/100)
            kwp = (c_auto/30) / (i_auto * pr)
            p_num = math.ceil((kwp*1000)/pp_auto)
            inv = carga_auto * (3.0 if mot_auto == "Sim" else 1.25)
            dod = 0.9 if tb_auto == "Lítio" else 0.5
            bat = math.ceil(((c_auto/30*1000*1)/(48*dod))/200)
            
            st.markdown("---")
            st.markdown("### 🛒 Lista de Compras Final")
            col_res1, col_res2, col_res3 = st.columns(3)
            col_res1.metric("Painéis Solares", f"{p_num} un.")
            col_res2.metric("Inversor", f"{inv/1000:.1f} kW")
            col_res3.metric("Baterias", f"{bat} un.")

    elif tipo_sistema_guia == "Energia Eólica":
        col1, col2 = st.columns(2)
        with col1:
            carga_eol = st.number_input("Carga Pico (W)", value=3000, key="t1_eol_carga")
            vento_eol = st.number_input("Vento (m/s)", value=6.0, key="t1_eol_v")
        with col2:
            raio_eol = st.number_input("Raio Pás (m)", value=2.0, key="t1_eol_r")
            tp_eol = st.selectbox("Tipo de Turbina", ["Eixo Horizontal", "Eixo Vertical"], key="t1_eol_t")
        if st.button("Calcular Projeto", key="btn_auto_eolico"):
            cp = 0.40 if tp_eol == "Eixo Horizontal" else 0.25
            pot = 0.5 * 1.225 * (math.pi * raio_eol**2) * (vento_eol**3) * cp
            st.markdown("---")
            st.markdown("### 🛒 Lista de Compras Final")
            col_res1, col_res2 = st.columns(2)
            col_res1.metric("Turbina Eólica", f"{pot/1000:.1f} kW")
            col_res2.metric("Inversor", f"{(carga_eol*1.25)/1000:.1f} kW")

    elif tipo_sistema_guia == "Energia Hídrica":
        col1, col2 = st.columns(2)
        with col1:
            vazao_hid = st.number_input("Vazão (m³/s)", value=10.0, key="t1_hid_q")
            queda_hid = st.number_input("Queda (m)", value=20.0, key="t1_hid_h")
        with col2:
            tp_hid = st.selectbox("Tipo de Turbina", ["Pelton", "Francis", "Kaplan"], key="t1_hid_t")
        if st.button("Calcular Projeto", key="btn_auto_hidrico"):
            ef = 0.90 if tp_hid == "Pelton" else (0.92 if tp_hid == "Francis" else 0.94)
            pot = 1000 * 9.81 * vazao_hid * queda_hid * ef
            st.markdown("---")
            st.markdown("### 🛒 Resultado Final")
            st.metric("Potência da Turbina Hídrica", f"{pot/1000:.1f} kW")

    elif tipo_sistema_guia == "Energia Térmica":
        col1, col2 = st.columns(2)
        with col1:
            vol_term = st.number_input("Volume Água (L/dia)", value=200, key="t1_term_v")
            dt_term = st.number_input("Aumento Temp (°C)", value=40, key="t1_term_dt")
        with col2:
            tp_term = st.selectbox("Tipo de Coletor", ["Plano", "Tubo a Vácuo"], key="t1_term_t")
        if st.button("Calcular Projeto", key="btn_auto_termico"):
            ef = 0.6 if tp_term == "Plano" else 0.75
            area = ((vol_term * 1.16 * dt_term) / 1000) / (5.5 * ef)
            st.markdown("---")
            st.markdown("### 🛒 Resultado Final")
            st.metric("Área de Coletores Solares", f"{area:.1f} m²")

    elif tipo_sistema_guia == "Biomassa":
        col1, col2 = st.columns(2)
        with col1:
            massa_bio = st.number_input("Massa Resíduo (kg/dia)", value=1000.0, key="t1_bio_m")
            poder_bio = st.number_input("Poder Calorífico (MJ/kg)", value=15.0, key="t1_bio_p")
        with col2:
            tp_bio = st.selectbox("Tipo de Processo", ["Combustão Direta", "Gaseificação", "Biodigestor"], key="t1_bio_t")
        if st.button("Calcular Projeto", key="btn_auto_bio"):
            ef = 0.25 if tp_bio == "Combustão Direta" else (0.35 if tp_bio == "Gaseificação" else 0.65)
            pot = ((massa_bio * poder_bio * ef) / 3.6) / 24
            st.markdown("---")
            st.markdown("### 🛒 Resultado Final")
            st.metric("Potência Contínua Gerada", f"{pot:.1f} kW")

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
    st.subheader("☀️ Dimensionamento Solar Fotovoltaico (Manual)")
    col1, col2 = st.columns(2)
    with col1:
        c_sol = st.number_input("Consumo (kWh)", value=300.0, key="t3_c")
        i_sol = st.number_input("Irradiação (kWh/m²/dia)", value=5.5, key="t3_i")
        s_sol = st.slider("Sombreamento (%)", 0, 50, 10, key="t3_s")
    with col2:
        tp_sol = st.selectbox("Tipo de Painel", ["Monocristalino", "Policristalino", "Filme Fino"], key="t3_tp")
        pp_sol = st.number_input("Potência Painel (W)", value=550, key="t3_pp")
        a_sol = st.number_input("Área Painel (m²)", value=2.6, key="t3_a")
    
    pr_sol = 0.8 * (1 - s_sol/100)
    kwp_sol = (c_sol/30) / (i_sol * pr_sol)
    num_sol = math.ceil((kwp_sol*1000)/pp_sol)
    st.metric("Potência Necessária", f"{kwp_sol:.2f} kWp")
    st.metric("Painéis Necessários", f"{num_sol} un. (Área total: {num_sol*a_sol:.1f} m²)")

# ==========================================
# ABA 4: TÉRMICA MANUAL
# ==========================================
with tab4:
    st.subheader("🌡️ Energia Térmica (Manual)")
    col1, col2 = st.columns(2)
    with col1:
        v_term = st.number_input("Volume Água (L/dia)", value=200, key="t4_v")
        dt_term = st.number_input("Aumento Temp (°C)", value=40, key="t4_dt")
    with col2:
        tp_term_m = st.selectbox("Tipo de Coletor (Manual)", ["Plano", "Tubo a Vácuo"], key="t4_tp")
    
    ef_term = 0.6 if tp_term_m == "Plano" else 0.75
    e_term = (v_term * 1.16 * dt_term) / 1000
    area_term = e_term / (5.5 * ef_term)
    st.metric("Área de Coletores", f"{area_term:.1f} m²")

# ==========================================
# ABA 5: EÓLICA MANUAL
# ==========================================
with tab5:
    st.subheader("🌬️ Energia Eólica (Manual)")
    v_eol_m = st.number_input("Vento (m/s)", value=6.0, key="t5_v")
    r_eol_m = st.number_input("Raio Pás (m)", value=2.0, key="t5_r")
    tp_eol_m = st.selectbox("Tipo de Turbina (Manual)", ["Eixo Horizontal", "Eixo Vertical"], key="t5_tp")
    cp_eol_m = 0.40 if tp_eol_m == "Eixo Horizontal" else 0.25
    p_eol_m = 0.5 * 1.225 * (math.pi * r_eol_m**2) * (v_eol_m**3) * cp_eol_m
    st.metric("Potência Gerada", f"{p_eol_m:.0f} W")

# ==========================================
# ABA 6: HÍDRICA MANUAL
# ==========================================
with tab6:
    st.subheader("💧 Energia Hídrica (Manual)")
    q_hid_m = st.number_input("Vazão (m³/s)", value=10.0, key="t6_q")
    h_hid_m = st.number_input("Queda (m)", value=20.0, key="t6_h")
    tp_hid_m = st.selectbox("Tipo de Turbina (Manual)", ["Pelton", "Francis", "Kaplan"], key="t6_tp")
    
    ef_hid_m = 0.90 if tp_hid_m == "Pelton" else (0.92 if tp_hid_m == "Francis" else 0.94)
    p_hid_m = 1000 * 9.81 * q_hid_m * h_hid_m * ef_hid_m
    st.metric("Potência Gerada", f"{(p_hid_m/1000):.1f} kW")

# ==========================================
# ABA 7: BIOMASSA MANUAL
# ==========================================
with tab7:
    st.subheader("🌱 Biomassa (Manual)")
    m_bio_m = st.number_input("Massa Resíduo (kg/dia)", value=1000.0, key="t7_m")
    p_bio_m = st.number_input("Poder Calorífico (MJ/kg)", value=15.0, key="t7_p")
    tp_bio_m = st.selectbox("Tipo de Processo (Manual)", ["Combustão Direta", "Gaseificação", "Biodigestor"], key="t7_tp")
    
    ef_bio_m = 0.25 if tp_bio_m == "Combustão Direta" else (0.35 if tp_bio_m == "Gaseificação" else 0.65)
    p_bio_kw = ((m_bio_m * p_bio_m * ef_bio_m) / 3.6) / 24
    st.metric("Potência Contínua", f"{p_bio_kw:.1f} kW")

# ==========================================
# ABA 8: ELETROTÉCNICA (Com Corrente Contínua e Alternada + Frequência)
# ==========================================
with tab8:
    st.subheader("⚡ Eletrotécnica (Lei de Ohm e Resistência)")
    
    tipo_corrente = st.selectbox("Tipo de Corrente", ["Corrente Contínua (DC - Painéis/Baterias)", "Corrente Alternada Monofásica (AC - 220V)", "Corrente Alternada Trifásica (AC - 380V)"], key="t8_tipo_c")
    frequencia = st.selectbox("Frequência da Rede", ["50 Hz (Angola / Europa)", "60 Hz (Brasil / EUA)"], key="t8_freq")
    
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.markdown("**Dados do Circuito**")
        p_ele = st.number_input("Potência do Equipamento (W)", value=1000.0, key="t8_p")
        v_ele = st.number_input("Tensão do Sistema (V)", value=220.0, key="t8_v")
        d_ele = st.number_input("Distância do Cabo (m)", value=20.0, key="t8_d")
        mat_ele = st.selectbox("Material do Cabo", ["Cobre", "Alumínio"], key="t8_mat")
        
    with col_e2:
        st.markdown("**Resultados da Lei de Ohm**")
        if "Trifásica" in tipo_corrente:
            i_ele = p_ele / (math.sqrt(3) * v_ele * 0.8)
        else:
            i_ele = p_ele / v_ele
            
        st.metric("Corrente Elétrica (I)", f"{i_ele:.2f} A")
        r_carga = v_ele / i_ele if i_ele > 0 else 0
        st.metric("Resistência da Carga (R)", f"{r_carga:.2f} Ω")

    st.divider()
    st.markdown("### Dimensionamento do Cabo e Queda de Tensão")
    resistividade = 0.0172 if mat_ele == "Cobre" else 0.0282
    
    if "Trifásica" in tipo_corrente:
        area_ele = (math.sqrt(3) * resistividade * d_ele * i_ele) / (v_ele * 0.03)
    else:
        area_ele = (2 * resistividade * d_ele * i_ele) / (v_ele * 0.03)
        
    r_cabo = (2 * resistividade * d_ele) / area_ele if area_ele > 0 else 0
    
    c_res1, c_res2 = st.columns(2)
    c_res1.metric(f"Cabo Mínimo ({mat_ele})", f"{area_ele:.2f} mm²")
    c_res2.metric("Resistência do Cabo", f"{r_cabo:.3f} Ω")
    
    st.info(f"💡 **Nota Técnica:** Cálculo efetuado para **{tipo_corrente}** a **{frequencia}**. A resistência do cabo de {area_ele:.1f}mm² ao longo de {d_ele}m é de {r_cabo:.3f} Ω (Queda de Tensão máx 3%).")

# ==========================================
# ABA 9: BATERIAS MANUAL
# ==========================================
with tab9:
    st.subheader("🔋 Baterias (Manual)")
    c_bat = st.number_input("Consumo (kWh)", value=300.0, key="t9_c")
    t_bat = st.selectbox("Tipo de Bateria", ["Lítio", "Chumbo-Ácido"], key="t9_t")
    v_bat = st.selectbox("Tensão (V)", [12, 24, 48], index=2, key="t9_v")
    cap_bat = st.number_input("Capacidade (Ah)", value=200, key="t9_cap")
    d_bat = st.number_input("Dias Autonomia", 1, 5, 1, key="t9_d")
    dod_bat = 0.9 if t_bat == "Lítio" else 0.5
    num_bat = math.ceil(((c_bat/30*1000*d_bat)/(v_bat*dod_bat))/cap_bat)
    st.metric("Baterias Necessárias", f"{num_bat} un.")

# ==========================================
# ABA 10: INVERSORES
# ==========================================
with tab10:
    st.subheader("🔌 Inversores (Manual)")
    carga_inv = st.number_input("Carga Contínua (W)", value=2000.0, key="t10_c")
    tp_inv = st.selectbox("Tipo de Inversor", ["Híbrido", "Off-Grid", "On-Grid"], key="t10_tp")
    mot_inv = st.selectbox("Tem motores?", ["Sim", "Não"], key="t10_m")
    p_inv = carga_inv * (3.0 if mot_inv == "Sim" else 1.25)
    st.metric(f"Potência do Inversor ({tp_inv})", f"{p_inv:.0f} W")

# ==========================================
# ABA 11: GERADORES
# ==========================================
with tab11:
    st.subheader("⚙️ Geradores (Manual)")
    p_ger = st.number_input("Carga Pico (kW)", value=5.0, key="t11_p")
    tp_ger = st.selectbox("Tipo de Gerador", ["Diesel / Gasóleo", "Gasolina", "Gás Natural / Biogás"], key="t11_tp")
    tensao_ger = st.selectbox("Tensão do Gerador", ["Monofásico (220V)", "Trifásico (380V)"], key="t11_tensao")
    fp_ger = st.number_input("Fator Potência", value=0.8, key="t11_fp")
    kva_ger = (p_ger * 1.25) / fp_ger
    st.metric("Gerador Necessário", f"{kva_ger:.1f} kVA")
    st.info(f"💡 Nota: Para um gerador **{tp_ger}** do tipo **{tensao_ger}**, certifique-se de que o quadro elétrico tem as devidas proteções diferenciais.")

# ==========================================
# ABA 12: MANUTENÇÃO
# ==========================================
with tab12:
    st.subheader("🛠️ Gestão de Manutenção Sincronizada")
    sist_man = st.selectbox("Sistema Alvo", ["Solar Fotovoltaico", "Térmico", "Eólico", "Hídrico", "Biomassa", "Gerador"], key="t12_s")
    
    if sist_man == "Solar Fotovoltaico":
        tp_man = st.selectbox("Tecnologia do Painel", ["Monocristalino", "Policristalino", "Filme Fino"], key="t12_tp")
        if tp_man == "Monocristalino": st.info("💡 **Dica:** Verifique conectores MC4 para evitar 'Hot Spots'.")
        st.checkbox("Limpeza dos painéis", key="chk_s1")
        st.checkbox("Verificação de cabos", key="chk_s2")
    elif sist_man == "Térmico":
        tp_man_t = st.selectbox("Tipo de Coletor", ["Plano", "Tubo a Vácuo"], key="t12_term_tp")
        if tp_man_t == "Plano": st.info("💡 **Dica:** Verifique o isolamento térmico da caixa.")
        st.checkbox("Limpeza dos vidros", key="chk_t1")
        st.checkbox("Verificação de fugas", key="chk_t2")
    elif sist_man == "Eólico":
        tp_man_e = st.selectbox("Tipo de Turbina", ["Eixo Horizontal", "Eixo Vertical"], key="t12_eol_tp")
        if tp_man_e == "Eixo Horizontal": st.info("💡 **Dica:** Verifique o sistema de orientação.")
        st.checkbox("Lubrificação", key="chk_e1")
        st.checkbox("Inspeção das pás", key="chk_e2")
    elif sist_man == "Hídrico":
        tp_man_h = st.selectbox("Tipo de Turbina", ["Pelton", "Francis", "Kaplan"], key="t12_hid_tp")
        if tp_man_h == "Pelton": st.info("💡 **Dica:** Verifique desgaste das pás.")
        st.checkbox("Limpeza das grades", key="chk_h1")
        st.checkbox("Fugas de óleo", key="chk_h2")
    elif sist_man == "Biomassa":
        tp_man_b = st.selectbox("Tipo de Processo", ["Combustão Direta", "Gaseificação", "Biodigestor"], key="t12_bio_tp")
        if tp_man_b == "Combustão Direta": st.info("💡 **Dica:** Limpeza da fuligem.")
        st.checkbox("Limpeza geral", key="chk_b1")
    elif sist_man == "Gerador":
        tp_man_g = st.selectbox("Tipo de Gerador", ["Diesel", "Gasolina", "Gás"], key="t12_ger_tp")
        if tp_man_g == "Diesel": st.info("💡 **Dica:** Drene a água do filtro.")
        st.checkbox("Verificar óleo", key="chk_g1")
        st.checkbox("Filtro de ar", key="chk_g2")

# ==========================================
# ABA 13: PROJETO EXECUTIVO (Com Resistência em TODAS as Fontes)
# ==========================================
with tab13:
    st.subheader("🔧 Projeto Executivo e Detalhamento de Campo")
    tipo_exec = st.selectbox("Selecione o Sistema", ["Solar Fotovoltaico", "Eólico", "Hídrico", "Térmico", "Biomassa"], key="t13_t")

    if tipo_exec == "Solar Fotovoltaico":
        tp_painel_exec = st.selectbox("Tipo de Painel", ["Monocristalino", "Policristalino", "Filme Fino"], key="t13_tp")
        voc = st.number_input("Voc do Painel (V)", value=49.5, key="t13_voc")
        vmax = st.number_input("Tensão Max Inv (V)", value=500, key="t13_vmax")
        max_serie = math.floor(vmax / voc)
        st.success(f"**String:** Máximo de {max_serie} painéis em série (Painel {tp_painel_exec}).")
        st.info("**Cabo DC:** Utilize cabo solar de 6 mm².")
        st.warning("**Proteções:** Disjuntor DC e AC, DPS.")
        st.error("**Obrigatório (Segurança):** Instalação de Haste de Terra com resistência máxima de **10 Ω** para proteção contra descargas atmosféricas.")

    elif tipo_exec == "Térmico":
        tp_col_exec = st.selectbox("Tipo de Coletor", ["Plano", "Tubo a Vácuo"], key="t13_term_tp")
        area_col = st.number_input("Área Total de Coletores (m²)", value=4.0, key="t13_term_area")
        dist_term = st.number_input("Distância até ao Depósito (m)", value=10.0, key="t13_term_dist")
        
        tubo = "22mm" if dist_term <= 15 else "28mm"
        vaso = 18 if area_col <= 5 else 24
        
        st.success(f"**Tubagem:** Tubo de cobre de {tubo} para o circuito primário (glicol).")
        st.info(f"**Vaso de Expansão:** Recomendado vaso de {vaso} Litros para {area_col} m².")
        st.warning(f"**Proteções:** Válvula de segurança de 6 bar, purgador de ar automático. (Para coletor {tp_col_exec}).")
        st.error("**Obrigatório (Segurança):** Caso o sistema tenha bombas de circulação elétricas, estas devem ter ligação à Haste de Terra com resistência máxima de **10 Ω**.")

    elif tipo_exec == "Eólico":
        tp_turb_exec = st.selectbox("Tipo de Turbina", ["Eixo Horizontal", "Eixo Vertical"], key="t13_eol_tp")
        pot_eol_exec = st.number_input("Potência da Turbina (kW)", value=2.0, key="t13_eol_pot")
        v_eol_exec = st.number_input("Tensão do Sistema (V)", value=48.0, key="t13_eol_v")
        dist_eol_exec = st.number_input("Distância Turbina-Inversor (m)", value=30.0, key="t13_eol_dist")
        
        corrente_eol = (pot_eol_exec * 1000) / v_eol_exec
        area_cabo_eol = (2 * 0.0172 * dist_eol_exec * corrente_eol) / (v_eol_exec * 0.03)
        
        st.success(f"**Cabo DC:** Cabo de {math.ceil(area_cabo_eol)} mm² com proteção UV (solar).")
        st.warning(f"**Proteções:** Controlador de carga (Dumpload) obrigatório. Para turbina {tp_turb_exec}, utilize DPS DC.")
        st.error("**Obrigatório (Segurança):** Instalação de Haste de Terra na torre da turbina e no quadro elétrico com resistência máxima de **10 Ω**.")

    elif tipo_exec == "Hídrico":
        tp_hid_exec = st.selectbox("Tipo de Turbina", ["Pelton", "Francis", "Kaplan"], key="t13_hid_tp")
        pot_hid_exec = st.number_input("Potência do Gerador (kW)", value=10.0, key="t13_hid_pot")
        v_hid_exec = st.number_input("Tensão de Saída AC (V)", value=380.0, key="t13_hid_v")
        dist_hid_exec = st.number_input("Distância até ao Quadro (m)", value=50.0, key="t13_hid_dist")
        
        corrente_hid = (pot_hid_exec * 1000) / (math.sqrt(3) * v_hid_exec * 0.8)
        area_cabo_hid = (math.sqrt(3) * 0.0172 * dist_hid_exec * corrente_hid) / (v_hid_exec * 0.03)
        
        st.success(f"**Cabo AC:** Cabo trifásico de {math.ceil(area_cabo_hid)} mm².")
        st.warning(f"**Proteções:** Disjuntor tripolar, DPS, regulador AVR. (Turbina {tp_hid_exec}).")
        st.error("**Obrigatório (Segurança):** Instalação de Haste de Terra para o gerador e quadro elétrico com resistência máxima de **10 Ω**.")

    elif tipo_exec == "Biomassa":
        tp_bio_exec = st.selectbox("Tipo de Processo", ["Combustão Direta", "Gaseificação", "Biodigestor"], key="t13_bio_tp")
        pot_bio_exec = st.number_input("Potência do Gerador (kW)", value=5.0, key="t13_bio_pot")
        dist_bio_exec = st.number_input("Distância até ao Motor/Gerador (m)", value=15.0, key="t13_bio_dist")
        
        if "Biodigestor" in tp_bio_exec:
            st.success(f"**Tubagem:** Tubo PEAD ou Inox de 50mm para o biogás, com distância de {dist_bio_exec}m.")
            st.warning(f"**Proteções:** Válvula corta-fogo, filtro de H2S (ácido sulfídrico) e purga de condensado.")
        else:
            st.success(f"**Tubagem:** Sistema de alimentação mecânica para resíduos sólidos.")
            st.warning(f"**Proteções:** Válvula de alívio de pressão na caldeira/gaseificador e sistema de exaustão de gases.")
        st.error("**Obrigatório (Segurança):** Ligação à terra de todas as massas metálicas (motor, caldeira, tubagens) com resistência máxima de **10 Ω** e proteção contra eletricidade estática.")

# ==========================================
# ABA 14: NEGÓCIO
# ==========================================
with tab14:
    st.subheader("💼 Meu Negócio (Simulador)")
    st.metric("Faturamento Estimado (Ano 1)", "$ 3.000,00 (Base de 5 empresas)")

# --- BARRA LATERAL ---
st.sidebar.title("EcoRenováveis Pro")
st.sidebar.info(
    "Desenvolvido por **Adão Cassessa**.\n\n"
    "Técnico em Energias Renováveis e Desenvolvedor Python.\n\n"
    "Contacto: +244 946 419 656"
)
st.sidebar.caption("© 2026 EcoRenováveis. Todos os direitos reservados.")
