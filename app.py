import streamlit as st
import math

st.set_page_config(page_title="EcoRenováveis Pro - Global", page_icon="🌍", layout="wide")

st.title("🌍 EcoRenováveis Pro: Engenharia e Gestão")
st.write("Plataforma de dimensionamento, potencial energético, gestão de serviços e manutenção.")

# Criando as abas (Agora com 11 abas)
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs([
    "☀️ Solar Fotovoltaico", 
    "🌬️ Energia Eólica", 
    "💧 Hídrica (Micro e Grandes)",
    "🌱 Biomassa",
    "⚡ Eletrotécnica",
    "🔋 Baterias",
    "🔌 Inversores",
    "🗺️ Potencial Macroeconómico",
    "🛠️ Serviços e Manutenção",
    "📚 Guia do Técnico",
    "💼 Meu Negócio (Faturamento)"
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
    tipo_painel = st.selectbox("Tecnologia do Painel", [
        "Monocristalino (Alta Eficiência - Telhados pequenos)", 
        "Policristalino (Custo-benefício - Telhados grandes)", 
        "Filme Fino (Flexível - Grandes áreas)"
    ])

    if "Monocristalino" in tipo_painel:
        st.success("💡 Dica: Melhor para aproveitar pouco espaço. Eficiência média de 18% a 22%.")
    elif "Policristalino" in tipo_painel:
        st.warning("💡 Dica: Mais económico, mas ocupa 20% mais área do que o Monocristalino.")
    else:
        st.info("💡 Dica: Use apenas se o cliente tiver uma área gigante ou telhado curvo. Eficiência baixa (7% a 12%).")

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
    tipo_turbina = st.selectbox("Tipo de Turbina Eólica", [
        "Eixo Horizontal (Hélice - Mais comum)",
        "Eixo Vertical (Savonius/Darrieus - Ventos fracos)"
    ])
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
    tipo_hidro = st.selectbox("Tipo de Turbina Hídrica", [
        "Pelton (Alta Queda, Baixa Vazão)",
        "Francis (Queda Média, Vazão Média)",
        "Kaplan (Baixa Queda, Alta Vazão)"
    ])
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
    tipo_biomassa = st.selectbox("Tipo de Processo", [
        "Combustão Direta (Queima em Caldeira)",
        "Gaseificação (Gás de Síntese)",
        "Biodigestor (Biogás)"
    ])
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
    st.subheader("🔌 Dimensionamento e Escolha do Inversor")
    st.write("O inversor é o cérebro do sistema. Ele deve suportar os equipamentos da casa e os picos de arranque (motores).")
    
    tipo_inversor = st.selectbox("Tipo de Inversor", [
        "Híbrido (Rede + Baterias - Recomendado em Angola)",
        "Off-Grid (Apenas Baterias - Zonas rurais)",
        "On-Grid (Apenas Rede - Sem baterias)"
    ])
    
    if "Híbrido" in tipo_inversor:
        st.success("💡 Ideal para locais com cortes frequentes de energia. Carrega as baterias e usa a rede quando o sol acaba.")
    elif "Off-Grid" in tipo_inversor:
        st.warning("💡 Necessita de um banco de baterias maior. Não tem ligação à rede pública.")
    else:
        st.info("💡 Desliga-se em caso de corte de energia da rede, por segurança dos técnicos da rede elétrica.")

    col10, col11 = st.columns(2)
    with col10:
        carga_total_continuа = st.number_input("Carga total contínua (Watts)", min_value=100, value=2000, step=100, help="Soma de todos os aparelhos ligados ao mesmo tempo.")
    with col11:
        tem_motores = st.selectbox("Tem equipamentos com motor? (Geleira, Bomba de água)", ["Sim", "Não"])
    
    fator_seguranca = 1.25
    potencia_continua_inversor = carga_total_continuа * fator_seguranca
    
    if tem_motores == "Sim":
        potencia_pico_inversor = carga_total_continuа * 3.0 # Pico de arranque
        st.warning(f"⚠️ Atenção: Devido aos motores, o inversor precisa de suportar um pico de **{potencia_pico_inversor:.0f} W** por alguns segundos.")
    else:
        potencia_pico_inversor = potencia_continua_inversor

    st.divider()
    st.subheader("Resultado do Inversor")
    i1, i2 = st.columns(2)
    i1.metric("Potência Contínua Recomendada", f"{potencia_continua_inversor:.0f} W")
    i2.metric("Potência de Pico (Surge)", f"{potencia_pico_inversor:.0f} W")
    
    st.caption("Procure no mercado um inversor que tenha estas especificações ou superiores.")

with tab8:
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

with tab9:
    st.subheader("🛠️ Gestão de Serviços e Manutenção")
    tipo_manutencao = st.selectbox("Tipo de Manutenção", [
        "Preventiva (Planeada - Ex: Limpezas e inspeções)",
        "Corretiva (Urgente - Ex: Avarias e quebras)",
        "Preditiva (Monitorização - Ex: Análise de dados e sensores)"
    ])
    sistema_alvo = st.selectbox("Sistema Alvo", ["Solar Fotovoltaico", "Eólico", "Hídrico", "Biomassa"])

    st.markdown("### 📋 Checklist de Operação")
    if sistema_alvo == "Solar Fotovoltaico":
        if "Preventiva" in tipo_manutencao:
            st.checkbox("Limpeza dos painéis (remoção de pó e areia) - A cada 15 dias", value=True)
            st.checkbox("Verificação do aperto dos cabos e conectores MC4", value=False)
            st.checkbox("Inspeção visual de fissuras ou pontos quentes (Hot Spots)", value=False)
            st.checkbox("Limpeza do dissipador de calor do inversor", value=False)
        elif "Corretiva" in tipo_manutencao:
            st.checkbox("Substituição de fusíveis ou disjuntores queimados")
            st.checkbox("Substituição de inversor avariado")
            st.checkbox("Reparação de cabos roídos por animais")
        else:
            st.checkbox("Termografia com câmara térmica para detetar painéis com falha")
            st.checkbox("Análise da curva I-V do sistema")
            
    elif sistema_alvo == "Eólico":
        if "Preventiva" in tipo_manutencao:
            st.checkbox("Lubrificação do multiplicador (gearbox) e rolamentos")
            st.checkbox("Inspeção visual das pás (fissuras, erosão)")
            st.checkbox("Aperto dos parafusos da torre")
    elif sistema_alvo == "Hídrico":
        if "Preventiva" in tipo_manutencao:
            st.checkbox("Limpeza das grades de captação (remoção de troncos e lixo)")
            st.checkbox("Verificação de fugas de óleo na turbina")
            st.checkbox("Inspeção do sistema de vedação (selos mecânicos)")
    elif sistema_alvo == "Biomassa":
        if "Preventiva" in tipo_manutencao:
            st.checkbox("Limpeza da fuligem na caldeira")
            st.checkbox("Verificação do sistema de alimentação de combustível")
            st.checkbox("Análise do pH do biodigestor")

    st.divider()
    st.subheader("💰 Simulador de Orçamento de Limpeza (Exemplo Solar)")
    num_paineis_limpeza = st.number_input("Quantidade de painéis a limpar", min_value=1, value=50, step=10)
    preco_por_painel = st.number_input("Preço de limpeza por painel (na sua moeda)", min_value=0.0, value=1500.0, step=100.0)
    st.metric("Valor a Cobrar ao Cliente", f"{num_paineis_limpeza * preco_por_painel:,.2f}")

with tab10:
    st.subheader("📚 Guia do Engenheiro Consultor")
    st.markdown("""
    **Inversores Híbridos (O Padrão em Angola):**
    *   **Porquê usar?** Porque a rede elétrica pode falhar, mas você não quer que a casa fique no escuro. O inversor híbrido carrega as baterias com o sol e, ao mesmo tempo, usa a rede da ENDE para o consumo imediato. Se a rede cair, ele muda para as baterias instantaneamente.
    *   **Potência de Pico:** Um inversor de 3kW contínuos pode aguentar 6kW (ou mais) por 2 segundos. É isso que salva a sua geleira quando o motor arranca.
    *   **Cuidado com o Fator de Potência:** Equipamentos com motores têm um Fator de Potência (FP) baixo. Se for comprar um inversor, procure um com FP de 0.8 ou superior.
    """)

with tab11:
    st.subheader("💼 Simulador de Faturamento do Meu Software")
    col16, col17 = st.columns(2)
    with col16:
        preco_setup = st.number_input("Preço de Customização por Empresa (USD)", min_value=0.0, value=150.0, step=10.0)
        preco_mensal = st.number_input("Mensalidade por Empresa (USD)", min_value=0.0, value=25.0, step=5.0)
    with col17:
        num_empresas = st.number_input("Nº de Empresas Clientes", min_value=1, value=5, step=1)
        num_formacoes = st.number_input("Nº de Centros de Formação (Licença Única 100$)", min_value=0, value=2, step=1)

    receita_setup = (num_empresas * preco_setup) + (num_formacoes * 100.0)
    receita_recorrente_ano = (num_empresas * preco_mensal) * 12
    receita_total_ano1 = receita_setup + receita_recorrente_ano
    
    st.divider()
    st.markdown("### 📈 Projeção Financeira (Ano 1)")
    st.metric("Receita de Setup", f"$ {receita_setup:,.2f}")
    st.metric("Receita Recorrente (Anual)", f"$ {receita_recorrente_ano:,.2f}")
    st.success(f"**Faturamento Total Estimado no Primeiro Ano:** $ {receita_total_ano1:,.2f}")

st.sidebar.title("EcoRenováveis Pro")
st.sidebar.info("Desenvolvido por **Adão Cassessa**.\n\nEngenheiro de Energias Renováveis e Desenvolvedor Python.")
