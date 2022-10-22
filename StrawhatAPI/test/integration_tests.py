import requests
import pytest

#Endpoint
GRAPHQL_API_ENDPOINT = "http://localhost:5000/graphql"

#Queries
query_for_single_pirate = """{
  "data": {
    "getSingleCharacter": {
      "character": {
        "name": "Shanks"
      }
    }
  }
}"""
