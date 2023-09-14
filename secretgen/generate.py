from os import PathLike
from pathlib import Path
from typing import Union
import secrets

PathLikeStr = Union[PathLike[str], str, Path]


def create_secret(path: PathLikeStr, length: int) -> bytes:
    path = Path(path)

    if path.exists() and path.is_file():
        return path.read_bytes()

    token = secrets.token_bytes(length)
    path.write_bytes(token)
    return token
