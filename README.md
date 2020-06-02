### Adavance Learning for Text and Graph Data (Altegrad 2020)
>**Khaoula BELAHSEN - Aicha BOUJANDAR - Emma DEMARECAUX**
************************
>*Kaggle Challenge: French Web Domain Classification*

# Architecture of the project

The file `preprocess.py` in the root directory contains the preprocessing steps applied on the text data and used by almost all models.

## Folder 1: data 
It contains the challenge data that was provided: `edgelist.txt`, `train.csv` and `test.csv`.

## Folder 2: texts 
It contains the folder `text` which contains all the web domains texts.

## Folder 3: models 
Each `.py` file contained in this folder represents a model. Here is a brief description of the files models (the models are detailed in the report):
* `graph baseline.py`: the graph model that was initially provided.
* `text_baseline.py`: the text model model that was initially provided.
* `tfidf_deepwalk.py`: applies a _TF-IDF_ transformation on the text data and the _Deepwalk_ method (contained in `utils_deepwalk.py`) on the graph data. It applies a _Logistic Regression_ model to the resulting features.
* `word2vec_deepwalk.py` : applies a _Word2Vec_ transformation on the text data and the _Deepwalk_ method (contained in `utils_deepwalk.py`) on the graph data. It applies a _Logistic Regression_ model to the resulting features.
* `tfidf_gnn.py`: applies a _TF-IDF_ transformation on the text data and the _GNN_ method (contained in `utils_gnn.py`) on the graph data.
* `tfidf_text.py`: applies a _TF-IDF_ transformation on the text data followed by a _Logistic Regression_ model.
* `separate_texts.py`: creates _subtexts_ in a `./data` folder and runs a _Logistic Regression_ model on the new data before aggregating the predictions.

To generate the prediction file corresponding to a model, one needs to run the corresponding `.py` file as follows:

1. Change the current working directory to `models`:
```
cd models
```
2. Run the `model.py` file using the command: 
```
python3 model.py
```
3. The `.csv` prediction file will be saved in the root directory.

## Folder 4 : utils 
It contains the following util files:

* `utils_deepwalk.py`: contains the util functions to perform the _Deepwalk_ algortihm.
* `utils_gnn.py`: contains the util functions to perform the _GNN_ model.
* `tfidf_text_param_opt.py`: contains the code to optimize the parameters of the _TF-IDF_ - _Logistic Regression_ model using `skopt` bayesian optimisation. In order to perform the optimisation:

    i. Change the current working directory to `utils`:
    ```
    cd utils
    ```
    ii. Run the `tfidf_text_param_opt.py` file using the command: 
    ```
    python3 tfidf_text_param_opt.py
    ```
 
# Results

Our best performing model on the Kaggle public leaderboard (http://www.kaggle.com/c/fr-domain-classification) comes from the model `tfidf_text.py`: the multi-class loss achieved is 1.03771. 
