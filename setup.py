import setuptools

setuptools.setup(
        name = 'erarigilo',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        entry_points = {'console_scripts': ['erg = erarigilo.main:main',]})

