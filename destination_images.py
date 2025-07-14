"""
Destination image generation and management for the AI Travel Planner
Uses AI to generate beautiful SVG images for destinations
"""

import json
import base64

# Destination image mappings and descriptions
DESTINATION_IMAGES = {
    # United States
    "New York": {
        "description": "Iconic NYC skyline with Empire State Building, Times Square neon lights, and Central Park",
        "colors": ["#1E3A8A", "#FBBF24", "#EF4444"],
        "style": "modern urban cityscape"
    },
    "Los Angeles": {
        "description": "Hollywood sign, palm trees, Beverly Hills, and sunset over the Pacific Ocean",
        "colors": ["#F59E0B", "#EC4899", "#8B5CF6"],
        "style": "vibrant coastal city"
    },
    "San Francisco": {
        "description": "Golden Gate Bridge, steep hills, Victorian houses, and fog rolling over the bay",
        "colors": ["#EF4444", "#F59E0B", "#6B7280"],
        "style": "hilly coastal city"
    },
    
    # United Kingdom
    "London": {
        "description": "Big Ben, red double-decker buses, Thames River, and traditional British architecture",
        "colors": ["#DC2626", "#1F2937", "#F59E0B"],
        "style": "historic European capital"
    },
    "Edinburgh": {
        "description": "Edinburgh Castle on volcanic rock, Royal Mile, and Scottish highlands in background",
        "colors": ["#6B7280", "#059669", "#7C3AED"],
        "style": "medieval Scottish city"
    },
    
    # France
    "Paris": {
        "description": "Eiffel Tower, Seine River, Haussmanian architecture, and romantic evening lighting",
        "colors": ["#374151", "#F59E0B", "#EC4899"],
        "style": "romantic European capital"
    },
    "Nice": {
        "description": "French Riviera coastline, azure Mediterranean Sea, and colorful buildings",
        "colors": ["#3B82F6", "#F59E0B", "#EC4899"],
        "style": "Mediterranean coastal city"
    },
    
    # Japan
    "Tokyo": {
        "description": "Mount Fuji, cherry blossoms, modern skyscrapers, and traditional temples",
        "colors": ["#EC4899", "#6B7280", "#EF4444"],
        "style": "futuristic Asian metropolis"
    },
    "Kyoto": {
        "description": "Traditional temples, bamboo forests, geishas, and peaceful zen gardens",
        "colors": ["#059669", "#F59E0B", "#7C3AED"],
        "style": "traditional Japanese city"
    },
    
    # Thailand
    "Bangkok": {
        "description": "Golden Buddhist temples, floating markets, tuk-tuks, and tropical vegetation",
        "colors": ["#F59E0B", "#DC2626", "#059669"],
        "style": "vibrant Southeast Asian city"
    },
    "Chiang Mai": {
        "description": "Mountain temples, elephant sanctuaries, night markets, and lush tropical landscapes",
        "colors": ["#059669", "#F59E0B", "#7C3AED"],
        "style": "tropical mountain city"
    },
    
    # India
    "Delhi": {
        "description": "Red Fort, India Gate, bustling markets, and mix of modern and Mughal architecture",
        "colors": ["#EF4444", "#F59E0B", "#7C3AED"],
        "style": "historic Indian capital"
    },
    "Mumbai": {
        "description": "Gateway of India, Bollywood glamour, marine drive, and colonial architecture",
        "colors": ["#3B82F6", "#F59E0B", "#EC4899"],
        "style": "coastal Indian metropolis"
    },
    "Jaipur": {
        "description": "Pink City palaces, Amber Fort, camels, and Rajasthani desert architecture",
        "colors": ["#EC4899", "#F59E0B", "#EF4444"],
        "style": "desert palace city"
    },
    
    # Australia
    "Sydney": {
        "description": "Opera House, Harbour Bridge, beautiful beaches, and modern skyline",
        "colors": ["#3B82F6", "#F59E0B", "#6B7280"],
        "style": "modern harbor city"
    },
    "Melbourne": {
        "description": "Street art, coffee culture, Victorian architecture, and cultural diversity",
        "colors": ["#7C3AED", "#F59E0B", "#059669"],
        "style": "cultural Australian city"
    },
    
    # Brazil
    "Rio de Janeiro": {
        "description": "Christ the Redeemer, Sugarloaf Mountain, Copacabana Beach, and carnival colors",
        "colors": ["#059669", "#F59E0B", "#3B82F6"],
        "style": "tropical Brazilian city"
    },
    "São Paulo": {
        "description": "Modern skyscrapers, street art, diverse neighborhoods, and urban energy",
        "colors": ["#6B7280", "#EC4899", "#F59E0B"],
        "style": "urban Brazilian metropolis"
    }
}

