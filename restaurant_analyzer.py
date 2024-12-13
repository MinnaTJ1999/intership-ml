import json
from datetime import datetime
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from mock_data import (
    get_mock_village_data,
    get_mock_nearby_restaurants,
    get_mock_weather,
    get_mock_busy_times
)

class RestaurantAnalyzer:
    def __init__(self):
        self.village_location = {'lat': 40.7675, 'lng': -73.5252}  # Hicksville coordinates

    def get_village_details(self):
        """Get mock details for Village restaurant"""
        return get_mock_village_data()

    def get_nearby_restaurants(self):
        """Get mock nearby restaurants"""
        return get_mock_nearby_restaurants()

    def get_weather(self):
        """Get mock weather data"""
        return get_mock_weather()

    def get_busy_status(self):
        """Get mock busy status"""
        return get_mock_busy_times()

    def kelvin_to_fahrenheit(self, kelvin):
        """Convert Kelvin to Fahrenheit"""
        return (kelvin - 273.15) * 9/5 + 32

    def get_base_price(self, item_name, nearby_restaurants):
        """Get the lowest price for a menu item from nearby restaurants"""
        prices = []
        for restaurant in nearby_restaurants:
            for item in restaurant['menu_items']:
                if item['name'].lower() == item_name.lower():
                    prices.append(item['price'])
        return min(prices) if prices else None

    def predict_price(self, menu_item, weather, busy_status, nearby):
        """Predict price adjustments based on conditions"""
        # Get base price from nearby restaurants
        base_price = self.get_base_price(menu_item['name'], nearby)
        if not base_price:
            return menu_item['price']  # Keep current price if no comparison available
        
        # Get conditions
        temp_f = self.kelvin_to_fahrenheit(weather['main']['temp'])
        is_raining = weather['weather'][0]['main'] in ['Rain', 'Snow']
        is_busy = busy_status['is_busy']
        
        # Apply price adjustment
        if temp_f < 45 and (is_raining or is_busy):
            predicted_price = base_price * 1.15  # 15% markup
        else:
            predicted_price = base_price
        
        return predicted_price

    def analyze_and_display(self):
        """Main analysis function"""
        # Get all data
        village = self.get_village_details()
        nearby = self.get_nearby_restaurants()
        weather = self.get_weather()
        busy_status = self.get_busy_status()
        
        # Calculate predicted prices
        predictions = []
        for item in village['menu_items']:
            predicted_price = self.predict_price(item, weather, busy_status, nearby)
            predictions.append({
                'item': item['name'],
                'current_price': item['price'],
                'predicted_price': predicted_price,
                'price_difference': predicted_price - item['price']
            })

        # Prepare output
        output = {
            'village': village,
            'nearby_restaurants': nearby,
            'weather': {
                'temperature_f': self.kelvin_to_fahrenheit(weather['main']['temp']),
                'is_raining': weather['weather'][0]['main'] == 'Rain',
                'description': weather['weather'][0]['description']
            },
            'busy_status': busy_status,
            'price_predictions': predictions
        }

        # Save results
        with open('data.json', 'w') as f:
            json.dump(output, f, indent=2)

        return output

if __name__ == "__main__":
    analyzer = RestaurantAnalyzer()
    results = analyzer.analyze_and_display()
    
    # Print analysis results
    print("\nAnalysis Results:")
    print("================")
    print(f"Temperature: {results['weather']['temperature_f']:.1f}°F")
    print(f"Weather: {results['weather']['description']}")
    print(f"Restaurant Status: {'Busy' if results['busy_status']['is_busy'] else 'Normal'}")
    
    print("\nPrice Predictions:")
    print("================")
    for pred in results['price_predictions']:
        print(f"\n{pred['item']}:")
        print(f"  Current Price: ${pred['current_price']:.2f}")
        print(f"  Predicted Price: ${pred['predicted_price']:.2f}")
        print(f"  Difference: ${pred['price_difference']:.2f}")