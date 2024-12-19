# Polyline Analyzer

A Python tool for parsing and visualizing polyline data from XML files.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your XML file containing polyline data in the project directory
2. Run the script:
```bash
python polyline_parser.py
```

The script will:
- Parse the XML file containing polyline data
- Extract vertex coordinates and bounds information
- Generate a visualization of all polylines
- Save the plot as 'polylines.png' (or display it if no save path is specified)

## Features

- Parses XML files containing polyline vertex data
- Extracts bounds information from the XML
- Visualizes multiple polylines on a single plot
- Maintains aspect ratio for accurate visualization
- Supports saving plots to file
