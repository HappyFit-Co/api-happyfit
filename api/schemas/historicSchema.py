from marshmallow import Schema, fields

from api.schemas.consumptionSchema import ConsumptionSchema


class HistoricSchema(Schema):
    _id = fields.String()
    consumption = fields.Nested(ConsumptionSchema, many=True)