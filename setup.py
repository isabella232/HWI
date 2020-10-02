# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hwilib',
 'hwilib.devices',
 'hwilib.devices.btchip',
 'hwilib.devices.ckcc',
 'hwilib.devices.trezorlib',
 'hwilib.devices.trezorlib.messages',
 'hwilib.devices.trezorlib.transport']

package_data = \
{'': ['*'], 'hwilib': ['udev/*', 'ui/*']}

modules = \
['hwi', 'hwi-qt']
install_requires = \
['bitbox02>=4.1.0',
 'ecdsa>=0.13.0,<0.14.0',
 'hidapi>=0.7.99,<0.8.0',
 'libusb1>=1.7,<2.0',
 'mnemonic>=0.18.0,<0.19.0',
 'pyaes>=1.6,<2.0',
 'typing-extensions>=3.7,<4.0']

extras_require = \
{'qt': ['pyside2>=5.14.0,<6.0.0']}

entry_points = \
{'console_scripts': ['hwi = hwilib.cli:main', 'hwi-qt = hwilib.gui:main']}

setup_kwargs = {
    'name': 'hwi',
    'version': '1.2.0rc1',
    'description': 'A library for working with Bitcoin hardware wallets',
    'long_description': "# Bitcoin Hardware Wallet Interface\n\n[![Build Status](https://travis-ci.org/bitcoin-core/HWI.svg?branch=master)](https://travis-ci.org/bitcoin-core/HWI)\n\nThe Bitcoin Hardware Wallet Interface is a Python library and command line tool for interacting with hardware wallets.\nIt provides a standard way for software to work with hardware wallets without needing to implement device specific drivers.\nPython software can use the provided library (`hwilib`). Software in other languages can execute the `hwi` tool.\n\nCaveat emptor: Inclusion of a specific hardware wallet vendor does not imply any endorsement of quality or security.\n\n## Prerequisites\n\nPython 3 is required. The libraries and [udev rules](hwilib/udev/README.md) for each device must also be installed. Some libraries will need to be installed\n\nFor Ubuntu/Debian:\n```\nsudo apt install libusb-1.0-0-dev libudev-dev python3-dev\n```\n\nFor Centos:\n```\nsudo yum -y install python3-devel libusbx-devel systemd-devel\n```\n\nFor macOS:\n```\nbrew install libusb\n```\n\n## Install\n\n```\ngit clone https://github.com/bitcoin-core/HWI.git\ncd HWI\npoetry install # or 'pip3 install .' or 'python3 setup.py install'\n```\n\nThis project uses the [Poetry](https://github.com/sdispater/poetry) dependency manager. HWI and its dependencies can be installed via poetry by executing the following in the root source directory:\n\n```\npoetry install\n```\n\nPip can also be used to automatically install HWI and its dependencies using the `setup.py` file (which is usually in sync with `pyproject.toml`):\n\n```\npip3 install .\n```\n\nThe `setup.py` file can be used to install HWI and its dependencies so long as `setuptools` is also installed:\n\n```\npip3 install -U setuptools\npython3 setup.py install\n```\n\n## Dependencies\n\nSee `pyproject.toml` for all dependencies. Dependencies under `[tool.poetry.dependecies]` are user dependencies, and `[tool.poetry.dev-dependencies]` for development based dependencies. These dependencies will be installed with any of the three above installation methods.\n\n## Usage\n\nTo use, first enumerate all devices and find the one that you want to use with\n\n```\n./hwi.py enumerate\n```\n\nOnce the device type and device path is known, issue commands to it like so:\n\n```\n./hwi.py -t <type> -d <path> <command> <command args>\n```\n\nAll output will be in JSON form and sent to `stdout`.\nAdditional information or prompts will be sent to `stderr` and will not necessarily be in JSON.\nThis additional information is for debugging purposes.\n\nTo see a complete list of available commands and global parameters, run\n`./hwi.py --help`.  To see options specific to a particular command,\npass the `--help` parameter after the command name; for example:\n\n```\n./hwi.py getdescriptors --help\n```\n\n## Device Support\n\nThe below table lists what devices and features are supported for each device.\n\nPlease also see [docs](docs/) for additional information about each device.\n\n| Feature \\ Device | Ledger Nano X | Ledger Nano S | Trezor One | Trezor Model T | BitBox01 | BitBox02 | KeepKey | Coldcard |\n|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|\n| Support Planned | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |\n| Implemented | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |\n| xpub retrieval | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |\n| Message Signing | Yes | Yes | Yes | Yes | Yes | N/A | Yes | Yes |\n| Device Setup | N/A | N/A | Yes | Yes | Yes | Yes | Yes | N/A |\n| Device Wipe | N/A | N/A | Yes | Yes | Yes | Yes | Yes | N/A |\n| Device Recovery | N/A | N/A | Yes | Yes | N/A | Yes | Yes | N/A |\n| Device Backup | N/A | N/A | N/A | N/A | Yes | Yes | N/A | Yes |\n| P2PKH Inputs | Yes | Yes | Yes | Yes | Yes | N/A | Yes | Yes |\n| P2SH-P2WPKH Inputs | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |\n| P2WPKH Inputs | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |\n| P2SH Multisig Inputs | Yes | Yes | Yes | Yes | Yes | N/A | Yes | Yes |\n| P2SH-P2WSH Multisig Inputs | Yes | Yes | Yes | Yes | Yes | N/A | Yes | Yes |\n| P2WSH Multisig Inputs | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |\n| Bare Multisig Inputs | Yes | Yes | N/A | N/A | Yes | N/A | N/A | N/A |\n| Arbitrary scriptPubKey Inputs | Yes | Yes | N/A | N/A | Yes | N/A | N/A | N/A |\n| Arbitrary redeemScript Inputs | Yes | Yes | N/A | N/A | Yes | N/A | N/A | N/A |\n| Arbitrary witnessScript Inputs | Yes | Yes | N/A | N/A | Yes | N/A | N/A | N/A |\n| Non-wallet inputs | Yes | Yes | Yes | Yes | Yes | N/A | Yes | Yes |\n| Mixed Segwit and Non-Segwit Inputs | N/A | N/A | Yes | Yes | Yes | Yes | Yes | Yes |\n| Display on device screen | Yes | Yes | Yes | Yes | N/A | Yes | Yes | Yes |\n\n## Using with Bitcoin Core\n\nSee [Using Bitcoin Core with Hardware Wallets](docs/bitcoin-core-usage.md).\n\n## License\n\nThis project is available under the MIT License, Copyright Andrew Chow.\n",
    'author': 'Andrew Chow',
    'author_email': 'andrew@achow101.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bitcoin-core/HWI',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<3.9',
}


setup(**setup_kwargs)
