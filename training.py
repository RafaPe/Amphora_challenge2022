import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
import joblib


def read_data(path):
    data = pd.read_csv(path + 'data.csv', index_col= 0)
    labels = pd.read_csv(path + 'labels.csv')
    return data, labels



if __name__ == '__main__':
    data, labels = read_data('data_training/')
    
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.20, random_state=42)

    African_model = svm.SVC(C = 0.6, kernel = 'sigmoid', probability = True)
    African_model.fit(X_train, y_train['AFR'])

    SouthAsian_model = svm.SVC(C = 1.2, kernel = 'sigmoid' , probability = True)
    SouthAsian_model.fit(X_train, y_train['SAS'])

    EastAsian_model = svm.SVC(C = 1.2, kernel = 'linear' , probability = True)
    EastAsian_model.fit(X_train, y_train['EAS'])

    European_model = svm.SVC(C = 0.6, kernel = 'linear' , probability = True)
    European_model.fit(X_train, y_train['EUR'])

    American_model = svm.SVC(C = 1, kernel = 'poly', degree = 3, probability = True)
    American_model.fit(X_train, y_train['AMR'])

    joblib.dump(African_model, 'models/African_model.pkl')
    joblib.dump(SouthAsian_model, 'models/SouthAsian_model.pkl')
    joblib.dump(EastAsian_model, 'models/EastAsian_model.pkl')
    joblib.dump(European_model, 'models/European_model.pkl')
    joblib.dump(American_model, 'models/American_model.pkl')

