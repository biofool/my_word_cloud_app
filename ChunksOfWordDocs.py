from bs4 import BeautifulSoup
import requests


def split_google_doc_content(url, chunk_size):
    """
    Splits a published Google Doc's content into chunks based on the number of paragraphs.

    Args:
    - url (str): The URL of the published Google Doc.
    - chunk_size (int): The number of paragraphs per chunk.

    Returns:
    - List of BeautifulSoup objects, each representing a chunk.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Google Docs uses multiple tags for paragraphs, including <p> and <span>
    paragraphs = soup.find_all(['p', 'span'], class_='c4')

    chunks = []
    for i in range(0, len(paragraphs), chunk_size):
        chunk = BeautifulSoup('<root></root>', 'html.parser')
        for para in paragraphs[i:i + chunk_size]:
            chunk.root.append(para)
        chunks.append(chunk)

    return chunks


# Example Usage:
url = "https://docs.google.com/document/d/e/2PACX-1vTCI9J8wv2GbLICKKTsVmVVTn0D4QM63nMjSgU0i03Jgj34-9UgrDe-521qCfiFxCQdxsiuGZLof71M/pub"
chunk_size = 500  # Adjust this based on your needs
chunks = split_google_doc_content(url, chunk_size)

# Save the chunks to separate files
for i, chunk in enumerate(chunks):
    with open(f"chunk_{i + 1}.html", 'w', encoding='utf-8') as file:
        file.write(str(chunk))
