from hypothesis import given
import hypothesis.strategies as st

from src import Thing, NestedObject, hash_function


@given(st.lists(st.text()))
def test_hash_function_is_well_defined(contents):
    nested_object = NestedObject(
        name='whatevs',
        things=[Thing(content=content) for content in contents]
    )

    first_pass = hash_function(nested_object)
    second_pass = hash_function(nested_object)
    assert first_pass == second_pass


@given(st.lists(st.text()))
def test_hash_function_is_well_defined(contents):
    nested_object = NestedObject(
        name='whatevs',
        things=[Thing(content=content) for content in contents]
    )
    nested_object2 = nested_object.copy(deep=True)
    nested_object2.things = nested_object2.things[::-1]

    assert hash_function(nested_object) == hash_function(nested_object2)
