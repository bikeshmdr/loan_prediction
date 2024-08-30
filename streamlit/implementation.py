import streamlit as st
import joblib
import pandas as pd

# loading the pretrained model
loaded_rf_clf = joblib.load('random_forest_classifier.pkl')
# Standardizing all numeric features
scaler = joblib.load('scaler.pkl')

def main():
    # Define the numeric and categorical columns
    initial_numeric_columns = [
        'no_of_dependents', 
        'loan_term', 
        'cibil_score',
        'income_annum', 
        'loan_amount', 
        'residential_assets_value', 
        'commercial_assets_value', 
        'luxury_assets_value', 
        'bank_asset_value'
    ]

    categorical_columns = {
        'education': ['Graduate', 'Not Graduate'],
        'self_employed': ['Yes', 'No']
    }

    # Streamlit app title
    st.title("Loan Application Input Form")

    # Numeric inputs
    st.header("Numeric Inputs")
    numeric_inputs = {}
    for col in initial_numeric_columns:
        numeric_inputs[col] = st.number_input(f"Enter {col.replace('_', ' ').capitalize()}", value=0.0, step=0.01)

    # Categorical inputs using radio buttons
    st.header("Categorical Inputs")
    categorical_inputs = {}
    for col, options in categorical_columns.items():
        categorical_inputs[col] = st.radio(f"Select {col.replace('_', ' ').capitalize()}", options)

    # Combine numeric and categorical inputs into a single dictionary
    combined_inputs = {**numeric_inputs, **categorical_inputs}

    # Add a submit button
    if st.button("Submit"):
        st.write("Information Submitted")
        # Encode categorical inputs manually
        combined_inputs['education'] = 0 if combined_inputs['education'] == 'Graduate' else 1
        combined_inputs['self_employed'] = 0 if combined_inputs['self_employed'] == 'Yes' else 1

        # Feature engineering
        combined_inputs['total_assets_value'] = (
            combined_inputs['residential_assets_value'] + 
            combined_inputs['commercial_assets_value'] + 
            combined_inputs['luxury_assets_value'] + 
            combined_inputs['bank_asset_value']
        )
        combined_inputs['income_to_loan_ratio'] = combined_inputs['income_annum'] / combined_inputs['loan_amount'] if combined_inputs['loan_amount'] != 0 else 0
        combined_inputs['assets_to_loan_ratio'] = combined_inputs['total_assets_value'] / combined_inputs['loan_amount'] if combined_inputs['loan_amount'] != 0 else 0

        # Updated numeric columns after feature engineering
        numeric_columns = ['no_of_dependents', 'income_annum', 'loan_amount', 'loan_term', 'cibil_score','total_assets_value', 'income_to_loan_ratio', 'assets_to_loan_ratio']
        
        # Convert combined_inputs to a DataFrame for standardization
        combined_df = pd.DataFrame([combined_inputs])
        
        # Separate numeric features for standardization
        numeric_df = combined_df[numeric_columns]
        
        #scaler = joblib.load('streamlit/model/scaler.pkl')

        standardized_numeric_values = scaler.transform(numeric_df)
        # Update the combined_inputs dictionary with standardized numeric values
        for i, col in enumerate(numeric_columns):
            combined_inputs[col] = standardized_numeric_values[0, i]  # Use 0 to access the first (and only) row
        
        
        # Sort combined_inputs dictionary by keys
        sorted_combined_inputs = dict(sorted(combined_inputs.items()))
        # Convert sorted_combined_inputs to DataFrame with the same columns as used in training
        
        input_df = pd.DataFrame([sorted_combined_inputs])
        input_df = input_df.drop(columns=['bank_asset_value',
                                'commercial_assets_value',
                                'luxury_assets_value',
                                'residential_assets_value'], axis=1)
        # Load the pre-trained model and make prediction
        
        #loaded_rf_clf = joblib.load('streamlit/model/random_forest_classifier.pkl')

        prediction = loaded_rf_clf.predict(input_df)

        # Show prediction result
        if prediction < 0.5:
            st.write("Loan Approved")
        else:
            st.write("Loan Denied")

if __name__ == "__main__":
    main()