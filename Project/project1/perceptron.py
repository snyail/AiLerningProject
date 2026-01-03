class Perceptron():
    def __init__(self, input_signal: int, weight: int):
        self._inpit_signal = input_signal
        self._weight = weight
    
    def outputSignal(self):
        return self._inpit_signal * self._weight