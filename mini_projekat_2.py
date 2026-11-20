
import time
from abc import ABC, abstractmethod
from functools import wraps

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# FACTORY PATTERN

class MLModel(ABC):

    @abstractmethod
    def train(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass


class LogisticRegressionModel(MLModel):

    def __init__(self):
        self.model = LogisticRegression(max_iter=200)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)


class DecisionTreeModel(MLModel):

    def __init__(self):
        self.model = DecisionTreeClassifier(random_state=42)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)


class KNNModel(MLModel):

    def __init__(self):
        self.model = KNeighborsClassifier(n_neighbors=5)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)


class ModelFactory:

    @staticmethod
    def create_model(model_type: str) -> MLModel:

        models = {
            "logistic_regression": LogisticRegressionModel,
            "decision_tree": DecisionTreeModel,
            "knn": KNNModel,
        }

        if model_type not in models:
            raise ValueError(f"Nepoznat model: {model_type}")

        return models[model_type]()


# STRATEGY PATTERN

class MetricStrategy(ABC):

    @abstractmethod
    def calculate(self, y_true, y_pred):
        pass


class AccuracyStrategy(MetricStrategy):

    def calculate(self, y_true, y_pred):
        return accuracy_score(y_true, y_pred)


class PrecisionStrategy(MetricStrategy):

    def calculate(self, y_true, y_pred):
        return precision_score(
            y_true, y_pred, average="weighted", zero_division=0
        )


class RecallStrategy(MetricStrategy):

    def calculate(self, y_true, y_pred):
        return recall_score(
            y_true, y_pred, average="weighted", zero_division=0
        )


class F1Strategy(MetricStrategy):

    def calculate(self, y_true, y_pred):
        return f1_score(
            y_true, y_pred, average="weighted", zero_division=0
        )


# OBSERVER PATTERN

class Observer(ABC):

    @abstractmethod
    def update(self, message: str):
        pass


class TrainingLogger(Observer):

    def update(self, message: str):
        print(f"[OBSERVER] {message}")


class ExperimentMonitor:

    def __init__(self):
        self.observers = []

    def subscribe(self, observer: Observer):
        self.observers.append(observer)

    def notify(self, message: str):
        for observer in self.observers:
            observer.update(message)


# DECORATOR PATTERN

def measure_time(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        end = time.perf_counter()

        print(
            f"[DECORATOR] Vrijeme izvrsavanja: "
            f"{end - start:.6f} sekundi"
        )

        return result

    return wrapper


# TEMPLATE METHOD PATTERN

class ExperimentTemplate(ABC):

    def __init__(self, model, metrics, monitor):
        self.model = model
        self.metrics = metrics
        self.monitor = monitor
        self.results = {}

    def run(self, X_train, X_test, y_train, y_test):
        self.monitor.notify("Eksperiment je zapocet.")

        self.prepare_data(X_train, X_test, y_train, y_test)
        self.train_model()
        self.evaluate_model()
        self.show_results()

        self.monitor.notify("Eksperiment je zavrsen.")

        return self.results

    @abstractmethod
    def prepare_data(self, X_train, X_test, y_train, y_test):
        pass

    def train_model(self):
        self.monitor.notify("Treniranje modela je zapoceto.")
        self.model.train(self.X_train, self.y_train)
        self.monitor.notify("Treniranje modela je zavrseno.")

    def evaluate_model(self):
        predictions = self.model.predict(self.X_test)

        for name, metric in self.metrics.items():
            self.results[name] = metric.calculate(
                self.y_test, predictions
            )

    def show_results(self):
        print("Rezultati eksperimenta:")

        for name, value in self.results.items():
            print(f"{name}: {value:.4f}")


class ClassificationExperiment(ExperimentTemplate):

    def prepare_data(self, X_train, X_test, y_train, y_test):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test


# POVEZIVANJE SVIH OBRAZACA

@measure_time
def run_experiment(model_name, X_train, X_test, y_train, y_test):

    model = ModelFactory.create_model(model_name)

    metrics = {
        "Accuracy": AccuracyStrategy(),
        "Precision": PrecisionStrategy(),
        "Recall": RecallStrategy(),
        "F1-score": F1Strategy(),
    }

    monitor = ExperimentMonitor()
    monitor.subscribe(TrainingLogger())

    experiment = ClassificationExperiment(
        model=model,
        metrics=metrics,
        monitor=monitor
    )

    return experiment.run(
        X_train, X_test, y_train, y_test
    )


# DEMONSTRACIJA NA IRIS SKUPU PODATAKA

def main():

    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model_names = [
        "logistic_regression",
        "decision_tree",
        "knn",
    ]

    all_results = []

    for model_name in model_names:
        print("\n" + "=" * 50)
        print("MODEL:", model_name.upper())
        print("=" * 50)

        results = run_experiment(
            model_name,
            X_train,
            X_test,
            y_train,
            y_test
        )

        results["Model"] = model_name
        all_results.append(results)

    for result in all_results:
        print(result)


if __name__ == "__main__":
    main()
