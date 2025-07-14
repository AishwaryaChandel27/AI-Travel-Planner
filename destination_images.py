import random

def get_destination_image_url(destination: str) -> str:
    """Get a placeholder image URL for a destination."""
    # Using Unsplash for high-quality travel images
    image_keywords = [
        'travel', 'city', 'landscape', 'architecture', 'tourism', 
        'vacation', 'adventure', 'culture', 'landmark', 'scenic'
    ]

    # Create a consistent but varied image for each destination
    seed = sum(ord(c) for c in destination.lower())
    random.seed(seed)

    keyword = random.choice(image_keywords)
    width = 800
    height = 600

    # Use Unsplash API for beautiful images
    return f"https://source.unsplash.com/{width}x{height}/?{keyword},{destination.lower().replace(' ', ',')}"

def get_destination_colors(destination: str) -> dict:
    """Get color scheme for a destination card."""
    # Predefined color schemes
    color_schemes = [
        {'primary': '#3498db', 'secondary': '#2980b9', 'accent': '#ecf0f1'},
        {'primary': '#e74c3c', 'secondary': '#c0392b', 'accent': '#f8f9fa'},
        {'primary': '#2ecc71', 'secondary': '#27ae60', 'accent': '#f1f2f6'},
        {'primary': '#f39c12', 'secondary': '#e67e22', 'accent': '#ffeaa7'},
        {'primary': '#9b59b6', 'secondary': '#8e44ad', 'accent': '#f8f9fa'},
        {'primary': '#1abc9c', 'secondary': '#16a085', 'accent': '#dff9fb'},
        {'primary': '#34495e', 'secondary': '#2c3e50', 'accent': '#ecf0f1'},
        {'primary': '#e67e22', 'secondary': '#d35400', 'accent': '#ffeaa7'}
    ]

    # Create consistent color scheme for each destination
    seed = sum(ord(c) for c in destination.lower())
    return color_schemes[seed % len(color_schemes)]