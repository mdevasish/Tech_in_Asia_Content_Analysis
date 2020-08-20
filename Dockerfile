FROM continuumio/anaconda3
COPY . /usr/app
EXPOSE 5000
WORKDIR /usr/app
RUN conda create --name venv
RUN pip install -r requirements.txt
CMD python app.py