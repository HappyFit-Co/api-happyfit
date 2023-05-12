from marshmallow import Schema, fields

class ExerciseSchema(Schema):
    _id = fields.String()
    name = fields.String()
    body_part = fields.String()
    target = fields.String()
    repetition = fields.Integer()
    series = fields.Integer()
    interval = fields.Integer()
    equipment = fields.String()
    execution_gif = fields.String()