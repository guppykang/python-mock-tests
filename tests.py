import requests_mock
import pytest
from nose.tools import assert_true, assert_is_not_none, assert_list_equal
import requests
from satcom_mock_demo import services
from unittest.mock import Mock, patch


res_paylaod = [{
    'messages': {
        'hi': 'mom'
    },
    'data_exists': True
}]


def test_access_server():
    with requests_mock.Mocker() as m:
        m.get('http://127.0.0.1:5000/', status_code=200, text='1')

        resp = services.ping_server()

        assert resp != None
        assert resp.text == '1'

# bad juju
# actual test on live server


def live_test_hello_world():
    response = services.ping_server()
    assert_is_not_none(response)


# method 1 (super hand wavy, me don't like)
@patch('satcom_mock_demo.services.requests.get')  # this is so trippy i hate it
def mock_test_hello_world(mock_get):
    mock_get.return_value.ok = true  # requests.get now returns an object whose "ok" field is a function

    response = services.ping_server()
    assert_is_not_none(response)


# method 2 (makes me feel a little better but still meh)
def mock_test_hello_world_2():
    with patch('satcom_mock_demo.services.requests.get') as mock_get:  # requests.get now returns an object whose "ok" field is a function
        mock_get.return_value.ok = true
        mock_get.return_value.json.return_value = res_paylaod

        response = services.ping_server()
        assert_is_not_none(response)
        assert_list_equal(response.json(), res_paylaod)


# method 3 (meh can be useful if you want to be a total weirdo lol)
def test_getting_todos():
    mock_get_patcher = patch('satcom_mock_demo.services.requests.get')

    # start patching `requests.get`.
    mock_get = mock_get_patcher.start()

    # configure the mock to return a response with an ok status code.
    mock_get.return_value.ok = true

    # call the service, which will send a request to the server.
    response = services.ping_server()

    # stop patching `requests.get`.
    mock_get_patcher.stop()

    # if the request is sent successfully, then i expect a response to be returned.
    assert_is_not_none(response)
