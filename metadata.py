def generate_metadata(text: str, analysis: dict) -> dict:
    """Generate metadata from text and analysis results."""
    lines = text.split('\n')
    title = lines[0].strip() if lines else 'Unknown'
    author = next((ent[0] for ent in analysis['entities'] if ent[1] == 'PERSON'), 'Unknown')
    date = next((ent[0] for ent in analysis['entities'] if ent[1] == 'DATE'), 'Unknown')
    keywords = analysis['keywords']
    summary = ' '.join(text.split()[:100]) + '...' if text else 'No summary available'
    return {
        'title': title,
        'author': author,
        'date': date,
        'keywords': keywords,
        'summary': summary
    }