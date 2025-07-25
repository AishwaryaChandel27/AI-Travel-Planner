"""
Country-specific data for the AI Travel Planner
Contains budget ranges, popular destinations, and travel information by country
"""

COUNTRY_DATA = {
    # North America
    "United States": {
        "currency": "USD",
        "currency_symbol": "$",
        "exchange_rate": 1.0,  # Base currency
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
        "currency_symbol": "£",
        "exchange_rate": 0.79,  # Approximate GBP to USD
        "budget_ranges": {
            "budget": {"min": 40, "max": 70, "description": "Budget traveler - hostels, pub food, public transport"},
            "mid_range": {"min": 70, "max": 160, "description": "Mid-range - B&Bs, restaurants, trains"},
            "luxury": {"min": 160, "max": 400, "description": "Luxury - boutique hotels, fine dining, private tours"},
            "ultra_luxury": {"min": 400, "max": 1000, "description": "Ultra luxury - historic estates, Michelin dining"}
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
        "currency_symbol": "€",
        "exchange_rate": 0.92,  # Approximate EUR to USD
        "budget_ranges": {
            "budget": {"min": 55, "max": 90, "description": "Budget traveler - hostels, bistros, metro"},
            "mid_range": {"min": 90, "max": 200, "description": "Mid-range - hotels, brasseries, regional trains"},
            "luxury": {"min": 200, "max": 500, "description": "Luxury - boutique hotels, fine dining, wine tours"},
            "ultra_luxury": {"min": 500, "max": 1400, "description": "Ultra luxury - châteaux, Michelin stars, private guides"}
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
        "currency_symbol": "¥",
        "exchange_rate": 150.0,  # Approximate JPY to USD
        "budget_ranges": {
            "budget": {"min": 8000, "max": 12000, "description": "Budget traveler - hostels, convenience stores, local trains"},
            "mid_range": {"min": 12000, "max": 25000, "description": "Mid-range - business hotels, restaurants, JR Pass"},
            "luxury": {"min": 25000, "max": 60000, "description": "Luxury - ryokans, kaiseki dining, private tours"},
            "ultra_luxury": {"min": 60000, "max": 150000, "description": "Ultra luxury - exclusive ryokans, private experiences"}
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
        "currency_symbol": "฿",
        "exchange_rate": 36.0,  # Approximate THB to USD
        "budget_ranges": {
            "budget": {"min": 800, "max": 1500, "description": "Budget traveler - hostels, street food, tuk-tuks"},
            "mid_range": {"min": 1500, "max": 3500, "description": "Mid-range - hotels, restaurants, tours"},
            "luxury": {"min": 3500, "max": 8000, "description": "Luxury - resorts, fine dining, private transfers"},
            "ultra_luxury": {"min": 8000, "max": 25000, "description": "Ultra luxury - exclusive resorts, private islands"}
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
        "currency_symbol": "₹",
        "exchange_rate": 83.0,  # Approximate INR to USD
        "budget_ranges": {
            "budget": {"min": 1500, "max": 3000, "description": "Budget traveler - guesthouses, street food, trains"},
            "mid_range": {"min": 3000, "max": 7000, "description": "Mid-range - hotels, restaurants, private transport"},
            "luxury": {"min": 7000, "max": 20000, "description": "Luxury - heritage hotels, fine dining, guided tours"},
            "ultra_luxury": {"min": 20000, "max": 60000, "description": "Ultra luxury - palace hotels, exclusive experiences"}
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

def get_country_info(country):
    """Get country information including currency, language, etc."""
    country_data = {
        'Japan': {
            'currency': 'JPY',
            'language': 'Japanese',
            'best_time': 'Spring (March-May) and Fall (September-November)',
            'cultural_notes': 'Bowing is customary, remove shoes indoors, quiet on public transport',
            'visa_info': 'Tourist visa required for most countries'
        },
        'Thailand': {
            'currency': 'THB',
            'language': 'Thai',
            'best_time': 'Cool season (November-February)',
            'cultural_notes': 'Dress modestly at temples, wai greeting, respect for monarchy',
            'visa_info': 'Visa on arrival for many countries'
        },
        'India': {
            'currency': 'INR',
            'language': 'Hindi/English',
            'best_time': 'Winter (October-March)',
            'cultural_notes': 'Diverse cultures, respect religious customs, bargaining common',
            'visa_info': 'E-visa available for most countries'
        },
        'United Kingdom': {
            'currency': 'GBP',
            'language': 'English',
            'best_time': 'Late spring to early autumn (May-September)',
            'cultural_notes': 'Queuing culture, pub etiquette, politeness valued',
            'visa_info': 'Visa required for most non-EU countries'
        },
        'France': {
            'currency': 'EUR',
            'language': 'French',
            'best_time': 'Late spring to early autumn (May-September)',
            'cultural_notes': 'Greeting with kisses, dining etiquette, fashion conscious',
            'visa_info': 'Schengen visa required for most countries'
        },
        'Italy': {
            'currency': 'EUR',
            'language': 'Italian',
            'best_time': 'Spring (April-June) and Fall (September-October)',
            'cultural_notes': 'Family-oriented, dining traditions, art appreciation',
            'visa_info': 'Schengen visa required for most countries'
        },
        'Spain': {
            'currency': 'EUR',
            'language': 'Spanish',
            'best_time': 'Spring (March-May) and Fall (September-November)',
            'cultural_notes': 'Siesta culture, late dining, social gatherings',
            'visa_info': 'Schengen visa required for most countries'
        },
        'Germany': {
            'currency': 'EUR',
            'language': 'German',
            'best_time': 'Late spring to early autumn (May-September)',
            'cultural_notes': 'Punctuality valued, direct communication, recycling important',
            'visa_info': 'Schengen visa required for most countries'
        },
        'Australia': {
            'currency': 'AUD',
            'language': 'English',
            'best_time': 'Spring (September-November) and Fall (March-May)',
            'cultural_notes': 'Laid-back culture, outdoor lifestyle, tipping not mandatory',
            'visa_info': 'ETA or visa required for most countries'
        },
        'United States': {
            'currency': 'USD',
            'language': 'English',
            'best_time': 'Varies by region',
            'cultural_notes': 'Tipping culture, diverse regions, friendly demeanor',
            'visa_info': 'ESTA or visa required for most countries'
        }
    }

    return country_data.get(country, {
        'currency': 'USD',
        'language': 'Local language',
        'best_time': 'Year-round',
        'cultural_notes': 'Research local customs',
        'visa_info': 'Check visa requirements'
    })

def get_popular_destinations(country):
    """Get popular destinations for a country."""
    destinations = {
        'Japan': ['Tokyo', 'Kyoto', 'Osaka', 'Hiroshima', 'Nara'],
        'Thailand': ['Bangkok', 'Chiang Mai', 'Phuket', 'Koh Samui', 'Pattaya'],
        'India': ['Delhi', 'Mumbai', 'Jaipur', 'Agra', 'Goa'],
        'United Kingdom': ['London', 'Edinburgh', 'Manchester', 'Bath', 'York'],
        'France': ['Paris', 'Nice', 'Lyon', 'Marseille', 'Bordeaux'],
        'Italy': ['Rome', 'Florence', 'Venice', 'Milan', 'Naples'],
        'Spain': ['Madrid', 'Barcelona', 'Seville', 'Valencia', 'Bilbao'],
        'Germany': ['Berlin', 'Munich', 'Hamburg', 'Cologne', 'Frankfurt'],
        'Australia': ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide'],
        'United States': ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'Miami']
    }

    return destinations.get(country, [f'Capital of {country}', f'Major city in {country}'])

def get_budget_ranges(country):
    """Get budget ranges for a country."""
    ranges = {
        'Japan': {'budget': 60, 'mid_range': 120, 'luxury': 300, 'ultra_luxury': 600},
        'Thailand': {'budget': 25, 'mid_range': 50, 'luxury': 150, 'ultra_luxury': 400},
        'India': {'budget': 15, 'mid_range': 40, 'luxury': 120, 'ultra_luxury': 300},
        'United Kingdom': {'budget': 50, 'mid_range': 100, 'luxury': 250, 'ultra_luxury': 500},
        'France': {'budget': 60, 'mid_range': 120, 'luxury': 280, 'ultra_luxury': 550},
        'Italy': {'budget': 50, 'mid_range': 100, 'luxury': 220, 'ultra_luxury': 450},
        'Spain': {'budget': 45, 'mid_range': 90, 'luxury': 200, 'ultra_luxury': 400},
        'Germany': {'budget': 55, 'mid_range': 110, 'luxury': 250, 'ultra_luxury': 500},
        'Australia': {'budget': 70, 'mid_range': 140, 'luxury': 350, 'ultra_luxury': 700},
        'United States': {'budget': 60, 'mid_range': 120, 'luxury': 300, 'ultra_luxury': 600}
    }

    return ranges.get(country, {'budget': 40, 'mid_range': 80, 'luxury': 200, 'ultra_luxury': 400})

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
"""
Country data and information for the AI Travel Planner
"""

def get_country_info(country):
    """Get country-specific information."""
    country_data = {
        'Japan': {
            'currency': 'JPY',
            'language': 'Japanese',
            'best_time': 'Spring (March-May) and Fall (September-November)',
            'cultural_notes': 'Bow when greeting, remove shoes indoors, be quiet on public transport',
            'visa_info': 'Tourist visa required for most countries'
        },
        'Thailand': {
            'currency': 'THB',
            'language': 'Thai',
            'best_time': 'Cool season (November-February)',
            'cultural_notes': 'Dress modestly at temples, respect the monarchy, remove shoes when entering homes',
            'visa_info': 'Visa on arrival or visa exemption for many countries'
        },
        'India': {
            'currency': 'INR',
            'language': 'Hindi/English',
            'best_time': 'Winter (October-March)',
            'cultural_notes': 'Dress conservatively, use right hand for eating, respect religious customs',
            'visa_info': 'e-Visa available for most countries'
        },
        'United Kingdom': {
            'currency': 'GBP',
            'language': 'English',
            'best_time': 'Late spring to early autumn (May-September)',
            'cultural_notes': 'Queue politely, respect personal space, tipping 10-15% at restaurants',
            'visa_info': 'Check visa requirements based on nationality'
        },
        'France': {
            'currency': 'EUR',
            'language': 'French',
            'best_time': 'Late spring to early autumn (May-September)',
            'cultural_notes': 'Greet with bonjour/bonsoir, dress well, dining etiquette important',
            'visa_info': 'Schengen visa for non-EU citizens'
        },
        'Italy': {
            'currency': 'EUR',
            'language': 'Italian',
            'best_time': 'Spring (April-June) and Fall (September-October)',
            'cultural_notes': 'Dress well, especially at religious sites, lunch is sacred time',
            'visa_info': 'Schengen visa for non-EU citizens'
        },
        'Spain': {
            'currency': 'EUR',
            'language': 'Spanish',
            'best_time': 'Spring (March-May) and Fall (September-November)',
            'cultural_notes': 'Late dining times, siesta culture, dress smartly',
            'visa_info': 'Schengen visa for non-EU citizens'
        },
        'Germany': {
            'currency': 'EUR',
            'language': 'German',
            'best_time': 'Late spring to early autumn (May-September)',
            'cultural_notes': 'Punctuality is important, direct communication style, respect quiet hours',
            'visa_info': 'Schengen visa for non-EU citizens'
        },
        'Australia': {
            'currency': 'AUD',
            'language': 'English',
            'best_time': 'Spring (September-November) and Autumn (March-May)',
            'cultural_notes': 'Casual culture, sun safety important, tipping not mandatory',
            'visa_info': 'Electronic Travel Authority (ETA) for many countries'
        },
        'United States': {
            'currency': 'USD',
            'language': 'English',
            'best_time': 'Varies by region - Spring and Fall generally best',
            'cultural_notes': 'Tipping culture (15-20%), diverse customs by region, friendly conversation',
            'visa_info': 'ESTA for eligible countries, tourist visa for others'
        }
    }
    
    return country_data.get(country, {
        'currency': 'USD',
        'language': 'Local language',
        'best_time': 'Year-round',
        'cultural_notes': 'Research local customs before traveling',
        'visa_info': 'Check visa requirements'
    })

def get_popular_destinations(country):
    """Get popular destinations for a country."""
    destinations = {
        'Japan': ['Tokyo', 'Kyoto', 'Osaka', 'Hiroshima', 'Nara'],
        'Thailand': ['Bangkok', 'Chiang Mai', 'Phuket', 'Krabi', 'Koh Samui'],
        'India': ['Delhi', 'Mumbai', 'Jaipur', 'Goa', 'Kerala'],
        'United Kingdom': ['London', 'Edinburgh', 'Bath', 'York', 'Cambridge'],
        'France': ['Paris', 'Nice', 'Lyon', 'Bordeaux', 'Marseille'],
        'Italy': ['Rome', 'Florence', 'Venice', 'Milan', 'Naples'],
        'Spain': ['Madrid', 'Barcelona', 'Seville', 'Valencia', 'Granada'],
        'Germany': ['Berlin', 'Munich', 'Hamburg', 'Cologne', 'Dresden'],
        'Australia': ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide'],
        'United States': ['New York', 'Los Angeles', 'Chicago', 'Miami', 'San Francisco']
    }
    
    return destinations.get(country, ['Capital City', 'Major City', 'Coastal City'])

def get_budget_ranges(country):
    """Get budget ranges for a country."""
    country_info = get_country_info(country)
    currency = country_info['currency']
    
    # Base ranges in USD, adjust based on country
    base_ranges = {
        'budget': {'min': 30, 'max': 60},
        'mid_range': {'min': 60, 'max': 150},
        'luxury': {'min': 150, 'max': 400},
        'ultra_luxury': {'min': 400, 'max': 1000}
    }
    
    # Currency conversion factors (approximate)
    conversion_factors = {
        'JPY': 110,
        'THB': 35,
        'INR': 75,
        'GBP': 0.8,
        'EUR': 0.9,
        'AUD': 1.4,
        'USD': 1.0
    }
    
    factor = conversion_factors.get(currency, 1.0)
    
    ranges = {}
    for budget_type, range_data in base_ranges.items():
        ranges[budget_type] = {
            'min': int(range_data['min'] * factor),
            'max': int(range_data['max'] * factor),
            'currency': currency
        }
    
    return ranges
