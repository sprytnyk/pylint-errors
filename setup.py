"""Setup of a plerr package."""

import pathlib
import re
import setuptools

ROOT = pathlib.Path(__file__).resolve().parent
VERSION = (
    re.compile(r'__version__ = ["\'](.*?)["\']', re.S)
    .match((ROOT / 'plerr' / '__init__.py').read_text())
    .group(1)
)
LONG_DESCRIPTION = (ROOT / 'README.md').read_text()


setuptools.setup(
    name='plerr',
    version=VERSION,
    author='Vladyslav Krylasov',
    author_email='vladyslav.krylasov@gmail.com',
    description=(
        'A list of pylint-errors with reasoning and examples of erroneous and '
        'correct code.'
    ),
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/vald-phoenix/pylint-errors',
    packages=setuptools.find_packages(),
    install_requires=['Pygments==2.7.4'],
    test_suite='plerr.tests.test_package',
    python_requires='>=3.5',
    include_package_data=True,
    keywords=['pylint', 'errors', 'documentation'],
    entry_points={'console_scripts': ['plerr=plerr.cli:main']},
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance'
    ]
)
