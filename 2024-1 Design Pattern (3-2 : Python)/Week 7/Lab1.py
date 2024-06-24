# Implementor API
class TestUnit:
    def start_test(self):
        pass

class Dijkstra(TestUnit):
    def start_test(self):
        print("Starting Dijkstra Test")

class MinimumSpanningTree(TestUnit):
    def start_test(self):
        print("Starting Minimum Spanning Tree Test")

class A_Star(TestUnit):
    def start_test(self):
        print("Starting A_Star Test")


# Abstraction API
class System:
    def __init__(self, test_unit: TestUnit):
        self.test_unit = test_unit

    def run_test(self):
        pass

class Android(System):
    def run_test(self):
        print("Android:")
        self.test_unit.start_test()

class IOS(System):
    def run_test(self):
        print("IOS:")
        self.test_unit.start_test()

dijkstra = Dijkstra()
ios = IOS(dijkstra)
ios.run_test()