# .mp3 Song Detail Adder

This Python script is used to add album information and cover art to a collection of MP3 files within a specified directory. It utilizes the `eyed3` and `mutagen` libraries to manipulate the metadata of MP3 files.

## **Prerequisites**

-   Python 3 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
-   `eyed3` library: Install using `pip install eyed3`
-   `mutagen` library: `pip install mutagen`

## **Usage**

1. **Prepare your MP3 files:** Place all the MP3 files that you want to update into a single directory.
2. **Get the album cover:** Download or make the image for the album cover and name it "cover.png". Place this image file in the same directory as your MP3 files.
3. **Run the script:**
    - Open a terminal or command prompt.
    - Navigate to the directory where you saved the Python script.
    - Execute the script using the following command:

```bash
python main.py
```

## **Script Explanation**

-   **Import Statements:** Imports the `os`, `eyed3`, and `mutagen` libraries.
-   **Functions:**
    -   `get_mp3_files(directory)`: Scans the given directory to find all MP3 files.
    -   `set_album_info(mp3_file, album, cover_artist)`: Uses `eyed3` to set the album name and artist information within the MP3 file's metadata.
    -   `add_album_cover(mp3_file, album_cover)`: Uses `mutagen` to embed the "cover.png" image file as the album artwork.
-   **Main Execution (`if __name__ == "__main__":`)**
    -   Prompts the user to enter the following:
        -   The directory containing the MP3 files
        -   The name of the cover artist
    -   Calls the `main` function to process the files.

## **How It Works**

1. The script asks you to input a directory and the cover artist's name.
2. Locates all MP3 files within the provided directory.
3. Extracts and uses the provided directory name as the album name.
4. Updates the metadata of each MP3 file, setting the album and artist information.
5. Embeds the "cover.png" file as the album artwork in each MP3 file.

## **Notes:**

-   This script assumes the presence of a "cover.png" file in the same directory as the MP3 files. Make sure you have a suitable image ready.
-   The script automatically uses the directory name as the album name for all files.
