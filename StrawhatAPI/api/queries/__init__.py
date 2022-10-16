from ariadne import ObjectType

from . import characters, origin, crew, piratefleet

query = ObjectType("Query")

query.set_field("getSingleCharacter", characters.getSingleCharacter_resolver)
query.set_field("getMultipleCharacters", characters.listOnePieceCharacters_resolver)

query.set_field("getSingleOrigin", origin.getSingleOrigin_resolver)
query.set_field("getMultipleOrigins", origin.listOrigin_resolver)

query.set_field("getSingleCrew", crew.getSingleCrew_resolver)
query.set_field("getMultipleCrews", crew.listCrews_resolver)

query.set_field("getSinglePirateFleet", crew.getSinglePirateFleet_resolver)
query.set_field("getMultiplePirateFleets", crew.listPirateFleets_resolver)


