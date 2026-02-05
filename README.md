# Weather API Project

A simple Python weather API project created with Claude Code and managed by OpenClaw assistant MiniRami.

## Project Details
- **Created:** 2026-02-05
- **Author:** MiniRami (OpenClaw AI Assistant)
- **GitHub Account:** [MiniRami298](https://github.com/MiniRami298)
- **Repository:** https://github.com/MiniRami298/weather-api-project

## Features
- Fetches weather data from OpenWeatherMap API
- Displays temperature, humidity, and weather conditions
- Simple command-line interface
- Error handling for API requests

## Setup
1. Install dependencies:
   ```bash
   uv pip install requests python-dotenv
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Add your OpenWeatherMap API key to .env
   ```

3. Run the weather script:
   ```bash
   python weather.py
   ```

## Project Structure
```
weather-api-project/
├── weather.py          # Main weather application
├── README.md           # This file
└── .env.example        # Environment variables template
```

## Technologies Used
- Python 3.x
- Requests library for HTTP calls
- OpenWeatherMap API
- UV package manager

## Created By
This project was automatically created and managed by **MiniRami**, an OpenClaw AI assistant running on Omar's Windows machine.

## License
MIT