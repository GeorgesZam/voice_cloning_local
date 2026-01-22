"""
🎤 VoiceClone Studio - Local Voice Cloning App
"""

import streamlit as st
import tempfile
import os
from pathlib import Path
import time

st.set_page_config(page_title="VoiceClone Studio", page_icon="🎤", layout="wide")

# CSS
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0f0f1a 0%, #1e1e3f 50%, #0f0f1a 100%); }
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
    }
    section[data-testid="stSidebar"] { background: rgba(15, 15, 26, 0.95); }
</style>
""", unsafe_allow_html=True)


def get_device():
    import torch
    if torch.cuda.is_available():
        return "cuda"
    elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
        return "mps"
    return "cpu"


@st.cache_resource
def load_model(device):
    from chatterbox.tts import ChatterboxTTS
    return ChatterboxTTS.from_pretrained(device=device)


def main():
    st.title("🎤 VoiceClone Studio")
    st.caption("Clone your voice locally with AI • 100% private")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        device = get_device()
        st.success(f"Device: {device.upper()}")
        
        st.divider()
        
        exaggeration = st.slider("😄 Emotion", 0.0, 1.0, 0.5, 0.1, 
                                  help="0 = monotone, 1 = very expressive")
        cfg_weight = st.slider("🎯 Voice fidelity", 0.0, 1.0, 0.5, 0.1,
                                help="Higher = closer to your voice")
    
    # Main content
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1️⃣ Your voice sample")
        uploaded_file = st.file_uploader(
            "Upload audio (5-15 sec)",
            type=["wav", "mp3", "m4a", "ogg", "flac"]
        )
        if uploaded_file:
            st.audio(uploaded_file)
            st.success("✅ Audio loaded")
    
    with col2:
        st.subheader("2️⃣ Text to speak")
        text = st.text_area(
            "Enter text",
            value="Hello! This is a test of voice cloning with artificial intelligence.",
            height=150
        )
        st.caption(f"{len(text)} characters")
    
    # Generate button
    st.divider()
    
    col_btn = st.columns([1, 2, 1])[1]
    with col_btn:
        generate = st.button(
            "🎤 Clone my voice", 
            use_container_width=True,
            disabled=not uploaded_file or not text.strip()
        )
    
    # Generation
    if generate and uploaded_file and text.strip():
        
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name
        
        try:
            with st.spinner("Loading model..."):
                model = load_model(device)
            
            with st.spinner("Generating audio..."):
                start = time.time()
                
                wav = model.generate(
                    text,
                    audio_prompt_path=tmp_path,
                    exaggeration=exaggeration,
                    cfg_weight=cfg_weight,
                )
                
                duration = time.time() - start
            
            # Save output
            import torchaudio as ta
            output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
            ta.save(output_path, wav, model.sr)
            
            st.success(f"✅ Generated in {duration:.1f}s")
            st.audio(output_path)
            
            # Download
            with open(output_path, "rb") as f:
                st.download_button(
                    "⬇️ Download",
                    data=f.read(),
                    file_name="cloned_voice.wav",
                    mime="audio/wav"
                )
            
            os.unlink(output_path)
            
        except Exception as e:
            st.error(f"❌ Error: {e}")
        
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)


if __name__ == "__main__":
    main()
