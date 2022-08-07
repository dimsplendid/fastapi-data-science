import pytest

from introduction_fixtures import Address, Gender, Person

@pytest.fixture
def address():
    return Address(
        stree_address="123 Main Street",
        postal_code="12345",
        city="Anytown",
        country="USA",
    )
    
@pytest.fixture
def person(address):
    return Person(
        first_name="John",
        last_name="Doe",
        gender=Gender.MALE,
        birthdate="1991-01-01",
        interests=["travel", "sports"],
        address=address,
    )

def test_address_country(address):
    assert address.country == "USA"
    
def test_person_first_name(person):
    assert person.first_name == "John"
    
def test_person_address_city(person):
    assert person.address.city == "Anytown"