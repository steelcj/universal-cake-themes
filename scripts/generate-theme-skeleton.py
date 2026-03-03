#!/usr/bin/env python3
"""
generate-theme-skeleton.py

UniversalCake Theme Skeleton Generator
---------------------------------------

• Loads default YAML: scripts/theme-definition.yml
• Allows overrides via --theme-name and --theme-creator
• OS agnostic
• Safe directory creation
• No shell calls
"""

import sys
from pathlib import Path
import argparse

try:
    import yaml
except ImportError:
    print("Error: PyYAML is required.")
    print("Install with: pip install pyyaml")
    sys.exit(1)


DEFAULT_YAML_PATH = Path("scripts/theme-definition.yml")


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def create_file(path: Path):
    if not path.exists():
        path.touch()
        print(f"Created file: {path}")
    else:
        print(f"Skipped existing file: {path}")


def create_directory(path: Path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {path}")
    else:
        print(f"Skipped existing directory: {path}")


def generate_structure(base_path: Path, structure: list):
    for item in structure:
        item_path = base_path / item

        # Ensure cross-platform normalization
        item_path = Path(str(item_path))

        if item.endswith("/"):
            create_directory(item_path)
        elif "." in item_path.name:
            create_directory(item_path.parent)
            create_file(item_path)
        else:
            create_directory(item_path)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a UniversalCake theme skeleton."
    )

    parser.add_argument(
        "--theme-name",
        type=str,
        help="Override theme name from YAML"
    )

    parser.add_argument(
        "--theme-creator",
        type=str,
        help="Override theme creator from YAML"
    )

    parser.add_argument(
        "--yaml",
        type=str,
        default=str(DEFAULT_YAML_PATH),
        help="Path to YAML definition file (default: scripts/theme-definition.yml)"
    )

    args = parser.parse_args()

    yaml_path = Path(args.yaml).resolve()

    if not yaml_path.exists():
        print(f"YAML file not found: {yaml_path}")
        sys.exit(1)

    config = load_yaml(yaml_path)

    # Load values from YAML
    theme_config = config.get("theme", {})
    theme_name = args.theme_name or theme_config.get("name")
    theme_creator = args.theme_creator or theme_config.get("creator")
    structure = config.get("structure")

    if not theme_name:
        print("Error: theme.name is required (YAML or --theme-name).")
        sys.exit(1)

    if not structure:
        print("Error: structure section is required in YAML.")
        sys.exit(1)

    base_dir = Path("themes").resolve()
    theme_dir = base_dir / theme_name

    print(f"\nGenerating theme: {theme_name}")
    if theme_creator:
        print(f"Creator: {theme_creator}")

    create_directory(theme_dir)
    generate_structure(theme_dir, structure)

    print("\nTheme skeleton generation complete.")


if __name__ == "__main__":
    main()
