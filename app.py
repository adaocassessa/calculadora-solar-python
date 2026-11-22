import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="EcoRenováveis Pro - Engenharia Global", page_icon="🌍", layout="wide")

st.title("🌍 EcoRenováveis Pro: Engenharia Global")
st.write("Plataforma completa: Renováveis, Elétrica, Civil, Estradas, Indústria e Mobilidade.")

# Criando as 23 abas (TODAS FUNCIONAIS)
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16, tab17, tab18, tab19, tab20, tab21, tab22, tab23 = st.tabs([
    "🌟 Guia Automático", "📍 Mapa", "☀️ Solar", "🌡️ Térmica", "🌬️ Eólica", "💧 Hídrica", 
    "🚰 Bombeamento", "🌱 Biomassa", "⚡ Eletrotécnica", "🚗 Mobilidade EV", "🤖 Automação", 
    "🏗️ Eng. Civil", "🛣️ Estradas", "💡 Iluminação", "🏭 Indústria", "⚙️ Mecânica", 
    "🔋 Baterias", "🔌 Inversores", "⚙️ Geradores", "🛠️ Manutenção", "📚 Guia Técnico", 
    "🔧 Executivo", "💼 Negócio"
])

if 'latitude' not in st.session_state: st.session_state.latitude = -8.8390
if 'longitude' not in st.session_state: st.session_state.longitude = 13.2894

