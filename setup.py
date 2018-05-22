import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kryptobot",
    packages=[
        'kryptobot',
        'kryptobot.ccxt',
        'kryptobot.db',
        'kryptobot.harvesters',
        'kryptobot.markets',
        'kryptobot.portfolio',
        'kryptobot.signals',
        'kryptobot.strategies',
        'kryptobot.ta',
    ],
    version="0.0.1",
    author="Stephan Miller",
    author_email="stephanmil@gmail.com",
    description="Cryptocurrency trading bot framework",
    long_description=long_description,
    url="https://github.com/eristoddle/KryptoBot",
    zip_safe=False,
    install_requires=[
          'pypubsub',
          'requests',
          'SQLAlchemy',
          'psycopg2',
          'pyti',
          'ccxt',
          'pandas',
          'enigma-catalyst'
      ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)