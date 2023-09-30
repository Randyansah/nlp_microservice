from lib.hug_me import trans_version
import transformer


def test_trans():
    assert "2.13.0" in trans_version(transformer.version.VERSION)    