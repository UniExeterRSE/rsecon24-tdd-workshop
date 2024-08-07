def make_table_str(data: dict) -> str:
    if not data:
        return ""
    
    headers = list(data)
    header_column_names = "  ".join(headers)
    header_border = "-" * len(header_column_names)
    return header_column_names + "\n" + header_border
