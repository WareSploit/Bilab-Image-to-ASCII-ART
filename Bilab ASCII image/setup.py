from setuptools import setup, find_packages

setup(
    name='bilab-ascii',
    version='1.0.0',
    description='High-performance ASCII art generator',
    author='Bilab Team',
    packages=find_packages(),
    install_requires=[
        'pillow',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'bilab=bilab.main:main',
        ],
    },
)