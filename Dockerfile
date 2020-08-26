FROM ubuntu
FROM python
ENV DASH_DEBUG_MODE True
COPY . /usr/app
EXPOSE 5000
WORKDIR /usr/app
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN python -c "import nltk;nltk.download('punkt')"
CMD ["python","app.py"]