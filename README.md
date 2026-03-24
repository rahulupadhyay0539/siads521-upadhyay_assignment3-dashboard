# Assignment 3  Interactive Data Dashboard

This project presents an interactive dashboard built using Panel to explore vehicle fuel efficiency data.

## Features
- Histogram for distribution analysis
- Scatter plot for relationship exploration
- Box plot for category comparison
- Line plot for trend over time
- Interactive widgets for dynamic filtering

## Key Insights
- Fuel efficiency decreases as vehicle weight increases
- Japanese vehicles tend to have higher MPG
- Most vehicles fall within 15-30 MPG range
- MPG improves over model years

## Setup
Pip install panel hvplot seaborn pandas

## How to depoly dashboard locally, App hosted locally: http://localhost:5006/assignment3_dashboard

pip install -r requirements.txt
python -m panel serve assignment3_dashboard.py
