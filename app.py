import streamlit as st

st.title("DE LÊ CAMINHÕES")

# Menu lateral
st.sidebar.image("logo.png", width=150)
st.sidebar.title("MENU")
opcao = st.sidebar.selectbox("Escolha uma seção:",["scania p310", "ford cargo 4532", "volks 19 320", "axor 2544", "scania super 560", "volvo fh 540"])

 ###CRIANDO A LISTA DE NOMES 
nomes = ["scania p310", "ford cargo 4532", "volks 19 320", "axor 2544", "scania super 580", "volvo fh 540"]

if opcao == "Início":
    st.write("Bem-vindo à página inicial, Aqui voce poderá ver o melhor caminhão para você!")

    ###CRIANDO A LISTA DE NOMES 
    nomes = ["scania p310", "ford cargo 4532", "volks 19 320", "axor 2544", "scania super 580", "volvo fh 540"]
else:
    st.write("Clique e saiba mais sobre!!!")

    st.image(f"{opcao}.png")
    st.markdown(f"Você deseja comprar esse modelo?")
if opcao == "scania p310" :
    st.link_button(url="https://www.caminhoesecarretas.com.br/veiculo/sao-jose-do-rio-preto/sp/caminhao/scania/scania-p310/2014/bitruck-8x2/chassis/rodrigao-caminhoes/1320070", label= "Comprar")

elif opcao == "ford cargo 4532" :
    st.link_button(url="https://www.caminhoesecarretas.com.br/veiculo/navegantes/sc/caminhao/ford/cargo-4532/2009/toco-4x2/cavalo-mecanico/itajai-caminhoes/938890",label="Comprar")

elif opcao == "axor 2544":
    st.link_button(url="https://www.caminhoesecarretas.com.br/veiculo/sao-jose-dos-pinhais/pr/caminhao/mercedes-benz/mb-2544/2022/cavalo-6x2/cavalo-mecanico/5001-caminhoes---sao-jose-dos-pinhais/1311554", label="Comprar")

elif opcao == "scania super 560":
    st.link_button(url="https://www.caminhoesecarretas.com.br/veiculo/rio-verde/go/caminhao/scania/scania-s560/2024/cavalo-6x4/cavalo-mecanico/comber-seminovos/1275388", label="Comprar")

elif opcao == "volks 19 320":
    st.link_button(url="https://www.caminhoesecarretas.com.br/veiculo/sumare/sp/caminhao/volkswagen/vw-19320/2006/cavalo-4x2/cavalo-mecanico/rt-caminhoes/1309820", label="Comprar")

else:
    st.link_button(url="https://www.caminhoesecarretas.com.br/veiculo/porto-alegre/rs/caminhao/volvo/volvo-fh-540/2021/cavalo-6x4/cavalo-mecanico/patria-caminhoes/1304512", label="Comprar")
 