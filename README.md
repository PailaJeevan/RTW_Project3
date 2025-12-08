# 🌦️ Real-Time Weather Information & Data Logger  
A Python application that fetches **live weather data**, displays it to the user, and stores it in a **CSV log file** with timestamps.

## 📁 Project Structure
```
.
├── main.py
├── Data.py
├── Storage.py
└── weather_data.csv  (auto-generated)
```

## 🚀 Features

### ✔️ Fetch Live Weather Data  
Uses OpenWeatherMap API to retrieve:
- Temperature  
- Feels like  
- Humidity  
- Weather condition  
- Wind speed  

### ✔️ Input-Based Data Retrieval  
User enters a city name, the system fetches real-time weather.

### ✔️ Error Handling  
Handles:
- Invalid city (404)  
- Invalid API key (401)  
- Rate limit exceeded (429)  
- Server errors (500)  

### ✔️ CSV Logging with Timestamp  
Automatically stores data in **weather_data.csv** including:
- Timestamp  
- City & Country  
- Temperature  
- Feels like  
- Humidity  
- Condition  
- Wind speed  

### ✔️ Auto-Create CSV File  
If `weather_data.csv` doesn’t exist, the program generates it with headers.

## 🧠 How the Application Works

### 1️⃣ **User Input**
The app asks for a city name.

### 2️⃣ **Weather Fetching**
`Weather.weather_info(city)` sends a GET request to OpenWeather API.

### 3️⃣ **Display Results**
The system prints detailed weather results in the console.

### 4️⃣ **Store Data**
`logging.store_weather_data(city)` logs the data into a CSV file.

## 📦 Requirements

- Python 3.x  
- `requests` library  
  ```
  pip install requests
  ```
- OpenWeatherMap API Key (already included in your code)

## ▶️ How to Run

1. Save all project files in the same folder.
2. Run the application:

```
python main.py
```

3. Enter any city name when prompted.

## 📝 Example Output

```
Weather in Hyderabad:
 Temperature: 29°C
 Feels Like: 31°C
 Condition: Clear sky
 Humidity: 45%
 Wind Speed: 3 m/s
```

Weather data is then saved inside:  
```
weather_data.csv
```

---

## 🧱 OOP Structure

### **Weather Class**
Handles:
- API call  
- Validating response  
- Displaying weather details  

### **logging Class**
Handles:
- Writing data to CSV  
- Adding header on first run  

### **main() Function**
Coordinates input and class interactions.

---
## 🔮 Future Improvements

- GUI using Tkinter or PyQt  
- Convert CSV logs into charts  
- Add weekly/weekly forecast  
- Error-based retry mechanism  
- Use `.env` to hide API key

---

## 👨‍💻 Author  
**Paila Jeevan** 

---
## 📩 Contact

- 👨‍💻 **Developer:** Paila Jeevan
- 📧 **Email:** pailajeevan21@gmail.com
- 🌐 **GitHub:**
https://github.com/PailaJeevan

---

## 📜 License

- **License:** MIT License — see the `LICENSE` file at the project root for full terms.
