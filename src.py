import hashlib

import pydantic


class Thing(pydantic.BaseModel):
    content: str


class NestedObject(pydantic.BaseModel):
    name: str
    things: list[Thing]


def hash_function(nested_object: NestedObject) -> str:
    m = hashlib.md5()
    m.update(nested_object.json())
    return m.hexdigest()