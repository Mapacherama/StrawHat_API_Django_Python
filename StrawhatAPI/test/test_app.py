import requests
import pytest

#Endpoint
GRAPHQL_API_ENDPOINT = "http://localhost:5000/graphql"

#Queries
query_for_single_pirate = """query{
	getSingleCharacter(id:1){
    character{
      name
    }
  }
}"""

def test_retrieve_graphql_data_should_yield_http_200():
    response = requests.post(GRAPHQL_API_ENDPOINT, json={'query': query_for_single_pirate})
    assert response.status_code == 200

def test_retrieve_character_name_should_be_correct():
    response = requests.post(GRAPHQL_API_ENDPOINT, json={'query': query_for_single_pirate})

    response_body = response.json()
    assert response_body['data']['getSingleCharacter']['character']['name'] == 'Monkey D. Luffy'
