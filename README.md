# PAP-Cocktail-Automtico
<div align="center">
    <img src="./Fotos/imagem_modelo3d.png" />
</div>


## Descrição

Este repositório contém todos os recursos relacionados ao projeto de PAP (Projeto de Aptidão Profissional) de um Cocktail Automático, desenvolvido por, Lucas de Linhares e Roberto Fernandes.  
A PAP é um projeto que desenvolvemos como parte do processo de formação profissional.    Esta inclui vários elementos, como um sistema de mistura de liquidos, um WebSite, pombas peristálticas e mais!



## Instalação do WebSite

```bash
# Clone o repositório
git clone https://github.com/lucascompython/PAP-Cocktail-Automatico

# Entre no diretório do repositório
cd PAP-Cocktail-Automatico/WebSite

# Instale as dependências
pnpm install

# Inicie o servidor de desenvolvimento
pnpm run dev

# Para gerar uma build de produção
pnpm run build

##############

# Instalar as dependências do backend

# Entre no diretório do backend
cd ../Raspberry

# Instale as dependências
pip3 install fastapi uvicorn[standard]

# Inicie APENAS o servidor de backend
uvicorn api:app --reload

# Inicie o programa inteiro (incluindo o controle dos motores)
python3 main.py


```


## Licenciamento

Acreditamos no poder do software de código aberto para impulsionar a inovação e tornar o mundo um lugar melhor. Como tal, estamos empenhados em contribuir para a comunidade de código aberto, tornando o nosso trabalho disponível gratuitamente para outros usarem, estudarem e desenvolverem.

O código neste repositório está licenciado sob a GNU General Public License v3.0. Consulte o arquivo `LICENSE` na raiz deste repositório para obter o texto completo da licença.

As fotos, modelos 3D, documentos Word, documentos PowerPoint e PDFs neste repositório estão licenciados sob a Licença Creative Commons Atribuição-CompartilhaIgual 4.0 Internacional. Consulte o arquivo `LICENSE-CC-BY-SA` tambem na raiz deste repositório para obter o texto completo da licença.
