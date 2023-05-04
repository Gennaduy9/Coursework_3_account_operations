import pytest

import main

def test_encave_numbers():
    assert main.encave_numbers("Master card 1234567898765432") == 'Master card 1234 56** **** 5432'
    assert main.encave_numbers("Счет 35389700990735323760") == 'Счет **3760'
    assert main.encave_numbers("Счет 353897009745330172") == 'Счет None'

@pytest.fixture
def data_positive():
    return [{
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  },
  {
    "id": 895315941,
    "state": "EXECUTED",
    "date": "2018-08-19T04:27:37.904916",
    "operationAmount": {
        "amount": "56883.54",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Classic 6831982476737658",
    "to": "Visa Platinum 8990922113665229"
  }]

def test_latter_5_operations(data_positive):
    with pytest.raises(IndexError):
        type(main.latter_5_operations(data_positive)) ==str
