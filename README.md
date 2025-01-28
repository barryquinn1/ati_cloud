# High Performance Cloud Computing in Finance

This repository contains slides for the course "AI and Trading (FIN7030)" focused on high-performance cloud computing in finance. The slides are created using Quarto with Reveal.js for presentation.

## Course Overview

The course covers the following topics:
- What is cloud computing?
- Introduction to the Q-RaP
- Taxonomy of parallel computing
- Performance computing in Python

## Setup Instructions

### Prerequisites

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) should be installed on your system.
- [Posit IDE](https://posit.co/products/open-source/rstudio/) (formerly RStudio) for running R and Python code.

### Setting Up the Conda Environment

1. **Create the Conda Environment:**

   Open your terminal and run the following command to create a new conda environment named `finance_hpc`:

   ```bash
   conda create -n finance_hpc python=3.9
   ```

2. **Activate the Environment:**

   ```bash
   conda activate finance_hpc
   ```

3. **Install Python Dependencies:**

   Use the `requirements.txt` file to install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Setting Up R and Reticulate

1. **Install R Packages:**

   Open R or Posit IDE and run the following command to install the required R packages:

   ```r
   install.packages(c("reticulate", "htmltools", "knitr", "tidyverse", "babynames", "fontawesome", "DiagrammeR", "xaringanExtra", "timevis"))
   ```

2. **Configure Reticulate:**

   In your R session, ensure that the `reticulate` package is configured to use the `finance_hpc` conda environment:

   ```r
   library(reticulate)
   use_condaenv("finance_hpc")
   ```

3. **Unset RETICULATE_PYTHON (if necessary):**

   If you encounter issues with the Python environment, you can unset the `RETICULATE_PYTHON` environment variable:

   ```r
   Sys.unsetenv("RETICULATE_PYTHON")
   ```

## Running the Presentation

To render the presentation, open the `index.qmd` file in Posit IDE and click the "Render" button. Ensure that the `finance_hpc` environment is active and all dependencies are installed.

## License

This project is licensed under the MIT License.