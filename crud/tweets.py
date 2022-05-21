from crud.base import BaseCRUD


class TweetCRUD(BaseCRUD):
	_file_path = 'data/tweets.json'


tweet_crud = TweetCRUD()
