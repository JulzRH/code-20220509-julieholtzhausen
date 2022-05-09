from setuptools import setup

setup(name='bmi_calculator',
      version='0.1',
      description='A BMI Calculator',
      url='http://github.com/storborg/funniest',
      author='Julie Holtzhausen',
      author_email='julieholtz@gmail.com',
      license='MIT',
      packages=['bmi_calculator'],
      package_dir={'bmi_calculator': 'src/bmi_calculator'},
      zip_safe=False)