from beings.person import Person
import pytest

@pytest.fixture
def person():
    return Person("Jumana Abanda", 22, jobs=["QA"])

def test_init(person):
    assert person.name == "Jumana Abanda"
    assert person.age == 22
    assert person.jobs == ["QA"]

def test_forename(person: Person):
    assert person.forename == "Jumana"

def test_surname(person: Person):
    assert person.surname == "Abanda"

def test_no_surname(person: Person): 
    person.name=="Jumana"
    assert person.surname


def test_celebrate_birthday(person: Person):
    person.celebrate_birthday()
    assert person.age == 23

def test_add_job(person: Person):
    person.add_job("Teacher")
    assert person.jobs == ["QA", "Teacher"]