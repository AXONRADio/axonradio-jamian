import os
from flask import Flask, jsonify, url_for, redirect, request, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import requests
from flask_cors import CORS
import random
import predictions
from bson.json_util import dumps

##change this to set the score before songs won't be played##
score_threshold = -5

class CustomFlask(Flask):
  jinja_options = Flask.jinja_options.copy()
  jinja_options.update(dict(
    block_start_string='(%',
    block_end_string='%)',
    variable_start_string='((',
    variable_end_string='))',
    comment_start_string='(#',
    comment_end_string='#)',
  ))

app = CustomFlask(__name__,
                  static_folder = "./dist/static",
                  template_folder = "./dist")

cors = CORS(app, resources={r"/api/*": {"origins":"http://localhost:5000"}})
cors = CORS(app, resources={r"/api/*": {"origins":"http://167.99.98.179:5000"}})
# app.config['MONGO_HOST'] = os.environ['DB_PORT_27017_TCP_ADDR']
# app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'song_db'
mongo = PyMongo(app, config_prefix='MONGO')

def jazz():
    count = mongo.db.jazz.count()
    return mongo.db.jazz.find({"score": {"$gt": score_threshold}})[random.randrange(count)]

def rock():
    count = mongo.db.rock.count()
    return mongo.db.rock.find({"score": {"$gt": score_threshold}})[random.randrange(count)]

def blues():
    count = mongo.db.blues.count()
    return mongo.db.blues.find({"score": {"$gt": score_threshold}})[random.randrange(count)]

def pop():
    count = mongo.db.pop.count()
    return mongo.db.pop.find({"score": {"$gt": score_threshold}})[random.randrange(count)]

def reggae():
    count = mongo.db.reggae.count()
    return mongo.db.reggae.find({"score": {"$gt": score_threshold}})[random.randrange(count)]

def hiphop():
    count = mongo.db.hiphop.count()
    return mongo.db.hiphop.find({"score": {"$gt": score_threshold}})[random.randrange(count)]

def disco():
    count = mongo.db.disco.count()
    return mongo.db.disco.find({"score": {"$gt": score_threshold}})[random.randrange(count)]

def country():
    count = mongo.db.country.count()
    return mongo.db.country.find({"score": {"$gt": score_threshold}})[random.randrange(count)]

def classical():
    count = mongo.db.classical.count()
    return mongo.db.classical.find({"score": {"$gt": score_threshold}})[random.randrange(count)]

def metal():
    count = mongo.db.metal.count()
    return mongo.db.metal.find({"score": {"$gt": score_threshold}})[random.randrange(count)]



##############################################################


def jazzUp(id, updown):
    if updown:
        mongo.db.jazz.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': 1
          }
        }, upsert=False)
    else:
        mongo.db.jazz.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': -1
          }
        }, upsert=False)

def rockUp(id, updown):
    if updown:
        mongo.db.rock.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': 1
          }
        }, upsert=False)
    else:
        mongo.db.rock.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': -1
          }
        }, upsert=False)
def bluesUp(id, updown):
    if updown:
        mongo.db.blues.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': 1
          }
        }, upsert=False)
    else:
        mongo.db.blues.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': -1
          }
        }, upsert=False)
def popUp(id, updown):
    if updown:
        mongo.db.pop.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': 1
          }
        }, upsert=False)
    else:
        mongo.db.pop.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': -1
          }
        }, upsert=False)
def reggaeUp(id, updown):
    if updown:
        mongo.db.reggae.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': 1
          }
        }, upsert=False)
    else:
        mongo.db.reggae.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': -1
          }
        }, upsert=False)
def hiphopUp(id, updown):
    if updown:
        mongo.db.hiphop.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': 1
          }
        }, upsert=False)
    else:
        mongo.db.hiphop.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': -1
          }
        }, upsert=False)
def discoUp(id, updown):
    if updown:
        mongo.db.disco.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': 1
          }
        }, upsert=False)
    else:
        mongo.db.disco.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': -1
          }
        }, upsert=False)
def countryUp(id, updown):
    if updown:
        mongo.db.country.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': 1
          }
        }, upsert=False)
    else:
        mongo.db.country.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': -1
          }
        }, upsert=False)

def classicalUp(id, updown):
    if updown:
        mongo.db.classical.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': 1
          }
        }, upsert=False)
    else:
        mongo.db.classical.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': -1
          }
        }, upsert=False)

def metalUp(id, updown):
    if updown:
        mongo.db.metal.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': 1
          }
        }, upsert=False)
    else:
        mongo.db.metal.update({
          '_id': ObjectId(id)
        },{
          '$inc': {
          'score': -1
          }
        }, upsert=False)

