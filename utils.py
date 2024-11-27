"""Utility functions for the IUP Performance Comparison application."""

import numpy as np
from config import ADJUSTMENT_LEVELS, CATEGORY_WEIGHTS

def normalize_value(value, optimal_direction, min_val, max_val):
    """Normalize a value between 0 and 1."""
    if min_val == max_val:
        return 1.0
    
    if optimal_direction == 'higher':
        return (value - min_val) / (max_val - min_val)
    else:
        return (max_val - value) / (max_val - min_val)

def calculate_parameter_score(value, adjustment, param_config, min_val, max_val):
    """Calculate score for a single parameter."""
    normalized = normalize_value(value, param_config['optimal_direction'], min_val, max_val)
    adjustment_multiplier = ADJUSTMENT_LEVELS[adjustment]
    return normalized * adjustment_multiplier * param_config['weight']

def get_min_max_values(all_data, param_key):
    """Get minimum and maximum values for a parameter across all IUPs."""
    values = []
    for iup_data in all_data.values():
        if param_key in iup_data:
            values.append(iup_data[param_key]['value'])
    
    if not values:
        return 0, 1  # Default values if no data
    
    min_val = min(values)
    max_val = max(values)
    
    # If min equals max, add a small buffer
    if min_val == max_val:
        if min_val == 0:
            max_val = 1
        else:
            min_val = max(0, min_val * 0.9)
            max_val = max_val * 1.1
    
    return min_val, max_val

def calculate_category_score(category_data, category_params, all_data):
    """Calculate score for a category."""
    total_score = 0
    total_weight = 0
    
    for subcategory, params in category_params.items():
        for param_key, param_config in params.items():
            if param_key in category_data:
                value = category_data[param_key]['value']
                adjustment = category_data[param_key]['adjustment']
                
                min_val, max_val = get_min_max_values(all_data, param_key)
                
                score = calculate_parameter_score(value, adjustment, param_config, min_val, max_val)
                total_score += score
                total_weight += param_config['weight']
    
    return total_score / total_weight if total_weight > 0 else 0

def calculate_final_score(scores):
    """Calculate final weighted score across all categories."""
    final_score = 0
    for category, score in scores.items():
        final_score += score * CATEGORY_WEIGHTS[category]
    return final_score

def format_number(value, unit):
    """Format number with appropriate precision based on unit."""
    if unit == '%':
        return f"{value:.1f}%"
    elif 'USD' in unit:
        return f"${value:.2f}"
    else:
        return f"{value:.2f}"

def get_comparison_color(value, benchmark, optimal_direction):
    """Get color for comparison based on value relative to benchmark."""
    if optimal_direction == 'higher':
        return 'green' if value > benchmark else 'red'
    else:
        return 'green' if value < benchmark else 'red'
