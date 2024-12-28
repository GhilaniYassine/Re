# Fashion Image Search Using CLIP Embeddings

## Overview
This project is a learning exercise to understand and implement multimodal embeddings using OpenAI's CLIP (Contrastive Language-Image Pre-Training) model. It allows users to search for fashion images using natural language queries.

## Technology Stack
- **Streamlit**: Web interface
- **Haystack**: Document store and retrieval pipeline
- **CLIP**: Text-to-image embedding model (sentence-transformers/clip-ViT-B-32)
- **Python**: Programming language

## How It Works
The application uses CLIP embeddings to:
1. Convert fashion images into vector embeddings
2. Transform text queries into the same vector space
3. Find similarities between text queries and images
4. Return the most 3 relevant images based on the query

## Installation
```bash
pip install -r requirements.txt