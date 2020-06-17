from typing import List
from pathlib import Path

try:
    DEFAULT_ENCODING
except:
    from locale import getpreferredencoding
    DEFAULT_ENCODING: str = getpreferredencoding(do_setlocale=True) or "utf-8"


def readme(file_name: str = "readme.md", path_name=__file__) -> (str):
    """ Returns the text of the README file

        The default file is `README.md` and is *NOT* case sensitive. (e.g. `README` is the same as `readme`)
        Can load *any* text file, but the default search path is setup for readme files

        ```
        Search path = ["readme.md", "readme.rst", "readme", "readme.txt"]
        ```

        Example:

        ```
        long_description=readme()
        ```
        """

    search_list: List[str] = ["readme.md",
                              "readme.rst", "readme", "readme.txt"]
    if file_name not in search_list:
        search_list.insert(0, file_name)
    found: bool = False
    for searchfile in search_list:
        for parent in Path(path_name).resolve().parents:
            find_path = Path(parent / searchfile)
            if find_path.exists():
                found = True
                break
        if found:
            break
    if found:
        try:
            with open(find_path, mode="rt", encoding=DEFAULT_ENCODING) as fd:
                return fd.read()
        except IOError as e:
            raise IOError(f"Cannot read from the 'readme' file '{find_path}'")
    else:
        raise FileNotFoundError(
            f"Cannot find project 'readme' file in project tree. Search list = {search_list}"
        )
