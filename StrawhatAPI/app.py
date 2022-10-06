from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

#API Related imports
from api import app, db
from api.queries import listOnePieceCharacters_resolver, getSingleCharacter_resolver, listOrigin_resolver, getSingleOrigin_resolver
from api.mutations import create_character_resolver, \
    update_character_resolver, delete_character_resolver

#Data management
query = ObjectType("Query")
mutation = ObjectType("Mutation")

#Setting fields
query.set_field("listCharacters", listOnePieceCharacters_resolver)
query.set_field("getCharacter", getSingleCharacter_resolver)
query.set_field("listOrigins", listOrigin_resolver)
# query.set_field("getOrigin", getSingleOrigin_resolver)

mutation.set_field("createOnePieceCharacter", create_character_resolver)
mutation.set_field("updateOnePieceCharacter", update_character_resolver)
mutation.set_field("deleteOnePieceCharacter", delete_character_resolver)


type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, query, mutation,
                                snake_case_fallback_resolvers)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema,
                                   data,
                                   context_value=request,
                                   debug=app.debug)
    status_code = 200 if success else 400
    return jsonify(result), status_code