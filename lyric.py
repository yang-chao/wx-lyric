#coding:utf-8
from flask import Flask, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
import json, md5

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

class Artist(db.Model):
	__tablename__= 'artist'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	country = db.Column(db.String(10))
	sex = db.Column(db.String(1))

class Music(db.Model):
	__tablename__= 'music'

	id = db.Column(db.String(32), primary_key=True)
	name = db.Column(db.String(100))
	style = db.Column(db.String(10))
	language = db.Column(db.String(4))
	album = db.Column(db.String(20))

class Lyric(db.Model):
	__tablename__= 'lyric'

	id = db.Column(db.Integer, primary_key=True)
	music_id = db.Column(db.String(32))
	artist_id = db.Column(db.Integer)
	sentence = db.Column(db.String(200))


@app.route("/music", methods=['GET'])
def get_all_music():
	musicArray = []
	lyricList = db.session.query(Lyric).all()
	for lyric in lyricList:
		musicList = db.session.query(Music).filter(Music.id==lyric.music_id).all()
		if musicList and musicList[0]:
			musicObj = {}
			musicObj['id'] = lyric.id
			musicObj['lyric'] = lyric.sentence
			musicObj['name'] = musicList[0].name
			musicObj['artist'] = musicList[0].artist
			musicObj['style'] = musicList[0].style
			musicObj['language'] = musicList[0].language
			musicArray.append(musicObj)
	return Response(json.dumps(musicArray), mimetype="text/json")

@app.route("/music/add", methods=['GET', 'POST'])
def add_music():
	if request.method == 'GET':
		return render_template('music_add.html')
	else:
		musics = request.form['musics']
		result = {}
		if musics:
			lines = musics.split('\n')
			for line in lines:
				print('line: ' + line)
				elements = line.split('|')
				m = md5.new()
				m.update((elements[0] + '+' + elements[1]).encode(encoding='utf-8'))
				id = m.hexdigest()
				print('id: ' + id)
				sentence = elements[4]
				print('sentence: ' + sentence)

				# insert into music
				music = Music(id=id, name=elements[0], artist=elements[1], style=elements[2],
					language=elements[3])
				db.session.merge(music)

				# insert into lyric
				lyric = Lyric(music_id=id, sentence=sentence.replace('\r',''))
				db.session.add(lyric)

			db.session.commit()
			db.session.close()
			result['code'] = 0
		else:
			result['code'] = 1
		return Response(json.dumps(result), mimetype="text/json")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)