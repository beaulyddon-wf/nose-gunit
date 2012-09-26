from setuptools import setup

VERSION = '0.0.1'

setup(
    name="NoseGunit",
    version=VERSION,
    author='Beau Lyddon',
    author_email='lyddonb@gmail.com',
    maintainer='Beau Lyddon',
    maintainer_email='lyddonb@gmail.com',
    descrption='nose plugin for bootstrapping the GAE SDK and GAE Testbed',
    url='https://github.com/beaulyddon-wf/nose-gunit',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 2 Pre-Alpha',
        'License :: Apache License 2.0',
        'Programming Language :: Python',
        ],
    entry_points= {
        'nose.plugins.0.10':  [
            'nosegunit = nosegunit:NoseGunit'
            ]
    },
    py_modules=['nosegunit'],
    install_requires=['nose>=0.10.1'],
)