def countSwitch(arg):
    switcher = {
        'jazz': jazz,
        'rock': rock,
        'blues': blues,
        'pop': pop,
        'reggae': reggae,
        'hiphop': hiphop,
        'disco': disco,
        'country': country,
        'classical': classical,
        'metal': metal
    }
    func = switcher.get(arg, lambda:'invalid genre')
    return func()

#if arg3 is true then score goes up if else score goes down
def updateSwitch(arg1, arg2, arg3):
    switcher = {
        'jazz': jazzUp,
        'rock': rockUp,
        'blues': bluesUp,
        'pop': popUp,
        'reggae': reggaeUp,
        'hiphop': hiphopUp,
        'disco': discoUp,
        'country': countryUp,
        'classical': classicalUp,
        'metal': metalUp
    }
    func = switcher.get(arg1, lambda:'invalid genre')
    return func(arg2, arg3)


# route to the static vue build or the local host
# when running on dev server
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

# endpoint for a random video query by genre
@app.route('/api/video/', methods=['GET', 'POST'])
def get_random_video():
    gid = request.args.get('genre')
    ret = countSwitch(gid)
    return jsonify({"name": ret['name'], "genre": ret['genre'],
                    "vidID":ret['vidID'], "mean": ret['mean'],
                    "id": str(ret['_id']), "score": ret['score']})


# endpoint for the database count() content
@app.route('/api/data/', methods=['GET'])
def get_db_data():
    ret = [
        mongo.db.blues.count(),
        mongo.db.classical.count(),
        mongo.db.country.count(),
        mongo.db.disco.count(),
        mongo.db.hiphop.count(),
        mongo.db.jazz.count(),
        mongo.db.metal.count(),
        mongo.db.pop.count(),
        mongo.db.reggae.count(),
        mongo.db.rock.count()
    ]
    total = 0
    for i in range(0, len(ret)):
        total += ret[i]
    return jsonify({"collections": ret, "total": total})

@app.route('/api/top/', methods=['GET'])
def get_top_songs():
    ret = {
       "jazz": mongo.db.jazz.find({},{"name": 1, "vidID":1, "_id":0}).limit(1).sort("score", -1)[0],
       "rock": mongo.db.rock.find({},{"name": 1, "vidID":1, "_id":0}).limit(1).sort("score", -1)[0],
       "blues": mongo.db.blues.find({},{"name": 1, "vidID":1, "_id":0}).limit(1).sort("score", -1)[0],
       "pop": mongo.db.pop.find({},{"name": 1, "vidID":1, "_id":0}).limit(1).sort("score", -1)[0],
       "reggae": mongo.db.reggae.find({},{"name": 1, "vidID":1, "_id":0}).limit(1).sort("score", -1)[0],
       "hiphop": mongo.db.hiphop.find({},{"name": 1, "vidID":1, "_id":0}).limit(1).sort("score", -1)[0],
       "disco": mongo.db.disco.find({},{"name": 1, "vidID":1, "_id":0}).limit(1).sort("score", -1)[0],
       "country": mongo.db.country.find({},{"name": 1, "vidID":1, "_id":0}).limit(1).sort("score", -1)[0],
       "classical": mongo.db.classical.find({},{"name": 1, "vidID":1, "_id":0}).limit(1).sort("score", -1)[0],
       "metal": mongo.db.metal.find({},{"name": 1, "vidID":1, "_id":0}).limit(1).sort("score", -1)[0],
    }
    return jsonify(ret)

#localhost:5000/api/upvote/?genre=metal&songID=5adfab685db15f2f1e9c3569
@app.route('/api/upvote/', methods=['GET','POST'])
def upvote():
    gid = request.args.get('genre')
    sid = request.args.get('songID')
    updateSwitch(gid, sid, True)
    return "Song upvoted!"

@app.route('/api/downvote/', methods=['GET','POST'])
def downvote():
    gid = request.args.get('genre')
    sid = request.args.get('songID')
    updateSwitch(gid, sid, False)
    return "Song downvoted!"

@app.route('/api/predict', methods=['GET', 'POST'])
def predict():
    link = request.args.get('vid_id')
    info = predictions.get_genre(link)
    return jsonify(info)

#endpoint for background prediction task
@app.route('/tasks/predict/', methods=['GET'])
def get_prediction():
    predictions.get_genre()
    return "song succesfully classified"

# make sure to remove debug mode in production
if __name__ == '__main__':
    app.run(host='0.0.0.0')