# ==========================================
# ABA 1: GUIA AUTOMÁTICO (Todos os Sistemas Preenchidos)
# ==========================================
with tab1:
    st.subheader("🌟 Assistente de Criação de Projeto (Tudo-em-Um)")
    tipo_sistema_guia = st.selectbox("Selecione o Tipo de Sistema", [
        "Solar Fotovoltaico", "Energia Térmica", "Energia Eólica", "Energia Hídrica", 
        "Bombeamento Solar", "Biomassa", "Eletrotécnica", "Mobilidade Elétrica", 
        "Automação", "Engenharia Civil", "Estradas", "Iluminação Pública", "Indústria"
    ], key="t1_tipo")
    
    if tipo_sistema_guia == "Solar Fotovoltaico":
        c = st.number_input("Consumo (kWh)", value=300.0, key="t1_c")
        i = st.number_input("Irradiação", value=5.5, key="t1_i")
        if st.button("Calcular Solar", key="btn_auto_solar"):
            st.metric("Painéis Necessários (550W)", f"{math.ceil(((c/30)/(i*0.8)*1000)/550)} un.")
    elif tipo_sistema_guia == "Energia Térmica":
        v = st.number_input("Volume Água (L/dia)", value=200, key="t1_term_v")
        if st.button("Calcular Térmica", key="btn_auto_term"):
            st.metric("Área de Coletores", f"{((v * 1.16 * 40) / 1000) / (5.5 * 0.6):.1f} m²")
    elif tipo_sistema_guia == "Energia Eólica":
        vento = st.number_input("Vento (m/s)", value=6.0, key="t1_eol_v")
        if st.button("Calcular Eólica", key="btn_auto_eol"):
            st.metric("Potência Estimada (Raio 2m)", f"{0.5 * 1.225 * (math.pi * 2**2) * (vento**3) * 0.40:.0f} W")
    elif tipo_sistema_guia == "Energia Hídrica":
        q = st.number_input("Vazão (m³/s)", value=10.0, key="t1_hid_q")
        h = st.number_input("Queda (m)", value=20.0, key="t1_hid_h")
        if st.button("Calcular Hídrica", key="btn_auto_hid"):
            st.metric("Potência Gerada", f"{(1000 * 9.81 * q * h * 0.9)/1000:.1f} kW")
    elif tipo_sistema_guia == "Bombeamento Solar":
        prof = st.number_input("Profundidade (m)", value=50.0, key="t1_b_p")
        alt = st.number_input("Altura (m)", value=10.0, key="t1_b_a")
        if st.button("Calcular Bombeamento", key="btn_auto_bomb"):
            st.metric("HMT", f"{(prof + alt) * 1.1:.1f} m")
    elif tipo_sistema_guia == "Biomassa":
        m = st.number_input("Massa Resíduo (kg/dia)", value=1000.0, key="t1_bio_m")
        if st.button("Calcular Biomassa", key="btn_auto_bio"):
            st.metric("Potência Contínua", f"{((m * 15 * 0.25) / 3.6) / 24:.1f} kW")
    elif tipo_sistema_guia == "Eletrotécnica":
        p = st.number_input("Potência (W)", value=1000.0, key="t1_ele_p")
        v = st.number_input("Tensão (V)", value=220.0, key="t1_ele_v")
        if st.button("Calcular Elétrica", key="btn_auto_ele"):
            st.metric("Corrente", f"{(p/v):.2f} A")
    elif tipo_sistema_guia == "Mobilidade Elétrica":
        n = st.number_input("Nº Carregadores", value=5, key="t1_ev_n")
        pot = st.number_input("Potência (kW)", value=22.0, key="t1_ev_p")
        if st.button("Calcular EV", key="btn_auto_ev"):
            st.metric("Potência Total", f"{n * pot:.1f} kW")
    elif tipo_sistema_guia == "Automação":
        p_robo = st.number_input("Potência (W)", value=500.0, key="t1_auto_p")
        h_robo = st.number_input("Horas", value=8.0, key="t1_auto_h")
        if st.button("Calcular Automação", key="btn_auto_aut"):
            st.metric("Consumo Diário", f"{(p_robo * h_robo)/1000:.1f} kWh")
    elif tipo_sistema_guia == "Engenharia Civil":
        comp = st.number_input("Comprimento (m)", value=5.0, key="t1_civ_c")
        larg = st.number_input("Largura (m)", value=4.0, key="t1_civ_l")
        alt = st.number_input("Altura (m)", value=0.15, key="t1_civ_a")
        if st.button("Calcular Betão", key="btn_auto_civ"):
            st.metric("Volume Betão", f"{comp * larg * alt:.2f} m³")
    elif tipo_sistema_guia == "Estradas":
        km = st.number_input("Comprimento (km)", value=1.0, key="t1_est_km")
        larg = st.number_input("Largura (m)", value=7.0, key="t1_est_l")
        if st.button("Calcular Estrada", key="btn_auto_est"):
            st.metric("Volume Asfalto", f"{(km * 1000 * larg * 0.05):,.0f} m³")
    elif tipo_sistema_guia == "Iluminação Pública":
        comp = st.number_input("Comprimento (m)", value=1000, key="t1_ilu_c")
        esp = st.number_input("Espaçamento (m)", value=30, key="t1_ilu_e")
        if st.button("Calcular Iluminação", key="btn_auto_ilu"):
            st.metric("Nº de Postes", f"{math.ceil(comp / esp) + 1} un.")
    elif tipo_sistema_guia == "Indústria":
        prod = st.number_input("Produção Diária", value=10, key="t1_ind_p")
        en = st.number_input("Energia/Unidade (kWh)", value=150.0, key="t1_ind_e")
        if st.button("Calcular Indústria", key="btn_auto_ind"):
            st.metric("Consumo Diário", f"{(prod * en):,} kWh")

# ==========================================
# ABA 2: MAPA
# ==========================================
with tab2:
    st.subheader("📍 Geolocalização do Projeto")
    lat = st.number_input("Latitude", value=st.session_state.latitude, key="t2_lat")
    lon = st.number_input("Longitude", value=st.session_state.longitude, key="t2_lon")
    st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}), zoom=12)

