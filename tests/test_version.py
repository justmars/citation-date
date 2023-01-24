import toml

import citation_date


def test_version():
    assert (
        toml.load("pyproject.toml")["tool"]["poetry"]["version"]
        == citation_date.__version__
    )
