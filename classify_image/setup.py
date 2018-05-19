"""Setup file"""

from setuptools import setup, find_packages
import classify_image

setup(
    name='classify_image',
    version=classify_image.__version__,
    description='Classify image',
    long_description=open('README.md').read(),
    url='',
    author='taniy935',
    author_email='taniy935@yandex.ru',
    license='MIT',
    install_requires=['tensorflow'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'classify_image = classify_image.classify_image:run'
        ]
    },
    include_package_data=True,
    packages=find_packages(exclude=['tests']),
    test_suite='tests'
)