# ==========================================
# ABAS 3 a 15: CÁLCULOS MANUAIS COM TIPOS
# ==========================================
with tab3:
    st.subheader("☀️ Solar")
    tp = st.selectbox("Tipo de Painel", ["Monocristalino", "Policristalino"], key="t3_tp")
    c = st.number_input("Consumo (kWh)", value=300.0, key="t3_c")
    st.metric("Painéis", f"{math.ceil(((c/30)/(5.5*0.8)*1000)/550)} un.")

with tab4:
    st.subheader("🌡️ Térmica")
    tp = st.selectbox("Tipo de Coletor", ["Plano", "Tubo a Vácuo"], key="t4_tp")
    v = st.number_input("Volume Água (L/dia)", value=200, key="t4_v")
    st.metric("Área Coletores", f"{((v * 1.16 * 40) / 1000) / (5.5 * (0.6 if tp=='Plano' else 0.75)):.1f} m²")

with tab5:
    st.subheader("🌬️ Eólica")
    tp = st.selectbox("Tipo de Turbina", ["Eixo Horizontal", "Eixo Vertical"], key="t5_tp")
    v = st.number_input("Vento (m/s)", value=6.0, key="t5_v")
    st.metric("Potência", f"{0.5 * 1.225 * (math.pi * 2**2) * (v**3) * (0.40 if tp=='Eixo Horizontal' else 0.25):.0f} W")

with tab6:
    st.subheader("💧 Hídrica")
    tp = st.selectbox("Tipo de Turbina", ["Pelton", "Francis", "Kaplan"], key="t6_tp")
    q = st.number_input("Vazão (m³/s)", value=10.0, key="t6_q")
    h = st.number_input("Queda (m)", value=20.0, key="t6_h")
    ef = 0.90 if tp == "Pelton" else (0.92 if tp == "Francis" else 0.94)
    st.metric("Potência", f"{(1000 * 9.81 * q * h * ef)/1000:.1f} kW")

with tab7:
    st.subheader("🚰 Bombeamento")
    prof = st.number_input("Profundidade (m)", value=50.0, key="t7_p")
    st.metric("HMT", f"{(prof + 10) * 1.1:.1f} m")

with tab8:
    st.subheader("🌱 Biomassa")
    tp = st.selectbox("Tipo", ["Combustão", "Gaseificação", "Biodigestor"], key="t8_tp")
    m = st.number_input("Massa (kg/dia)", value=1000.0, key="t8_m")
    st.metric("Potência", f"{((m * 15 * (0.25 if tp=='Combustão' else (0.35 if tp=='Gaseificação' else 0.65))) / 3.6) / 24:.1f} kW")

with tab9:
    st.subheader("⚡ Eletrotécnica")
    tp = st.selectbox("Tipo de Instalação", ["Monofásico", "Bifásico", "Trifásico"], key="t9_tp")
    p = st.number_input("Potência (W)", value=1000.0, key="t9_p")
    v = st.number_input("Tensão (V)", value=220.0, key="t9_v")
    i = p / (math.sqrt(3) * v * 0.8) if tp == "Trifásico" else (p / v)
    st.metric("Corrente", f"{i:.2f} A")

with tab10:
    st.subheader("🚗 Mobilidade EV")
    n = st.number_input("Nº Carregadores", value=5, key="t10_n")
    st.metric("Potência Total", f"{n * 22:.1f} kW")

with tab11:
    st.subheader("🤖 Automação")
    p = st.number_input("Potência Robô (W)", value=1500.0, key="t11_p")
    h = st.number_input("Horas", value=16.0, key="t11_h")
    st.metric("Consumo Diário", f"{(p * h)/1000:.1f} kWh")

with tab12:
    st.subheader("🏗️ Eng. Civil")
    comp = st.number_input("Comprimento (m)", value=5.0, key="t12_c")
    larg = st.number_input("Largura (m)", value=4.0, key="t12_l")
    alt = st.number_input("Altura (m)", value=0.15, key="t12_a")
    st.metric("Volume Betão", f"{comp * larg * alt:.2f} m³")

