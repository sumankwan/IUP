"""Visualization functions for the IUP Performance Comparison application."""

import plotly.graph_objects as go
import plotly.express as px
from config import CHART_CONFIG, IUP_LIST

def create_radar_chart(category_scores, category):
    """Create radar chart for category comparison across IUPs."""
    fig = go.Figure()
    
    for iup in IUP_LIST:
        if iup in category_scores:
            scores = category_scores[iup]
            if category in scores:  # Add check for category
                fig.add_trace(go.Scatterpolar(
                    r=[scores[category]],  # Single score for the category
                    theta=[category],
                    name=iup,
                    fill='toself'
                ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )
        ),
        showlegend=True,
        title=f"{category} Performance Comparison",
        **CHART_CONFIG
    )
    
    return fig

def create_bar_chart(parameter_values, parameter_name, unit):
    """Create bar chart for parameter comparison across IUPs."""
    fig = go.Figure()
    
    iups = []
    values = []
    colors = []
    
    for iup, data in parameter_values.items():
        if 'value' in data:  # Add check for value key
            iups.append(iup)
            values.append(data['value'])
            colors.append('rgba(31, 119, 180, 0.8)')  # Default blue color
    
    if values:  # Only create chart if there are values
        fig.add_trace(go.Bar(
            x=iups,
            y=values,
            marker_color=colors,
            text=[f"{v:.2f} {unit}" for v in values],
            textposition='auto',
        ))
        
        fig.update_layout(
            title=f"{parameter_name} Comparison",
            xaxis_title="IUP",
            yaxis_title=unit,
            **CHART_CONFIG
        )
    
    return fig

def create_trend_chart(historical_data, parameter_name, unit):
    """Create line chart for historical trend analysis."""
    fig = go.Figure()
    
    for iup in IUP_LIST:
        if iup in historical_data:
            data = historical_data[iup]
            fig.add_trace(go.Scatter(
                x=list(data.keys()),
                y=list(data.values()),
                mode='lines+markers',
                name=iup
            ))
    
    fig.update_layout(
        title=f"{parameter_name} Historical Trend",
        xaxis_title="Date",
        yaxis_title=unit,
        **CHART_CONFIG
    )
    
    return fig

def create_comparison_table(data, category):
    """Create comparison table for parameters within a category."""
    headers = ['Parameter', 'Unit'] + IUP_LIST + ['Best Performer']
    rows = []
    
    for param_key, param_data in data.items():
        row = [
            param_data['name'],
            param_data['unit']
        ]
        
        values = {}
        for iup in IUP_LIST:
            if iup in param_data['values'] and 'value' in param_data['values'][iup]:
                value = param_data['values'][iup]['value']
                values[iup] = value
                row.append(f"{value:.2f}")
            else:
                row.append("-")
        
        # Determine best performer
        if values:
            best_iup = max(values.items(), key=lambda x: x[1])[0]
            row.append(best_iup)
        else:
            row.append("-")
        
        rows.append(row)
    
    return headers, rows
