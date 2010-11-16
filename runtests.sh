#!/bin/bash
cd tests
echo "setting up test environment (this might take a while)..."
python bootstrap.py
./bin/buildout
./bin/coverage run testapp/manage.py test fixture_shell
retcode=$?
if [ $retcode -ne 0 ]; then
    exit $retcode
fi
./bin/coverage html
cd ..
echo ""
echo "done"
echo ""
exit $retcode
