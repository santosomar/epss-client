# EPSS Client

A Python client to query the FIRST EPSS API for CVE EPSS scores. This tool allows users to easily fetch EPSS scores for different CVEs right from the command line.

## Installation

Before installing the EPSS Checker, make sure you have Python 3.6+ installed on your system. You can install the EPSS Checker using pip:

```sh
pip install epss-checker
```

## Usage

You can use the EPSS Client from the command line as follows:

```sh
epss-checker CVE-XXXX-XXXX
```

Replace `CVE-XXXX-XXXX` with the actual CVE identifier you want to query. The tool will fetch the EPSS score for the given CVE identifier and display it in the console. The following is the help message of the tool:

```sh
┌──(omar㉿websploit)-[~]
└─$ epss-checker -h
usage: epss-checker [-h] [-s] cve_id

 EPSS-Checker
 Author: @santosomar
 A tool to fetch EPSS scores for CVEs from the FIRST EPSS API.

positional arguments:
  cve_id        The CVE identifier to query (format: CVE-XXXX-XXXX)

options:
  -h, --help    show this help message and exit
  -s, --silent  Only display the EPSS score, without any additional text
```


## Contributing
To contribute to this project, please read the [CONTRIBUTING](CONTRIBUTING.md) file.



## License

This project is licensed under the MIT License. See the LICENSE file for details.
