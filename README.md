# abhailes_wall
Wallpaper engine utilising NASA's APOD (Astronomy Picture Of The Day)

## Setup
1. Clone the repository
2. Get an API key from NASA's API
3. Copy `public/example_api_data.json` to `public/api_data.json`
4. Fill in the `api_key` field in `api_data.json` with your API key
5. Create a virtual environment
6. Install the requirements
      `pip install -r requirements.txt`
7. Run the script
      `sh ./main.sh`

## Usage
The script will download the Astronomy Picture Of The Day from NASA's API and set it as your wallpaper.
