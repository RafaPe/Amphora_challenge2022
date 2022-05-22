import pandas as pd
import joblib


def read_samples(path):
    samples = pd.read_csv(path, index_col= 0)
    return samples

def load_models(path):
    African_model = joblib.load(path + 'African_model.pkl')
    SouthAsian_model = joblib.load(path + 'SouthAsian_model.pkl')
    EastAsian_model = joblib.load(path + 'EastAsian_model.pkl')
    European_model = joblib.load(path + 'European_model.pkl')
    American_model = joblib.load(path + 'American_model.pkl')

    return African_model, SouthAsian_model, EastAsian_model, European_model, American_model


if __name__ == '__main__':
    path = 'data_training/samples.csv'
    samples = read_samples(path)

    African_model, SouthAsian_model, EastAsian_model, European_model, American_model = load_models('models/')

    African_pred = African_model.predict(samples)
    SouthAsian_pred = SouthAsian_model.predict(samples)
    EastAsian_pred = EastAsian_model.predict(samples)
    European_pred = European_model.predict(samples)
    American_pred = American_model.predict(samples)

    preds = [African_pred, SouthAsian_pred, EastAsian_pred, European_pred, American_pred]

    results = pd.DataFrame(preds, index=['AFR', 'SAS', 'EAS', 'EUR', 'AMR'], columns=samples.index).T

    print(results)



    