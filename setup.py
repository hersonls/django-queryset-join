from setuptools import setup, find_packages

setup(
    name = "django-queryset-join",
    version = "1.0",
    url = 'http://github.com/hersonls/django-queryset-join',
    license = 'BSD',
    description = "Django queryset join is a simple way to join QuerySets of different models and manipulates them",
    author = 'Herson Leite - Hersonls',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
