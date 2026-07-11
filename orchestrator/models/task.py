from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    title: str
    description: str

    status: str = "pending"
    priority: str = "normal"

    created_at: datetime = field(default_factory=datetime.now)