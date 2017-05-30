import mnist_loader
import sys
arg1 = sys.argv[1]
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
import neural_network
net = neural_network.Network([784,30,10], cost = neural_network.CrossEntropyCost)
net.large_weight_initializer()
net.SGD(training_data[:1000], int(arg1), 10, 0.5, evaluation_data=test_data, lmbda = 0.1, monitor_evaluation_cost=True, monitor_evaluation_accuracy=True, monitor_training_cost=True, monitor_training_accuracy=True)