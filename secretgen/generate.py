from os import PathLike
from pathlib import Path
from typing import Union
import secrets

PathLikeStr = Union[PathLike[str], str, Path]
cache: dict[Path, bytes] = {}


def create_secret(path: PathLikeStr, length: int) -> bytes:
    path = Path(path)
    if path in cache:
        return cache[path]

    if path.exists() and path.is_file():
        token = path.read_bytes()
    else:
        token = secrets.token_bytes(length)
        path.write_bytes(token)

    cache[path] = token
    return token
