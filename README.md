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
The Challenge.ipynb notebook cannot be executed directly because I could not upload the data used due to its size and the github restrictions for large files. If you want to execute the notebook please download the files from 

In order to execute the training.py file, first we need to unzip the data.zip file in the data_training directory. After that we should have three csv files in the directory as shown below

    ├── data_training                    
    │   ├── data.csv          
    │   ├── labels.csv         
    │   └── samples.csv                
    └── ...

After that you'll just need to run the following command

```
python3 training.py
```
