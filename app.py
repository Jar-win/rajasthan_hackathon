#!/usr/bin/ python
from flask import abort
import random
from flask import Flask, jsonify
app = Flask(__name__)

'''
tasks = [
    {
        'id': 1,
        'title': u'something',
        'description': u'APple, banana, pomogranade, kiwi', 
        'done': True
    },
    {
        'id': 2,
        'title': u'Something more',
        'description': u'Loreum Ipsum', 
        'done': False
    }
]


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
'''

@app.route('/api/v1.0/<float:lat>@<float:longt>|<float:dlat>@<float:dlongt>', methods=['GET'])
def get_coordinate(lat, longt, dlat, dlongt):
    """
    import direction_handler
    direction_json = direction_handler.get_direction_json(lat, longt, dlat, dlongt)
    for step in direction_json['legs'][0]['steps']:
      try:
        if step['maneuver'] == 'turn-left' or step['maneuver'] == 'turn-slight-left':
            continue
        get_speed_stat(step)
      except (KeyError, IndexError) as e:
            continue
    """
    random_speed = random.randint(5,80)
    return jsonify({'speed': random_speed, "callback_time":random_speed})

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=8090)

