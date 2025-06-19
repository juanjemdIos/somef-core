# Software Metadata Extraction Framework CORE (SOMEF-core)

TO DO: Add badges.

<img src="docs/logo.png" alt="logo" width="150"/>

A command line interface for automatically extracting relevant metadata from code repositories (readme, configuration files, documentation, etc.).

This repository is extracted from https://github.com/KnowledgeCaptureAndDiscovery/somef/


**Authors:** Daniel Garijo, Allen Mao, Miguel Ángel García Delgado, Haripriya Dharmala, Vedant Diwanji, Jiaying Wang, Aidan Kelley, Jenifer Tabita Ciuciu-Kiss, Luca Angheluta and Juanje Mendoza.

## Features

Given a readme file (or a GitHub/Gitlab repository) SOMEF will extract the following categories (if present), listed in alphabetical order:

- **Acknowledgement**: Text acknowledging funding sources or contributors
- **Build file**: Build file(s) of the project. For example, files used to create a Docker image for the target software, package files, etc.
- **Citation**: Preferred citation as the authors have stated in their readme file. SOMEF recognizes Bibtex, Citation File Format files and other means by which authors cite their papers (e.g., by in-text citation). We aim to recognize the following properties:
  - Title: Title of the publication
  - Author: list of author names in the publication
  - URL: URL of the publication 
  - DOI: Digital object identifier of the publication
  - Date published
- **Code of conduct**: Link to the code of conduct of the project
- **Code repository**: Link to the GitHub/GitLab repository used for the extraction
- **Contact**: Contact person responsible for maintaining a software component
- **Continuous integration**: Link to continuous integration service(s)
- **Contribution guidelines**: Text indicating how to contribute to this code repository
- **Contributors**: Contributors to a software component
- **Creation date**: Date when the repository was created
- **Date updated**: Date of last release.
- **Description**: A description of what the software does
- **Documentation**: Where to find additional documentation about a software component
- **Download URL**: URL where to download the target software (typically the installer, package or a tarball to a stable version)
- **Executable examples**: Jupyter notebooks ready for execution (e.g., files, or through myBinder/colab links)
- **FAQ**: Frequently asked questions about a software component
- **Forks count**: Number of forks of the project
- **Forks url**: Links to forks made of the project
- **Full name**: Name + owner (owner/name)
- **Full title**: If the repository is a short name, we will attempt to extract the longer version of the repository name
- **Identifier**: Identifier associated with the software (if any), such as Digital Object Identifiers. DOIs associated with publications will also be detected.
- **Images**: Images used to illustrate the software component
- **Installation instructions**: A set of instructions that indicate how to install a target repository
- **Invocation**: Execution command(s) needed to run a scientific software component
- **Issue tracker**: Link where to open issues for the target repository
- **Keywords**: set of terms used to commonly identify a software component
- **License**: License and usage terms of a software component
- **Logo**: Main logo used to represent the target software component
- **Name**: Name identifying a software component
- **Owner**: Name and type of the user or organization in charge of the repository
- **Package distribution**: Links to package sites like pypi in case the repository has a package available.
- **Package files**: Links to package files used to wrap the project in a package.
- **Programming languages**: Languages used in the repository
- **Related papers**: URL to possible related papers within the repository stated within the readme file (from Arxiv)
- **Releases** (GitHub only): Pointer to the available versions of a software component. For each release, somef will track the following properties:
  - Description: Release notes
  - Author: Agent responsible of creating the release
  - Name: Name of the release
  - Tag: version number of the release
  - Date of publication
  - Date of creation
  - Link to the html page of the release
  - Id of the release
  - Link to the tarball zip and code of the release 
