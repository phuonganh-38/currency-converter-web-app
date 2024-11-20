import streamlit as st
import datetime

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output

# Display Streamlit App Title
st.title("FX Converter")

# Get the list of available currencies from Frankfurter
currencies = get_currencies_list()

# If the list of available currencies is None, display an error message in Streamlit App
if currencies is None:
    st.error('Can not get available currencies')

# Add input fields for capturing amount, from and to currencies
amount_input = st.number_input("Amount to be converted", min_value=float(0))

from_currency_input = st.selectbox(
    "From Currency",
    currencies)

to_currency_input = st.selectbox(
    "To Currency",
    currencies)

# Add a button to get and display the latest rate for selected currencies and amount
get_latest_rate_btn = st.button("Get Latest Rate", type="secondary")

# Add a date selector (calendar)
date_selector = st.date_input("Select date", max_value=datetime.datetime.now())

# Add a button to get and display the historical rate for selected date, currencies and amount
get_historical_rate_btn = st.button("Get Historical Rate", type="secondary")

st.subheader("Conversion Rate")

if get_latest_rate_btn:
    date, rate = get_latest_rates(from_currency_input, to_currency_input, amount_input)
    
    if date is None or rate is None:
        st.error("Error when getting rate")
    else:
        result = st.caption(format_output(
            date=date,
            from_currency=from_currency_input,
            to_currency=to_currency_input,
            rate=rate,
            amount=amount_input
            ))

if get_historical_rate_btn:
    rate = get_historical_rate(from_currency_input, to_currency_input, date_selector, amount_input)
    
    if rate is None:
        st.error("Error when getting rate")
    else:
        result = st.caption(format_output(
            date=date_selector,
            from_currency=from_currency_input,
            to_currency=to_currency_input,
            rate=rate,
            amount=amount_input
            ))







