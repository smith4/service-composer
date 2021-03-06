### Copyright 2014, MTA SZTAKI, www.sztaki.hu
###
### Licensed under the Apache License, Version 2.0 (the "License");
### you may not use this file except in compliance with the License.
### You may obtain a copy of the License at
###
###    http://www.apache.org/licenses/LICENSE-2.0
###
### Unless required by applicable law or agreed to in writing, software
### distributed under the License is distributed on an "AS IS" BASIS,
### WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
### See the License for the specific language governing permissions and
### limitations under the License.
#!/usr/bin/env -e python

import setuptools
from pip.req import parse_requirements

setuptools.setup(
    name='OCCO-ServiceComposer',
    version='0.2.0',
    author='MTA SZTAKI',
    author_email='occopus@lpds.sztaki.hu',
    namespace_packages=[
        'occo',
        'occo.plugins',
        'occo.plugins.servicecomposer',
    ],
    packages=[
        'occo.servicecomposer',
    ],
    py_modules=[
        'occo.plugins.servicecomposer.chef',
    ],
    scripts=[],
    url='https://github.com/occopus',
    license='LICENSE.txt',
    description='Occopus Service Composer',
    long_description=open('README.txt').read(),
    install_requires=[
        'pychef',
        'OCCO-InfoBroker',
        'OCCO-Util',
    ]
)
