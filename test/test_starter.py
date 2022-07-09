import starter.starter as impl


def test_process_empty():
    assert impl.process() == (0, ['starter'])  # type: ignore


def test_process_main_seq_42():
    assert impl.process([42]) == (0, ['integer', 'starter'])  # type: ignore


def test_process_main_seq_foo():
    assert impl.process(['foo']) == (1, [])  # type: ignore


def test_process_main_text_foo():
    assert impl.process('foo') == (1, [])  # type: ignore
