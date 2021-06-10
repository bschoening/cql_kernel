from setuptools import setup

setup(
    name='cql_jupyter',
    version='1.0.0',
    packages=['cqlshlib_cql_kernel', 'cqlshlib_cql_kernel.test', 'cql_kernel'],
    url='https://github.com/bschoening/cql_jupyter',
    license='Apache',
    author='Brad Schoening, Steven Lowenthal & Apache Cassandra Developers',
    install_requires = ['cassandra-driver>=3.25'],
    tests_require = ['jupyter_kernel_test','nose>=1.3.7'],
    description='CQL Kernel for Jupyter based on cqlsh',
    classifiers=[
        'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" 
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
