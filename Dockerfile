FROM python:3.6
WORKDIR /KubernetesClientPython
COPY ./requirement.txt /requirement.txt
RUN pip install -r /requirement.txt
COPY ./KubernetesClientPython/ ./
EXPOSE 8080

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8082"]
