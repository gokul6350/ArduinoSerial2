from setuptools import setup

setup(
    name='arduinoserial2',
    version='1.1.0',
    packages=['arduinoserial2'],
    install_requires=[
        'pyserial',  # Add any dependencies your module requires
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'detect-arduino-ports=arduinoserial2.arduinoserial2:main',
        ],
    },
    author='SK Gokulbarath',
    author_email='gokul00060@gmail.com',
    description='ArduinoSerial2: Connects Arudino with Computer ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/gokul6350/ArduinoSerial2',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
