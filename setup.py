# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
]


if __name__ == '__main__':
    setup(
        name='logtest',
        version='0.1',
        description='Log Test',
        url='https://github.com/socek/logtest',
        license='Apache License 2.0',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=install_requires,
        entry_points={

        }
    )
