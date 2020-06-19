# DesafioOctos
Desafio de Estágio Octos

A tarefa é desenvolver um sistema web para cadastro de câmeras como parte do sistema de video-analítico que você está construindo.

# Requisitos Funcionais

Esse sistema deverá permitir o cadastro de câmeras, contendo um nome da câmera para um humano identificá-la (ex: "Jardim", "Hall de Entrada") fabricante e número de série.

O Campo nome é livre, com limite de 50 caracteres.

O campo fabricante deverá ser selecionado de uma lista, sendo os possíveis fabricantes de câmera:

  -Secure Câmeras Inc
  
  -Surveillance Cams LLC
  
  -DigiEye Group
  
  -CâmeraFi Inc
  
  -VidMasters Inc
  
O Número de Série é um campo que permite caracteres alfanuméricos (maiúsculos) sem espaço, com limite de 16 caracteres.

O sistema deverá permitir:

  -Listar câmeras inseridas
  
  -Remover câmera
  
  -Adicionar nova câmera

# Requisitos Não Funcionais

  -A interface gráfica deverá funcionar pelo menos em um navegador moderno recente (Chrome, Firefox, Safari, etc).
  
  -Não é preciso suportar versões antigas dos navegadores.
  
  -Não é preciso suportar todos os navegadores ao mesmo tempo.
  
  -A comunicação entre a interface (frontend) e o resto do sistema (backend) deverá ser feita através de uma API JSON.
  
  -Os dados do sistema deverão persistir "restarts" (isto é, deverão salvar os dados em algum banco de dados ou arquivo no computador).
  
  # Framework Backend
  Está sendo utilizado o Django para criar APIs backend. Para saber mais: https://www.djangoproject.com/start/
  
  # Organização do código
  
  A pasta django se refere a pasta root do projeto. A pasta octos é a pasta do projeto (criada ao executar o comando: django-admin startproject octos). A pasta desafio é o aplicativo (criado ao executar o comando dentro da sua pasta principal (fora da pasta
meu-site): python manage.py startapp app) e dentro dela estão todos os arquivos criados.
 Para entender mas sobre a organização do django, acesse: https://docs.djangoproject.com/en/3.0/intro/tutorial01/
 
 # Como dar start
 
  Primeiro, instale o Python 3.8.3 na sua máquina. Você deverá ter instalado também o pip, que é o gerenciador de pacotes do Python. (Para instalar o “pip” na sua máquina, acesse https://pip.pypa.io/en/latest/installing/, e siga as instruções Installing with get-pip.py.). 
  Segundo, instale o django em sua máquina. (Pode ser instalado executando o comando: pip install django). Para entender mais sobre o django, acesse: https://www.djangoproject.com/start/ .
  Terceiro, baixe esse repositório em sua máquina.
  
  
 
 
 # Como acessar a API Rest
 
 Com o sistema já instalado, acesse o endereço http://localhost:8000/cameras/ para ter a lista de todas as câmeras instaladas e para adicionar novas câmeras (POST). Para acessar detalhes de uma câmera específica, acesse http://localhost:8000/cameras/o-id-da-camera (o-id-da-camera deve ser substituido pelo número id que aparece na descrição da câmera), onde poderá editar (PUT) ou deletar (DELETE) a câmera específica.
