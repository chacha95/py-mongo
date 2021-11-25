from pymongo import MongoClient
from multiprocessing import Lock
import traceback


class ChallengeDB:
    client = None
    _mutex = Lock()

    @classmethod
    def init_db(cls, host: str, port: int, user: str, pwd: str) -> None:
        cls.client = MongoClient(host=host, port=port, username=user, password=pwd)

    @classmethod
    def insert(cls, db: str, collection: str, record: dict):
        with cls._mutex:
            try:
                # create db or connect
                db = cls.client[db]

                # create collection or connect
                coll = db[collection]

                # insert record
                x = coll.insert_one(record)

            except Exception as e:
                print(traceback.format_exc())

            finally:
                cls.client.close()

    @classmethod
    def read(cls, db: str, collection: str):
        with cls._mutex:
            try:
                db = cls.client[db]
                coll = db[collection]

                return coll.find()
            except Exception as e:
                print(traceback.format_exc())

            finally:
                cls.client.close()

    @classmethod
    def read_query(cls, db: str, collection: str, query: dict):
        with cls._mutex:
            try:
                db = cls.client[db]
                coll = db[collection]

                return coll.find({}, query)

            except Exception as e:
                print(traceback.format_exc())

            finally:
                cls.client.close()


def init_db():
    # pymongo db client
    ChallengeDB.init_db(host="localhost", port=27017, user="root", pwd="return123")
    challenges = {
        "4l5qtrv84gup": {
            "create_time": "2019-09-28 04:32:22",
            "title": "Growing Hunter",
            "challenge_id": "4l5qtrv84gup",
            "metrics": ["diam", "maecenas"],
        },
        "4whxst3yztaw": {
            "create_time": "2019-12-02 04:30:29",
            "title": "The Dwindling Streams",
            "challange_id": "4whxst3yztaw",
            "metrics": ["sit", "amet", "aliquam"],
        },
        "e02758q786bm": {
            "create_time": "2018-05-11 13:50:46",
            "title": "Storms of Snake",
            "challenge_id": "e02758q786bm",
            "metrics": ["pharetra"],
        },
        "tvupalv94okr": {
            "create_time": "2018-09-18 10:20:05",
            "title": "The Star's Ring",
            "challenge_id": "tvupalv94okr",
            "metrics": ["consequat", "nisl", "vel", "pretium"],
        },
        "y3gjz3a6obve": {
            "create_time": "2019-07-18 06:44:43",
            "title": "The Touch of the Force",
            "challenge_id": "y3gjz3a6obve",
            "metrics": ["pretium", "nibh", "ipsum"],
        },
    }
    ChallengeDB.insert(
        db="metadata", collection="4l5qtrv84gup", record=challenges["4l5qtrv84gup"]
    )
    ChallengeDB.insert(
        db="metadata", collection="4whxst3yztaw", record=challenges["4whxst3yztaw"]
    )
    ChallengeDB.insert(
        db="metadata", collection="e02758q786bm", record=challenges["e02758q786bm"]
    )
    ChallengeDB.insert(
        db="metadata", collection="tvupalv94okr", record=challenges["tvupalv94okr"]
    )
    ChallengeDB.insert(
        db="metadata", collection="y3gjz3a6obve", record=challenges["y3gjz3a6obve"]
    )