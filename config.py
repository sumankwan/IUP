"""Configuration settings and constants for the IUP Performance Comparison application."""

# IUP List
IUP_LIST = ['BPM', 'BSJ', 'JAS', 'KFM']

# Bahasa Indonesia Labels
LABELS = {
    'title': 'Perbandingan Kinerja IUP',
    'settings': 'Pengaturan',
    'select_iups': 'Pilih IUP untuk Dibandingkan',
    'tabs': {
        'input': 'Input Parameter',
        'analysis': 'Analisis Kinerja',
        'comparison': 'Perbandingan Detail',
        'trends': 'Tren Historis'
    },
    'categories': {
        'OPERATIONAL': 'Parameter Operasional',
        'COST': 'Parameter Biaya',
        'QUALITY': 'Parameter Kualitas',
        'FINANCIAL': 'Parameter Keuangan'
    },
    'subcategories': {
        'Mining Metrics': 'Metrik Penambangan',
        'Equipment & Infrastructure': 'Peralatan & Infrastruktur',
        'Direct Mining Costs': 'Biaya Penambangan Langsung',
        'Equipment Costs': 'Biaya Peralatan',
        'Ore Grade Parameters': 'Parameter Kadar Bijih',
        'Revenue Metrics': 'Metrik Pendapatan',
        'Financial Health': 'Kesehatan Keuangan'
    },
    'adjustments': {
        'title': 'Tingkat Kesulitan',
        'SULIT': 'Sulit (1.2x)',
        'NORMAL': 'Normal (1.0x)',
        'MUDAH': 'Mudah (0.8x)',
        'SANGAT_MUDAH': 'Sangat Mudah (0.6x)'
    },
    'analysis': {
        'final_scores': 'Skor Akhir',
        'comparison': 'Perbandingan',
        'best_performer': 'Kinerja Terbaik'
    }
}

# Adjustment Levels
ADJUSTMENT_LEVELS = {
    'SULIT': 1.2,        # Difficult conditions
    'NORMAL': 1.0,       # Normal conditions
    'MUDAH': 0.8,        # Easy conditions
    'SANGAT_MUDAH': 0.6  # Very easy conditions
}

# Adjustment Descriptions
ADJUSTMENT_DESCRIPTIONS = {
    'SULIT': {
        'OPERATIONAL': 'Kondisi penambangan menantang (strip ratio tinggi, geologi kompleks, medan sulit)',
        'COST': 'Lingkungan biaya tinggi, supplier terbatas, lokasi terpencil',
        'QUALITY': 'Karakteristik bijih menantang, kebutuhan pengolahan kompleks',
        'FINANCIAL': 'Kondisi pasar menantang, kendala keuangan tinggi'
    },
    'NORMAL': {
        'OPERATIONAL': 'Kondisi penambangan standar dengan tantangan umum',
        'COST': 'Lingkungan biaya rata-rata dengan kondisi pasar standar',
        'QUALITY': 'Karakteristik bijih standar',
        'FINANCIAL': 'Kondisi pasar dan lingkungan keuangan normal'
    },
    'MUDAH': {
        'OPERATIONAL': 'Kondisi penambangan menguntungkan, geologi sederhana',
        'COST': 'Lingkungan biaya menguntungkan, banyak supplier',
        'QUALITY': 'Karakteristik bijih baik',
        'FINANCIAL': 'Kondisi pasar dan lingkungan keuangan menguntungkan'
    },
    'SANGAT_MUDAH': {
        'OPERATIONAL': 'Kondisi penambangan optimal, operasi sederhana',
        'COST': 'Lingkungan biaya sangat menguntungkan',
        'QUALITY': 'Karakteristik bijih sangat baik',
        'FINANCIAL': 'Kondisi pasar dan lingkungan keuangan sangat menguntungkan'
    }
}

# Category Weights
CATEGORY_WEIGHTS = {
    'OPERATIONAL': 0.35,
    'COST': 0.30,
    'QUALITY': 0.20,
    'FINANCIAL': 0.15
}

# Theme Configuration
THEME = {
    'primary_color': '#1f77b4',
    'background_color': '#0e1117',
    'secondary_background': '#262730',
    'text_color': '#fafafa',
    'font': 'sans-serif'
}

# Chart Configuration
CHART_CONFIG = {
    'template': 'plotly_dark',
    'height': 600,
    'width': 1000
}
