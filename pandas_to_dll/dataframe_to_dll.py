# -*- coding: utf-8 -*-

# https://pandas.pydata.org/docs/development/contributing.html#type-hints
def dataframe_to_dll(dataframe, table_name: str) -> str:
    """
    We use this function as an example for some real logic.

    This is how you can write a doctest:

    .. code:: python

        >>> dataframe_to_dll(nba_stats_df, "playoff_game_logs")
        "create table playoff_game_logs, etc, etc"

    Enjoy!
    """

    # https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes
    data_dtypes = dataframe.dtypes.reset_index().rename(
        columns={"index": "colname", 0: "datatype"}
    )

    # Mapping pandas datatypes into SQL BUT need to refactor.
    data_dtypes["sql_dtype"] = data_dtypes.datatype.astype(str).map(
        {
            "object": "varchar(24)",
            "float64": "float",
            "int64": "int",
            "datetime64[ns]": "timestamp",
            "bool": "boolean",
        }
    )

    # Joining Pandas rows to list of string with carriage return
    dll_from_rows = ", ".join(
        [
            "{colname} {sql_dtype} \n".format(**row)
            for row in data_dtypes[["colname", "sql_dtype"]].to_dict("records")
        ]
    )

    ddl_string_statement = """
    create table {tablename}
    (
    {ddl}
    )
    DISTSTYLE ALL
    ;

    """.format(
        tablename=table_name, ddl=dll_from_rows
    )

    return ddl_string_statement
