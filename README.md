# Tech_in_Asia_Content_Analysis

Author : Manikantha Devasish

Approach : 
1. Extract data from the APIs provided in the doc 'Data Scientist Assignment (2020).docx' and save it.
2. Explore and clean the data.
3. Implemet a topic Modelling to discover the topics form the articles.
4. Create a visualisation and convey the results using Dash framework of plotly.

Challenges and Limitations:
1. Cleaning data : Firstly the data is not huge but since the data origin is from the internet, cleaning the data was challenging.
2. Updating the stopwords and judging the topics : Despite the using the metrics coherence score and perplexity score, human judgement of the topics was exhausting and required a lot of time to update the stop words and rerun the model.
3. As the topics are from Tech in Asia where major articles are related to aggregated news articles around the world and few articles are specific happenings in specific sectors, segregating the topics is a challenge.
4. Chioce of models to proceed with. Even though the results from Bag of words and Tfidf model were close, I chose to go with the Bag of words model because of ease of judgement of topics from the topic word distribution.
6. Named Entity Recognition models developed by Spacy/nltk are not the ideal way of extracting the names of the organisation or regions but due to limited availability of time, I had to implement exisitng NER models which are not completely accurate.


Libraries used in the project are captured in requirements.txt

Further Work :
1. Author profiling : Append all the articles for each author and run a cosine similairty to understand the similarity of the content for each user. Based on the results a recommendation engine can be developed that can be deployed on the production environment to increase the readership.
2. Integrate the PCA visualisation for the BOW model into the dash app developed.
3. Customised training of spacy models for better Named entity recognition.

Steps to open the app:
1. Create a virtual environment and install the required libraries from requirements.txt .
2. Open command prompt in the directory where the file app.py resides and run the command 'python app.py'.

                                   (or)

1. Download the docker image and run the docker. Image is not pushed to the Docker Hub or any other docker registries*.

File Structure:

Application

|     app.py
|     BOW_Model.ipynb
|     Data Scientist Assignment (2020).docx
|     Data_Extraction.py
|     Dockerfile
|     NER_Model.py
|     output.txt
|     README.md
|     requirements.txt
|     TFIDF_Model.ipynb
|   
+---.ipynb_checkpoints
|       BOW_Model-checkpoint.ipynb
|       TFIDF_Model-checkpoint.ipynb
|       
+---assets
|       favicon.ico
|       TIA.gif
|       
+---Data
|       comments.csv
|       posts.csv
|       
+---Models
|   +---.ipynb_checkpoints
|   +---BOW
|   |       BOW_Topic_Modelling.csv
|   |       dictionary_lda.json
|   |       my_topics_bow.html
|   |       Topicmodelling_bow.h5
|   |       Topicmodelling_bow.h5.expElogbeta.npy
|   |       Topicmodelling_bow.h5.id2word
|   |       Topicmodelling_bow.h5.state
|   |       
|   \---TFIDF
|           dictionary_lda.json
|           my_topics_tfidf_corpus_tfidf.html
|           TFIDF_Topic_Modelling.csv
|           Topicmodelling_tfidf.h5
|           Topicmodelling_tfidf.h5.expElogbeta.npy
|           Topicmodelling_tfidf.h5.id2word
|           Topicmodelling_tfidf.h5.state
|           
+---Results
|       final.csv
|       ner.csv
|       
+---templates
|       my_topics_bow.html
|
\---__pycache__
        flask.cpython-38.pyc
        random.cpython-38.pyc

Demo of the App:

![Landing page](https://github.com/mdevasish/Tech_in_Asia_Content_Analysis/blob/master/assets/TIA.gif)

Steps to view the App:

Prerequisites : Dockers is installed.

1. Launch commandline interface after opening the folder 'Tech_in_Asia_Content_Analysis'

2. Run the following commands. <port1> is an available port of the system and 5000 is a free port available on the ubuntu system of the Docker.
    
    docker build -t app .
    
    docker run --rm -p <port1>:5000 app
  
  Ex : docker run --rm -p 5000:5000 app

3. If the above command execution is successful without any errors, launch a browser and hit the url : http://localhost:<port1>/

Thank you.
