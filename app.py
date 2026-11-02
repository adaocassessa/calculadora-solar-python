import streamlit as st
import math

st.set_page_config(page_title="EcoSolar Pro - Engenharia e Dimensionamento", page_icon="☀️", layout="wide")

st.title("☀️ EcoSolar Pro: Dimensionamento e Engenharia")
st.write("Ferramenta completa de pré-dimensionamento, seleção de equipamentos e guia técnico de energias renováveis.")

# Criando as abas
tab1, tab2, tab3, tab4 = st.tabs(["⚙️ Dimensionamento Base", "🔋 Equipamentos (Inversor e Baterias)", "💰 Financeiro", "📚 Guia do Técnico"])

with tab1:
    st.subheader("1. Dados do Consumo e Localização")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        consumo_mensal = st.number_input("Consumo mensal de energia (kWh)", min_value=1.0, value=300.0, step=10.0)
    with col2:
        irradiacao = st.number_input("Irradiação solar média local (kWh/m²/dia)", min_value=1.0, value=5.5, step=0.1)
    with col3:
        performance_ratio = st.slider("Performance Ratio (eficiência)", min_value=0.60, max_value=0.95, value=0.80, step=0.01)

    st.subheader("2. Dados do Painel Solar")
    col4, col5 = st.columns(2)
    with col4:
        potencia_painel = st.number_input("Potência de cada painel (W)", min_value=100, value=550, step=10)
    with col5:
        area_painel = st.number_input("Área de cada painel (m²)", min_value=0.5, value=2.6, step=0.1)

    # Cálculos Base
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
    st.subheader("Dimensionamento de Inversor e Baterias (Sistemas Isolados / Híbridos)")
    st.info("Nota: Para sistemas ligados à rede (On-Grid) puros, o banco de baterias não é necessário. Preencha os campos abaixo apenas se for Híbrido ou Isolado (Off-Grid).")
    
    col6, col7 = st.columns(2)
    with col6:
        fator_potencia_inversor = st.slider("Fator de segurança do Inversor", min_value=1.1, max_value=1.5, value=1.25, step=0.05, help="O inversor deve suportar um pouco mais que a potência dos painéis.")
        dias_autonomia = st.number_input("Dias de autonomia (sem sol)", min_value=1, max_value=5, value=1, step=1)
    
    with col7:
        profundidade_descarga = st.slider("Profundidade de Descarga (DoD) da bateria", min_value=0.50, max_value=0.90, value=0.80, step=0.05, help="Baterias de Lítio suportam 80-90%. Chumbo-ácido 50%.")
        tensao_sistema = st.selectbox("Tensão do sistema de baterias (V)", [12, 24, 48], index=2)
        capacidade_bateria = st.number_input("Capacidade de cada bateria (Ah)", min_value=50, value=200, step=50)

    # Cálculos de Equipamentos
    potencia_inversor_w = (potencia_kwp * 1000) * fator_potencia_inversor
    # Fórmula: (Consumo Diário * Dias Autonomia) / (Tensão * DoD)
    energia_bateria_necessaria_wh = (consumo_diario * 1000) * dias_autonomia
    capacidade_total_ah = energia_bateria_necessaria_wh / (tensao_sistema * profundidade_descarga)
    numero_baterias = math.ceil(capacidade_total_ah / capacidade_bateria)

    st.divider()
    st.subheader("🔌 Equipamentos Sugeridos")
    e1, e2 = st.columns(2)
    e1.metric("Potência do Inversor", f"{potencia_inversor_w:.0f} W")
    e2.metric("Baterias Necessárias", f"{numero_baterias} un. de {capacidade_bateria}Ah")

with tab3:
    st.subheader("Análise Financeira")
    col8, col9 = st.columns(2)
    with col8:
        preco_kwh = st.number_input("Preço do kWh local", min_value=0.01, value=150.0, step=10.0)
    with col9:
        custo_kwp = st.number_input("Custo estimado do sistema por kWp", min_value=100.0, value=1500.0, step=100.0)

    custo_total_sistema = potencia_kwp * custo_kwp
    economia_mensal = consumo_mensal * preco_kwh
    payback_meses = custo_total_sistema / economia_mensal
    payback_anos = payback_meses / 12

    st.divider()
    st.subheader("💵 Retorno do Investimento")
    f1, f2, f3 = st.columns(3)
    f1.metric("Custo Estimado", f"{custo_total_sistema:,.0f}")
    f2.metric("Economia Mensal", f"{economia_mensal:,.0f}")
    f3.metric("Tempo de Retorno", f"{payback_anos:.1f} anos", f"{payback_meses:.0f} meses", delta_color="inverse")

with tab4:
    st.subheader("📚 Guia Rápido de Dimensionamento para Técnicos")
    st.markdown("""
    Esta ferramenta foi desenhada para evitar erros comuns de operação humana. Abaixo estão as diretrizes técnicas utilizadas nos cálculos:

    **1. Potência do Arranjo Fotovoltaico (kWp)**
    *   **Fórmula:** `Consumo Diário / (Irradiação Solar * Performance Ratio)`
    *   **O que é Performance Ratio (PR)?** É a eficiência real do sistema. Perdas por calor, sujidade nos painéis e cabos fazem com que o sistema nunca produza 100%. O valor ideal fica entre **0.75 e 0.85**.

    **2. Escolha do Inversor**
    *   **Regra de Ouro:** O inversor não deve trabalhar no seu limite máximo o tempo todo. Usamos um fator de segurança (geralmente 1.25). Um sistema de 2 kWp exige um inversor de cerca de 2.5 kW.
    *   **Erro Comum:** Comprar um inversor menor que a potência dos painéis (causa queima do equipamento ou perda de geração).

    **3. Banco de Baterias (Off-Grid)**
    *   **Fórmula:** `(Consumo Diário * Dias de Autonomia) / (Tensão do Sistema * Profundidade de Descarga)`
    *   **Profundidade de Descarga (DoD):** Nunca descarregue baterias de chumbo-ácido abaixo de 50% (elas viciam). Baterias de Lítio suportam até 80-90%.
    *   **Tensão:** Sistemas residenciais pequenos usam 12V ou 24V. Sistemas maiores (acima de 3kWp) exigem 48V para não derreter os cabos (Lei de Ohm).

    *Dica de Ouro para Técnicos:* Sempre verifique a ficha técnica (Datasheet) do inversor para ver a tensão máxima de entrada (Voc) e a corrente máxima. Este software faz a estimativa base, mas a validação final do datasheet é obrigatória.
    """)

st.sidebar.title("Sobre o Software")
st.sidebar.info("Desenvolvido por **Adão Cassessa**.\n\nEspecialista em Python e Energias Renováveis. Esta ferramenta tem como objetivo capacitar técnicos e otimizar empresas de instalação solar.")
