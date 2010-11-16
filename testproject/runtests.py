import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'testproject.settings'
extra_path = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.insert(0, extra_path)

from django.test.utils import get_runner
from django.conf import settings

def runtests():
    from coverage import coverage
    cov = coverage(source=['fixture_shell'])
    cov.start()
    test_runner = get_runner(settings)()
    failures = test_runner.run_tests([], verbosity=1, interactive=True)
    cov.stop()
    cov.save()
    sys.exit(failures)

if __name__ == '__main__':
    runtests()