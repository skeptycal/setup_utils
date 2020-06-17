#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" AutoSys Setup
    ---
    Part of the [AutoSys][1] package

    Copyright (c) 2018 [Michael Treanor][2]

    AutoSys is licensed under the [MIT License][3]

    [1]: https://www.github.com/skeptycal/autosys
    [2]: https://www.twitter.com/skeptycal
    [3]: https://opensource.org/licenses/MIT
    """

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import re

from functools import lru_cache
from os import linesep as NL
from pathlib import Path
from sys import path as PYTHONPATH

import pip_safe
import readme

from colorama import init
from setuptools import find_packages, setup

from typing import Dict, Final, List, Optional, Sequence, Tuple

# from .readme import readme
# from .pip_safe import pip_safe_name

if True:
    from package_metadata import *

init()

here = Path(__file__).resolve().parent
if here not in PYTHONPATH:
    PYTHONPATH.insert(0, here)


def main():
    print(f"Setup for '{NAME}' version {VERSION}")

    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        python_requires=REQUIRES_PYTHON,
        # package_dir=PACKAGE_DIR,
        packages=find_packages(
            f'{NAME}', exclude=PACKAGE_EXCLUDE),
        # py_modules=[f"{NAME}"],
        license=LICENSE,
        long_description=LONG_DESCRIPTION,
        long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER or AUTHOR,
        maintainer_email=MAINTAINER_EMAIL or AUTHOR_EMAIL,
        url=URL,
        download_url=DOWNLOAD_URL,
        zip_safe=ZIP_SAFE,
        include_package_data=INCLUDE_PACKAGE_DATA,
        # setup_requires=["isort"],
        install_requires=REQUIRED,
        extras_require=EXTRAS,
        package_data=PACKAGE_DATA,
        project_urls=PROJECT_URLS,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
    )


if __name__ == "__main__":
    main()
