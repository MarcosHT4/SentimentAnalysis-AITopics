SENTIMENT_PROMPT = """ You are an NLP AI model, and you are asked to analyze the sentiment of the following text:{text}
    Your job is to output an analysis of the sentiment of the text, using a float number between -1 and 1, -1 being 
    the most negative sentiment and 1 being the most positive sentiment. The analysis should be done in spanish language.
    Also you must categorize the sentiment in one of the following categories, using the same float number:
    1. Muy Negativo
    2. Negativo
    3. Poco Negativo
    4. Neutral
    5. Poco Positivo
    6. Positivo
    7. Muy Positivo
    You must use the {format_instructions} to format the output.
"""