with tab13:
    st.subheader("🛣️ Estradas")
    km = st.number_input("Comprimento (km)", value=1.0, key="t13_km")
    st.metric("Volume Asfalto", f"{(km * 1000 * 7 * 0.05):,.0f} m³")

with tab14:
    st.subheader("💡 Iluminação")
    comp = st.number_input("Comprimento (m)", value=1000, key="t14_c")
    st.metric("Nº Postes", f"{math.ceil(comp / 30) + 1} un.")

with tab15:
    st.subheader("🏭 Indústria")
    prod = st.number_input("Produção Diária", value=10, key="t15_p")
    st.metric("Consumo Diário", f"{(prod * 150):,} kWh")

# ==========================================
# ABA 16: MECÂNICA (Com Tipos)
# ==========================================
with tab16:
    st.subheader("⚙️ Mecânica (Manual)")
    tp_mec = st.selectbox("Tipo de Transmissão", ["Correia/Polia", "Engrenagem", "Direto (Eixo)"], key="t16_tp")
    pot_mec = st.number_input("Potência Motor (kW)", value=10.0, key="t16_mec")
    rpm = st.number_input("Rotação (RPM)", value=1500.0, key="t16_rpm")
    torque = (pot_mec * 1000) / ((rpm * 2 * math.pi) / 60)
    st.metric("Torque", f"{torque:.1f} N.m")
    if tp_mec == "Correia/Polia":
        st.info("💡 Recomenda-se verificar a tensão da correia e alinhamento das polias.")
    elif tp_mec == "Engrenagem":
        st.info("💡 Recomenda-se lubrificação constante da caixa de engrenagens.")

# ==========================================
# ABA 17: BATERIAS (Com Tipos)
# ==========================================
with tab17:
    st.subheader("🔋 Baterias (Manual)")
    tp_bat = st.selectbox("Tipo de Bateria", ["Lítio", "Chumbo-Ácido"], key="t17_tp")
    c_bat = st.number_input("Consumo (kWh)", value=300.0, key="t17_c")
    dod = 0.9 if tp_bat == "Lítio" else 0.5
    st.metric("Baterias de 200Ah", f"{math.ceil(((c_bat/30*1000)/(48*dod))/200)} un.")

# ==========================================
# ABA 18: INVERSORES (Com Tipos)
# ==========================================
with tab18:
    st.subheader("🔌 Inversores (Manual)")
    tp_inv = st.selectbox("Tipo de Inversor", ["Híbrido", "Off-Grid", "On-Grid"], key="t18_tp")
    carga = st.number_input("Carga (W)", value=2000.0, key="t18_c")
    st.metric("Inversor", f"{carga * 1.25:.0f} W")

# ==========================================
# ABA 19: GERADORES (Com Tipos)
# ==========================================
with tab19:
    st.subheader("⚙️ Geradores (Manual)")
    tp_ger = st.selectbox("Tipo de Gerador", ["Diesel", "Gasolina", "Gás"], key="t19_tp")
    p_ger = st.number_input("Carga Pico (kW)", value=5.0, key="t19_p")
    st.metric("Gerador", f"{(p_ger * 1.25) / 0.8:.1f} kVA")

