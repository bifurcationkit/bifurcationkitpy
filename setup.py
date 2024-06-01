from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='diffeqpy',
      version='0.0.1',
      description='Computing bifurcation diagrams in Python',
      long_description=readme(),
      long_description_content_type="text/markdown",
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics'
      ],
      url='https://github.com/bifurcationkit/diffeqpy',
      keywords='bifurcation continuation periodic orbits normal form',
      author='Romain Veltz',
      author_email='romain.veltz@inria.fr',
      license='MIT',
      packages=['bifurcationkitpy','bifurcationkitpy.tests'],
      install_requires=['juliacall>=0.9.14', 'jill'],
      include_package_data=True,
      zip_safe=False)
