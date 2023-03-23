from consumptionSchema import ConsumptionSchema
from marshmallow import Schema, fields


class HistoricSchema(Schema):
    _id = fields.String()
    consumption = fields.Nested(ConsumptionSchema)