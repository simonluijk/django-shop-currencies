import os

# Make filepaths relative to settings.
ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

DEBUG = True
TEMPLATE_DEBUG = True

SITE_ID = 1

TEST_RUNNER = 'django_nose.runner.NoseTestSuiteRunner'

GEOIP_PATH = u'/usr/share/GeoIP/'

DATABASES = {
    'default': {
        'NAME': 'test.db',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_nose',
    'south',
    'currencies',
    'shop',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'currencies.middleware.GeoIP2CountryMiddleware',
    'currencies.middleware.Country2CurrencyMiddleware',
)

ROOT_URLCONF = 'test_app.urls'

STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

SHOP_PRODUCT_MODEL = (u'test_app.models.Product', 'shop')
SHOP_CARTITEM_MODEL = (u'currencies.models.CurrenciesCartItem', 'shop')
SHOP_DEFAULT_CURRENCY = u'EUR'
