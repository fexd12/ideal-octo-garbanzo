# ideal-octo-garbanzo

  Projeto para classificar imagens da biblioteca mnist 
  link para visualização do model:
  https://colab.research.google.com/drive/11Zm9pCTEYobObsmS3hzZHWWF2Q8gZ3Vb#scrollTo=-lCgz6UC8pKT
# Pasta backend - python 3.7
  Responsavel pelo recebimento de requisições do frontend para predict na qual classe pertence a imagem e pelo processamento da mesma.
  
  Atraves do framework Flask, recebe as imagens e fornece ao model.
  
  # Como usar ( backend )
     - criar um ambiente virtual o python ( venv )
        - python -m venv venv
     - ativar o ambiente virtual
        - windows 
            - venv\Scripts\activate
        - linux 
            - source venv\bin\activate
     - pip install -e . ( para instalar as dependencias )
     - flask run ( ira rodar na pota 2000 ) 
        - para alterar a porta de executar mudar no arquivo .flaskenv
  
# Pasta frontend - Vue Js
   Responsavel do envio da imagem ao backend para processamento e predict da classe a qual a imagem pertence, e mostrando a resposta ao usuario.

   # Como usar ( frontend )
     - npm install ( para instalar node_modules )
     - npm start
