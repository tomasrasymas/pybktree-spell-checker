from setuptools import setup

setup(
    name='pybktreespellchecker',
    version='0.0.5',
    description='Python implementation of BK-tree and Levenshtein distance to perform spell checking',
    url='https://github.com/tomasrasymas/pybktree-spell-checker',
    author='Tomas Rasymas',
    author_email='tomas.rasymas@gmail.com',
    license='MIT',
    data_files=[('', ['LICENSE'])],
    install_requires=[],
    test_suite='tests',
    packages=['pybktreespellchecker']
)