import pytest
import requests

### Tests ###

@pytest.mark.duckduckgo
@pytest.mark.rest_api
def test_duckduckgo_insta_answer_api():

    #Arrange
    input_string = "python+programming"
    url ='https://api.duckduckgo.com/?q={}&format=json&pretty=1'.format(input_string)
    
    #Act
    response = requests.get(url)
    body = response.json()

    #Assert
    assert response.status_code ==200
    assert 'Python' in body['Abstract']
