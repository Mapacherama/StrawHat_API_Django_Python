import requests

from sgqlc.types import String, Type, Field, Boolean
from sgqlc.operation import Operation

class originType(Type):
    id = String
    name = String
    description = String

    #test