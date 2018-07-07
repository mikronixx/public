from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = r.read()

setup ( 
    name='pgbackup',
    version='0.1.0',
    description='Database backups locally or to AWS S3',
    long_description=readme,
    author='mikron',
    author_email='mikron@frieswiththat.org',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)

