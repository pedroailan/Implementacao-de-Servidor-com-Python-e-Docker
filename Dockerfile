FROM python:3-slim
LABEL version="1.0.0" description="Servidor da equipe mentos" maintainer="ALISSON OLIVEIRA NEVES <alisson.neves@dcomp.ufs.br>, PEDRO AILAN SILVA DE OLIVEIRA <pedroailan@academico.ufs.br>, RODRIGO FONTES MARTINS <rodrigo.martins@dcomp.ufs.br>"
WORKDIR /usr/src/filosofiaTupi
COPY . .
EXPOSE 22203
CMD ["python3", "ServerHttp.py"]
