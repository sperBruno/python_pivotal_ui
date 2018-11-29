from jsonschema import validate

def validate_json_schema(schema, json):
    validate(schema, json)