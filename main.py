from pathlib import Path
import shutil


# File categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".java", ".cpp", ".c", ".html", ".css", ".js"]
}


def get_file_category(file):
    """Return the category of a file based on its extension."""

    extension = file.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_destination(destination):
    """Create a unique file name if the destination already exists."""

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}"
            f"{destination.suffix}"
        )

        new_destination = destination.parent / new_name

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_files(folder_path):
    """Organize files inside the given folder."""

    folder = Path(folder_path)

    if not folder.exists():
        print("Error: Folder does not exist.")
        return

    if not folder.is_dir():
        print("Error: The provided path is not a folder.")
        return

    files_processed = 0

    print("\nStarting file organization...\n")

    for file in folder.iterdir():

        # Ignore folders
        if not file.is_file():
            continue

        category = get_file_category(file)

        category_folder = folder / category

        # Create category folder if it doesn't exist
        category_folder.mkdir(exist_ok=True)

        destination = category_folder / file.name

        # Avoid overwriting existing files
        destination = get_unique_destination(destination)

        try:
            shutil.move(str(file), str(destination))

            print(
                f"Moved: {file.name} "
                f"→ {category}/"
            )

            files_processed += 1

        except OSError as error:
            print(f"Could not move {file.name}: {error}")

    print("\n====================================")
    print("       ORGANIZATION COMPLETED")
    print("====================================")
    print(f"Files processed: {files_processed}")
    print("====================================")


def main():

    print("====================================")
    print("      PYTHON FILE ORGANIZER")
    print("====================================")

    folder_path = input(
        "Enter the folder path to organize: "
    ).strip()

    organize_files(folder_path)


if __name__ == "__main__":
    main()