- **Repository status**: Repository status as it is described in [repostatus.org](https://www.repostatus.org/).
- **Requirements**: Pre-requisites and dependencies needed to execute a software component
- **Stargazers count**: Total number of stargazers of the project
- **Support**: Guidelines and links of where to obtain support for a software component
- **Support channels**: Help channels one can use to get support about the target software component
- **Usage examples**: Assumptions and considerations recorded by the authors when executing a software component, or examples on how to use it

We use different supervised classifiers, header analysis, regular expressions, the GitHub/Gitlab API to retrieve all these fields (more than one technique may be used for each field) and language specific metadata parsers (e.g., for package files). Each extraction records its provenance, with the confidence and technique used on each step. For more information check the [output format description](https://somef.readthedocs.io/en/latest/output/)

## Documentation

We are working on  this

## Cite SOMEF and SOMEF-core:

Journal publication (preferred):

```
@article{10.1162/qss_a_00167,
    author = {Kelley, Aidan and Garijo, Daniel},
    title = "{A Framework for Creating Knowledge Graphs of Scientific Software Metadata}",
    journal = {Quantitative Science Studies},
    pages = {1-37},
    year = {2021},
    month = {11},
    issn = {2641-3337},
    doi = {10.1162/qss_a_00167},
    url = {https://doi.org/10.1162/qss_a_00167},
    eprint = {https://direct.mit.edu/qss/article-pdf/doi/10.1162/qss\_a\_00167/1971225/qss\_a\_00167.pdf},
}
```

Conference publication (first):

```
@INPROCEEDINGS{9006447,
author={A. {Mao} and D. {Garijo} and S. {Fakhraei}},
booktitle={2019 IEEE International Conference on Big Data (Big Data)},
title={SoMEF: A Framework for Capturing Scientific Software Metadata from its Documentation},
year={2019},
doi={10.1109/BigData47090.2019.9006447},
url={http://dgarijo.com/papers/SoMEF.pdf},
pages={3032-3037}
}
```

## Requirements

- Python 3.9 or Python 3.10 (default version support)

SOMEF has been tested on Unix, MacOS and Windows Microsoft operating systems.

If you face any issues when installing SOMEF, please make sure you have installed the following packages: `build-essential`, `libssl-dev`, `libffi-dev` and `python3-dev`.

## Install from Pypi

We are currently working on this

## Install from GitHub

To run somef_core, please follow the next steps:

Clone this GitHub repository

```
git clone https://github.com/KnowledgeCaptureAndDiscovery/somef-core.git
```

We use [Poetry](https://python-poetry.org/) to ensure library compatibility. It can be installed as follows:

```
curl -sSL https://install.python-poetry.org | python3 -
```

This option is recommended over installing Poetry with pip install.

Now Poetry will handle the installation of SOMEF-core and all its dependencies configured in the `toml` file.

To test the correct installation of poetry run:

```
poetry --version
```

Install somef and all their dependencies.

```
cd /somef-core
poetry install
```

Now we need to access our virtual environment, to do so you have to install the [poetry plugin shell](https://github.com/python-poetry/poetry-plugin-shell) and run the following command:

```
pip install poetry-plugin-shell
```
After `shell` is set up, you can run the following comand to access the virtual environment
```
poetry shell
```
Test SOMEF installation

```bash
somef --help
```

If everything goes fine, you should see:

```bash
Usage: somef_core [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  configure  Configure credentials
  describe   Running the Command Line Interface
  version    Show somef version.
```

## Installing through Docker

We are working on this section

## Configure

Before running SOMEF for the first time, you must **configure** it appropriately (you only need to do this once). Run:

```bash
somef_core configure
```

And you will be asked to provide the following:

- A GitHub authentication token [**optional, leave blank if not used**], which SOMEF uses to retrieve metadata from GitHub. If you don't include an authentication token, you can still use SOMEF. However, you may be limited to a series of requests per hour. For more information, see [https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)
- The path to the trained classifiers (pickle files). If you have your own classifiers, you can provide them here. Otherwise, you can leave it blank

If you want somef to be automatically configured (without GitHUb authentication key and using the default classifiers) just type:

```bash
somef_core configure -a
```

For showing help about the available options, run:

```bash
somef_core configure --help
```

Which displays:

```bash
Usage: somef_core configure [OPTIONS]

  Configure GitHub credentials and classifiers file path

Options:
  -a, --auto  Automatically configure SOMEF
  -h, --help  Show this message and exit.
```


## Usage

```bash
$ somef_core describe --help
  SOMEF Command Line Interface
Usage: somef_core describe [OPTIONS]

  Running the Command Line Interface

Options:
  Input: [mutually_exclusive, required]
    -r, --repo_url URL            Github/Gitlab Repository URL
    -d, --doc_src PATH            Path to the README file source
    -i, --in_file PATH            A file of newline separated links to GitHub/
                                  Gitlab repositories

  Output: [required_any]
    -o, --output PATH             Path to the output file. If supplied, the
                                  output will be in JSON

    -c, --codemeta_out PATH       Path to an output codemeta file
  -p, --pretty                    Pretty print the JSON output file so that it
                                  is easy to compare to another JSON output
                                  file.

  -m, --missing                   The JSON will include a field
                                  somef_missing_categories to report with the
                                  missing metadata fields that SOMEF was not
                                  able to find.

  -kt, --keep_tmp PATH            SOMEF will NOT delete the temporary folder
                                  where files are stored for analysis. Files
                                  will be stored at the
                                  desired path


  -h, --help                      Show this message and exit.
```

## Usage example:

The following command extracts all metadata available from [https://github.com/dgarijo/Widoco/](https://github.com/dgarijo/Widoco/).

```bash
somef_core describe -r https://github.com/dgarijo/Widoco/ -o test.json 
```

## Contribute:

If you want to contribute with a pull request, please do so by submitting it to the `dev` branch.
