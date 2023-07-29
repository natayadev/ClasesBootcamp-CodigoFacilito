""" Setup file for Multi_Maths Package """
# __doc__ (Setup file for testing modules and packages)

from setuptools import setup, find_packages

with open('requirements.txt', 'r', encoding="utf-8") as f:
    requirements = f.readlines()

LONG_DESCRIPTION_CONS = '''An arithmetic, geometry & statistics package.
For import or cli use, with multilanguage support
in english and spanish for now.'''

setup(
    name='multi_maths',
    version='1.0.7',
    author='Gonzalo Mahserdjian',
    author_email='gsmx64@outlook.com',
    url='https://github.com/gsmx64/python-adv-bootcamp-cf/tree/main/class03/challenge',  # noqa: E501  # pylint: disable=C0301
    description='An arithmetic, geometry & statistics package.',
    long_description=LONG_DESCRIPTION_CONS,
    long_description_content_type="text/markdown",
    license='GNU General Public License v3 (GPLv3)',
    packages=find_packages(),
    package_data={'multi_maths': ['languages/*',]},
    entry_points={
            'console_scripts': [
                'multi_maths = multi_maths:main',
                'multi_maths.cli = multi_maths.cli:main'
            ]
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
    keywords='multi maths, maths, arithmetic, geometry, statistics',
    install_requires=requirements,
    zip_safe=False
)
