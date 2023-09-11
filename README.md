# EPSS Client

A Python client to query the FIRST EPSS API for CVE EPSS scores. This tool allows users to easily fetch EPSS scores for different CVEs right from the command line.

## Installation

Before installing the EPSS Client, make sure you have Python 3.6+ installed on your system. You can install the EPSS Client using pip:

```sh
pip install epss_client
```

## Usage

You can use the EPSS Client from the command line as follows:

```sh
epss_client CVE-XXXX-XXXX
```

Replace `CVE-XXXX-XXXX` with the actual CVE identifier you want to query. The tool will fetch the EPSS score for the given CVE identifier and display it in the console.

## Development

If you want to contribute to the development of EPSS Client, you can clone the repository and set up a virtual environment:

```sh
git clone https://github.com/yourusername/epss_client
cd epss_client
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
pip install -e .
```

You can now run the EPSS Client locally using:

```sh
epss_client CVE-XXXX-XXXX
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
