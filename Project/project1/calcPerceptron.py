import perceptron as Perceptron

class calcPerceptron():
    def __init__(self, threshold):
        self._threshold = threshold

    def isNeuronActivate(self, *perceptrons: Perceptron) -> int:
        inputSignalSum = 0

        for perceptron in perceptrons:
            inputSignalSum += perceptron.outputSignal()
        
        if (inputSignalSum <= self._threshold):
            return 0
        else:
            return 1