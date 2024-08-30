import streamlit as st

# Define the numeric and categorical columns
numeric_columns = [
    'income_annum', 
    'loan_amount', 
    'residential_assets_value', 
    'commercial_assets_value', 
    'luxury_assets_value', 
    'bank_asset_value'
]

categorical_columns = {
    'education': ['Graduate', 'Not Graduate'],
    'self_employed': ['Yes', 'No'],
    'loan_status': ['Approved', 'Rejected']
}

# Streamlit app title
st.title("Loan Application Input Form")

# Numeric inputs
st.header("Numeric Inputs")
numeric_inputs = {}
for col in numeric_columns:
    numeric_inputs[col] = st.number_input(f"Enter {col.replace('_', ' ').capitalize()}", value=0.0, step=0.01)

# Categorical inputs using radio buttons
st.header("Categorical Inputs")
categorical_inputs = {}
for col, options in categorical_columns.items():
    categorical_inputs[col] = st.radio(f"Select {col.replace('_', ' ').capitalize()}", options)

# Combine numeric and categorical inputs into a single dictionary
combined_inputs = {**numeric_inputs, **categorical_inputs}

# Display entered data
st.write("### Combined Data")
st.write(combined_inputs)

# Add a submit button
if st.button("Submit"):
    st.success("Data submitted successfully!")
    st.write("Submitted Data:", combined_inputs)
