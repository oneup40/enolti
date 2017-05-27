from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), 'r') as f:
    long_description = f.read()

setup(
	name='enolti',
	version='0.0a0.dev0',
	description='A utility to easily transfer large amounts of data without a network connection',
	url='https://github.com/oneup40/enolti',
	author='oneup40',
	author_email='oneup40@gmail.com',
	license='Free for non-commercial use',
	classifiers=[
		'Development Status :: 1 - Planning',
		'Intended Audience :: Information Technology',
		'License :: Free for non-commercial use',
		'Operating System :: POSIX :: Linux',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Topic :: Communications :: File Sharing',
		'Topic :: System :: Archiving',
        'Topic :: Utilities',
	],
	keywords='transfer archive backup',
	packages=['enolti'],
	install_requires=['chunkfile','pathlib'],
	extras_require={},
	package_data={},
)
