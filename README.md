# Tech_in_Asia_Content_Analysis
Assignment for the role of Data Scientist 

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
7. Javascript : As per the assignment, the visualisation was to be developed in JavaScript. I have planned to pick up the necessary skills in two weeks of time for the visualisation but failed in picking up the skills completely, but later gave a thought about implementing the visualisation in Dash and proceeded with it due to limited amount of time.


Takeaways : 
1. Equipped myself with JavaScript basic skills. Started learning d3.js .
2. After analysing the results of Named Entity Recognition, I have explored the ways to train the pretrained models to give better results.

Libraries used in the project are captured in requirements.txt

Further Work :
1. Author profiling : Append all the articles for each author and run a cosine similairty to understand the similarity of the content for each user. Based on the results a recommendation engine can be developed that can be deployed on the production environment to increase the readership.
2. Integrate the PCA visualisation for the BOW model into the dash app developed.
3. Customised training of spacy models for better Named entity recognition.

Steps to open the app:
1. Create a virtual environment and install the required libraries from requirements.txt .
2. Open command prompt in the directory where the file app.py resides and run the command 'python app.py'.

                                   (or)

Download the docker image and run the docker. (applicable for Linux system). Image is not pushed to the Docker Hub*.

File Structure:

Application
|   app.py
|   BOW_Model.ipynb
|   Data Scientist Assignment (2020).docx
|   Data_Extraction.py
|   Dockerfile
|   NER_Model.py
|   output.docx
|   output.txt
|   README.md
|   requirements.txt
|   TFIDF_Model.ipynb
|   
+---.ipynb_checkpoints
|       BOW_Model-checkpoint.ipynb
|       TFIDF_Model-checkpoint.ipynb
|       
+---assets
|       favicon.ico
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
\---__pycache__
        flask.cpython-38.pyc
        random.cpython-38.pyc

Note : I would like to thank Ivan for giving an opprotunity to work on the articles (kind of an end to end project implementation) which has strengthened me by showing a new direction in my journey of learning. The last two weeks have been quiet hectic, fun, chaos yet productive.

Thank you.
