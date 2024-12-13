def get_mock_village_data():
    return {
        "name": "Village The Soul of India",
        "location": {
            "address1": "372 S Broadway",
            "city": "Hicksville",
            "state": "NY",
            "zip_code": "11801"
        },
        "phone": "+1 516-822-1222",
        "rating": 4.5,
        "price": "$$",
        "menu_items": [
            {"name": "Chicken Tikka Masala", "price": 16.99},
            {"name": "Butter Chicken", "price": 17.99},
            {"name": "Vegetable Biryani", "price": 14.99},
            {"name": "Garlic Naan", "price": 3.99},
            {"name": "Dal Makhani", "price": 13.99}
        ]
    }

def get_mock_nearby_restaurants():
    return [
        {
            "name": "Curry Club",
            "location": {"address1": "10 Sample St", "city": "Hicksville"},
            "rating": 4.3,
            "price": "$$",
            "menu_items": [
                {"name": "Chicken Tikka Masala", "price": 17.99},
                {"name": "Butter Chicken", "price": 18.99},
                {"name": "Vegetable Biryani", "price": 15.99},
                {"name": "Garlic Naan", "price": 4.49}
            ]
        },
        {
            "name": "Taste of India",
            "location": {"address1": "20 Test Ave", "city": "Hicksville"},
            "rating": 4.4,
            "price": "$$",
            "menu_items": [
                {"name": "Chicken Tikka Masala", "price": 16.49},
                {"name": "Butter Chicken", "price": 17.49},
                {"name": "Vegetable Biryani", "price": 14.49},
                {"name": "Garlic Naan", "price": 3.99},
                {"name": "Dal Makhani", "price": 12.99}
            ]
        },
        {
            "name": "Mumbai Spice",
            "location": {"address1": "30 Mock Rd", "city": "Hicksville"},
            "rating": 4.2,
            "price": "$$",
            "menu_items": [
                {"name": "Chicken Tikka Masala", "price": 18.99},
                {"name": "Butter Chicken", "price": 19.99},
                {"name": "Vegetable Biryani", "price": 16.99},
                {"name": "Garlic Naan", "price": 4.99},
                {"name": "Dal Makhani", "price": 14.99}
            ]
        }
    ]

def get_mock_weather():
    return {
        "main": {
            "temp": 280.15,  # About 44.6°F
            "humidity": 80
        },
        "weather": [
            {
                "main": "Rain",
                "description": "moderate rain"
            }
        ]
    }

def get_mock_busy_times():
    return {
        "current_popularity": 75,  # 0-100 scale
        "usual_popularity": 50,    # 0-100 scale
        "is_busy": True
    }