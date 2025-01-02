from anthropic import Anthropic
import pandas as pd
from tqdm import tqdm
import time

def call_ai(df, api_key, model="claude-3-5-haiku-20241022", system_prompt="You are a helpful AI assistant.", 
                       input_column='pre_llm_input',output_column='ai_response', max_retries=3, sleep_time=1):
    """
    Process texts through Claude and append responses to dataframe
    
    Args:
        df (pd.DataFrame): Input dataframe
        api_key (str): Anthropic API key
        system_prompt (str): System prompt for Claude
        input_column (str): Column containing texts to process
        max_retries (int): Maximum number of API call retries
        sleep_time (int): Seconds to wait between retries
    
    Returns:
        pd.DataFrame: Original dataframe with new 'claude_response' column
    """
    client = Anthropic(api_key=api_key)
    responses = []
    
    for text in tqdm(df[input_column]):
        for attempt in range(max_retries):
            try:
                response = client.messages.create(
                    model=model,
                    max_tokens=1000,
                    system=system_prompt,
                    messages=[
                        {"role": "user", "content": text}
                    ]
                )
                responses.append(response.content[0].text)
                break
            except Exception as e:
                if attempt == max_retries - 1:
                    print(f"Failed after {max_retries} attempts: {e}")
                    responses.append("Error: API call failed")
                else:
                    time.sleep(sleep_time)
                    continue
    
    df[output_column] = responses
    return df
