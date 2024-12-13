# Restaurant Price Analyzer

A Python application that analyzes and predicts restaurant prices based on local competition, weather conditions, and busy times. The application focuses on "Village The Soul of India" restaurant in Hicksville and compares its prices with nearby restaurants.

## Features

1. **Restaurant Data Analysis**
   - Restaurant details (name, address, contact info)
   - Menu items and prices
   - Comparison with nearby restaurants

2. **Environmental Factors**
   - Weather conditions (temperature, precipitation)
   - Restaurant busy times
   - Local competition analysis

3. **Price Prediction**
   - ML-based price adjustments
   - Factors considered:
     - Temperature < 45°F
     - Rain or snow conditions
     - Restaurant busy status
   - Competitive price analysis

## Project Structure

```
restaurant_analyzer/
├── restaurant_analyzer.py  # Main analysis script
├── mock_data.py           # Mock data for testing
├── requirements.txt       # Python dependencies
├── results.html          # Web-based results display
└── data.json            # Generated analysis results
```

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd restaurant-analyzer
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the analyzer:
```bash
python restaurant_analyzer.py
```

2. View results:
   - Check console output for immediate results
   - Open `results.html` in a web browser for detailed visualization
   - Review `data.json` for raw data

## Price Prediction Logic

The application predicts prices based on the following rules:
- If temperature < 45°F AND (it's raining OR restaurant is busy):
  - Price = Lowest local price * 1.15 (15% markup)
- Otherwise:
  - Price = Lowest local price

## Sample Output

The application provides:
1. Current restaurant details
2. Weather conditions
3. Restaurant busy status
4. Price predictions for each menu item:
   - Current price
   - Predicted price
   - Price difference

## Dependencies

- scikit-learn: Machine learning functionality
- pandas: Data manipulation
- numpy: Numerical computations

## Development

This project uses mock data for demonstration purposes. In a production environment, you would need to:
1. Replace mock_data.py with actual API integrations
2. Add proper error handling
3. Implement data caching
4. Add user authentication
5. Set up a proper database

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## Top Rated Restaurants Near Village the Soul of India 🍽️

This is Top 5 list of excellent dining options near Village the Soul of India from Yelp.

## Featured Restaurants

### 1. Village the Soul of India ⭐⭐⭐⭐½
- Rating: 4.5/5 (47 reviews)
- Address: 217 Bethpage Road, Hicksville, NY 11801
- Hours: Closed until 11:30 AM
- Cuisine: South Indian
- Specialties: Authentic South Indian cuisine
- Tags: Indian, Casual, Ethnic

#### Popular Menu Items
- Dosa varieties
- South Indian Thali
- Idli and Vada
- Curry dishes
- Biryani

#### Restaurant Details
- 🏠 Location: Hidden gem in Hicksville
- 🍽️ Dining Style: Casual dining
- 🚗 Parking: Available
- 💳 Price Range: $$
- 👥 Good For: Lunch, Dinner, Groups
- 🌶️ Specializes in authentic South Indian cuisine

### 2. Smartwich Sandwich Shop ⭐⭐⭐⭐½
- Rating: 4.5/5 (89 reviews)
- Closing Time: 11:00 AM
- Cuisine: Sandwiches
- Location: Middle of Long Island
- Known for: Creative sandwich combinations

### 3. Milas and Planchas ⭐⭐⭐⭐½
- Rating: 4.5/5 (4 reviews)
- Closing Time: 5:00 PM
- Cuisine: Mexican
- Location: Across the parking garage
- Known for: Authentic Mexican food

### 4. Uncle Don's Kitchen ⭐⭐⭐⭐½
- Rating: 4.5/5 (133 reviews)
- Closing Time: 11:30 AM
- Cuisine: Caribbean
- Specialties: Slow Chicken and Roti Curry Chicken dinner
- Tags: Caribbean, Casual, Ethnic

### 5. Chicken Gyro Galaxy ⭐⭐⭐⭐½
- Rating: 4.5/5 (13 reviews)
- Closing Time: 11:00 AM
- Cuisine: Mediterranean
- Known for: Generous portions and excellent value
- Tags: Seafood, Sandwiches, Greek

## Transportation Tips
- All restaurants are within walking distance of each other
- Ample parking available
- Public transportation accessible

## Additional Information
- Best to check current operating hours
- Some locations offer takeout and delivery
- Call ahead for large group reservations

*Note: Ratings and operating hours may vary. It's recommended to check directly with restaurants for current information.*