import json
import yaml
import joblib
from pathlib import Path
from typing import Any

from wine_quality_mlops.utils.logger import logger


def read_yaml(path_to_yaml: Path) -> dict:
    """
    Read YAML file and return dictionary.
    """

    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)

            if content is None:
                raise ValueError("YAML file is empty")

            logger.info(f"YAML file loaded: {path_to_yaml}")

            return content

    except Exception as e:
        logger.exception("Failed to read YAML file")
        raise e


def create_directories(paths: list[Path], verbose: bool = True):
    """
    Create directories.
    """

    for path in paths:
        path.mkdir(parents=True, exist_ok=True)

        if verbose:
            logger.info(f"Created directory: {path}")


def save_json(path: Path, data: dict):
    """
    Save dictionary as JSON.
    """

    with open(path, "w") as file:
        json.dump(data, file, indent=4)

    logger.info(f"JSON file saved: {path}")


def load_json(path: Path) -> dict:
    """
    Load JSON file.
    """

    with open(path, "r") as file:
        content = json.load(file)

    logger.info(f"JSON file loaded: {path}")

    return content


def save_bin(data: Any, path: Path):
    """
    Save binary object using joblib.
    """

    joblib.dump(data, path)

    logger.info(f"Binary file saved: {path}")


def load_bin(path: Path) -> Any:
    """
    Load binary object.
    """

    data = joblib.load(path)

    logger.info(f"Binary file loaded: {path}")

    return data