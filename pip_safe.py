def pip_safe_name(s: str):
    """ Return a name that is converted to pypi safe format. """
    return s.lower().replace("-", "_").replace(" ", "_")