# ==========================================
# ABA 20: MANUTENÇÃO (Com TODOS os Sistemas)
# ==========================================
with tab20:
    st.subheader("🛠️ Gestão de Manutenção Sincronizada")
    sist_man = st.selectbox("Selecione o Sistema Alvo", [
        "Solar Fotovoltaico", "Térmica", "Eólica", "Hídrica", "Bombeamento", "Biomassa", 
        "Eletrotécnica", "Mobilidade EV", "Automação", "Engenharia Civil", "Estradas", 
        "Iluminação", "Indústria", "Mecânica", "Baterias", "Inversores", "Geradores"
    ], key="t20_s")
    
    st.markdown(f"### 📋 Checklist: {sist_man}")
    if sist_man == "Solar Fotovoltaico":
        st.checkbox("Limpeza dos painéis (remoção de pó e areia)", key="m_sol1")
        st.checkbox("Verificação de conectores MC4", key="m_sol2")
    elif sist_man == "Térmica":
        st.checkbox("Limpeza dos vidros dos coletores", key="m_term1")
        st.checkbox("Verificação de fugas no circuito de glicol", key="m_term2")
    elif sist_man == "Eólica":
        st.checkbox("Lubrificação do multiplicador", key="m_eol1")
        st.checkbox("Inspeção visual das pás", key="m_eol2")
    elif sist_man == "Hídrica":
        st.checkbox("Limpeza das grades de captação", key="m_hid1")
        st.checkbox("Verificação de fugas de óleo", key="m_hid2")
    elif sist_man == "Bombeamento":
        st.checkbox("Verificar funcionamento a seco da bomba", key="m_bomb1")
        st.checkbox("Limpeza dos filtros de água", key="m_bomb2")
    elif sist_man == "Biomassa":
        st.checkbox("Limpeza da fuligem na caldeira", key="m_bio1")
    elif sist_man == "Eletrotécnica":
        st.checkbox("Aperto de terminais elétricos", key="m_ele1")
        st.checkbox("Teste de resistência de terra (Haste < 10 Ω)", key="m_ele2")
    elif sist_man == "Mobilidade EV":
        st.checkbox("Verificar cabos de carregamento", key="m_ev1")
    elif sist_man == "Automação":
        st.checkbox("Calibração de sensores", key="m_aut1")
        st.checkbox("Lubrificação de braços robóticos", key="m_aut2")
    elif sist_man == "Engenharia Civil":
        st.checkbox("Inspeção de fissuras no betão", key="m_civ1")
    elif sist_man == "Estradas":
        st.checkbox("Verificação de buracos e fissuras no asfalto", key="m_est1")
    elif sist_man == "Iluminação":
        st.checkbox("Teste de acendimento dos LED", key="m_ilu1")
        st.checkbox("Limpeza dos painéis solares dos postes", key="m_ilu2")
    elif sist_man == "Indústria":
        st.checkbox("Manutenção preventiva das máquinas", key="m_ind1")
    elif sist_man == "Mecânica":
        st.checkbox("Alinhamento de polias/engrenagens", key="m_mec1")
        st.checkbox("Troca de óleo dos rolamentos", key="m_mec2")
    elif sist_man == "Baterias":
        st.checkbox("Verificar tensão de cada bateria", key="m_bat1")
    elif sist_man == "Inversores":
        st.checkbox("Limpeza do dissipador de calor", key="m_inv1")
    elif sist_man == "Geradores":
        st.checkbox("Verificar nível de óleo e água", key="m_ger1")
        st.checkbox("Limpeza do filtro de ar", key="m_ger2")

