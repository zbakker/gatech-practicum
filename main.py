import pandas as pd
import numpy as np
from typing import Union, List
from regard_score import calculate_regard_scores, calculate_regard_differential

def analyze_regard(texts: Union[str, List[str], pd.Series]) -> pd.DataFrame:
    """
    Calculate regard scores and differentials for input text(s).
    
    Args:
        texts: Input text(s) to analyze. Can be:
            - Single string
            - List of strings
            - Pandas Series containing strings
    
    Returns:
        pandas.DataFrame: DataFrame containing the input texts and their regard scores/differentials
    """
    # Convert input to DataFrame
    if isinstance(texts, str):
        df = pd.DataFrame({'text': [texts]})
    elif isinstance(texts, list):
        df = pd.DataFrame({'text': texts})
    elif isinstance(texts, pd.Series):
        df = pd.DataFrame({'text': texts})
    else:
        raise ValueError("Input must be a string, list of strings, or pandas Series")

    # Calculate regard scores
    scores_df = calculate_regard_scores(df, 'text')
    
    # Calculate differential (positive - negative)
    scores_df['regard_differential'] = scores_df['regard_positive'] - scores_df['regard_negative']
    
    return scores_df


if __name__ == "__main__":

    # Submit your prompts as a list of strings
    texts = [
        "Sarah is a brilliant scientist leading groundbreaking research.",
        "The team worked efficiently to complete the project."
    ]
    result = analyze_regard(texts)
    print("\nMultiple texts analysis:")
    print(result[['text', 'regard_positive', 'regard_negative', 'regard_differential']])
