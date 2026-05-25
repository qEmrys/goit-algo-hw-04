import argparse
import shutil
from pathlib import Path


def read_directory(path: Path) -> list[Path]:
    files = []
    for item in path.iterdir():
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            files.extend(read_directory(item))
    return files


def copy_files(files: list[Path], destination: Path):
    for file in files:
        ext = file.suffix.lstrip(".").lower() or "no_extension"
        target_dir = destination / ext
        target_dir.mkdir(parents=True, exist_ok=True)
        try:
            shutil.copy(file, target_dir / file.name)
            print(f"Скопійовано '{file}' до '{target_dir}'.")
        except Exception as e:
            print(f"Помилка копіювання '{file}': {e}")


def main():
    parser = argparse.ArgumentParser(description="Copy files from a directory to a destination.")
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path, nargs="?", default=Path("dist"))

    args = parser.parse_args()

    if not args.source.is_dir():
        print(f"Помилка: '{args.source}' не є директорією.")
        return

    files = read_directory(args.source)
    copy_files(files, args.destination)


if __name__ == "__main__":
    main()
