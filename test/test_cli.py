import starter.cli as cli


def test_cli_main_empty(capsys):
    assert cli.main() == 0  # type: ignore
    out, err = capsys.readouterr()
    assert 'starter' in out.lower()
    assert not err


def test_cli_main_42():
    assert cli.main([42]) == 0  # type: ignore
