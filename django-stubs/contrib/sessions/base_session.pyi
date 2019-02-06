from datetime import datetime
from typing import Any, Dict, Optional

from django.db import models

class BaseSessionManager(models.Manager):
    creation_counter: int
    model: None
    name: None
    def encode(self, session_dict: Dict[str, int]) -> str: ...
    def save(self, session_key: str, session_dict: Dict[str, int], expire_date: datetime) -> AbstractBaseSession: ...

class AbstractBaseSession(models.Model):
    session_key: Any = ...
    session_data: Any = ...
    expire_date: Any = ...
    objects: Any = ...
    @classmethod
    def get_session_store_class(cls) -> None: ...
    def get_decoded(self) -> Dict[str, int]: ...
