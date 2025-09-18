import streamlit as st
import ollama
from typing import List, Dict, Optional, Any
import base64
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Ollama Gemma3:4b Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Title and description
st.title("🤖 Ollama Gemma3:4b Chatbot")
st.markdown("Chat and (optionally) analyze uploaded images using the Gemma3:4b model.")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize Ollama client
@st.cache_resource
def init_ollama_client():
    """Initialize Ollama client"""
    try:
        client = ollama.Client()
        return client
    except Exception as e:
        st.error(f"Failed to initialize Ollama client: {e}")
        return None

def get_ollama_response(client, prompt: str, chat_history: List[Dict], temperature: float = 0.7, system_prompt: str = "", image_data: Optional[bytes] = None) -> str:
    """Get response from Ollama Gemma3:4b model (sends images if provided)."""
    try:
        # Prepare messages for Ollama
        messages = []
        
        # Add system prompt if provided
        if system_prompt.strip():
            messages.append({
                "role": "system",
                "content": system_prompt.strip()
            })
        
        # Add chat history
        for msg in chat_history:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        
        # Prepare the user message
        user_message: Dict[str, Any] = {
            "role": "user",
            "content": prompt
        }
        
        # Add image if provided
        if image_data:
            user_message["images"] = [base64.b64encode(image_data).decode('utf-8')]
        
        messages.append(user_message)

        # Always use gemma3:4b per requirement
        response = client.chat(
            model="gemma3:4b",
            messages=messages,
            options={
                "temperature": temperature
            },
            stream=False
        )
        
        return response["message"]["content"]
    
    except Exception as e:
        if "model not found" in str(e).lower():
            return "Error: Model 'gemma3:4b' not found. Please install it with: `ollama pull gemma3:4b`"
        if "image" in str(e).lower() and "support" in str(e).lower():
            return (
                "This model may not support image inputs. Please use plain text, "
                "or consider a vision-capable model."
            )
        return f"Error communicating with Ollama: {str(e)}"

# Initialize client
client = init_ollama_client()

# Sidebar for model info and settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Temperature setting
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Controls randomness in responses"
    )
    
    # System prompt
    system_prompt = st.text_area(
        "System Prompt (Optional)",
        placeholder="You are a helpful assistant...",
        help="Set a system prompt to guide the AI's behavior"
    )
    
    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    
    # Model info
    st.header("📊 Model Info")
    st.info("Using: **gemma3:4b**")
    
    if client:
        try:
            models = client.list()
            available_models = [model['name'] for model in models.get('models', [])]
            
            # Check required model only
            if "gemma3:4b" in available_models:
                st.success("✅ gemma3:4b is available")
            else:
                st.warning("⚠️ gemma3:4b not found")
                st.info("Install with: `ollama pull gemma3:4b`")
                
        except Exception as e:
            st.write(f"Could not fetch model info: {e}")
    
    # Usage tips
    st.header("💡 Tips")
    st.markdown("""
    - Make sure Ollama is running
    - Install model: `ollama pull gemma3:4b`
    - You can upload an image for a short description (may require a vision-capable model)
    - Lower temperature = more focused; higher = more creative
    """)

# Main chat interface
st.header("💬 Chat")

# Image upload section
uploaded_file = st.file_uploader(
    "Upload an image for analysis (optional)", 
    type=['png', 'jpg', 'jpeg', 'gif', 'bmp'],
    help="Upload an image to get a short description"
)

# Display uploaded image and quick analysis button
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    if st.button("🔍 Analyze Image", help="Get a super short description of the uploaded image"):
        image_data = uploaded_file.getvalue()
        
        # Add analysis request to chat
        analysis_prompt = "Please provide a super short description of this image."
        user_message = {"role": "user", "content": analysis_prompt + " [Image uploaded]"}
        st.session_state.messages.append(user_message)
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(analysis_prompt)
            st.image(image, caption="Analyzing this image", width=200)
        
        # Get AI response
        if client:
            with st.chat_message("assistant"):
                with st.spinner("Analyzing image..."):
                    response = get_ollama_response(
                        client, 
                        analysis_prompt, 
                        st.session_state.messages[:-1], 
                        temperature,
                        system_prompt,
                        image_data
                    )
                    st.markdown(response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
        else:
            with st.chat_message("assistant"):
                st.error("Ollama client not available. Please check your Ollama installation and make sure the Ollama service is running.")
        
        # Rerun to update the chat
        st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response (text only for regular chat)
    if client:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_ollama_response(
                    client, 
                    prompt, 
                    st.session_state.messages[:-1], 
                    temperature,
                    system_prompt
                )
                st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        with st.chat_message("assistant"):
            st.error("Ollama client not available. Please check your Ollama installation and make sure the Ollama service is running.")

# Footer
st.markdown("---")
st.markdown("*Powered by Ollama and Streamlit*")
