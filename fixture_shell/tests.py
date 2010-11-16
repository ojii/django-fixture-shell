from __future__ import with_statement
from django.core.management import get_commands, call_command
from django.test.testcases import TestCase
from os import removedirs
from tempfile import mkdtemp
from testproject.models import MyModel
import os
import sys
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class MockStdin(object):
    def __init__(self, data):
        self.data = StringIO(data)
        self.data.seek(0)
        
    def __enter__(self):
        sys.stdin = self.data
        
    def __exit__(self, type, value, traceback):
        sys.stdin = sys.__stdin__


class FixtureShellTestCase(TestCase):
    def setUp(self):
        self.tempdir = mkdtemp()
        self.counter = 0
        self.tempfiles = []
        
    def tearDown(self):
        for filename in self.tempfiles:
            os.remove(filename)
        removedirs(self.tempdir)
        
    def _get_file(self):
        self.counter += 1
        filename = os.path.join(self.tempdir, 'file_%s.json' % self.counter)
        self.tempfiles.append(filename)
        return filename
    
    def test_01_command_exists(self):
        """
        Test if we even have the command
        """
        self.assertTrue('fixture_shell' in get_commands())
        
    def test_02_command_runs(self):
        with MockStdin(''):
            sio = StringIO()
            call_command('fixture_shell', self._get_file(), stdout=sio)

    def test_03_command_works(self):
        with MockStdin("""
from testproject.models import MyModel
MyModel.objects.create(name='test')
        """):
            sio = StringIO()
            fname = self._get_file()
            call_command('fixture_shell', fname, stdout=sio)
        # since both fixture_shell and the tests use :memory:, we have to flush
        call_command('flush', interactive=False)
        self.assertEqual(0, MyModel.objects.count())
        call_command('loaddata', fname)
        self.assertEqual(1, MyModel.objects.count())