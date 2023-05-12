from marshmallow import Schema, fields
from api.schemas.recordSchema import RecordSchema

class HistoricSchema(Schema):
    historic = fields.Nested(RecordSchema, many=True)