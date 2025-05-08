# Arizona Redistricting Analysis

A comprehensive analysis of Arizona's redistricting process using computational methods to evaluate gerrymandering, demographic patterns, and electoral fairness.

## Project Overview

This project analyzes Arizona's 2020 redistricting process through multiple lenses:
- Computational analysis of district plans using MCMC (Markov Chain Monte Carlo) simulations
- Evaluation of gerrymandering metrics including cut edges, democratic-won districts, and efficiency gap
- Analysis of majority-minority districts with focus on Native American representation
- Historical context and demographic changes in Arizona

## Analysis Methods

### MCMC Redistricting Simulation
The project uses Markov Chain Monte Carlo methods to generate and analyze alternative district plans, providing a statistical framework for evaluating the current districting scheme against a large ensemble of possible alternatives.

### Gerrymandering Metrics
Several quantitative metrics are employed to assess potential gerrymandering:
- Cut edges analysis of Markov chain partitions
- Democratic-won districts counting
- Efficiency gap calculations
- Analysis of 2020 Presidential and U.S. Senate election results

### Majority-Minority District Analysis
Short burst analysis is used to evaluate the representation of Native American communities in district plans, ensuring compliance with the Voting Rights Act and fair representation of minority populations.

## Project Structure

```
arizona-redistricting/
├── data/
│   ├── AZ_shapefile/        # Geographic boundary data
│   ├── AZ_recom_2020_SEND/  # MCMC analysis results
│   └── AZ_sb/               # Short burst analysis data
├── src/
│   ├── AZ_MAUP.ipynb       # MAUP analysis notebook
│   ├── AZ_recom.ipynb      # MCMC redistricting notebook
│   ├── AZ_sb.ipynb         # Short burst analysis notebook
│   ├── gingleator.py       # Analysis utilities
│   └── sb_runs.py          # Short burst run configurations
└── report/                  # Detailed analysis reports and visualizations
```

## Key Features

- **Historical Analysis**: Comprehensive review of Arizona's redistricting history from the 1990s to present
- **Demographic Tracking**: Analysis of population changes and demographic shifts
- **Computational Methods**: Implementation of MCMC and short burst analysis for district evaluation
- **Visualization**: Generated visualizations of district plans and analysis results
- **Legal Context**: Integration of relevant court cases and legal framework

## Data Sources

Please see the citation in the report for data source

## Key Findings

The analysis provides insights into:
- The fairness of Arizona's current district map
- Representation of minority communities
- Comparative analysis with alternative district plans
- Historical trends in redistricting outcomes

## Authors

- Marcus Kuan - [@shenghungKuan](https://github.com/shenghungKuan)
- Seth Villavicencio - [@sethvilla](https://github.com/sethvilla)

## License

This project is open source and available under the [MIT License](LICENSE).

## Citations

For a complete list of references and data sources, please see the detailed report in the `report` directory.