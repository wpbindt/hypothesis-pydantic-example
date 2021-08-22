import hashlib

import pydantic


class Thing(pydantic.BaseModel):
    content: str


class NestedObject(pydantic.BaseModel):
    name: str
    things: list[Thing]


def _prepare_for_hashing(nested_object: NestedObject) -> NestedObject:
    nested_object_copy = nested_object.copy(deep=True)
    nested_object_copy.things = sorted(nested_object_copy.things, key=lambda thing: thing.content)
    return nested_object_copy


def hash_function(nested_object: NestedObject) -> str:
    m = hashlib.md5()
    hashable = _prepare_for_hashing(nested_object)
    m.update(bytes(hashable.json(), 'utf-8'))
    return m.hexdigest()