# ==========================================
# ABA 21: GUIA TÉCNICO (TODAS as Fontes + Governo)
# ==========================================
with tab21:
    st.subheader("📚 Guia Técnico, Boas Práticas e Oportunidades")
    
    with st.expander("☀️ Solar Fotovoltaico"):
        st.write("**Fórmulas:** Potência (kWp) = Consumo Diário / (Irradiação × PR). Evite sombreamento.")
    with st.expander("🌡️ Térmica"):
        st.write("Use tubos a vácuo em climas frios e coletores planos em climas quentes.")
    with st.expander("🌬️ Eólica"):
        st.write("A potência cresce ao cubo da velocidade do vento. Altura mínima de 10m.")
    with st.expander("💧 Hídrica"):
        st.write("Pelton (Alta queda), Francis (Média), Kaplan (Baixa queda).")
    with st.expander("🚰 Bombeamento"):
        st.write("Verifique sempre a HMT (Altura Manométrica Total) para não queimar a bomba.")
    with st.expander("🌱 Biomassa"):
        st.write("Biodigestores requerem temperatura constante e resíduos orgânicos.")
    with st.expander("⚡ Eletrotécnica"):
        st.write("Cabo dimensionado por queda de tensão máx 3%. Haste de terra obrigatória (< 10 Ω).")
    with st.expander("🚗 Mobilidade EV"):
        st.write("Carregadores rápidos (DC) exigem transformadores dedicados.")
    with st.expander("🤖 Automação"):
        st.write("Robôs industriais exigem energia estabilizada e aterramento rigoroso.")
    with st.expander("🏗️ Engenharia Civil"):
        st.write("Estudo de solo é obrigatório. Betão 1:2:3 para alta resistência.")
    with st.expander("🛣️ Estradas"):
        st.write("Base de brita 0.20m, asfalto 0.05m (tráfego leve). Compactação é essencial.")
    with st.expander("💡 Iluminação"):
        st.write("Postes solares devem ter autonomia de 2-3 dias de chuva.")
    with st.expander("🏭 Indústria"):
        st.write("1 carro consome ~1.2t de aço. Fábricas precisam de energia trifásica.")
    with st.expander("⚙️ Mecânica"):
        st.write("Alinhamento de eixos com tolerância máx 0.05mm.")
    with st.expander("🔋 Baterias"):
        st.write("Lítio (DoD 90%) vs Chumbo (DoD 50%).")
    with st.expander("🔌 Inversores"):
        st.write("Fator de segurança de 1.25. Motores exigem pico de 3x.")
    with st.expander("⚙️ Geradores"):
        st.write("Manutenção a cada 250h. Nunca ligue à rede sem ATS.")
    
    st.divider()
    st.markdown("### 🇦🇴 Oportunidades de Investimento em Angola (Governo e Indústria)")
    with st.expander("Reativação de Fábricas (ZEE, Têxteis, Agroindústria)"):
        st.markdown("*   **Textang II:** Energia para máquinas e irrigação para algodão.\n*   **Inducamar (Pneus):** Potência de fornos e solda.\n*   **Sidurex (Aço):** Alta tensão para laminação.")
    with st.expander("Mineração (35 dos 45 minerais)"):
        st.markdown("*   **Lítio e Níquel:** Fábricas de processamento de baterias.\n*   **Diamantes e Ouro:** Energia para minas e refinarias.\n*   **Terras Raras:** Automação de separadores magnéticos.")
    with st.expander("Robótica e Automação"):
        st.markdown("*   **Drones Agrícolas:** Carregamento solar.\n*   **Robótica Médica:** Energia redundante em hospitais.")

