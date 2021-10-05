import numpy as np
import torch
import networkx as nx
import matplotlib.pyplot as plt
import random

class Maps(object):
    def __init__(self,graph, timeHorizon, init_attacker,init_defenders, exits):
        g = nx.from_dict_of_lists(graph)
        map_adjlist = graph
        max_actions = 0
        for node in map_adjlist:
            map_adjlist[node].sort()
            if len(map_adjlist[node]) > max_actions:
                max_actions = len(map_adjlist[node])
        self.num_nodes = len(map_adjlist)
        self.adjlist = map_adjlist
        self.defender_init = [init_defenders]
        self.attacker_init = init_attacker
        self.exits = exits
        self.num_defender = len(self.defender_init[0])
        self.max_actions = pow(max_actions, self.num_defender)
        self.graph = g
        self.embedding_size= 32
        self.hidden_size= 64
        self.relevant_v_size= 64
        self.size = None

        self.time_horizon=timeHorizon

