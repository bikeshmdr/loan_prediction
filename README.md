<h1>Dataset Source</h1>
    <p>This dataset is sourced from <a href =https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset>kaggle.com<a>

<h1>Data Cleaning</h1>
    <ol>
        <li>Firstly presence of null value is checked in the dataset.<br>
            <p>
            <img src= "documentation\images\data_cleaning\null_check.png" alt = "Null value checking" width = "500"><br>
            Then, during feature selection error occurred as visualized below the colum names contained prefix white space which was removed using string strip<br>
            <img src= "documentation\images\data_cleaning\column_index.png" alt = "Column name checking" width = "500">
            </p>
        </li>
        <li>Normality Test</li>
            <ul>
                <li>Normality Test for Numeric features
                    <p>
                    Firstly, Numeric features of the dataset were separated then skewness of numeric features were calculated with is observed to be in the valid skewness range of [-1, 1]<br>
                    <img src= "documentation\images\data_cleaning\numeric_skewness.png" alt = "Skewness of numeric features" width = "500">
                    </p>
                </li>
                <li>Normality Test for Categorical features<br>
                    <p>Then, unique values of the remaining categorical features were identified resulting two values of each categorical features as shown below.<br>
                    <img src= "documentation\images\data_cleaning\unique_categorical_data.png" alt = "Unique data of categorical features" width = "500"><br>
                    So, Label encoding was performed and stored in a different dataframe as not to encode data during cleaning process. Then the skewness of the categorical data was also performed which is also observed to be in appropriate skewness range as shown below.<br>
                    <img src= "documentation\images\data_cleaning\categorical_skewness.png" alt = "Skewness fo categorical features" width = "500">
                    </p>
                    </li>
            </ul>
            <p>Since the downloaded dataset doesnot have any null value and dataset is also in normal distribution form <b>so except column striping</b> no any modification was performed during data cleaning.</p>
    </ol>

<h1>Model Training</h1>
    <ol>
        <li>After loading dataset, label encoding is performed for the categorical features.</li>
        <li>Features correlation is calculated and visualized as.<br>
            <img src= "documentation\images\model_training\correlation_matrix.png" alt = "Heatmap of Correlation matrix" width = "500"><br>
            <p>From above correlation matrix high correlation is observed between multiple features listed below:</p>
            <ul>
                <li>income_annum</li>
                <li>loan_amount</li>
                <li>cibil_score</li>
                <li>residential_asset_value</li>
                <li>commercial_asset_value</li>
                <li>luxury_asset_value</li>
                <li>bank_asset_value</li>
            </ul>
            <p>So, in order to reduce the problem of multicollinearity problem, feature engineering is performed.</p>
        </li>
        <li>Feature Engineering</li>
            <ul>
                <li>Similar features like <b>residential_asset_value, commerical_asset_value, luxury_asset_value, bank_asset_value</b> were merged together into <b>total_asset_value</b></li>
                <li>New features addition utilizing existing features</li>
                <ul>
                    <li>income_to_loan_ratio</li>
                    <li>asset_to_loan_ratio</li>
                </ul>
            </ul>
        <li>Normality test<br>
            <p>Skewness is calculated to check for entire features and the dataset is observed to be in feasible range of skewness[-1,1] for normal distribution.<br>
            <img src= "documentation\images\model_training\normality_test.png" alt = "Normality test" width = "500">
            </p>
        </li>
        <li>Standardization
            <p>Standardization is performed to <b>all the numeric features</b> to bring all the features in same scale.</p>
        </li>
        <li>The trained model is listed below</li>
            <ul>
                <li>Logistic Regression</li>
                <li>Logistic Regression with L2 Regularization</li>
                <li>Decision Tree Classifier</li>
                <li>Random Forest Classifier</li>
                <li>Gaussian Naive Bayes</li>
            </UL>
    </ol>

<h1>Model Comparison</h1>
    <p>Various evaluation parameters were used to evaluate the models as shown below.<br>
    <img src = "documentation\loan_prediction.png" alt = "Model evaluation" width = "500">
    </p>

<h1>Model Deployment</h1>
<p>The link to streamlit code is <a href =https://github.com/bikeshmdr/load_predection_deployment.git>github.com<a></p>
<p>The deployed link for streamlit is <a href =https://sheqzxxqwqixwp9sz4gwcc.streamlit.app>streamlit.io<a></p>

<h1>Demo</h1>
    <p>
        https://github.com/user-attachments/assets/a5a26d32-9959-44dd-b8bc-72cf08c1ee6d
    </p>
