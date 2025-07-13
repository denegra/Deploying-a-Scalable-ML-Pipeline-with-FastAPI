import pytest
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model, compute_model_metrics, inference, process_data


DATA_PATH = "data/census.csv"

@pytest.fixture(scope="module")
def data():
    df = pd.read_csv(DATA_PATH)
    train = df.sample(frac=0.8, random_state=42)
    test = df.drop(train.index)

    cat_features = [
        "workclass", "education", "marital-status", "occupation",
        "relationship", "race", "sex", "native-country"
    ]

    X_train, y_train, encoder, lb = process_data(
        train, categorical_features=cat_features, label="salary", training=True
    )
    X_test, y_test, _, _ = process_data(
        test, categorical_features=cat_features, label="salary", training=False,
        encoder=encoder, lb=lb
    )
    return X_train, y_train, X_test, y_test


# Test_one checks to ensure that the model is a RandomForestClassifer
def test_one(data):
    X_train, y_train, _, _ = data
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), "Model should be RandomForestClassifier"

# Test_two checks to ensure prediction length matches input length
def test_two(data):
    X_train, y_train, X_test, _ = data
    model = train_model(X_train, y_train)
    preds = inference(model, X_test)
    assert len(preds) == len(X_test), "Inference output length should match input"


# Test_three checks to ensure that the metrics return values are in the correct range
def test_three(data):
    y_true = [1, 0, 1, 1, 0]
    y_pred = [1, 0, 0, 1, 0]
    precision, recall, f1 = compute_model_metrics(y_true, y_pred)

    assert 0.0 <= precision <= 1.0, "Precision should be between 0 and 1"
    assert 0.0 <= recall <= 1.0, "Recall should be between 0 and 1"
    assert 0.0 <= f1 <= 1.0, "F1 score should be between 0 and 1"
