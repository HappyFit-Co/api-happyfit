from flask_restx import fields, Namespace

ns = Namespace('notification', description='Notification operations')

workout_frequency = ['daily', 'weekly', 'every other day', 'every weekday', 'every weekend']
water_frequency = ['hourly', 'every 2 hours', 'every 3 hours', 'every 4 hours', 'every 6 hours']

workout = ns.model('Workout', {
    'frequency': fields.String(validate=fields.validate.OneOf(workout_frequency)),
    'hour': fields.Time(required=True)
})

water = ns.model('Water', {
    'frequency': fields.String(validate=fields.validate.OneOf(water_frequency)),
    'start_hour': fields.Time(required=True),
    'end_hour': fields.Time(required=True)
})

notification_schema = ns.model('Notification', {
    'workout': fields.Nested(workout),
    'water': fields.Nested(water)
})
