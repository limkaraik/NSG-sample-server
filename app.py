import flask
from flask_cors import CORS, cross_origin
from env import *
from misc import *
from maps import *
from agent import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#get data from the json file
graph,timeHorizon, init_attacker,init_defenders,exits = parseJsonData()
#initialise environment, defender etc...
environment=Env(graph, timeHorizon, init_attacker, tuple(init_defenders), exits)
game_state=environment.reset()
Map = Maps(graph,timeHorizon,init_attacker,tuple(init_defenders),exits)
defender=AgentEval(Map)

#reset and initialise the game 
@app.route("/api/reset", methods=["GET"])
@cross_origin()
def reset():
    global Map
    global defender
    global game_state
    global environment
    #get data from the json file
    graph,timeHorizon, init_attacker,init_defenders,exits = parseJsonData()
    #initialise environment, defender etc...
    environment=Env(graph, timeHorizon, init_attacker, tuple(init_defenders), exits)
    Map = Maps(graph,timeHorizon,init_attacker,tuple(init_defenders),exits)
    defender=AgentEval(Map)
    game_state=environment.reset()
    return flask.jsonify({'success': True})

#when the player select actions to move, return a list of next defenders positions
#/api/move?node=attacker_new_pos
@app.route("/api/move", methods=["GET"])
@cross_origin()
def move():
    global game_state
    global defender
    global environment
    try:
        #get attacker pos from request params
        attacker_a = int(flask.request.args.get('node'))
        defender_obs, attacker_obs = game_state.obs()
        def_current_legal_action, att_current_legal_action = game_state.legal_action()
        defender_a = defender.select_action([defender_obs], [def_current_legal_action])
        print(defender_a)
        game_state = environment.simu_step(defender_a, attacker_a)
        return flask.jsonify({'success': True, 'defenders':[int(i) for i in defender_a]})
    except Exception as e:
        print(e)
        return flask.jsonify({'success': False})

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)