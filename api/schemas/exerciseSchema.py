from marshmallow import Schema, fields


class ExerciseSchema(Schema):
    _id = fields.String()
    name = fields.String()
    muscle = fields.String()
    repetition = fields.Integer()
    series = fields.Integer()
    interval = fields.Integer()
    execution_gif = fields.String()
    description = fields.String()