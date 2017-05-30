import mnist_loader
import sys
arg1 = sys.argv[1]
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
import network
net = network.Network([784,30,10])
net.SGD(training_data, int(arg1), 10, 3.0, test_data=test_data)