# Changelog

## 2024-07-09 16:00:00
### Changes:
- Replaced Gemini API with OpenRouter API integration
- Added support for specifying different models in the request
- Updated error handling for OpenRouter API responses
- Created new OpenRouter implementation class

### Components affected:
- ai/openrouter.py (new)
- main.py

## 2024-07-09 15:45:00
### Changes:
- Updated Gemini model from preview version "gemini-2.5-flash-preview-05-20" to more widely available "gemini-1.5-pro"
- Added proper error handling for API calls in the chat endpoint
- Added specific exception handling for permission denied errors

### Components affected:
- ai/gemini.py
- main.py 