# Unemployment Rate Analysis (1991 - 2021)

## Project Overview
This project provides a comprehensive analysis of global unemployment rates over three decades, with a specialized focus on the socio-economic impact of the COVID-19 pandemic. Using Python, we explore trends across countries and regions to identify patterns of resilience and vulnerability.

## Dataset
The dataset (`unemployment analysis.csv`) contains unemployment percentage data for over 200 countries and regional aggregates from 1991 to 2021.

## Key Objectives
- **Data Transformation**: Convert wide-format annual data into a time-series ready format.
- **Trend Visualization**: Identify long-term global and regional unemployment cycles.
- **COVID-19 Impact**: Quantify the sudden spike in unemployment between 2019 and 2020.
- **Policy Insights**: Suggest evidence-based economic interventions.

## Installation & Usage
1. Clone the repository.
2. Ensure the dataset is in the `data/` folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the analysis:
   ```bash
   python analysis.py
   ```

## Key Findings
- **The 2020 Shock**: Globally, 2020 marked a significant departure from the downward trend seen in the mid-2010s. Countries like Costa Rica and Panama saw unprecedented double-digit spikes.
- **Structural vs. Occasional Unemployment**: Regional analysis shows that while the EU and North America experienced "shock" unemployment due to lockdowns, regions like the Arab World face higher structural unemployment rates that remained consistently high regardless of the pandemic.
- **Recovery Patterns**: By late 2021, many nations began showing signs of recovery, though rates in many developing nations remained elevated above 2019 levels.

## Policy Recommendations
1. **Targeted Stimulus**: Focus on sectors most affected by the 2020 shock (tourism, hospitality) to prevent temporary unemployment from becoming permanent.
2. **Reskilling Programs**: For regions with high structural unemployment, investment in vocational training for digital and green economies is essential.
3. **Social Safety Nets**: The data suggests that countries with robust automatic stabilizers (like the EU) managed the volatility better than those without.

## Repository Structure
```text
├── data/               # Raw CSV data
├── analysis.py         # Main processing and visualization script
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation and findings
```