from pydantic import BaseModel, validator
import uuid
from datetime import datetime
from datetime import datetime


class Tweet(BaseModel):
	id: str = str(uuid.uuid4())
	text: str
	author: str
	created_at: str = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
