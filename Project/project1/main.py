from calcPerceptron import calcPerceptron
from perceptron import Perceptron

def main():
    node_1 = Perceptron(3, 0.2)
    node_2 = Perceptron(3, 0.3)

    calc_perceptron = calcPerceptron(10)

    print(calc_perceptron.isNeuronActivate(
        node_1,
        node_2
    ))

    node_3 = Perceptron(3, 10)

    print(calc_perceptron.isNeuronActivate(
        node_1,
        node_2,
        node_3
    ))

if __name__ == "__main__":
    main()