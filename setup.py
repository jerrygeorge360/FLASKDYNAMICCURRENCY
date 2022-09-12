from setuptools import find_packages,setup

setup(name='flaskdynamiccurrency',version='0.1.0',
      description='converts currencies based on the user location',
      long_description='',
      author='Jbotrex',
      author_email='jbotrex@gmail.com',
      maintainer='Jbotrex',
      maintainer_email='jbotrex@gmail.com',
      download_url='',
      packages=find_packages(include=['flaskdynamiccurrency']),
      license='MIT',
      keywords='',
      platforms='',
      install_requires=['requests'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest==4.4.1'],
      test_suite='tests',
      )