class NextBoxNotifier:
    def __init__(self):
        self.next_box_type_observers = []

    def add_next_box_type_observer(self, observer):
        self.next_box_type_observers.append(observer)

    def remove_next_box_type_observer(self, observer):
        self.next_box_type_observers.remove(observer)

    def call_next_box_type_observers(self, nex_box_type):
        for o in self.next_box_type_observers:
            o.update(nex_box_type)
