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
            'lemminflect',
            'nltk'],
        entry_points = {
            'console_scripts': [
                'erg = erarigilo.main:main',
                'falsliter-data-split = falsliter.data_split:main',
                'falsliter-preprocess = falsliter.preprocess:main',
                'falsliter-data-merge = falsliter.data_merge:main',
                'falsliter-train = falsliter.train:main',
                'falsliter-dump = falsliter.dump:main',
                'falsliter-merge-model = falsliter.merge_model:main',
                'falsliter-dist = falsliter.dist:main',
                'falsliter-sample = falsliter.sample:main',
                'ortobruilo-sample = ortobruilo.sample:main',
                'ortobruilo-prepare = ortobruilo.prepare:main',
                ]})

