from ariadne import ObjectType

from . import characters, origin

query = ObjectType("Query")

query.set_field("getSingleCharacter", characters.getSingleCharacter_resolver)
query.set_field("getMultipleCharacters", characters.listOnePieceCharacters_resolver)

query.set_field("getSingleCharacter", origin.getSingleOrigin_resolver)
query.set_field("getMultipleCharacters", origin.listOrigin_resolver)


