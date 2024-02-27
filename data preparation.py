from flask import Flask, render_template_string
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64


app = Flask(__name__)
prepared_data = pd.read_csv('Prepared_data.csv')
print(prepared_data)


# Visualization 1: MMR Vaccination Rates Distribution
plt.figure(figsize=(10, 6))
sns.histplot(prepared_data['mmr'], bins=30, kde=True)
plt.title('Distribution of MMR Vaccination Rates')
plt.xlabel('MMR Vaccination Rate (%)')
plt.ylabel('Frequency')
plt.show()

# Visualization 2: MMR Vaccination Rates by State
plt.figure(figsize=(14, 8))
sns.boxplot(x='state', y='mmr', data=prepared_data)
plt.xticks(rotation=90)
plt.title('MMR Vaccination Rates by State')
plt.xlabel('State')
plt.ylabel('MMR Vaccination Rate (%)')
plt.show()

# Visualization 3: Enrollment Distribution
plt.figure(figsize=(10, 6))
sns.histplot(prepared_data['enroll'], bins=30, kde=True, color='green')
plt.title('Distribution of Enrollment Numbers')
plt.xlabel('Enrollment')
plt.ylabel('Frequency')
plt.xlim(0, 2000)  # Limiting x-axis for better visualization of distribution
plt.show()

# Visualization 4: MMR Vaccination Rates by Institution Type
plt.figure(figsize=(10, 6))
sns.boxplot(x='type', y='mmr', data=prepared_data)
plt.title('MMR Vaccination Rates by Institution Type')
plt.xlabel('Institution Type')
plt.ylabel('MMR Vaccination Rate (%)')
plt.show()

# Visualization 5: Correlation Heatmap of Numerical Features
plt.figure(figsize=(10, 8))
corr_matrix = prepared_data[['enroll', 'mmr', 'overall', 'xmed', 'xper']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Numerical Features')
plt.show()

def fig_to_base64(fig):
    """Convert a matplotlib figure to a base64 encoded string to embed in HTML."""
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
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.boxplot(x='state', y='mmr', data=data, ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    ax.set_title('MMR Vaccination Rates by State')
    ax.set_xlabel('State')
    ax.set_ylabel('MMR Vaccination Rate (%)')
    return fig_to_base64(fig)

# Define other plot functions similarly...

@app.route('/')
def index():
    # Generate base64 encoded images for embedding
    mmr_distribution_img = plot_mmr_distribution(prepared_data)
    mmr_by_state_img = plot_mmr_by_state(prepared_data)
    # Continue for other plots...

    # Render template with embedded plots
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Vaccination Data Visualizations</title>
    </head>
    <body>
        <h1>MMR Vaccination Data Insights</h1>
        <img src="data:image/png;base64,{{ mmr_distribution_img }}" alt="MMR Distribution">
        <img src="data:image/png;base64,{{ mmr_by_state_img }}" alt="MMR by State">
        <!-- Embed other images similarly -->
    </body>
    </html>
    """, mmr_distribution_img=mmr_distribution_img, mmr_by_state_img=mmr_by_state_img)

if __name__ == '__main__':
    app.run(debug=True)