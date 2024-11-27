"""Parameter definitions for the IUP Performance Comparison application."""

PARAMETERS = {
    'OPERATIONAL': {
        'Mining Metrics': {
            'stripping_ratio': {
                'name': 'Stripping Ratio',
                'unit': 'BCM:Ton',
                'weight': 9,
                'tooltip': 'Volume of overburden removed per ton of ore',
                'optimal_direction': 'lower'
            },
            'mining_recovery': {
                'name': 'Mining Recovery',
                'unit': '%',
                'weight': 8,
                'tooltip': 'Percentage of ore recovered during mining operations',
                'optimal_direction': 'higher'
            },
            'mining_sequence_adherence': {
                'name': 'Mining Sequence Adherence',
                'unit': '%',
                'weight': 7,
                'tooltip': 'Compliance with planned mining sequence',
                'optimal_direction': 'higher'
            },
            'pit_optimization_score': {
                'name': 'Pit Optimization Score',
                'unit': '%',
                'weight': 8,
                'tooltip': 'Measure of pit design efficiency',
                'optimal_direction': 'higher'
            },
            'hauling_distance': {
                'name': 'Hauling Distance',
                'unit': 'km',
                'weight': 7,
                'tooltip': 'Average hauling distance from pit to stockpile/port',
                'optimal_direction': 'lower'
            },
            'production_target_achievement': {
                'name': 'Production Target Achievement',
                'unit': '%',
                'weight': 9,
                'tooltip': 'Achievement of monthly production targets',
                'optimal_direction': 'higher'
            }
        },
        'Equipment & Infrastructure': {
            'equipment_availability': {
                'name': 'Equipment Availability',
                'unit': '%',
                'weight': 9,
                'tooltip': 'Percentage of time equipment is available for use',
                'optimal_direction': 'higher'
            },
            'equipment_utilization': {
                'name': 'Equipment Utilization',
                'unit': '%',
                'weight': 8,
                'tooltip': 'Percentage of available time equipment is actually used',
                'optimal_direction': 'higher'
            },
            'maintenance_compliance': {
                'name': 'Maintenance Compliance',
                'unit': '%',
                'weight': 7,
                'tooltip': 'Adherence to maintenance schedules',
                'optimal_direction': 'higher'
            }
        }
    },
    'COST': {
        'Direct Mining Costs': {
            'mining_cost': {
                'name': 'Mining Cost',
                'unit': 'USD/WMT',
                'weight': 10,
                'tooltip': 'Total direct mining cost per wet metric ton',
                'optimal_direction': 'lower'
            },
            'drilling_cost': {
                'name': 'Drilling Cost',
                'unit': 'USD/WMT',
                'weight': 7,
                'tooltip': 'Drilling cost per wet metric ton',
                'optimal_direction': 'lower'
            },
            'blasting_cost': {
                'name': 'Blasting Cost',
                'unit': 'USD/WMT',
                'weight': 7,
                'tooltip': 'Blasting cost per wet metric ton',
                'optimal_direction': 'lower'
            },
            'loading_cost': {
                'name': 'Loading Cost',
                'unit': 'USD/WMT',
                'weight': 8,
                'tooltip': 'Loading cost per wet metric ton',
                'optimal_direction': 'lower'
            },
            'hauling_cost': {
                'name': 'Hauling Cost',
                'unit': 'USD/WMT',
                'weight': 8,
                'tooltip': 'Hauling cost per wet metric ton',
                'optimal_direction': 'lower'
            }
        },
        'Equipment Costs': {
            'equipment_rental': {
                'name': 'Equipment Rental',
                'unit': 'USD/hour',
                'weight': 8,
                'tooltip': 'Average equipment rental cost per hour',
                'optimal_direction': 'lower'
            },
            'maintenance_cost': {
                'name': 'Maintenance Cost',
                'unit': 'USD/WMT',
                'weight': 8,
                'tooltip': 'Equipment maintenance cost per wet metric ton',
                'optimal_direction': 'lower'
            },
            'fuel_cost': {
                'name': 'Fuel Cost',
                'unit': 'USD/WMT',
                'weight': 8,
                'tooltip': 'Fuel cost per wet metric ton',
                'optimal_direction': 'lower'
            },
            'spare_parts_cost': {
                'name': 'Spare Parts Cost',
                'unit': 'USD/WMT',
                'weight': 7,
                'tooltip': 'Spare parts cost per wet metric ton',
                'optimal_direction': 'lower'
            }
        },
        'Administrative Costs': {
            'office_cost': {
                'name': 'Office Cost',
                'unit': 'USD/month',
                'weight': 6,
                'tooltip': 'Monthly office operational costs',
                'optimal_direction': 'lower'
            },
            'travel_cost': {
                'name': 'Travel Cost',
                'unit': 'USD/month',
                'weight': 6,
                'tooltip': 'Monthly travel and accommodation costs',
                'optimal_direction': 'lower'
            },
            'communication_cost': {
                'name': 'Communication Cost',
                'unit': 'USD/month',
                'weight': 5,
                'tooltip': 'Monthly communication and IT costs',
                'optimal_direction': 'lower'
            },
            'utilities_cost': {
                'name': 'Utilities Cost',
                'unit': 'USD/month',
                'weight': 5,
                'tooltip': 'Monthly utilities costs (electricity, water, etc.)',
                'optimal_direction': 'lower'
            }
        },
        'Personnel Costs': {
            'staff_salary': {
                'name': 'Staff Salary',
                'unit': 'USD/month',
                'weight': 7,
                'tooltip': 'Monthly staff salary costs',
                'optimal_direction': 'lower'
            },
            'employee_benefits': {
                'name': 'Employee Benefits',
                'unit': 'USD/month',
                'weight': 6,
                'tooltip': 'Monthly employee benefits costs',
                'optimal_direction': 'lower'
            },
            'training_cost': {
                'name': 'Training Cost',
                'unit': 'USD/month',
                'weight': 5,
                'tooltip': 'Monthly training and development costs',
                'optimal_direction': 'lower'
            }
        }
    },
    'QUALITY': {
        'Ore Grade Parameters': {
            'ni_content': {
                'name': 'Nickel Content',
                'unit': '%',
                'weight': 10,
                'tooltip': 'Average nickel content in ore',
                'optimal_direction': 'higher'
            },
            'moisture_content': {
                'name': 'Moisture Content',
                'unit': '%',
                'weight': 8,
                'tooltip': 'Moisture content in ore',
                'optimal_direction': 'lower'
            }
        }
    },
    'FINANCIAL': {
        'Revenue Metrics': {
            'revenue_per_wmt': {
                'name': 'Revenue per WMT',
                'unit': 'USD/WMT',
                'weight': 10,
                'tooltip': 'Revenue generated per wet metric ton',
                'optimal_direction': 'higher'
            },
            'price_realization': {
                'name': 'Price Realization',
                'unit': '%',
                'weight': 9,
                'tooltip': 'Actual price achieved vs benchmark price',
                'optimal_direction': 'higher'
            }
        },
        'Financial Health': {
            'operating_margin': {
                'name': 'Operating Margin',
                'unit': '%',
                'weight': 9,
                'tooltip': 'Operating profit as percentage of revenue',
                'optimal_direction': 'higher'
            },
            'ebitda_margin': {
                'name': 'EBITDA Margin',
                'unit': '%',
                'weight': 9,
                'tooltip': 'EBITDA as percentage of revenue',
                'optimal_direction': 'higher'
            }
        }
    }
}
