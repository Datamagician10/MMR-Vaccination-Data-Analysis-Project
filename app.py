from flask import Flask, render_template_string
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

app = Flask(__name__)
prepared_data = pd.read_csv('Prepared_data.csv')
print(prepared_data)

def fig_to_base64(fig):
    img_buf = BytesIO()
    fig.savefig(img_buf, format='png', bbox_inches='tight')
    img_buf.seek(0)
    return base64.b64encode(img_buf.getvalue()).decode('utf-8')

def plot_mmr_distribution(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data['mmr'], bins=30, kde=True, ax=ax)
    ax.set_title('Distribution of MMR Vaccination Rates')
    ax.set_xlabel('MMR Vaccination Rate (%)')
    ax.set_ylabel('Frequency')
    return fig_to_base64(fig)

def plot_mmr_by_state(data):
    plt.figure(figsize=(16, 10))  # Adjusting figure size
    ax = sns.boxplot(x='state', y='mmr', data=data)
    ax.set_title('MMR Vaccination Rates by State')
    ax.set_xlabel('State')
    ax.set_ylabel('MMR Vaccination Rate (%)')
    plt.xticks(rotation=90)  # Rotating x-tick labels for better visibility
    plt.tight_layout()  # Adjust layout
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    plt.close()
    img_buf.seek(0)
    return base64.b64encode(img_buf.getvalue()).decode('utf-8')


def plot_enrollment_distribution(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data['enroll'], bins=30, kde=True, color='green', ax=ax)
    ax.set_title('Distribution of Enrollment Numbers')
    ax.set_xlabel('Enrollment')
    ax.set_ylabel('Frequency')
    ax.set_xlim(0, 2000)
    return fig_to_base64(fig)

def plot_mmr_by_type(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='type', y='mmr', data=data, ax=ax)
    ax.set_title('MMR Vaccination Rates by Institution Type')
    ax.set_xlabel('Institution Type')
    ax.set_ylabel('MMR Vaccination Rate (%)')
    return fig_to_base64(fig)

def plot_correlation_heatmap(data):
    fig, ax = plt.subplots(figsize=(10, 8))
    corr_matrix = data[['enroll', 'mmr', 'overall', 'xmed', 'xper']].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Heatmap of Numerical Features')
    return fig_to_base64(fig)


@app.route('/')
def index():
    mmr_distribution_img = plot_mmr_distribution(prepared_data)
    mmr_by_state_img = plot_mmr_by_state(prepared_data)
    enrollment_distribution_img = plot_enrollment_distribution(prepared_data)
    mmr_by_type_img = plot_mmr_by_type(prepared_data)
    correlation_heatmap_img = plot_correlation_heatmap(prepared_data)

    # Add your insights for each visualization here
    insights = {
        "mmr_distribution": "This shows the distribution of MMR vaccination rates across various regions.",
        "mmr_by_state": "This boxplot reveals the variability in vaccination rates between states.",
        "enrollment_distribution": "Enrollment numbers vary widely, which could affect herd immunity.",
        "mmr_by_type": "Different institution types show varied MMR vaccination rates.",
        "correlation_heatmap": "There's a notable correlation between enrollment numbers and vaccination rates."
    }

    # Details of the dataset to be shown in the tab
    dataset_details = """
    This data set contains measles vaccination rate data for 46,412 schools in 32 states across the US.
    
    Data: 

    Vaccination rates are for the 2017-2018 school year for the following states:
    Colorado, Connecticut, Minnesota, Montana, New Jersey, New York, North Dakota, Pennsylvania, South Dakota, Utah, Washington.
    Rates for other states are for the time period 2018-2019.
 
    The data was compiled by The Wall Street Journal.
    """


    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Vaccination Data Visualizations</title>
        <style>
            body { font-family: Arial, sans-serif; display: flex; }
            .content { flex-grow: 1; padding-right: 20px; }
            .sidebar { width: 300px; position: fixed; right: 0; top: 0; bottom: 0; overflow: auto; background-color: #f0f0f0; padding: 20px; }
            .sidebar h2 { text-align: center; }
            img { max-width: 100%; height: auto; }
        </style>
    </head>
    <body>
        <div class="content">
            <h1>MMR Vaccination Data Insights</h1>
            
            <h2>Distribution of MMR Vaccination Rates</h2>
            <img src="data:image/png;base64,{{ mmr_distribution_img }}" alt="MMR Distribution">
            <p>{{ insights['mmr_distribution'] }}</p>
            
            <h2>MMR Vaccination Rates by State</h2>
            <img src="data:image/png;base64,{{ mmr_by_state_img }}" alt="MMR by State">
            <p>{{ insights['mmr_by_state'] }}</p>
            
            <h2>Distribution of Enrollment Numbers</h2>
            <img src="data:image/png;base64,{{ enrollment_distribution_img }}" alt="Enrollment Distribution">
            <p>{{ insights['enrollment_distribution'] }}</p>
            
            <h2>MMR Vaccination Rates by Institution Type</h2>
            <img src="data:image/png;base64,{{ mmr_by_type_img }}" alt="MMR by Institution Type">
            <p>{{ insights['mmr_by_type'] }}</p>
            
            <h2>Correlation Heatmap of Numerical Features</h2>
            <img src="data:image/png;base64,{{ correlation_heatmap_img }}" alt="Correlation Heatmap">
            <p>{{ insights['correlation_heatmap'] }}</p>
        </div>
        <div class="sidebar">
            <h2>Dataset Details</h2>
            <p>{{ dataset_details }}</p>
        </div>
        
        <script>
            // Add any JavaScript here for interactive elements if needed
        </script>
    </body>
    </html>
    """, mmr_distribution_img=mmr_distribution_img, 
         mmr_by_state_img=mmr_by_state_img, 
         enrollment_distribution_img=enrollment_distribution_img, 
         mmr_by_type_img=mmr_by_type_img, 
         correlation_heatmap_img=correlation_heatmap_img,
         insights=insights,
         dataset_details=dataset_details)

if __name__ == '__main__':
    app.run(debug=True)

