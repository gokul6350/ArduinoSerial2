from setuptools import setup

setup(
    name='arduinoserial2',
    version='1.0.0',
    packages=['arduinoserial2'],
    install_requires=[
        'pyserial',  # Add any dependencies your module requires
    ],
    entry_points={
        'console_scripts': [
            'detect-arduino-ports=arduinoserial2.detect_ports:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='ArduinoSerial2: Your module description here.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/arduinoserial2',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
