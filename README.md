# Amphora_challenge2022
The objective of the 2022 Amphora Health’s Data Challenge Internship is to explore the genomic information that exists in our cells and develop machine learning models that can predict the risk of developing or acquiring a given disease. 

## Requirements
- python3      

The following python3 libraries:      

- pandas
- seaborn
- sklearn
- joblib
- lime
- glob

## Execution
The Challenge.ipynb notebook cannot be executed directly because I could not upload the data used due to its size and the github restrictions for large files. If you want to execute the notebook please download the files from https://drive.google.com/file/d/1MGNVYNfholw0LSzXKUSpezCzWnuxFa50/view?usp=sharing

In order to execute the training.py file, first you'll need to unzip the data.zip file in the data_training directory. After that, you should have three csv files in the directory as shown below

    ├── data_training                    
    │   ├── data.csv          
    │   ├── labels.csv         
    │   └── samples.csv                
    └── ...

Then you'll just need to run the following command

```
python3 training.py
```

The output of the training.py file should create the pkl files in the models directory. If you don't want to train the models, I have added the trained models as a zip file, so you can just run the predict.py file to make predictions. You just need to unzip the models.zip file and make sure the that the models directory and the predict.py file are on the same directory level.


    ├── models                   
    │   ├── African_model.pkl          
    │   ├── American_model.pkl   
    │   ├── EastAsian_model.pkl
    │   ├── European.pkl
    │   └── SouthAsian_model.pkl               
    └── predict.py
    
  Then you can run it with the following command
  
```
python3 predict.py
```

You can edit the file to predict the ancestry of other patients by changin the path variable in the main function of the code. The path should lead to a csv file in which the first column must be the patient id and then the rest of the data as shown in the samples.csv file in the data_training directory. After running it you should get the prediction of each kind of ancestry. I made a test with a random sample of the test set used for validation in the Challenge.ipynb notebook. The results should look like this:

![image](results/sample_results.jpg)




