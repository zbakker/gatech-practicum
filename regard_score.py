import pandas as pd
from regard import Regard

def calculate_regard_scores(df, text_col, comparison_col=None):
    # Initialize the regard metric
    regard_metric = Regard()
    regard_metric._download_and_prepare(None)
    
    # Convert column to list
    text_list = df[text_col].tolist()
    
    # Calculate regard scores
    if comparison_col:
        comparison_list = df[comparison_col].tolist()
        results = regard_metric._compute(data=text_list, references=comparison_list)
    else:
        results = regard_metric._compute(data=text_list)
    
    # Create a list to store the scores
    scores_list = []
    for d in results['regard']:
        scores_dict = {l['label']: round(l['score'], 2) for l in d}
        scores_list.append(scores_dict)
    
    # Convert scores to DataFrame
    scores_df = pd.DataFrame(scores_list)
    
    # Add prefix to score columns to avoid confusion
    scores_df = scores_df.add_prefix('regard_')
    
    # Reset index to ensure proper merging
    return pd.concat([df.reset_index(drop=True), scores_df.reset_index(drop=True)], axis=1)

def calculate_regard_differential(df):
    """
    Calculate regard differential (positive - negative) for each AI response and control.
    
    Args:
        df (pandas.DataFrame): DataFrame containing AI responses and regard scores
    
    Returns:
        pandas.DataFrame: Original DataFrame with new regard differential columns
    """
    # Calculate differential for each response (0-3) and control
    for i in range(4):
        # Calculate regard scores for current response
        temp_df = calculate_regard_scores(df, f'ai_response_{i}')
        
        # Calculate differential and add to original dataframe
        df[f'regard_differential_{i}'] = temp_df['regard_positive'] - temp_df['regard_negative']
    
    # Calculate differential for control
    temp_df = calculate_regard_scores(df, 'ai_response_control')
    df['regard_differential_control'] = temp_df['regard_positive'] - temp_df['regard_negative']
    
    return df
