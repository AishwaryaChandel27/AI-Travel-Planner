import random

def get_destination_image_url(destination_name: str) -> str:
    """Get an image URL for a destination."""
    # Use Unsplash for high-quality destination images
    base_url = "https://images.unsplash.com/photo"

    # Map destinations to specific Unsplash photo IDs for consistency
    destination_images = {
        'paris': '1549813784-80d5d82d85bb',  # Eiffel Tower
        'tokyo': '1540959733332-eab4deabeeaf',  # Tokyo skyline
        'barcelona': '1539650116574-75c0c6698ecf',  # Sagrada Familia
        'london': '1513635269190-d10256ac6058',  # Big Ben
        'new york': '1496442226666-8d4d0e62e6e2',  # NYC skyline
        'rome': '1515542622106-78bda8ba0e5b',  # Colosseum
        'amsterdam': '1544461503-e0066c965c0e',  # Amsterdam canals
        'prague': '1541849546-216549ae8f3e',  # Prague castle
        'bangkok': '1508009603792-de1b7630e4de',  # Bangkok temple
        'sydney': '1506905925346-21bea4c00503',  # Sydney opera house
        'kyoto': '1545569341-9eb8b30979d9',  # Kyoto temple
        'chiang mai': '1578662996442-374dcbcf3e5e',  # Chiang Mai temple
        'delhi': '1587474679303-de4b2fe01037',  # Delhi landmarks
        'jaipur': '1599661228205-eea6cfee2bb4',  # Jaipur palace
        'mumbai': '1570168007719-70b4eaeebc38',  # Mumbai skyline
        'edinburgh': '1551731353-1e414905e13c',  # Edinburgh castle
        'nice': '1549813747-05b2a1ec93e2',  # Nice coastline
        'lisbon': '1555881400-74d7acaacd4b',  # Lisbon tram
        'madrid': '1539037116219-3f5e0b67dd55',  # Madrid palace
        'berlin': '1587564448504-c436b9b98b98',  # Berlin landmarks
        'vienna': '1516550893923-42d407bd4833',  # Vienna architecture
        'dubai': '1512453285698-6b08de22e3a9',  # Dubai skyline
        'singapore': '1525625293617-0131b5c3b0e7',  # Singapore marina
        'hong kong': '1536431311719-398b6704d4cc',  # Hong Kong skyline
        'istanbul': '1541432815-65b51b8e9101',  # Istanbul mosque
        'bali': '1537953773345-d172529d1d99',  # Bali temple
        'santorini': '1613395877344-13d4a8e0d49e',  # Santorini sunset
        'mykonos': '1601719506178-b6a9cbaaf44b',  # Mykonos windmills
        'venice': '1514890547357-a9ee288728e0',  # Venice canals
        'florence': '1545671913-b904b6c468ef',  # Florence duomo
        'cairo': '1539650116574-75c0c6698ecf',  # Cairo pyramids
        'marrakech': '1489749798305-4fea3ae436d8',  # Marrakech architecture
        'cape town': '1580060839326-a15b6df8c6c6',  # Cape Town mountain
    }

    # Clean destination name for lookup
    clean_name = destination_name.lower().strip().replace(',', '').replace('.', '')

    # Try exact match first
    if clean_name in destination_images:
        photo_id = destination_images[clean_name]
        return f"{base_url}-{photo_id}?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80"

    # Try partial match
    for key, photo_id in destination_images.items():
        if key in clean_name or any(word in clean_name for word in key.split()):
            return f"{base_url}-{photo_id}?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&q=80"

    # Fallback: generic travel image
    return f"{base_url}-1488646953615-e61a18fd3c24?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"

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