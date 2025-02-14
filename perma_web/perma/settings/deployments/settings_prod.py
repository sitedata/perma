from .settings_common import *

DEBUG = False

# This is handy for debugging problems that *only* happen when Debug = False,
# because exceptions are printed directly to the log/console when they happen.
# Just don't leave it on!
# DEBUG_PROPAGATE_EXCEPTIONS = True

# The base location, on disk, where we want to store our generated assets
MEDIA_ROOT = 'perma/assets/generated/'

# Schedule celerybeat jobs.
# These will be added to CELERYBEAT_SCHEDULE in settings.utils.post_processing
CELERY_BEAT_JOB_NAMES = [
    'update-stats',
    'send-links-to-internet-archive',
    'delete-links-from-internet-archive',
    'send-js-errors',
    'run-next-capture',
    'verify_webrecorder_api_available',
    'sync_subscriptions_from_perma_payments',
    'cache_playback_status_for_new_links',
]

# logging
LOGGING['handlers']['file']['filename'] = '/var/log/perma/perma.log'

# use separate subdomain for user content
MEDIA_URL = '//perma-archives.org/media/'

# Our sorl thumbnail settings
# We only use this redis config in prod. dev envs use the local db.
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_REDIS_HOST = 'localhost'
THUMBNAIL_REDIS_PORT = '6379'

# caching
CACHES["default"] = {
    "BACKEND": "django_redis.cache.RedisCache",
    "LOCATION": "redis://127.0.0.1:6379/0",
    "OPTIONS": {
        "CLIENT_CLASS": "django_redis.client.DefaultClient",
        "IGNORE_EXCEPTIONS": True,  # since this is just a cache, we don't want to show errors if redis is offline for some reason
    }
}

# subscription packages
TIERS['Individual'] = [
    {
        'period': 'monthly',
        'link_limit': 10,
        'rate_ratio': 1
    },{
        'period': 'monthly',
        'link_limit': 100,
        'rate_ratio': 2.5
    },{
        'period': 'monthly',
        'link_limit': 500,
        'rate_ratio': 10
    }
]

