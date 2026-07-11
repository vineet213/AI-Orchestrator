from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Task:
    title: str
    description: str

    status: str = "pending"
    priority: str = "normal"

    steps: List[str] = field(default_factory=list)

    created_at: datetime = field(default_factory=datetime.now)