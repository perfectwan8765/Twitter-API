from .. import models


def get_all(db) :
    celerbrity_tweets = db.query(models.Celerbrity_Tweet).all()
    return celerbrity_tweets

def get(celerbrity_name, start_date, end_date, db) :
    celerbrity_tweets = db.query(models.Celerbrity_Tweet).filter(models.Celerbrity_Tweet.celerbrity == celerbrity_name)

    if start_date :
        celerbrity_tweets = celerbrity_tweets.filter(models.Celerbrity_Tweet.created_at >= start_date)
    
    if end_date :
        celerbrity_tweets = celerbrity_tweets.filter(models.Celerbrity_Tweet.created_at <= end_date)

    return celerbrity_tweets.all()