# ==========================================
# ABA 22: PROJETO EXECUTIVO (TODOS os Sistemas)
# ==========================================
with tab22:
    st.subheader("🔧 Projeto Executivo e Detalhamento de Campo")
    tipo_exec = st.selectbox("Selecione o Sistema", [
        "Solar Fotovoltaico", "Térmica", "Eólica", "Hídrica", "Bombeamento", "Biomassa", 
        "Eletrotécnica", "Mobilidade EV", "Automação", "Engenharia Civil", "Estradas", 
        "Iluminação", "Indústria", "Mecânica", "Baterias", "Inversores", "Geradores"
    ], key="t22_sel")
    
    st.info(f"📋 **Instruções de Execução para {tipo_exec}:**")
    
    if tipo_exec == "Solar Fotovoltaico":
        st.success("**String:** Máximo de 10 painéis em série. **Cabo DC:** 6mm².")
        st.error("**Segurança:** Haste de Terra (< 10 Ω).")
    elif tipo_exec == "Térmica":
        st.success("**Tubagem:** Cobre 22mm. **Vaso de Expansão:** 18L.")
        st.error("**Segurança:** Válvula de segurança 6 bar.")
    elif tipo_exec == "Eólica":
        st.success("**Cabo DC:** Proteção UV. **Controlador:** Dumpload.")
        st.error("**Segurança:** Haste de terra na torre.")
    elif tipo_exec == "Hídrica":
        st.success("**Cabo AC:** Trifásico 380V. **Regulador:** AVR.")
        st.error("**Segurança:** Haste de terra no gerador.")
    elif tipo_exec == "Bombeamento":
        st.success("**Controlador:** VFD (Variador). **Cabo submersível:** 4mm².")
        st.error("**Segurança:** Proteção contra funcionamento a seco.")
    elif tipo_exec == "Biomassa":
        st.success("**Gás:** Tubo PEAD. **Filtro:** H2S.")
        st.error("**Segurança:** Válvula corta-fogo.")
    elif tipo_exec == "Eletrotécnica":
        st.success("**Quadro:** Disjuntor Geral, DPS, Identificação de circuitos.")
        st.error("**Segurança:** Haste de terra (< 10 Ω).")
    elif tipo_exec == "Mobilidade EV":
        st.success("**Cabos:** Dimensionados para alta corrente. **Transformador:** Dedicado.")
        st.error("**Segurança:** Proteção contra surtos (DPS).")
    elif tipo_exec == "Automação":
        st.success("**Cabos:** Blindados para evitar interferência. **Sensores:** Calibrados.")
        st.error("**Segurança:** Botão de emergência (cogumelo).")
    elif tipo_exec == "Engenharia Civil":
        st.success("**Betão:** Traço 1:2:3. **Cura:** Molhar por 7 dias.")
        st.error("**Segurança:** EPIs obrigatórios (capacete, botas).")
    elif tipo_exec == "Estradas":
        st.success("**Base:** Brita compactada. **Asfalto:** Aplicar entre 140-160°C.")
        st.error("**Segurança:** Sinalização de trânsito na obra.")
    elif tipo_exec == "Iluminação":
        st.success("**Postes:** Espaçamento 30m. **Cabo:** 16mm².")
        st.error("**Segurança:** Disjuntor diferencial no quadro.")
    elif tipo_exec == "Indústria":
        st.success("**Energia:** Trifásico 380V. **Manutenção:** Preventiva mensal.")
        st.error("**Segurança:** Aterramento rigoroso.")
    elif tipo_exec == "Mecânica":
        st.success("**Alinhamento:** Tolerância 0.05mm. **Lubrificação:** Massa grafitada.")
        st.error("**Segurança:** Carenagem de proteção nas correias.")
    elif tipo_exec == "Baterias":
        st.success("**Instalação:** Local ventilado. **Conexão:** Cabos grossos.")
        st.error("**Segurança:** Extintor de incêndio classe C por perto.")
    elif tipo_exec == "Inversores":
        st.success("**Instalação:** Local fresco. **Limpeza:** Dissipador a cada 6 meses.")
        st.error("**Segurança:** Desligar antes de intervir.")
    elif tipo_exec == "Geradores":
        st.success("**Óleo:** Trocar a cada 250h. **Combustível:** Filtrar.")
        st.error("**Segurança:** Chaminé de exaustão para o exterior.")

# ==========================================
# ABA 23: NEGÓCIO
# ==========================================
with tab23:
    st.subheader("💼 Meu Negócio")
    st.metric("Faturamento Estimado (Ano 1)", "$ 3.000,00 (Exemplo base)")
    st.info("💡 **Estratégia Modular:** Venda a plataforma completa ou módulos por setor (Governo, Mineração, Civil).")

# --- BARRA LATERAL ---
st.sidebar.title("EcoRenováveis Pro")
st.sidebar.info(
    "Desenvolvido por **Adão Cassessa**.\n\n"
    "Engenharia Total: Renováveis, Elétrica, Civil, Mecânica, Estradas, Iluminação e Indústria.\n\n"
    "Contacto: +244 946 419 656"
)
st.sidebar.caption("© 2026 EcoRenováveis. Todos os direitos reservados.")
