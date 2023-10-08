from kfp import dsl
from math_utils import add_numbers

@dsl.component(base_image='python:3.7',
               target_image='gcr.io/epishova-joonix-sandbox/my-component:v1')
def add(a: int, b: int) -> int:
    return add_numbers(a, b)
