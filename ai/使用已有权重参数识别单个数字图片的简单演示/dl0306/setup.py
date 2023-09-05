import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(name='dl0306',
                 packages=['dl0306'],
                 install_requires=install_requires)
