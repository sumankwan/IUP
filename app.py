"""Main Streamlit application for IUP Performance Comparison."""

import streamlit as st
import pandas as pd
from datetime import datetime
import json

from config import (
    IUP_LIST, ADJUSTMENT_LEVELS, ADJUSTMENT_DESCRIPTIONS,
    THEME, LABELS
)
from parameters import PARAMETERS
from utils import calculate_category_score, calculate_final_score, format_number
from visualization import (
    create_radar_chart,
    create_bar_chart,
    create_comparison_table
)

# Page configuration
st.set_page_config(
    page_title=LABELS['title'],
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom theme
st.markdown(f"""
    <style>
        .stApp {{
            background-color: {THEME['background_color']};
            color: {THEME['text_color']};
        }}
        .stSidebar {{
            background-color: {THEME['secondary_background']};
        }}
    </style>
""", unsafe_allow_html=True)

def main():
    st.title(f"⛏️ {LABELS['title']}")
    
    # Sidebar
    st.sidebar.header(LABELS['settings'])
    selected_iups = st.sidebar.multiselect(
        LABELS['select_iups'],
        IUP_LIST,
        default=IUP_LIST[:2]
    )
    
    # Main content
    if not selected_iups:
        st.warning("Silakan pilih minimal satu IUP untuk dianalisis.")
        return
    
    # Initialize session state for storing data
    if 'data' not in st.session_state:
        st.session_state.data = {iup: {} for iup in IUP_LIST}
    
    # Create tabs for different sections
    tabs = st.tabs([
        LABELS['tabs']['input'],
        LABELS['tabs']['analysis'],
        LABELS['tabs']['comparison']
    ])
    
    # Input Parameters Tab
    with tabs[0]:
        st.header(LABELS['tabs']['input'])
        
        for category, subcategories in PARAMETERS.items():
            st.subheader(LABELS['categories'][category])
            cols = st.columns(len(selected_iups))
            
            for idx, iup in enumerate(selected_iups):
                with cols[idx]:
                    st.markdown(f"### {iup}")
                    
                    for subcategory, params in subcategories.items():
                        st.markdown(f"**{LABELS['subcategories'].get(subcategory, subcategory)}**")
                        
                        for param_key, param_config in params.items():
                            value = st.number_input(
                                f"{param_config['name']} ({param_config['unit']})",
                                key=f"{iup}_{param_key}",
                                help=param_config['tooltip'],
                                value=0.0,
                                step=0.1
                            )
                            
                            adjustment = st.selectbox(
                                f"{LABELS['adjustments']['title']} - {param_config['name']}",
                                list(ADJUSTMENT_LEVELS.keys()),
                                key=f"{iup}_{param_key}_adj",
                                format_func=lambda x: LABELS['adjustments'][x],
                                help=ADJUSTMENT_DESCRIPTIONS[list(ADJUSTMENT_LEVELS.keys())[0]][category]
                            )
                            
                            # Store data
                            if category not in st.session_state.data[iup]:
                                st.session_state.data[iup][category] = {}
                            
                            st.session_state.data[iup][category][param_key] = {
                                'value': value,
                                'adjustment': adjustment
                            }
    
    # Performance Analysis Tab
    with tabs[1]:
        st.header(LABELS['tabs']['analysis'])
        
        # Calculate scores
        scores = {}
        for iup in selected_iups:
            scores[iup] = {}
            for category, subcategories in PARAMETERS.items():
                if category in st.session_state.data[iup]:
                    category_data = st.session_state.data[iup][category]
                    scores[iup][category] = calculate_category_score(
                        category_data,
                        subcategories,
                        st.session_state.data
                    )
        
        # Display radar charts
        for category in PARAMETERS.keys():
            st.subheader(LABELS['categories'][category])
            st.plotly_chart(
                create_radar_chart(scores, category),
                use_container_width=True
            )
        
        # Display final scores
        st.subheader(LABELS['analysis']['final_scores'])
        cols = st.columns(len(selected_iups))
        for idx, iup in enumerate(selected_iups):
            with cols[idx]:
                final_score = calculate_final_score(scores[iup])
                st.metric(
                    iup,
                    f"{final_score:.2f}",
                    delta=None
                )
    
    # Detailed Comparison Tab
    with tabs[2]:
        st.header(LABELS['tabs']['comparison'])
        
        for category, subcategories in PARAMETERS.items():
            st.subheader(LABELS['categories'][category])
            
            # Create comparison tables
            headers, rows = create_comparison_table(
                {
                    param_key: {
                        'name': param_config['name'],
                        'unit': param_config['unit'],
                        'values': {
                            iup: st.session_state.data[iup][category][param_key]
                            for iup in selected_iups
                            if category in st.session_state.data[iup]
                        }
                    }
                    for subcategory, params in subcategories.items()
                    for param_key, param_config in params.items()
                },
                category
            )
            
            df = pd.DataFrame(rows, columns=headers)
            st.dataframe(df, use_container_width=True)

if __name__ == "__main__":
    main()
