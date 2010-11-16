INSTALLED_APPS = (
    'fixture_shell',
    'testproject',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }         
}