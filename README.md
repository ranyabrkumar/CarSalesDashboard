# 🚗 Car Sales Dashboard

An interactive **Streamlit dashboard** for analyzing car sales data using visual charts and metrics. This application helps explore sales trends, compare manufacturers, and understand performance using multiple chart types.

---

## 📊 Features

### 🔹 Interactive Visualizations
- **Top Selling Car Models (Bar Chart)**
- **Sales Trend Over Launch Years (Line Chart)**
- **Market Share by Manufacturer (Pie Chart)**
- **Sales Distribution (Histogram)**
- **Scatter Plot: Sales vs Launch Year**
- **Correlation Heatmap**
- **Dynamic Filters** for Manufacturer & Vehicle Type

### 🔹 Data Preprocessing
- Clean missing values
- Convert launch dates to year format
- Aggregate and summarize sales

---

## 📁 Project Structure

```
CarSalesDashboard/
│
├── CarAnalysis.py            # Main Streamlit dashboard
├── README.md                 # Project documentation
├── requirements.txt          # Project dependencies
└── Project1/
    └── data/
        └── Car_sales.csv     # Dataset file
```

---

## 📦 Installation

Install all required dependencies:

```bash
pip install -r requirements.txt
```

If you need a base requirements file, use:

```
streamlit
pandas
matplotlib
seaborn
numpy
```

---

## ▶️ Running the Dashboard

### **Windows**
```bash
streamlit.exe run CarAnalysis.py
```

### **macOS / Linux**
```bash
streamlit run CarAnalysis.py
```

Your browser will open automatically at:
```
http://localhost:8501
```

<img width="2214" height="1362" alt="image" src="https://github.com/user-attachments/assets/acd45c6a-880e-4c77-8e2e-f6c955fc056f" />


---

## 🛠️ Technologies Used
- Python
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- NumPy

---

## 📈 Insights You Can Gain
- Identify best-selling models
- Compare manufacturer performance
- Evaluate distribution and correlation of key metrics
- Understand annual sales patterns

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to fork the repo and submit PRs.

---

## 📜 License
This project is licensed under the **MIT License**.

