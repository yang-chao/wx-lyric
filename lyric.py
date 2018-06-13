from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config["DEBUG"] = True
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
	username="root",
	password="root",
	hostname="140.143.12.108",
	databasename="music")
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Music(db.Model):
	__tablename__= 'music'

	id = db.Column(db.String(32), primary_key=True)
	name = db.Column(db.String(1000))
	artist = db.Column(db.String(30))
	style = db.Column(db.String(20))
	language = db.Column(db.String(10))

class Lyric(db.Model):
	__tablename__= 'lyric'
	id = db.Column(db.Integer, primary_key=True)
	music_id = db.Column(db.String(32))
	language = db.Column(db.String(1000))


@app.route("/music", methods=['GET'])
def get_all_music():
	musicList = db.session.query(Music).all()
	return str(rv)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)