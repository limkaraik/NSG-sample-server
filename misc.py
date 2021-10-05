import json
import networkx as nx

def parseJsonData():
    #initialise data
    data= {}
    # Opening JSON file
    try:
        f = open('yishun.json')
        # returns JSON object as a dictionary into data
        data = json.load(f)
    except:
        print("error loading file")
        return None

    #gets all the data
    timeHorizon, attacker,defenders,graph,exits = None,None,None,None,None
    if data.get('timeHorizon')==None:
        print('timeHorizon is missing')
        return None
    else:
        timeHorizon = data['timeHorizon']
    if data.get('attacker')==None:
        print('attacker is missing')
        return None
    else:
        attacker = data['attacker']
    if data.get('defenders')==None:
        print('defenders is missing')
        return None
    else:
        defenders = data['defenders']
    if data.get('graph')==None:
        print('graph is missing')
        return None
    else:
        graph = data['graph']
        try:
            new_graph= {}
            for k,v in graph.items():
                new_graph[int(k)] = v
            graph= new_graph
        except:
            print('Invalid graph data')
            return None
    if data.get('exits')==None:
        print('exits is missing')
        return None
    else:
        exits = data['exits']
    return [graph,timeHorizon, attacker,defenders,exits]
