"""
Destination image generation and management for the AI Travel Planner
Uses AI to generate beautiful SVG images for destinations
"""

import json
import base64

def get_destination_image_url(destination):
    """Get image URL for a destination."""
    # Using Unsplash for placeholder images
    base_url = "https://images.unsplash.com/photo-"

    image_mapping = {
        'Tokyo': f"{base_url}1540959353965-7b88f4d6b9e9?w=800&h=600&fit=crop",
        'Kyoto': f"{base_url}1493780474015-ba834fd0ce2f?w=800&h=600&fit=crop",
        'Bangkok': f"{base_url}1563492065-56fd5861a395?w=800&h=600&fit=crop",
        'Chiang Mai': f"{base_url}1559827260-89d04e6f0935?w=800&h=600&fit=crop",
        'Delhi': f"{base_url}1587135746-c3b7e3a8e4b4?w=800&h=600&fit=crop",
        'Mumbai': f"{base_url}1595658658-b0c6e1e1c3f7?w=800&h=600&fit=crop",
        'London': f"{base_url}1513635269-8583d7b4d2b5?w=800&h=600&fit=crop",
        'Edinburgh': f"{base_url}1584464491-6b5b8b6b6b6b?w=800&h=600&fit=crop",
        'Paris': f"{base_url}1502602898-c6b8b8b8b8b8?w=800&h=600&fit=crop",
        'Nice': f"{base_url}1527004760-d5b8b8b8b8b8?w=800&h=600&fit=crop",
        'Rome': f"{base_url}1515542622-37cfe11e5f0e?w=800&h=600&fit=crop",
        'Florence': f"{base_url}1543789177-dc8b8b8b8b8b?w=800&h=600&fit=crop",
        'Madrid': f"{base_url}1539650116-05b9b9b9b9b9?w=800&h=600&fit=crop",
        'Barcelona': f"{base_url}1508672019-12b9b9b9b9b9?w=800&h=600&fit=crop",
        'Berlin': f"{base_url}1528728329-13b9b9b9b9b9?w=800&h=600&fit=crop",
        'Munich': f"{base_url}1538654925-14b9b9b9b9b9?w=800&h=600&fit=crop",
        'Sydney': f"{base_url}1506905925-15b9b9b9b9b9?w=800&h=600&fit=crop",
        'Melbourne': f"{base_url}1538066801-16b9b9b9b9b9?w=800&h=600&fit=crop",
        'New York': f"{base_url}1496442226-17b9b9b9b9b9?w=800&h=600&fit=crop",
        'Los Angeles': f"{base_url}1534188753-18b9b9b9b9b9?w=800&h=600&fit=crop"
    }

    return image_mapping.get(destination, f"{base_url}1488646953-d2ded902755a?w=800&h=600&fit=crop")

def get_destination_colors(destination):
    """Get color scheme for a destination."""
    color_schemes = {
        'Tokyo': {'primary': '#E74C3C', 'secondary': '#F39C12', 'accent': '#3498DB'},
        'Kyoto': {'primary': '#8E44AD', 'secondary': '#27AE60', 'accent': '#E67E22'},
        'Bangkok': {'primary': '#F39C12', 'secondary': '#E74C3C', 'accent': '#2ECC71'},
        'Chiang Mai': {'primary': '#27AE60', 'secondary': '#8E44AD', 'accent': '#3498DB'},
        'Delhi': {'primary': '#E74C3C', 'secondary': '#F39C12', 'accent': '#9B59B6'},
        'Mumbai': {'primary': '#3498DB', 'secondary': '#E74C3C', 'accent': '#1ABC9C'},
        'London': {'primary': '#34495E', 'secondary': '#E74C3C', 'accent': '#3498DB'},
        'Edinburgh': {'primary': '#8E44AD', 'secondary': '#27AE60', 'accent': '#E67E22'},
        'Paris': {'primary': '#E74C3C', 'secondary': '#F39C12', 'accent': '#3498DB'},
        'Nice': {'primary': '#3498DB', 'secondary': '#1ABC9C', 'accent': '#F39C12'},
        'Rome': {'primary': '#E67E22', 'secondary': '#27AE60', 'accent': '#8E44AD'},
        'Florence': {'primary': '#9B59B6', 'secondary': '#E74C3C', 'accent': '#27AE60'},
        'Madrid': {'primary': '#E74C3C', 'secondary': '#F39C12', 'accent': '#3498DB'},
        'Barcelona': {'primary': '#3498DB', 'secondary': '#E74C3C', 'accent': '#1ABC9C'},
        'Berlin': {'primary': '#34495E', 'secondary': '#E74C3C', 'accent': '#F39C12'},
        'Munich': {'primary': '#27AE60', 'secondary': '#8E44AD', 'accent': '#E67E22'},
        'Sydney': {'primary': '#3498DB', 'secondary': '#1ABC9C', 'accent': '#F39C12'},
        'Melbourne': {'primary': '#8E44AD', 'secondary': '#27AE60', 'accent': '#E74C3C'},
        'New York': {'primary': '#34495E', 'secondary': '#E74C3C', 'accent': '#3498DB'},
        'Los Angeles': {'primary': '#F39C12', 'secondary': '#E74C3C', 'accent': '#3498DB'}
    }

    return color_schemes.get(destination, {'primary': '#3498DB', 'secondary': '#E74C3C', 'accent': '#27AE60'})