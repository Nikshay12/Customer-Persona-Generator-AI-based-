import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess(file_path):
    df = pd.read_csv(file_path)
    # Encode categorical variables
    df = pd.get_dummies(df, columns=['gender','country'], drop_first=True)
    # Scale numeric features
    scaler = StandardScaler()
    df[['age','avg_session_time','features_used']] = scaler.fit_transform(
        df[['age','avg_session_time','features_used']]
    )
    return df
