import os

from ariadne import snake_case_fallback_resolvers, load_schema_from_path, make_executable_schema, upload_scalar, ScalarType

from api.mutations import mutation
from api.queries import query
from api.extra_features.base_type_resolvers import character_type, origin_type

# Тип Date
date_scalar = ScalarType("Date")
@date_scalar.serializer
def serialize_date(value):
    return value.isoformat()


type_defs = load_schema_from_path(
    os.path.join(os.path.dirname(__file__), "schema")
)

schema = make_executable_schema(
    type_defs,
    query, mutation, snake_case_fallback_resolvers
)