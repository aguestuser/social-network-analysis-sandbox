try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'just hacking around on social network analysis problems',
    'author': '@aguestuser',
    'url': 'https://github.com/aguestuser/social-network-analysis',
    'author_email': 'aguestuser@riseup.net',
    'version': '0.0.1',
    'install_requires': ['nose2', 'numpy'],
    'packages': ['sna'],
    'package_dir': {'': 'src'},
    'scripts': [],
    'name': 'social-network-analysis-sandbox'
}

setup(**config)
