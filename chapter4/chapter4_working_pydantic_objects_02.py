from datetime import date
from enum import Enum

from pydantic import BaseModel, ValidationError

class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"

class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str

class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: list[str]
    address: Address

person = Person(
    first_name="John",
    last_name="Doe",
    gender=Gender.MALE,
    birthdate="1991-01-01",
    interests=["travel", "sports"],
    address={
        "street_address": "12 S Street",
        "postal_code": "424242",
        "city": "Woodtown",
        "country": "US",
    },
)

person_include = person.dict(include={"first_name", "last_name"})
print(person_include)

person_exclude = person.dict(exclude={"birthdate", "interestings"})
print(person_exclude)

person_nested_include = person.dict(
    include={
        "first_name": ...,
        "last_name": ...,
        "address": {"city", "country"},
        # or
        # "address": {"city": ..., "country": ...},
    }
)
print(person_nested_include)