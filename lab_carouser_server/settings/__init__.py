from split_settings.tools import optional, include

settings = [
    'base.py',
    optional('local.py')
]

include(*settings)
