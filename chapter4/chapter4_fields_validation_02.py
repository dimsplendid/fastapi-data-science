import time
from datetime import datetime

from pydantic import BaseModel, Field

def list_factory():
    return ["a", "b", "c"]

class Model(BaseModel):
    l: list[str] = Field(default_factory=list_factory)
    d: datetime = Field(default_factory=datetime.now)
    l2: list[str] = Field(default_factory=list)

m1 = Model()
time.sleep(1)
m2 = Model()

print(m1)
print(m2)