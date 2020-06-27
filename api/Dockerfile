#Fazendo o pull da imagem base
#FROM python:3.6.8-alpine3.9 AS multistage
FROM python:3.6.8-alpine3.9

#Responsável por manter a imagem
LABEL MAINTAINER="Lucas de Araújo (lucasdearaujo.trabalho@gmail.com)"

#Definindo as variáveis de ambiente
ENV GROUP_ID=1000 \
USER_ID=1000 \
HOME=/var/www \
FLASK_APP=api_comentarios.py \
USER=www \
USER_GROUP=www 

#Diretório de trabalho padrão do container
WORKDIR $HOME

#Copiando tudo que está dentro do diretório api do repositório para dentro do diretório de trabalho (WORKDIR) do container
COPY . $HOME

#Atualizando o pip, instalando as dependências do arquivo requirements.txt, instalando Python WSGI HTTP Server gunicorn e definindo permissões de usuário e grupo de usuário
RUN pip install --upgrade pip==20.1 && \
pip install -r requirements.txt && \
pip install gunicorn==20.0.4 && \
addgroup -g $GROUP_ID $USER_GROUP && \
adduser -D -u $USER_ID -G $USER_GROUP $USER -s /bin/sh

#Técnica para reduzir o tamanho da imagem
#FROM alpine:3.9
#ENV HOME=/home
#WORKDIR $HOME
#RUN pip install gunicorn==20.0.4
#COPY --from=multistage /var/www/api_comentarios.py $HOME
#COPY --from=multistage /var/www/wsgi.py $HOME

#Usuário que executará a aplicação
USER $USER

#Expondo a aplicação na porta 5000
EXPOSE 5000

#Comando para iniciar a aplicação junto com o container
CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]