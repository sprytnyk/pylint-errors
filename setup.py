"""Setup of a plerr package."""
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='plerr',
    version='1.0.1',
    author='Vladyslav Krylasov',
    author_email='vladyslav.krylasov@gmail.com',
    description=(
        'A list of pylint-errors with reasoning and examples of erroneous and '
        'correct code.'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vald-phoenix/pylint-errors',
    packages=setuptools.find_packages(),
    install_requires=['Pygments'],
    test_suite='plerr.tests',
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
