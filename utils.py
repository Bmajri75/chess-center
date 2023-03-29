import json
from dataclasses import dataclass


@dataclass
class Utils:
    def tojson(objet):
        return json.loads(json.dumps(objet.__dict__, indent=4,
                                     sort_keys=True, default=str))
