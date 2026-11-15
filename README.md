# 🚗 U.S. Road Accident Analysis (2016–March 2023)

**An Exploratory Data Analysis of 7.73 Million U.S. Traffic Accident Records Using Python**

## 📌 Project Overview

This project explores over **7.73 million traffic accident records** across the United States from 2016 to March 2023. The primary objective is to identify patterns in accident frequency, geographical distribution, weather conditions, road infrastructure, and traffic-impact severity.

Using Python, Pandas, NumPy, Matplotlib, and GeoPandas, this analysis investigates when and where accidents occur, how environmental and infrastructure conditions relate to accident patterns, and how severity distributions vary across different categories.

The analysis covers **49 states, 13,679 cities, and 1,871 counties**, providing a large-scale overview of recorded U.S. traffic accidents.

## 🎯 Project Objectives

- Analyze accident frequency across different years, months, days, and hours.
- Identify states and cities with the highest numbers of recorded accidents.
- Explore geographical accident patterns and hotspots.
- Investigate the relationship between weather conditions and accident severity.
- Examine accident distributions around road infrastructure features.
- Compare severity distributions across geographical, temporal, and environmental categories.
- Extract meaningful insights while acknowledging data limitations.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data cleaning, manipulation, and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| GeoPandas | Geographical data analysis |
| Jupyter Notebook | Interactive analysis |
| Parquet | Efficient dataset storage |

## 📂 Project Structure

```text
US-Road-Accident-Analysis/
│
├── new_analysis.ipynb
│
├── US_Accidents_March23.parquet
│
├── README.md
│
└── images/
    ├── overview.png
    ├── geographical_analysis.png
    ├── weather_analysis.png
    └── severity_analysis.png
```

*Note: The images folder is suggested for storing exported charts and screenshots. The notebook and Parquet dataset are the primary analysis files.*

## 📊 Dataset Overview

The project uses the **US Accidents (2016–March 2023)** dataset.

- **Total records:** Approximately 7.73 million
- **Geographical coverage:** 49 U.S. states
- **Cities:** 13,679
- **Counties:** 1,871
- **Time period:** 2016 – March 2023
- **Format used for analysis:** Parquet

The original CSV dataset was converted into Parquet format to improve data-loading and processing efficiency.

### Important Note About Severity

The dataset defines accident severity based on its impact on traffic flow:

- **Level 1:** Lowest traffic impact
- **Level 2:** Moderate traffic impact
- **Level 3:** Serious traffic impact
- **Level 4:** Highest traffic impact

These severity levels do **not** represent bodily injury classifications or accident fatality levels.

## ⚙️ Data Cleaning & Feature Engineering

Several preprocessing and feature-engineering steps were performed to prepare the dataset for analysis.

### Data Cleaning
- Removed unnecessary columns that were not required for the analysis.
- Checked for duplicate records.
- Replaced missing categorical values with `Unknown`.
- Preserved missing numerical values rather than introducing potentially misleading artificial values.
- Investigated unusually high wind-speed observations.

### Feature Engineering

Created additional features to support deeper analysis:

| Feature | Description |
|---|---|
| Year | Extracted accident year |
| Month | Extracted accident month |
| Day | Extracted day of the month |
| Hour | Extracted accident hour |
| Day_of_Week | Extracted weekday |
| Weekend_Weekday | Categorized records into weekdays and weekends |
| Duration_Minutes | Calculated accident duration |
| Temperature(C) | Converted Fahrenheit to Celsius |
| Humidity_Group | Categorized humidity levels |
| Visibility_Group | Categorized visibility levels |
| Wind_Speed_Group | Categorized wind speeds |
| Precipitation_Group | Categorized precipitation levels |
| Severity_Label | Converted severity codes into descriptive labels |

## 🔍 Exploratory Data Analysis

The analysis is organized into five major analytical sections.

### 1. Overall Accident Analysis

Examined accident frequency and distribution across:

- Yearly and monthly trends.
- Hourly accident patterns.
- Weekday versus weekend distributions.
- Average accident duration.
- Average affected road distance.
- Seasonal accident patterns.

### 2. Geographical Analysis

Investigated the geographical distribution of recorded accidents.

- State-wise accident distribution.
- Identification of the highest-volume states.
- City-wise accident comparisons.
- Geographical accident hotspots.
- State-level severity comparisons.
- Humidity and visibility patterns across states.

### 3. Weather & Environmental Analysis

Explored how environmental conditions are represented in accident records.

- Weather-condition distribution.
- Temperature and humidity patterns.
- Visibility conditions.
- Wind-speed categories.
- Precipitation levels.
- Severity distribution across environmental categories.

### 4. Road Infrastructure Analysis

Investigated accident records associated with different road infrastructure features.

