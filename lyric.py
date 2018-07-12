# coding:utf-8
from flask import Flask, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
from spider import spider
import json
import md5
import random
import numpy as np

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
    __tablename__ = 'artist'

    _id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer)
    name = db.Column(db.String(20))
    avatar = db.Column(db.String(200))
    kind = db.Column(db.String(7))
    sex = db.Column(db.String(1))


class Music(db.Model):
    __tablename__ = 'music'

    _id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer)
    name = db.Column(db.String(100))
    artist = db.Column(db.String(50))
    album = db.Column(db.String(20))


class Lyric(db.Model):
    __tablename__ = 'lyric'

    id = db.Column(db.Integer, primary_key=True)
    music_id = db.Column(db.String(32))
    artist_id = db.Column(db.Integer)
    sentence = db.Column(db.String(200))


@app.route("/music", methods=['GET'])
def get_all_music():
    musicArray = []
    lyricList = db.session.query(Lyric).all()
    for lyric in lyricList:
        musicList = db.session.query(Music).filter(
            Music.id == lyric.music_id).all()
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
                m.update((elements[0] + '+' + elements[1]
                          ).encode(encoding='utf-8'))
                id = m.hexdigest()
                print('id: ' + id)
                sentence = elements[4]
                print('sentence: ' + sentence)

                # insert into music
                music = Music(id=id, name=elements[0], artist=elements[1], style=elements[2],
                              language=elements[3])
                db.session.merge(music)

                # insert into lyric
                lyric = Lyric(music_id=id, sentence=sentence.replace('\r', ''))
                db.session.add(lyric)

            db.session.commit()
            db.session.close()
            result['code'] = 0
        else:
            result['code'] = 1
        return Response(json.dumps(result), mimetype="text/json")


@app.route('/spider/artist/add')
def insertArtists():
    ids = [1001, 1002, 1003, 2001, 2002, 2003]
    kind = ['华语', '华语', '华语', '欧美', '欧美', '欧美']
    sex = ['男', '女', '组合', '男', '女', '组合']
    for index in range(len(ids)):
        artists = spider.fetchArtists(ids[index])['artists']
        for artist in artists:
            newArtist = Artist(
                id=artist['id'], name=artist['name'], avatar=artist['img1v1Url'],
                kind=kind[index], sex=sex[index])
            db.session.add(newArtist)
    db.session.commit()
    db.session.close()
    return Response(json.loads('{"code": 0}'), mimetype="text/json")


# @app.route('/spider/music/add')
# def insertMusics():
#     allArtist = db.session.query(Artist).offset(100).limit(100).all()
#     print('allArtist length: ' + str(len(allArtist)))
#     for artist in allArtist:
#         hotMusics = spider.fetchMusics(artist.id)
#         print('hotMusics id: ' + str(artist.id))
#         print('hotMusics length: ' + str(len(hotMusics)))
#         for music in hotMusics:
#             newMusic = Music(id=music['id'], name=music['name'],
#                              artist=artist.name, album=music['al']['name'])
#             db.session.add(newMusic)
#     db.session.commit()
#     db.session.close()
#     return Response(json.loads('{"code": 0}'), mimetype="text/json")


@app.route('/topic')
def getTopic():
    # 随机选取一个歌词
    sql = "SELECT * FROM {table} AS t1 JOIN (SELECT ROUND(RAND() * ((SELECT MAX(id) FROM {table})-(SELECT MIN(id) FROM {table}))+(SELECT MIN(id) FROM {table})) AS id) AS t2 WHERE t1.id >= t2.id ORDER BY t1.id LIMIT 1;".format(table='lyric')
    result = db.engine.execute(sql)
    for r in result:
        print(r.sentence)
    topic = {}
    if r:
        # 查询歌曲
        musicResult = db.session.query(Music).filter(
            Music.id == r.music_id).first()
        print('music name: ' + musicResult.name)

        # 查询歌手
        artistResult = db.session.query(Artist).filter(
            Artist.id == r.artist_id).first()
        print('artist name: ' + artistResult.name)

        # 随机查询歌手的其它歌曲
        answer = []
        # connection = db.engine.connect()
        # for index in range(3):
        #     musicSql = u"SELECT * FROM {table} AS t1 JOIN (SELECT ROUND(RAND() * ((SELECT MAX(id) FROM {table})-(SELECT MIN(id) FROM {table}))+(SELECT MIN(id) FROM {table})) AS id) AS t2 WHERE t1.id >= t2.id AND t1.artist = '{artist}' ORDER BY t1.id LIMIT 1;".format(
        #         table='music',
        #         artist=artistResult.name)
        #     randomMusic = connection.execute(musicSql).first()
        #     print('index: ' + str(index))
        #     answer.append(randomMusic.name)
 
        wrongAnswers = db.session.query(Music).filter(Music.artist==artistResult.name, 
            Music.artist!=musicResult.name).all()

        wrongArr = []
        for wa in wrongAnswers:
            wrongArr.append(wa)
        randomArr = np.random.permutation(len(wrongArr))
        print(randomArr)
        for i in randomArr[0:3]:
            answer.append(wrongArr[i].name)
        
        correctIndex = random.randint(0, 3)
        answer.insert(correctIndex, musicResult.name)

        topic['question'] = r.sentence
        topic['answer'] = answer
        topic['correctAnswer'] = correctIndex
        topic['type'] = 1
        topic['artist'] = artistResult.name
    else:
        topic['error'] = 1
    return Response(json.dumps(topic), mimetype="text/json")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
