from setuptools import setup, find_packages

classifiers = [
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Topic :: Internet",
    "Topic :: Utilities",
    
]

package = __import__('fixture_shell')
if package.__stage__ == 'final':
    version = package.__version__
    classifiers.append("Development Status :: 5 - Production/Stable")
else:
    version = '%s-%s-%s' % (package.__version__, package.__stage__, package.__stage_version__)
    if package.__stage__ == 'alpha':
        classifiers.append("Development Status :: 3 - Alpha")
    else:
        classifiers.append("Development Status :: 4 - Beta")

setup(
    name='django-fixture-shell',
    version=version,
    description='Utility app/project to generate fixtures from shell.',
    author='Jonas Obrist',
    url='http://github.com/ojii/django-fixture-shell',
    packages=find_packages(),
    zip_safe=False,
    classifiers=classifiers,
    install_requires=[
        'Django>=1.2.3',
    ],
    tests_require=[
        'coverage>=3.4',
    ],
    test_suite = "testproject.runtests.runtests",
)