def generate_destination_svg(destination_name: str) -> str:
    """Generate an SVG image for a destination"""
    if destination_name not in DESTINATION_IMAGES:
        # Default generic destination image
        return generate_generic_destination_svg(destination_name)
    
    image_data = DESTINATION_IMAGES[destination_name]
    
    # Create SVG with destination-specific elements
    svg_content = f"""<svg viewBox="0 0 400 250" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="skyGradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#87CEEB;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#E0F6FF;stop-opacity:1" />
        </linearGradient>
        <linearGradient id="buildingGradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:{image_data['colors'][0]};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{image_data['colors'][1]};stop-opacity:0.8" />
        </linearGradient>
    </defs>
    
    <!-- Sky background -->
    <rect width="400" height="250" fill="url(#skyGradient)"/>
    
    <!-- Buildings silhouette -->
    <rect x="50" y="150" width="40" height="80" fill="url(#buildingGradient)" rx="2"/>
    <rect x="100" y="120" width="35" height="110" fill="url(#buildingGradient)" rx="2"/>
    <rect x="145" y="140" width="30" height="90" fill="url(#buildingGradient)" rx="2"/>
    <rect x="185" y="100" width="45" height="130" fill="url(#buildingGradient)" rx="2"/>
    <rect x="240" y="130" width="38" height="100" fill="url(#buildingGradient)" rx="2"/>
    <rect x="290" y="110" width="42" height="120" fill="url(#buildingGradient)" rx="2"/>
    
    <!-- Destination name -->
    <text x="200" y="40" text-anchor="middle" font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="#1F2937">{destination_name}</text>
    
    <!-- Decorative elements -->
    <circle cx="350" cy="60" r="25" fill="#FBBF24" opacity="0.8"/>
    <path d="M 20 220 Q 200 200 380 220" stroke="{image_data['colors'][2]}" stroke-width="3" fill="none"/>
    
    <!-- Icons or landmarks -->
    <rect x="170" y="80" width="60" height="40" fill="{image_data['colors'][0]}" rx="5" opacity="0.7"/>
    <polygon points="200,60 180,80 220,80" fill="{image_data['colors'][1]}"/>
</svg>"""
    
    return svg_content

def generate_generic_destination_svg(destination_name: str) -> str:
    """Generate a generic destination SVG"""
    return f"""<svg viewBox="0 0 400 250" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="skyGradient" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" style="stop-color:#87CEEB;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#E0F6FF;stop-opacity:1" />
        </linearGradient>
    </defs>
    
    <!-- Sky background -->
    <rect width="400" height="250" fill="url(#skyGradient)"/>
    
    <!-- Generic landscape -->
    <path d="M 0 200 Q 100 180 200 190 Q 300 200 400 185 L 400 250 L 0 250 Z" fill="#059669"/>
    <path d="M 0 220 Q 150 200 400 210 L 400 250 L 0 250 Z" fill="#16A34A"/>
    
    <!-- Mountains -->
    <polygon points="0,200 100,120 200,200" fill="#6B7280" opacity="0.7"/>
    <polygon points="150,200 250,100 350,200" fill="#4B5563" opacity="0.7"/>
    <polygon points="300,200 400,140 400,200" fill="#6B7280" opacity="0.7"/>
    
    <!-- Sun -->
    <circle cx="350" cy="60" r="25" fill="#FBBF24"/>
    
    <!-- Destination name -->
    <text x="200" y="40" text-anchor="middle" font-family="Arial, sans-serif" font-size="24" font-weight="bold" fill="#1F2937">{destination_name}</text>
    
    <!-- Travel icon -->
    <path d="M 180 80 L 220 80 L 210 100 L 190 100 Z" fill="#EF4444"/>
    <circle cx="200" cy="90" r="8" fill="#FFF"/>
</svg>"""

def get_destination_image_url(destination_name: str) -> str:
    """Get the image URL for a destination (returns SVG data URL)"""
    svg_content = generate_destination_svg(destination_name)
    # Convert SVG to data URL
    svg_bytes = svg_content.encode('utf-8')
    svg_b64 = base64.b64encode(svg_bytes).decode('utf-8')
    return f"data:image/svg+xml;base64,{svg_b64}"

def get_destination_colors(destination_name: str) -> list:
    """Get the color palette for a destination"""
    if destination_name in DESTINATION_IMAGES:
        return DESTINATION_IMAGES[destination_name]['colors']
    return ["#3B82F6", "#F59E0B", "#EF4444"]  # Default colors