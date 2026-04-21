import sys
from streamlit.web import cli as stcli

# Ele diz ao Python para rodar o Streamlit apontando para o app.py
sys.argv = ["streamlit", "run", "app.py"]
sys.exit(stcli.main())# Escreva o seu código aqui :-)
