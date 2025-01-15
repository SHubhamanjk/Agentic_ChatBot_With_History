# Conversational AI with LangChain and Groq

This project demonstrates a Streamlit-based chatbot application powered by LangChain and Groq, utilizing tools like Wikipedia and Arxiv for enriched conversational capabilities.

## Features
- **Conversational Interface:** Interactive chat functionality with a user-friendly Streamlit interface.
- **Knowledge Tools:** Leverages Wikipedia and Arxiv APIs to fetch relevant information for user queries.
- **LLM Integration:** Powered by Groq's `gemma2-9b-it` large language model for advanced responses.
- **Session History:** Retains chat history within the session for contextual conversations.

## Setup
### Prerequisites
1. Python 3.8+
2. Streamlit
3. LangChain
4. Groq API key

### Installation
1. Clone this repository:
   ```bash
   git clone <https://github.com/SHubhamanjk/Agentic_ChatBot_With_History>
   cd <repository_directory>
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root and add your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Running the Application
Start the Streamlit application with the following command:
```bash
streamlit run app.py
```

## Usage
1. Open the Streamlit app in your browser (default: `http://localhost:8501`).
2. Interact with the chatbot by typing your queries in the input box.
3. View the assistant's responses, which may include insights from Wikipedia and Arxiv.

## Project Structure
- `app.py`: Main application script.
- `.env`: Environment variables file containing sensitive API keys.
- `requirements.txt`: List of Python dependencies.

## Key Highlights of the Code
1. **Environment Variables:**
   - Uses `dotenv` to securely load API keys.

2. **Session State Management:**
   - Maintains chat history using Streamlit's session state.

3. **Error Handling:**
   - Graceful handling of errors during LLM initialization or response generation.

4. **Integration with External APIs:**
   - Wikipedia and Arxiv tools for fetching additional information.

## Example Interaction
### Input
```plaintext
What is machine learning?
```

### Output
```plaintext
Machine learning is a type of artificial intelligence (AI) that allows computer systems to learn from data without being explicitly programmed. It is used in various fields such as image recognition, recommendation systems, and natural language processing.
```

## Troubleshooting
- Ensure your `.env` file contains the correct API key.
- Check your internet connection for API requests.
- Review logs in the Streamlit app for detailed error messages.


## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality.

## Acknowledgments
- [LangChain](https://www.langchain.com/) for providing the powerful framework.
- [Groq](https://www.groq.com/) for their large language models.
- Streamlit for enabling rapid development of interactive applications.

