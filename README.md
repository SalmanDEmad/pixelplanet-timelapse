# Guide
Pixel Planet Time Lapse Generator. You can create a time-lapse of Pixel Planet for a specific time in a specific area with this bot.

## Installation

1. How to install this:

   Open the terminal and clone the repository:
   
git clone https://github.com/SalmanDEmad/pixelplanet-timelapse.git

Unzip the file and navigate to the project directory:

cd pixelplanet-timelapse

Install the required dependencies:

pip install -r requirements.txt


## Configuration

1. Make some changes:

Open the `main.py` file and go to line 38.

It says `download_folder = "path to where the downloaded files go normally."`

Change the value to the directory path of your computer's download folder. Note: Don't put where you want the file downloaded.

## Usage

1. How to use:

In the terminal, run the following command:

py main.py


It will ask for the Pixel Planet coordinate link. The link should look like this: `https://pixelplanet.fun/#d,-15939,-8212,-12`

Next, it will ask for the date from when you want to start archiving. Enter the date in the format `yyyy-mm-dd`. For example: `2023-02-23`.

The tool will automatically take screenshots and collect them in the specified download folder.

Note: The time-lapse generation may take some time depending on the duration and area selected.

Turn this into a proper README file by adding additional information and sections as necessary. Feel free to customize and adapt the instructions based on your specific project requirements.

Enjoy!!!
