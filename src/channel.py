import os
import json
from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel = None
        self.channel_id = channel_id
        self.API_KEY = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.API_KEY)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.channel = json.dumps(self.channel, indent=2, ensure_ascii=False)
        print(f"{self.channel}")

