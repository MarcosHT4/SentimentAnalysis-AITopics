ANALYSIS_PROMPT = """You are an NLP AI model, and you are asked to analyze the following text:{text}
    Your job is to output a very simplified representation of the analysis, with the following results:
    1. Part of speech tagging
    2. Named entity recognition
    The analysis should be done in spanish language, using the {format_instructions}
    The analysis is not expected to be perfect as it is a difficult task that should be done by an NLP tool, 
    such as Spacy or NLTK."""