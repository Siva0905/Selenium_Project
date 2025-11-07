def test_file_create_delete(tmp_path):
    f = tmp_path / "test.txt"; f.write_text("hello")
    assert f.read_text() == "hello"; f.unlink(); assert not f.exists()

def test_file_permissions(tmp_path):
    f = tmp_path / "test.txt"; f.write_text("data")
    assert f.exists() and f.is_file()

def test_file_content(tmp_path):
    f = tmp_path / "test.txt"; f.write_text("content")
    assert "content" in f.read_text()

def test_binary_file(tmp_path):
    f = tmp_path / "bin.dat"; f.write_bytes(b"\x00\x01")
