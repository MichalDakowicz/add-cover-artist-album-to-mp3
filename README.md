# .mp3 Song Tagger

This Python script effectively adds album information and cover art to MP3 files in a given directory. It employs the `mutagen` library for seamless metadata handling.

## Prerequisites

-   Python 3 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
-   `mutagen` library: Install using `pip install mutagen`

## Usage

1. **Prepare your MP3s:** Organize the MP3 files you wish to update within a single directory.
2. **Get the album cover:** Download or create the album cover image and save it as "cover.png" in the same directory as your MP3 files.
3. **Run the script:**
    - Open a terminal or command prompt.
    - Navigate to the directory containing the Python script.
    - Execute the script: `python main.py`

## Script Explanation

-   **Imports:** Includes the `os` and `mutagen` libraries.
-   **Functions:**
    -   `get_mp3_files(directory)`: Locates all MP3 files within the specified directory.
-   **Main Execution (`if __name__ == "__main__":`)**
    -   Prompts the user for:
        -   Directory containing MP3 files (this will also be used as the album name)
        -   The cover artist's name
    -   Calls the `main` function to process the files.

## How It Works

1. The script requests input for a directory and cover artist's name.
2. It finds all MP3 files within the provided directory.
3. The directory name is automatically used as the album name.
4. The script updates each MP3 file's metadata, adding the album name and artists' information.
5. It embeds the "cover.png" image as the album artwork.

## Important Notes

-   This script relies on a "cover.png" file present in the same directory as the MP3 files. Ensure you have the image ready.
-   The embedded cover art should be visible on music players and platforms that support MP3 metadata, including Android devices and Spotify (on both Windows and Android).
-   While extensive testing has been done, compatibility across all possible music players cannot be guaranteed.
