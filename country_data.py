"""
Country-specific data for the AI Travel Planner
Contains budget ranges, popular destinations, and travel information by country
"""

COUNTRY_DATA = {
    # North America
    "United States": {
        "currency": "USD",
        "budget_ranges": {
            "budget": {"min": 80, "max": 150, "description": "Budget traveler - hostels, street food, public transport"},
            "mid_range": {"min": 150, "max": 300, "description": "Mid-range - 3-star hotels, casual dining, mix of transport"},
            "luxury": {"min": 300, "max": 800, "description": "Luxury - 4-5 star hotels, fine dining, private transport"},
            "ultra_luxury": {"min": 800, "max": 2000, "description": "Ultra luxury - premium everything, exclusive experiences"}
        },
        "popular_destinations": ["New York", "Los Angeles", "San Francisco", "Las Vegas", "Chicago", "Miami", "Boston", "Seattle"],
        "best_time": "Spring (March-May) and Fall (September-November)",
        "visa_info": "ESTA required for most visitors",
        "language": "English",
        "time_zones": ["EST", "CST", "MST", "PST"],
        "cultural_notes": "Tipping is customary (15-20%). Diverse culture varies by region."
    },
    
    "Canada": {
        "currency": "CAD",
        "budget_ranges": {
            "budget": {"min": 60, "max": 120, "description": "Budget traveler - hostels, casual dining, public transport"},
            "mid_range": {"min": 120, "max": 250, "description": "Mid-range - hotels, restaurants, car rental"},
            "luxury": {"min": 250, "max": 600, "description": "Luxury - premium hotels, fine dining, guided tours"},
            "ultra_luxury": {"min": 600, "max": 1500, "description": "Ultra luxury - exclusive lodges, private experiences"}
        },
        "popular_destinations": ["Toronto", "Vancouver", "Montreal", "Quebec City", "Calgary", "Ottawa", "Banff", "Niagara Falls"],
        "best_time": "Summer (June-August) for most regions, Winter for ski resorts",
        "visa_info": "eTA required for most visitors",
        "language": "English and French",
        "time_zones": ["EST", "CST", "MST", "PST"],
        "cultural_notes": "Polite and multicultural society. Tipping 15-18% is standard."
    },
    
    # Europe
    "United Kingdom": {
        "currency": "GBP",
        "budget_ranges": {
            "budget": {"min": 50, "max": 90, "description": "Budget traveler - hostels, pub food, public transport"},
            "mid_range": {"min": 90, "max": 200, "description": "Mid-range - B&Bs, restaurants, trains"},
            "luxury": {"min": 200, "max": 500, "description": "Luxury - boutique hotels, fine dining, private tours"},
            "ultra_luxury": {"min": 500, "max": 1200, "description": "Ultra luxury - historic estates, Michelin dining"}
        },
        "popular_destinations": ["London", "Edinburgh", "Bath", "Oxford", "Cambridge", "Liverpool", "Manchester", "Brighton"],
        "best_time": "Late spring to early autumn (May-September)",
        "visa_info": "Tourist visa required for most non-EU visitors",
        "language": "English",
        "time_zones": ["GMT", "BST"],
        "cultural_notes": "Queueing culture. Pub etiquette important. Tipping 10-15% optional."
    },
    
    "France": {
        "currency": "EUR",
        "budget_ranges": {
            "budget": {"min": 60, "max": 100, "description": "Budget traveler - hostels, bistros, metro"},
            "mid_range": {"min": 100, "max": 220, "description": "Mid-range - hotels, brasseries, regional trains"},
            "luxury": {"min": 220, "max": 550, "description": "Luxury - boutique hotels, fine dining, wine tours"},
            "ultra_luxury": {"min": 550, "max": 1500, "description": "Ultra luxury - châteaux, Michelin stars, private guides"}
        },
        "popular_destinations": ["Paris", "Nice", "Lyon", "Marseille", "Bordeaux", "Strasbourg", "Toulouse", "Cannes"],
        "best_time": "Late spring to early autumn (May-September)",
        "visa_info": "Schengen visa required for most non-EU visitors",
        "language": "French",
        "time_zones": ["CET", "CEST"],
        "cultural_notes": "Formal greetings important. Long lunch breaks. Service charge included."
    },
    
    "Germany": {
        "currency": "EUR",
        "budget_ranges": {
            "budget": {"min": 50, "max": 80, "description": "Budget traveler - hostels, beer gardens, public transport"},
            "mid_range": {"min": 80, "max": 180, "description": "Mid-range - hotels, restaurants, trains"},
            "luxury": {"min": 180, "max": 400, "description": "Luxury - boutique hotels, fine dining, private tours"},
            "ultra_luxury": {"min": 400, "max": 1000, "description": "Ultra luxury - castle hotels, gourmet experiences"}
        },
        "popular_destinations": ["Berlin", "Munich", "Hamburg", "Cologne", "Frankfurt", "Dresden", "Heidelberg", "Neuschwanstein"],
        "best_time": "Late spring to early autumn (May-September)",
        "visa_info": "Schengen visa required for most non-EU visitors",
        "language": "German",
        "time_zones": ["CET", "CEST"],
        "cultural_notes": "Punctuality highly valued. Direct communication style. Tipping 10% customary."
    },
    
    "Italy": {
        "currency": "EUR",
        "budget_ranges": {
            "budget": {"min": 55, "max": 95, "description": "Budget traveler - hostels, trattorias, regional trains"},
            "mid_range": {"min": 95, "max": 200, "description": "Mid-range - hotels, ristorantes, guided tours"},
            "luxury": {"min": 200, "max": 500, "description": "Luxury - boutique hotels, fine dining, private transfers"},
            "ultra_luxury": {"min": 500, "max": 1300, "description": "Ultra luxury - historic palazzos, Michelin dining"}
        },
        "popular_destinations": ["Rome", "Florence", "Venice", "Milan", "Naples", "Tuscany", "Amalfi Coast", "Sicily"],
        "best_time": "Late spring to early autumn (May-September), avoid August crowds",
        "visa_info": "Schengen visa required for most non-EU visitors",
        "language": "Italian",
        "time_zones": ["CET", "CEST"],
        "cultural_notes": "Leisurely dining culture. Dress well in cities. Tipping not mandatory but appreciated."
    },
    
    "Spain": {
        "currency": "EUR",
        "budget_ranges": {
            "budget": {"min": 45, "max": 80, "description": "Budget traveler - hostels, tapas bars, buses"},
            "mid_range": {"min": 80, "max": 160, "description": "Mid-range - hotels, restaurants, trains"},
            "luxury": {"min": 160, "max": 400, "description": "Luxury - boutique hotels, fine dining, private tours"},
            "ultra_luxury": {"min": 400, "max": 1000, "description": "Ultra luxury - paradors, gourmet experiences"}
        },
        "popular_destinations": ["Madrid", "Barcelona", "Seville", "Granada", "Valencia", "Bilbao", "Toledo", "Santiago"],
        "best_time": "Spring (March-May) and Fall (September-November)",
        "visa_info": "Schengen visa required for most non-EU visitors",
        "language": "Spanish",
        "time_zones": ["CET", "CEST"],
        "cultural_notes": "Late dining culture. Siesta traditions. Relaxed pace of life."
    },
    
    # Asia
    "Japan": {
        "currency": "JPY",
        "budget_ranges": {
            "budget": {"min": 60, "max": 100, "description": "Budget traveler - hostels, convenience stores, local trains"},
            "mid_range": {"min": 100, "max": 250, "description": "Mid-range - business hotels, restaurants, JR Pass"},
            "luxury": {"min": 250, "max": 600, "description": "Luxury - ryokans, kaiseki dining, private tours"},
            "ultra_luxury": {"min": 600, "max": 1500, "description": "Ultra luxury - exclusive ryokans, private experiences"}
        },
        "popular_destinations": ["Tokyo", "Kyoto", "Osaka", "Hiroshima", "Nara", "Nikko", "Hakone", "Takayama"],
        "best_time": "Spring (March-May) and Fall (September-November)",
        "visa_info": "Visa-free for many countries (90 days)",
        "language": "Japanese",
        "time_zones": ["JST"],
        "cultural_notes": "Bow as greeting. Remove shoes indoors. No tipping culture."
    },
    
    "Thailand": {
        "currency": "THB",
        "budget_ranges": {
            "budget": {"min": 25, "max": 50, "description": "Budget traveler - hostels, street food, tuk-tuks"},
            "mid_range": {"min": 50, "max": 120, "description": "Mid-range - hotels, restaurants, tours"},
            "luxury": {"min": 120, "max": 300, "description": "Luxury - resorts, fine dining, private transfers"},
            "ultra_luxury": {"min": 300, "max": 800, "description": "Ultra luxury - exclusive resorts, private islands"}
        },
        "popular_destinations": ["Bangkok", "Chiang Mai", "Phuket", "Pattaya", "Koh Samui", "Krabi", "Ayutthaya", "Kanchanaburi"],
        "best_time": "Cool season (November-February)",
        "visa_info": "Visa-free for many countries (30 days)",
        "language": "Thai",
        "time_zones": ["ICT"],
        "cultural_notes": "Wai greeting. Respect for monarchy. Remove shoes in temples."
    },
    
    "India": {
        "currency": "INR",
        "budget_ranges": {
            "budget": {"min": 20, "max": 40, "description": "Budget traveler - guesthouses, street food, trains"},
            "mid_range": {"min": 40, "max": 100, "description": "Mid-range - hotels, restaurants, private transport"},
            "luxury": {"min": 100, "max": 300, "description": "Luxury - heritage hotels, fine dining, guided tours"},
            "ultra_luxury": {"min": 300, "max": 800, "description": "Ultra luxury - palace hotels, exclusive experiences"}
        },
        "popular_destinations": ["Delhi", "Mumbai", "Jaipur", "Agra", "Goa", "Kerala", "Rajasthan", "Varanasi"],
        "best_time": "Winter (October-March)",
        "visa_info": "Tourist visa required for most visitors",
        "language": "Hindi, English",
        "time_zones": ["IST"],
        "cultural_notes": "Namaste greeting. Dress modestly. Diverse cultural practices."
    },
    
    "China": {
        "currency": "CNY",
        "budget_ranges": {
            "budget": {"min": 30, "max": 60, "description": "Budget traveler - hostels, local food, public transport"},
            "mid_range": {"min": 60, "max": 150, "description": "Mid-range - hotels, restaurants, trains"},
            "luxury": {"min": 150, "max": 400, "description": "Luxury - boutique hotels, fine dining, private guides"},
            "ultra_luxury": {"min": 400, "max": 1000, "description": "Ultra luxury - exclusive hotels, premium experiences"}
        },
        "popular_destinations": ["Beijing", "Shanghai", "Xi'an", "Guilin", "Chengdu", "Hangzhou", "Suzhou", "Lhasa"],
        "best_time": "Spring (April-June) and Fall (September-November)",
        "visa_info": "Tourist visa required for most visitors",
        "language": "Mandarin Chinese",
        "time_zones": ["CST"],
        "cultural_notes": "Business card etiquette. Respect for elders. Gift-giving customs."
    },
    
    # Australia & Oceania
    "Australia": {
        "currency": "AUD",
        "budget_ranges": {
            "budget": {"min": 70, "max": 120, "description": "Budget traveler - hostels, food courts, public transport"},
            "mid_range": {"min": 120, "max": 250, "description": "Mid-range - hotels, restaurants, car rental"},
            "luxury": {"min": 250, "max": 600, "description": "Luxury - boutique hotels, fine dining, private tours"},
            "ultra_luxury": {"min": 600, "max": 1500, "description": "Ultra luxury - exclusive lodges, premium experiences"}
        },
        "popular_destinations": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold Coast", "Cairns", "Darwin"],
        "best_time": "Spring (September-November) and Fall (March-May)",
        "visa_info": "ETA required for most visitors",
        "language": "English",
        "time_zones": ["AEST", "ACST", "AWST"],
        "cultural_notes": "Casual culture. Outdoor lifestyle. Tipping not mandatory but appreciated."
    },
    
    # South America
    "Brazil": {
        "currency": "BRL",
        "budget_ranges": {
            "budget": {"min": 30, "max": 60, "description": "Budget traveler - hostels, local food, buses"},
            "mid_range": {"min": 60, "max": 140, "description": "Mid-range - hotels, restaurants, domestic flights"},
            "luxury": {"min": 140, "max": 350, "description": "Luxury - boutique hotels, fine dining, private tours"},
            "ultra_luxury": {"min": 350, "max": 900, "description": "Ultra luxury - exclusive resorts, premium experiences"}
        },
        "popular_destinations": ["Rio de Janeiro", "São Paulo", "Salvador", "Brasília", "Recife", "Manaus", "Iguazu Falls", "Pantanal"],
        "best_time": "Fall and Winter (April-September)",
        "visa_info": "Visa required for many countries",
        "language": "Portuguese",
        "time_zones": ["BRT", "AMT", "ACT"],
        "cultural_notes": "Warm, friendly culture. Beach lifestyle. Late dining times."
    },
    
    "Argentina": {
        "currency": "ARS",
        "budget_ranges": {
            "budget": {"min": 25, "max": 50, "description": "Budget traveler - hostels, parrillas, buses"},
            "mid_range": {"min": 50, "max": 120, "description": "Mid-range - hotels, restaurants, domestic flights"},
            "luxury": {"min": 120, "max": 300, "description": "Luxury - boutique hotels, wine tours, private guides"},
            "ultra_luxury": {"min": 300, "max": 800, "description": "Ultra luxury - estancias, premium experiences"}
        },
        "popular_destinations": ["Buenos Aires", "Mendoza", "Bariloche", "Ushuaia", "Salta", "Córdoba", "Iguazu", "El Calafate"],
        "best_time": "Fall and Spring (March-May, September-November)",
        "visa_info": "Visa-free for many countries",
        "language": "Spanish",
        "time_zones": ["ART"],
        "cultural_notes": "Tango culture. Late dining. European influence."
    },
    
    # Africa
    "South Africa": {
        "currency": "ZAR",
        "budget_ranges": {
            "budget": {"min": 25, "max": 50, "description": "Budget traveler - backpacker lodges, local food, buses"},
            "mid_range": {"min": 50, "max": 120, "description": "Mid-range - guesthouses, restaurants, car rental"},
            "luxury": {"min": 120, "max": 300, "description": "Luxury - boutique hotels, wine tours, safaris"},
            "ultra_luxury": {"min": 300, "max": 800, "description": "Ultra luxury - exclusive lodges, private safaris"}
        },
        "popular_destinations": ["Cape Town", "Johannesburg", "Durban", "Kruger National Park", "Garden Route", "Stellenbosch", "Hermanus", "Knysna"],
        "best_time": "Fall and Spring (March-May, September-November)",
        "visa_info": "Visa-free for many countries",
        "language": "English, Afrikaans, Zulu",
        "time_zones": ["SAST"],
        "cultural_notes": "Rainbow Nation diversity. Braai culture. Tipping 10-15% expected."
    },
    
    # Middle East
    "United Arab Emirates": {
        "currency": "AED",
        "budget_ranges": {
            "budget": {"min": 60, "max": 100, "description": "Budget traveler - hostels, food courts, metro"},
            "mid_range": {"min": 100, "max": 250, "description": "Mid-range - hotels, restaurants, taxis"},
            "luxury": {"min": 250, "max": 600, "description": "Luxury - 5-star hotels, fine dining, private tours"},
            "ultra_luxury": {"min": 600, "max": 2000, "description": "Ultra luxury - exclusive resorts, private experiences"}
        },
        "popular_destinations": ["Dubai", "Abu Dhabi", "Sharjah", "Fujairah", "Ras Al Khaimah", "Ajman", "Al Ain", "Umm Al Quwain"],
        "best_time": "Winter (October-April)",
        "visa_info": "Visa on arrival for many countries",
        "language": "Arabic, English",
        "time_zones": ["GST"],
        "cultural_notes": "Conservative dress code. No alcohol in public. Respect for Islamic customs."
    }
}

def get_country_list():
    """Get list of all supported countries"""
    return list(COUNTRY_DATA.keys())

def get_country_info(country_name):
    """Get information for a specific country"""
    return COUNTRY_DATA.get(country_name)

def get_budget_ranges(country_name):
    """Get budget ranges for a specific country"""
    country_info = COUNTRY_DATA.get(country_name)
    if country_info:
        return country_info.get("budget_ranges", {})
    return {}

def get_popular_destinations(country_name):
    """Get popular destinations for a specific country"""
    country_info = COUNTRY_DATA.get(country_name)
    if country_info:
        return country_info.get("popular_destinations", [])
    return []

def suggest_daily_budget(country_name, budget_type="mid_range"):
    """Suggest daily budget based on country and budget type"""
    ranges = get_budget_ranges(country_name)
    if budget_type in ranges:
        budget_range = ranges[budget_type]
        return {
            "min": budget_range["min"],
            "max": budget_range["max"],
            "description": budget_range["description"],
            "currency": COUNTRY_DATA[country_name]["currency"]
        }
    return None