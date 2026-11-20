
import pytest
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from mini_projekat_2 import (
    AccuracyStrategy,
    DecisionTreeModel,
    ExperimentMonitor,
    F1Strategy,
    KNNModel,
    LogisticRegressionModel,
    ModelFactory,
    Observer,
    PrecisionStrategy,
    RecallStrategy,
    run_experiment,
)


def test_factory_kreira_logisticku_regresiju():
    model = ModelFactory.create_model("logistic_regression")
    assert isinstance(model, LogisticRegressionModel)


def test_factory_kreira_stablo_odlucivanja():
    model = ModelFactory.create_model("decision_tree")
    assert isinstance(model, DecisionTreeModel)


def test_factory_kreira_knn():
    model = ModelFactory.create_model("knn")
    assert isinstance(model, KNNModel)


def test_factory_nepoznat_model():
    with pytest.raises(ValueError):
        ModelFactory.create_model("nepostojeci")


def test_strategy_metrike():
    y_true = [0, 1, 2, 1]
    y_pred = [0, 1, 2, 0]

    strategies = [
        AccuracyStrategy(),
        PrecisionStrategy(),
        RecallStrategy(),
        F1Strategy(),
    ]

    for strategy in strategies:
        rezultat = strategy.calculate(y_true, y_pred)
        assert 0 <= rezultat <= 1


def test_observer_prima_obavjestenje():

    class TestObserver(Observer):

        def __init__(self):
            self.messages = []

        def update(self, message):
            self.messages.append(message)

    monitor = ExperimentMonitor()
    observer = TestObserver()

    monitor.subscribe(observer)
    monitor.notify("Test poruka")

    assert observer.messages == ["Test poruka"]


def test_eksperiment_vraca_rezultate():
    iris = load_iris()

    X_train, X_test, y_train, y_test = train_test_split(
        iris.data,
        iris.target,
        test_size=0.2,
        random_state=42,
        stratify=iris.target
    )

    results = run_experiment(
        "knn",
        X_train,
        X_test,
        y_train,
        y_test
    )

    assert "Accuracy" in results
    assert "Precision" in results
    assert "Recall" in results
    assert "F1-score" in results
