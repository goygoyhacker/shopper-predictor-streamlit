import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("best_model_online_shoppers.pkl")

st.set_page_config(page_title="Shopper Predictor", layout="centered")

st.title("Online Shopper Purchase Predictor")
st.write("Enter the shopping session details below.")

def field_help(definition, example):
    st.caption(f"**Definition:** {definition}")
    st.caption(f"**Input hint:** {example}")

# 1
st.subheader("1. Account or Site Utility Pages Visited")
field_help(
    "This means the number of non-shopping pages the visitor opened, such as account pages, login pages, profile pages, settings pages, or other general website pages that are not mainly for viewing products. (Input only the number of pages)",
    "Example: 3"
)
administrative = st.number_input("", min_value=0, value=0, step=1, key="administrative")

# 2
st.subheader("2. Time Spent on Account or Site Utility Pages")
field_help(
    "This means the total time the visitor spent on those non-shopping pages, such as login, account, settings, or similar website utility pages. (Enter only the number of seconds)",
    "Example: 45"
)
administrative_duration = st.number_input("", min_value=0, value=0, step=1, key="administrative_duration")

# 3
st.subheader("3. Help or Information Pages Visited")
field_help(
    "This means the number of information pages the visitor opened, such as Help, FAQ, About Us, customer support, shipping information, or return policy pages. (Input only the number of pages)",
    "Example: 2"
)
informational = st.number_input("", min_value=0, value=0, step=1, key="informational")

# 4
st.subheader("4. Time Spent on Help or Information Pages")
field_help(
    "This means the total time the visitor spent reading help or information pages, such as FAQ, About Us, support, shipping, or return policy pages. (Enter only the number of seconds)",
    "Example: 30"
)
informational_duration = st.number_input("", min_value=0, value=0, step=1, key="informational_duration")

# 5
st.subheader("5. Product Pages Visited")
field_help(
    "This means the number of shopping or product pages the visitor opened, such as product listings, item details, or pages directly related to products being sold. (Input only the number of pages)",
    "Example: 25"
)
product_related = st.number_input("", min_value=0, value=0, step=1, key="product_related")

# 6
st.subheader("6. Time Spent on Product Pages")
field_help(
    "This means the total time the visitor spent viewing product-related pages, such as product listings, item details, and product information pages. (Enter only the number of seconds)",
    "Example: 850"
)
product_related_duration = st.number_input("", min_value=0, value=0, step=1, key="product_related_duration")

# 7
st.subheader("7. Single-Page Leave Rate")
field_help(
    "This shows how often visitors leave the website after viewing only one page. A higher value means people often leave immediately without exploring more pages. (Enter only the numeric rate value)",
    "Example: 0.02"
)
bounce_rates = st.number_input("", min_value=0.0, value=0.0, format="%.4f", key="bounce_rates")

# 8
st.subheader("8. Last-Page Exit Rate")
field_help(
    "This shows how often a page is the last page visited before the visitor leaves the website. A higher value means many visitors end their session on that page. (Enter only the numeric rate value)",
    "Example: 0.05"
)
exit_rates = st.number_input("", min_value=0.0, value=0.0, format="%.4f", key="exit_rates")

# 9
st.subheader("9. Estimated Purchase Value of Visited Pages")
field_help(
    "This is the estimated value of the pages visited in helping lead to a purchase. A higher value suggests the session was more related to buying activity. (Enter only the numeric value)",
    "Example: 12"
)
page_values = st.number_input("", min_value=0.0, value=0.0, format="%.2f", key="page_values")

# 10
st.subheader("10. Closeness to a Special Shopping Day")
field_help(
    "This shows how close the visit date is to a special shopping occasion, such as Valentine’s Day, Mother’s Day, or another important shopping day. A value closer to 1 means it is very near that special day. (Enter only the numeric value from 0 to 1)",
    "Example: 0.40"
)
special_day = st.number_input("", min_value=0.0, max_value=1.0, value=0.0, format="%.2f", key="special_day")

# 11
st.subheader("11. Month of Visit")
st.caption("**Definition:** This indicates the month when the shopping session happened. (Select only one month)")
month_display = st.selectbox(
    "",
    [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ],
    key="month_display"
)

month_map = {
    "January": "Jan",
    "February": "Feb",
    "March": "Mar",
    "April": "Apr",
    "May": "May",
    "June": "June",
    "July": "Jul",
    "August": "Aug",
    "September": "Sep",
    "October": "Oct",
    "November": "Nov",
    "December": "Dec"
}
month = month_map[month_display]

# 12
st.subheader("12. Visitor Device Operating System")
st.caption("**Definition:** This indicates the type of operating system used by the visitor’s device during the session. (Select the operating system category that best matches the visitor’s device)")
os_display = st.selectbox(
    "",
    [
        "Windows / Desktop OS",
        "MacOS / Apple Desktop",
        "Android Mobile",
        "iPhone / iOS",
        "Linux / Other Desktop",
        "Tablet Device",
        "Smart Device / Embedded",
        "Other / Unknown"
    ],
    key="os_display"
)

