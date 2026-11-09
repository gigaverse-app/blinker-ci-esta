import sys


def test_gate_probe_fails_only_on_python_3_11() -> None:
    assert sys.version_info[:2] != (3, 11)
