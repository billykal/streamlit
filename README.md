# Car Price Prediction Streamlit App

This repository packages an end-to-end Streamlit experience for estimating the resale price of a car and exploring the dataset the model was trained on. The main app (`cars_app.py`) lets you describe a vehicle, predicts its market value with a pre-trained LightGBM model, and explains the key feature contributions with SHAP. A companion page under `pages/Insights.py` surfaces interactive Altair charts that summarise dataset trends.

## Features
- Interactive sidebar to describe manufacturer, drivetrain, fuel type, odometer value, and other attributes for the car you want to appraise.
- Real-time price prediction powered by a scikit-learn LightGBM regressor loaded from `model.pickle`.
- Local explanation of each prediction via SHAP value summaries along with a Plotly box-plot explorer of price ranges by manufacturer.
- Exploratory dashboards (Altair) highlighting counts, medians, and distributions across categorical and numeric vehicle attributes.

## Getting Started
1. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   The requirements pin specific versions of Streamlit, scikit-learn, LightGBM, SHAP, and Altair to match the serialized artifacts in this repo.

## Running the App
- Launch the prediction dashboard:
  ```bash
  streamlit run cars_app.py
  ```
- Streamlit automatically detects the `pages/` folder, so you can switch to **Insights** from the sidebar for the exploratory dashboards.

## Project Structure
- `cars_app.py` – main Streamlit interface for inference, SHAP explanations, and Plotly visualisations.
- `pages/Insights.py` – Altair-based exploratory data analysis page surfaced as a Streamlit multipage view.
- `dataset.pickle` – pre-processed dataset used for interactive visuals and mapping option lists for the sidebar inputs.
- `model.pickle` – trained LightGBM regressor used to produce price predictions.
- Additional pickled artifacts (`explainer.pickle`, `lgbm_cv.pickle`, `shap_values.pickle`) hold training-time objects that can support deeper investigations.
- `photo.jpeg` – splash image shown at the top of the main app.
