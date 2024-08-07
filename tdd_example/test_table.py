from table import make_table_str


def test_empty_table_returns_empty_string():
    assert make_table_str({}) == ""


def test_headers_given_by_dict_keys():
    for header in ["colA", "colB"]:
        data = {header: []}
        table = make_table_str(data)
        assert table == f"{header}\n----"

    data = {"colA": [], "colB": []}
    table = make_table_str(data)
    assert table == "colA  colB\n----------"
