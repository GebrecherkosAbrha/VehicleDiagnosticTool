# Vehicle Diagnostic Tool

## Overview

The Vehicle Diagnostic Tool is designed to diagnose potential issues in vehicle components such as the engine, battery, and tires. The tool generates random sensor data and analyzes it to provide diagnostic results.

## Features

- Diagnoses engine, battery, and tire issues based on configurable thresholds.
- Uses a data generator to simulate sensor readings.
- Provides clear output for identified issues.


## Setup Instructions

1. Clone the repository:

   ```bash
    git clone https://github.com/GebrecherkosAbrha/VehicleDiagnosticTool.git
   ```

2. Navigate to the project directory:
   ```bash
   cd VehicleDiagnosticTool
   ```

## Usage

1. Run the main program:

   ```bash
   python main.py
   ```

2. Follow the prompts to run diagnostics or exit.

## Testing

To run tests, use pytest:

```bash
pytest tests/
```

This will run all tests in the tests directory.

## Configuration

You can adjust diagnostic thresholds in the `config.py` file.
