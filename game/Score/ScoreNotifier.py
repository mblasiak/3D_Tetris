class ScoreNotifier:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def call_observer(self,score):
        for o in self.observers:
            o.update(score)
