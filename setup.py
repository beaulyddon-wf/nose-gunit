from setuptools import setup


setup(
    name="nose-gunit",
    entry_points= {
        'nose.plugins.0.10':  [
            'nosegunit = nosegunit:NoseGunit'
            ]
    },
    py_modules=['nosegunit'],
    install_requires=['nose>=0.10.1'],
)
