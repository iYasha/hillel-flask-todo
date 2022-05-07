from crud.base import BaseCRUD


class ArticleCRUD(BaseCRUD):
	_file_path = 'data/articles.json'


article_crud = ArticleCRUD()
