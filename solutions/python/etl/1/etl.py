def transform(legacy_data):
    return {item.lower():keys for keys, sublist in legacy_data.items() for item in sublist}