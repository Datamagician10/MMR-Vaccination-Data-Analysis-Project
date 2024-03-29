# MMR-Vaccination-Data-Analysis-Project
This project analyzes MMR (Measles, Mumps, Rubella) vaccination rates across various institutions in different states.The goal is to uncover insights that could inform public health strategies and vaccination campaigns. The analysis includes visualizations of vaccination rates by state, institution type, enrollment numbers, and correlations between these factors.
## Dataset
The dataset contains vaccination rate data for 46,412 schools in 32 states across the U.S. for the school years 2017-2018 and 2018-2019. It was compiled by The Wall Street Journal.
Content
Vaccination rates are for the 2017-201818 school year for the following states:

Colorado
Connecticut
Minnesota
Montana
New Jersey
New York
North Dakota
Pennsylvania
South Dakota
Utah
Washington
Rates for other states are for the time period 2018-2019.


## Visualizations
- `plot_mmr_distribution`: Shows the distribution of MMR vaccination rates across regions.
- `plot_mmr_by_state`: Reveals variability in vaccination rates between states.
- `plot_enrollment_distribution`: Illustrates the distribution of enrollment numbers, highlighting how institution size may affect herd immunity.
- `plot_mmr_by_type`: Compares MMR vaccination rates by institution type.
- `plot_correlation_heatmap`: Examines the correlation between enrollment numbers and vaccination rates, among other factors.

## Setup and Installation
To run this project, you'll need to install the following Python libraries:
- Flask
- Pandas
- Matplotlib
- Seaborn

You can install these with pip using the following command:
pip install Flask Pandas Matplotlib Seaborn


Once the dependencies are installed, you can run the Flask app with:
python app.py

## Flask App
![image](https://github.com/vansh007/MMR-Vaccination-Data-Analysis-Project/assets/53010250/dd8890d6-cde5-4648-ae40-c6bad22bfe0d)
![image](https://github.com/vansh007/MMR-Vaccination-Data-Analysis-Project/assets/53010250/f5e3e1ca-3052-41cd-876e-d185dad3ed8a)



## Usage
After running the Flask application, navigate to `localhost:5000` in your web browser to view the visualizations.

## Contributions
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
Not needed its just for research
