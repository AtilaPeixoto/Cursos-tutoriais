import streamlit as st
# streamliti run nome programa
#cessar -> contrl +c no terminal

# textos
st.header('texto')
st.text('texto menor')

st.markdown('# markdown')
st.markdown('~~markdown riscado~~')  
          
st.sidebar.text('MENU')

st.caption('legenda')

lista = [
    {'nome': 'nome1','idade': '30' },
    {'nome': 'nome2', 'idade': '20'}
]

st.write('# Pessoas', lista)

#exibição de dados
import pandas as pd
import numpy as np
import datetime

st.sidebar.text_input(
    'Digite seu texto',
)

st.number_input(
    'degite um numero',
    
)

st.slider(
    'minimo e maximo',
    0.0, 100.0, (25.0, 75.0)
)

st.sidebar.date_input(
    'Escolha a data',
    datetime.date(2022,2,2)
)

#st.sidebar.selectbox()
st.selectbox(
    'selecione uma opção',
    ('Perço', 'Taxa de ocupação', 'aqui')
)
st.sidebar.multiselect(
    'selecione as opção',
    ('opção1', 'opção2', 'opção3')
)

mark = st.checkbox('termos?')
# st.sidebar.checkbox('')
if mark:
    st.write('marcado')

data_frame = pd.DataFrame(
    np.random.rand(10, 4), 
    columns=['PREÇO', 'TAXA DE OCUPAÇAO', 'TAXA DE INADIMPLENCIA', 'PESSOAS POR CASA']
)
#tabea fixa padrao
if st.sidebar.button('Table'):
    st.table(data_frame)
    
# tabela maleavel com colunas regulaveis
if st.sidebar.button('wirte'):
    st.write(data_frame)
    
#nao parece ter diferença entre o write
if st.sidebar.button('dataframe'):
    st.dataframe(data_frame)
    
#grafico em linha
if st.sidebar.button('grafico em linha'):
    st.line_chart(data_frame)
    
    opcao = st.radio(
    'selecione uma opção', 
    ('TABELA', 'PREÇO', 'TAXA DE INADIMPLENCIA')
    )
    if opcao == 'TABELA':
        #st.line_chart(data_frame)
        st.text('texto1')
    elif opcao == 'PREÇO':
        #columns=['PREÇO']
        #st.line_chart(data_frame)
        st.text('texto2')
    elif opcao == 'TAXA DE INADIMPLENCIA':
        #columns=['TAXA DE INADIMPLENCIA']
        #st.line_chart(data_frame)
        st.text('texto3')
        #---> esta guardando pois esta na sidebar.
    
#grafico e barra    
if st.sidebar.button('grafico em colunas'):
    st.bar_chart(data_frame)
    
    

