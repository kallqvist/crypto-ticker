import os
from setuptools import setup
from pip.req import parse_requirements
from pip.download import PipSession

req_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')
reqs = [str(r.req) for r in parse_requirements(req_file, session=PipSession())]

setup(
    name='cryptocheck',
    version='0.1',
    install_requires=reqs,
    packages=[],
)
