import random
import argparse


parser = argparse.ArgumentParser(description="gossip protocol simulator")
parser.add_argument('-n', type=int, action='store', default=9, help='total numbers of nodes')
parser.add_argument('-i', type=int, action='store', default=1, help='iterations')
parser.add_argument('--double', action='store_true', help='use double activation')
args = parser.parse_args()


total_nodes = args.n
total_iterations = args.i
results = []
iterations = 0   # counter for iterations


class CustomNode(object):

    def __init__(self, x):
        self.state = False
        self.x = x
        self.repeat = args.double



for _ in range(total_iterations):

    x = random.randint(4, 6)    # how many attempts to send packet
    nodes = [CustomNode(x) for i in range(total_nodes)]
    infected_nodes = []
    current = random.choice(nodes)  # choosing which node will start send packets
    current.state = True
    infected_nodes.append(current)


    for node in infected_nodes:
        while node.x:   # start broadcasting
            random_node = random.choice(nodes)

            if node == random_node: # node can't send packet to yourself
                continue

            if random_node in infected_nodes:

                if node.repeat: # im my algorithm is activated
                    node.repeat = False
                    continue

                else:
                    break   # stop broadcasting

            else:
                random_node.state = True    # infect node
                infected_nodes.append(random_node)

            node.x -= 1
        iterations += 1

    results.append(len(infected_nodes))


percent = map(lambda x: x/total_nodes*100, results)
print("in {:.2f} % cases all nodes received the packet".format(sum(percent) / len(results)))
print("total iterations: {}".format(iterations))