- Junctions.
- Traffic signals.
- Crossings.
- Railway locations.
- Stops.
- Give-way signs.
- Roundabouts.
- Traffic calming features and road bumps.

Compared accident frequency and severity distributions between records with and without these infrastructure flags.

### 5. Severity Analysis

Investigated how traffic-impact severity varies across different dimensions.

- Severity distribution across years.
- State-wise severity comparisons.
- Hourly severity patterns.
- Weather-related severity distribution.
- Visibility-related severity distribution.
- Daytime versus nighttime severity.
- Overall severity patterns.

## 💡 Key Findings & Insights

### 1. Temporal Patterns
- Recorded accidents increased from 2016 to 2022.
- The first quarter of 2023 recorded more than **80,000 accidents per month** on average.
- Approximately **84.1%** of recorded accidents occurred on weekdays.
- Accident frequency peaked at **7 AM (587,472)**, followed by **4 PM (581,969)** and **8 AM (577,576)**.
- Wednesday, Thursday, and Friday recorded the highest accident counts.

### 2. Geographical Patterns
- California recorded more than **1.7 million accidents**, followed by Florida with approximately **880,000** and Texas with approximately **580,000**.
- Miami recorded approximately **190,000 accidents**.
- High accident volumes did not necessarily correspond to higher proportions of Level 4 accidents.
- California, Florida, and Texas recorded Level 4 shares of **0.78%, 1.49%, and 1.24%**, respectively.

### 3. Weather & Environmental Patterns
- Most recorded accidents occurred under Fair or cloudy weather conditions.
- Approximately **89.7%** of accidents occurred under Good visibility.
- Approximately **93%** occurred under Calm or Light wind conditions.
- Approximately **98.6%** occurred under No Rain or Very Light precipitation.
- Rain-related weather conditions showed higher Level 3 proportions than Fair weather.

### 4. Road Infrastructure Patterns
- Traffic signals, crossings, and junctions were among the most frequently recorded infrastructure features.
- Junction-related accidents showed a higher combined Level 3 and Level 4 share (**26.79%**) compared with accidents without a junction flag (**18.88%**).
- Accidents associated with signals, crossings, stops, and railways generally showed lower traffic-impact severity distributions.

### 5. Severity Patterns
- Level 2 dominated the dataset, accounting for approximately **79.7%** of all records.
- Level 3 accounted for **16.8%**, Level 4 for **2.6%**, and Level 1 for **0.9%**.
- Level 4 proportions were higher during late-night and early-morning hours.
- Nighttime accidents recorded a higher Level 4 share (**3.50%**) than daytime accidents (**2.24%**).
- Rain-related conditions showed higher Level 3 proportions compared with Fair weather.

## ⚠️ Data Limitations

Several limitations should be considered when interpreting the results:

1. **Incomplete 2023 Data:** The dataset contains records only through March 2023, making direct annual comparisons inappropriate.

2. **Severity Recording Changes:** The distribution of severity changes substantially across years. The sharp decline in Level 3 records may reflect changes in data collection or recording practices rather than actual improvements in road safety.

3. **Missing Numerical Values:** Several numerical columns contain missing values. These were not artificially filled, particularly where imputation could distort environmental distributions.

4. **Extreme Values:** Some accident-duration observations are unusually high and can substantially influence average-duration calculations.

5. **Small Sample Categories:** Rare infrastructure features and environmental categories may produce unstable percentage distributions.

6. **No Exposure Data:** The dataset does not provide traffic volume, vehicle miles traveled, population exposure, or road-length denominators. Therefore, accident counts cannot directly establish accident risk.

7. **Correlation vs. Causation:** The findings describe associations and patterns in recorded accident data. They do not establish causal relationships.

## 🚀 Possible Future Improvements

- Normalize accident counts using traffic volume or population data.
- Investigate junction-related and nighttime accidents in greater depth.
- Examine weather-severity relationships across individual years.
- Apply statistical tests to evaluate selected relationships.
- Develop an interactive dashboard using Power BI.
- Explore predictive modeling for accident severity as a separate extension.

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Install Dependencies

```bash
pip install pandas numpy matplotlib geopandas pyarrow jupyter
```

### 3. Prepare the Dataset

Download the dataset and place the processed Parquet file in the project directory:

```text
US_Accidents_March23.parquet
```

The notebook currently reads this file directly.

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open `new_analysis.ipynb` and execute the cells sequentially.

## 👨‍💻 Author

**Emon Sen**

Computer Science & Engineering

Interested in Data Analytics, Business Intelligence, and Machine Learning.

---

*This project was developed as part of my data analytics portfolio to strengthen practical skills in Python, data preprocessing, exploratory data analysis, geographical analysis, and data-driven insight generation.*