os_map = {
    "Windows / Desktop OS": 1,
    "MacOS / Apple Desktop": 2,
    "Android Mobile": 3,
    "iPhone / iOS": 4,
    "Linux / Other Desktop": 5,
    "Tablet Device": 6,
    "Smart Device / Embedded": 7,
    "Other / Unknown": 8
}
operating_systems = os_map[os_display]

# 13
st.subheader("13. Visitor Web Browser")
st.caption("**Definition:** This indicates the browser used by the visitor to access the shopping website. (Select the browser category that best matches the visitor’s browser)")
browser_display = st.selectbox(
    "",
    [
        "Chrome",
        "Firefox",
        "Safari",
        "Edge",
        "Opera",
        "Samsung Internet",
        "Internet Explorer",
        "Mobile Browser",
        "In-App Browser",
        "Privacy Browser",
        "Chromium-Based Other",
        "Legacy Browser",
        "Other / Unknown"
    ],
    key="browser_display"
)

browser_map = {
    "Chrome": 1,
    "Firefox": 2,
    "Safari": 3,
    "Edge": 4,
    "Opera": 5,
    "Samsung Internet": 6,
    "Internet Explorer": 7,
    "Mobile Browser": 8,
    "In-App Browser": 9,
    "Privacy Browser": 10,
    "Chromium-Based Other": 11,
    "Legacy Browser": 12,
    "Other / Unknown": 13
}
browser = browser_map[browser_display]

# 14
st.subheader("14. Website Traffic Source Type")
st.caption("**Definition:** This indicates how the visitor reached the website, such as direct visit, search, referral, or campaign source. (Select the traffic source category that best matches the visit)")
traffic_display = st.selectbox(
    "",
    [
        "Direct Visit",
        "Search Engine",
        "Social Media",
        "Referral Link",
        "Email Campaign",
        "Paid Advertisement",
        "Affiliate Link",
        "Shopping Campaign",
        "Display Ad",
        "Organic Search",
        "Partner Website",
        "Internal Promotion",
        "Messaging App Link",
        "Video Platform Link",
        "Marketplace Link",
        "Blog or Article Link",
        "Mobile App Redirect",
        "Notification Link",
        "Retargeting Campaign",
        "Other / Unknown"
    ],
    key="traffic_display"
)

traffic_map = {
    "Direct Visit": 1,
    "Search Engine": 2,
    "Social Media": 3,
    "Referral Link": 4,
    "Email Campaign": 5,
    "Paid Advertisement": 6,
    "Affiliate Link": 7,
    "Shopping Campaign": 8,
    "Display Ad": 9,
    "Organic Search": 10,
    "Partner Website": 11,
    "Internal Promotion": 12,
    "Messaging App Link": 13,
    "Video Platform Link": 14,
    "Marketplace Link": 15,
    "Blog or Article Link": 16,
    "Mobile App Redirect": 17,
    "Notification Link": 18,
    "Retargeting Campaign": 19,
    "Other / Unknown": 20
}
traffic_type = traffic_map[traffic_display]

# 15
st.subheader("15. Type of Visitor")
st.caption("**Definition:** This indicates whether the visitor has visited the website before or is visiting for the first time. (Select only one visitor type)")
visitor_display = st.selectbox(
    "",
    ["Returning Visitor", "New Visitor", "Other / Unknown"],
    key="visitor_display"
)

visitor_map = {
    "Returning Visitor": "Returning_Visitor",
    "New Visitor": "New_Visitor",
    "Other / Unknown": "Other"
}
visitor_type = visitor_map[visitor_display]

# 16
st.subheader("16. Weekend Visit Status")
st.caption("**Definition:** This indicates whether the shopping session happened on a weekend or not. (Select only one option)")
weekend_display = st.selectbox(
    "",
    ["Yes, Weekend Session", "No, Weekday Session"],
    key="weekend_display"
)

weekend_map = {
    "Yes, Weekend Session": True,
    "No, Weekday Session": False
}
weekend = weekend_map[weekend_display]

def get_recommendation(prediction):
    if prediction == 1:
        return "Prioritize this customer with checkout assistance, promotional reminders, or product suggestions."
    return "Provide standard browsing assistance and avoid high-priority intervention."

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "Administrative": int(administrative),
        "Administrative_Duration": int(administrative_duration),
        "Informational": int(informational),
        "Informational_Duration": int(informational_duration),
        "ProductRelated": int(product_related),
        "ProductRelated_Duration": int(product_related_duration),
        "BounceRates": float(bounce_rates),
        "ExitRates": float(exit_rates),
        "PageValues": float(page_values),
        "SpecialDay": float(special_day),
        "Month": month,
        "OperatingSystems": int(operating_systems),
        "Browser": int(browser),
        "Region": 1,
        "TrafficType": int(traffic_type),
        "VisitorType": visitor_type,
        "Weekend": weekend
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    st.write("Purchase probability:", round(float(probability), 4))

    result = "Purchase" if prediction == 1 else "No Purchase"

    st.subheader("Prediction Result")
    st.write(f"**Output:** {result}")

    st.subheader("Confidence Score")
    st.write(f"**Output hint:** {probability * 100:.2f}%")

    st.subheader("Recommendation")
    st.write(f"**Output:** {get_recommendation(prediction)}")