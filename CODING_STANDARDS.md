## Coding guidelines for Python

-   The following standards are inspired from [Coding guidelines for TypeScript](https://github.com/Microsoft/TypeScript/wiki/Coding-guidelines) (which is recommended reading), although any pre-existing practices or styles that are obviously in place in an existing codebase override either style guide.

### Example - incomplete code as an example of formatting

```py
#!/usr/bin/env python3
""" link_checker.py """

import logging
from contextlib import closing
from dataclasses import dataclass, Field, field
from sys import argv, stderr, stdout

from requests import codes as Request_Codes, get, Response
from requests.exceptions import RequestException

DEFAULT_ENCODING: str = 'UTF-8'

_example_url: str = 'https://www.skeptycal.com'
log = logging.GetLogger(__file__)

@dataclass
class WebPage:
    url: str = _example_url
    DEFAULT_ENCODING: Final[str] = DEFAULT_ENCODING
    _response: requests.Response = field(init=False)


    def __post_init__(self):
        _response = self._get(self.url)

    ...
    ...
    ...

    def _get(self,
            url: str,
            encoding: str = DEFAULT_ENCODING)
            -> (str, Exception):
    """
    Attempts to get the content at `url` by making an HTTP
    GET request. If the content-type of response is some
    kind of HTML/XML, return the text content, otherwise
    return None.
    """

    try:
        with closing(get(url, stream=True)) as resp:
            if self.is_good_response(resp):
                self._response = resp
                return resp.content
            else:
                return None

    # !! http errors are ignored here, but logged !!
    except RequestException as e:
        log.error(f"Error during request to {url} : {str(e)}")
        return None

    @property
    def headers(self)-> (Dict):
        '''
        Returns a dict of headers in the form:
        {
            'content-encoding': 'gzip',
            'transfer-encoding': 'chunked',
            'connection': 'close',
            'server': 'nginx/1.0.4',
            'x-runtime': '148ms',
            'etag': '"e1ca502697e5c9317743dc078f67693f"',
            'content-type': 'application/json'
        }
        '''
        if self._response:
            return self._response.headers

def main(args=argv[1:]):
    ''' link checker for urls passed in as CLI args. '''
    _silent_: bool = False
    if args[0] == 'silent':
        _silent_ = True
        args = args[1:]
    for url in args:
        wp = WebPage(url)
        if wp.status_code == Request_Codes.ok:
            if _silent_:
               log.info(f"  PASS : {url}")
            else:
                print(f"  PASS : {url}", file=stdout)
        else:
            if _silent_:
               log.error(f"  FAIL : {url}")
            else:
                print(f"  FAIL : {url}", file=stderr)

if __name__ == "__main__":
    main()
```

---

### Names

-   Use `PascalCase` for class and type names.
-   Use `ALL_CAPS` for constant values.
-   Use `snake_case` for function names.
-   Use `snake_case` for property names and local variables.
-   Use whole words in names when possible.
-   Names must start with a single alpha/underscore `'[a..z][A..Z]_'` character and must contain only alphanumeric/underscore `'[a..z][A..Z][0..9]_'` characters.

### Underlines ... yes, it's a thing in Python

-   Use `_` as a prefix for private properties (but remember that in python these are not enforced, only agreed upon).
-   Use `__` as a prefix for properties that may be in danger of collision with other class derivatives or parents. (name mangling)
-   Use `_` as a suffix for properties that would otherwise conflict with python keywords.
-   Do not use 'dunder' (double underline) methods (like `__add__`) unless you are specifically overriding inherited methods.

### Organization

-   Do not export types/functions unless you need to share it across multiple components. Use the `__all__` list to specify preferred exports.
-   Use the `_` prefix to prevent private items from being automatically imported during `*` imports (e.g. `from sys import *`)
-   Avoid introducing new types/values to the global namespace.
-   Prefer `dataclass` structures if available (3.7+)
-   Within a file, a Doc should come first, then imports, type definitions, constants, variables, classes, and finally a `main()` function if desired.

*   If there is no ardent debate about type definitions, I recommend including them. e.g.

```py
# instead of
def parse(s):
    ...

# use this unless other guidance is available
def parse(s: str) -> str:
    ...
```

### null and undefined

Use None. Do not try to be creative with values for null.

### Comments

-   Doc Style Comments (DocBlocks) must bounded by triple quotes (`'''`)
-   Use Doc style comments for modules, functions, and classes.
-   Avoid inline comments (beginning with #) by writing clean, readable code

### Strings

Use single quotes for strings unless a single quote appears in the string.

### Imports

-   Import only modules, classes, or functions that are required.

### Style

#### List Comprehensions

`[expression for item in iterable if condition_eval]`

-   Use the list constructor when possible (creating lists from iterables)
-   Use generators when the entire list is not needed (when not directly manipulating the list elements)
-   Use list comprehensions when it is clear and readable.

### Code Formatting

-   Use `pylint` and `autopep8` or equivalent to format `python` code.
-   Use `prettier` to format `json`, `html`, and `JavaScript` code.
-   Use a single line between sections (imports, constants, etc) and double lines around class definitions
-   Use 4 spaces per indentation. Not Tabs ... without tabs ... sans tabulations ... even Guido finally agreed ... use spaces
-   All files must end with an empty line.
