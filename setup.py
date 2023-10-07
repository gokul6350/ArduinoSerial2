from setuptools import setup

setup(
    name='arduinoserial2',
    version='1.0.1',
    packages=['arduinoserial2'],
    install_requires=[
        'pyserial',  # Add any dependencies your module requires
    ],
    entry_points={
        'console_scripts': [
            'detect-arduino-ports=arduinoserial2.detect_ports:main',
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
