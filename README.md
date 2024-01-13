# Engine Math

This repository provides a suite of tools for automotive enthusiasts and engineers to calculate critical engine parameters and gear ratios. The current version includes two main calculators:

1. **Compression Calculator**

   This module calculates the compression ratio of an engine. The calculation takes into account various engine parameters such as bore diameter, stroke length, combustion chamber volume, piston dome volume, and more. Users can input these parameters through a JSON file (`engine_parameters.json`), and the script (`compression_calculator/main.py`) computes the compression ratio, quench, and engine displacement.

   **Key Features:**

   - Calculation of compression ratio
   - Determination of engine quench
   - Engine displacement computation
   - Input File: `compression_calculator/engine_parameters.json`
   - Main Script: `compression_calculator/main.py`

2. **Gear Calculator**

   The gear calculator (`gear_calculator/main.py`) helps in determining drive ratios and expected cruise RPMs for different gears. It is useful for optimizing transmission settings and understanding the vehicle's performance at various speeds.

   **Key Features:**

   - Calculation of drive ratios based on transmission and rear differential gear ratios
   - Estimation of cruise RPMs for various speeds
   - PrettyTable representation for clear and concise output
   - Main Script: `gear_calculator/main.py`

## Usage

To use these calculators, clone the repository and run the respective Python scripts. Make sure to update the input files with your specific engine or gear parameters before execution.

## Contributing

Contributions to enhance existing calculators or to add new functionalities are welcome. Please follow standard GitHub contribution guidelines.

## License

This project is open-source and available under the [MIT License](#mit-license).

---

## MIT License

MIT License

Copyright (c) 2024 Matt Woolly

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

**The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.**

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. **IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.**
