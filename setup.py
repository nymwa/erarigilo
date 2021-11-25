import setuptools

setuptools.setup(
        name = 'erarigilo',
        version = '0.1.0',
        packages = setuptools.find_packages(),
        install_requires=[
            'tqdm',
            'pyyaml',
            'numpy',
            'tabulate',
            'spacy>=3.2.0',
            'lemminflect'],
        entry_points = {'console_scripts': ['erg = erarigilo.main:main',]})

