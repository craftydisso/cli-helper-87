import json
from typing import Any, Dict

def parse_json(data: str) -> Dict[str, Any]:
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return {}  # Return an empty dict on error


def format_data(data: Dict[str, Any]) -> str:
    return json.dumps(data, indent=4)


def get_value(data: Dict[str, Any], key: str, default: Any = None) -> Any:
    return data.get(key, default)


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def filter_keys(data: Dict[str, Any], keys: set) -> Dict[str, Any]:
    return {k: data[k] for k in data if k in keys}
