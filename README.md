# DesafioOctos
Desafio de Estágio Octos

A sua tarefa é desenvolver um sistema web para cadastro de câmeras como parte do sistema de video-analítico que você está construindo.

Requisitos Funcionais

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

Requisitos Não Funcionais

  -A interface gráfica deverá funcionar pelo menos em um navegador moderno recente (Chrome, Firefox, Safari, etc).
  
  -Não é preciso suportar versões antigas dos navegadores.
  
  -Não é preciso suportar todos os navegadores ao mesmo tempo.
  
  -A comunicação entre a interface (frontend) e o resto do sistema (backend) deverá ser feita através de uma API JSON.
  
  -Os dados do sistema deverão persistir "restarts" (isto é, deverão salvar os dados em algum banco de dados ou arquivo no computador).
