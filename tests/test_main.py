from ohsome_filter_to_sql.main import OhsomeFilterToSql, main


def test_main():
    assert isinstance(main(), OhsomeFilterToSql)
