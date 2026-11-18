
import streamlit as st
from src.translator import NLLBTranslator
import html

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="ANUVAAD AI | Language Translator",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

MODEL_PATH = "./models/nllb_en_mr_finetuned"


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f5f7fc;
}

.block-container {
    padding-top: 2rem;
    max-width: 1250px;
    padding-bottom: 3rem;
}

/* HERO */

.hero {
    background: linear-gradient(120deg, #172554, #2563eb);
    padding: 38px;
    border-radius: 20px;
    color: white;
    margin-bottom: 28px;
    box-shadow: 0 8px 25px rgba(37, 99, 235, 0.12);
}

.hero h1 {
    color: white;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero h3 {
    color: #bfdbfe;
    font-size: 20px;
    font-weight: 600;
}

.hero p {
    color: #dbeafe;
    font-size: 15px;
    line-height: 1.7;
}

/* SECTION TITLES */

.section-title {
    color: #172554;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 12px;
}

/* DASHBOARD CARDS */

.info-card {
    background: white;
    padding: 22px;
    border: 1px solid #e2e8f0;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
}

.info-card h3 {
    color: #1e3a8a;
    margin: 0;
    font-size: 21px;
    font-weight: 700;
}

.info-card p {
    color: #64748b;
    margin: 7px 0 0 0;
    font-size: 13px;
}

/* OUTPUT CARD */

.output-card {
    background: white;
    border: 1px solid #dbeafe;
    border-radius: 15px;
    padding: 24px;
    min-height: 180px;
    color: #172554;
    font-size: 18px;
    line-height: 1.9;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    box-shadow: 0 3px 12px rgba(15, 23, 42, 0.03);
}

/* BUTTONS */

.stButton > button {
    background: #2563eb;
    color: white;
    border: none;
    border-radius: 10px;
    height: 48px;
    font-weight: 600;
    transition: 0.2s;
}

.stButton > button:hover {
    background: #1d4ed8;
    color: white;
    border: none;
}

/* DOWNLOAD BUTTON */

.stDownloadButton > button {
    background: #0f766e;
    color: white;
    border: none;
    border-radius: 10px;
    height: 48px;
    font-weight: 600;
}

.stDownloadButton > button:hover {
    background: #115e59;
    color: white;
}

/* TEXT AREA */

.stTextArea textarea {
    border-radius: 12px;
    border: 1px solid #cbd5e1;
    background: white;
    font-size: 15px;
    line-height: 1.7;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e2e8f0;
}

/* FOOTER */

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# LOAD FINE-TUNED MODEL
# =====================================================

@st.cache_resource
def load_model():
    return NLLBTranslator(MODEL_PATH)


# =====================================================
# SESSION STATE
# =====================================================

if "translation" not in st.session_state:
    st.session_state.translation = ""

if "history" not in st.session_state:
    st.session_state.history = []

if "last_input" not in st.session_state:
    st.session_state.last_input = ""


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("## 🌐 ANUVAAD AI")

    st.caption("Intelligent Language Translator")

    st.divider()

    st.markdown("### Translation Mode")

    mode = st.radio(
        "Choose your mode",
        [
            "Text Translation",
            "Dialogue Translation"
        ],
        index=0
    )

    st.divider()

    st.markdown("### Language Pair")

    st.markdown("🇬🇧 **English**")
    st.markdown("⬇️")
    st.markdown("🇮🇳 **Marathi**")

    st.divider()

    st.markdown("### Model Information")

    st.caption("Model: Fine-tuned NLLB-200")
    st.caption("Architecture: Seq2Seq Transformer")
    st.caption("Framework: PyTorch")
    st.caption("Direction: English → Marathi")

    st.divider()

    if st.button(
        "🗑️ Clear Translation History",
        use_container_width=True
    ):
        st.session_state.history = []
        st.rerun()


# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="hero">
<h1>🌐 ANUVAAD AI</h1>
<h3>Intelligent Language Translator</h3>
<p>
Breaking Language Barriers with Artificial Intelligence.
Translate English text, paragraphs and conversations
into Marathi using a fine-tuned Neural Machine Translation model.
</p>
</div>
""", unsafe_allow_html=True)


# =====================================================
# DASHBOARD
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
<div class="info-card">
<h3>🤖 NLLB-200</h3>
<p>Fine-tuned AI Model</p>
</div>
""", unsafe_allow_html=True)


with col2:

    st.markdown("""
<div class="info-card">
<h3>🇬🇧 → 🇮🇳</h3>
<p>English to Marathi</p>
</div>
""", unsafe_allow_html=True)


with col3:

    st.markdown(f"""
<div class="info-card">
<h3>{len(st.session_state.history)}</h3>
<p>Translations This Session</p>
</div>
""", unsafe_allow_html=True)


st.write("")


# =====================================================
# TRANSLATION INPUT SECTION
# =====================================================

st.markdown(
    f'<div class="section-title">📝 {mode}</div>',
    unsafe_allow_html=True
)

if mode == "Text Translation":

    placeholder = "Enter your English text here..."

else:

    placeholder = """Enter your English conversation here...

Example:

Person 1: Hello, how are you?

Person 2: I am doing great. Thank you!

Person 1: What are you doing today?"""


input_text = st.text_area(
    "English Input",
    placeholder=placeholder,
    height=230,
    key="english_input"
)


# WORD AND CHARACTER COUNTER

word_count = len(input_text.split()) if input_text.strip() else 0
character_count = len(input_text)

col1, col2 = st.columns(2)

with col1:
    st.caption(f"📝 Words: {word_count}")

with col2:
    st.caption(f"Characters: {character_count}")


# =====================================================
# TRANSLATION BUTTON
# =====================================================

if st.button(
    "✨ Translate to Marathi",
    use_container_width=True
):

    if not input_text.strip():

        st.warning("Please enter some English text first.")

    else:

        try:

            with st.spinner(
                "🤖 ANUVAAD AI is translating your text..."
            ):

                translator = load_model()

                result = translator.translate(input_text)

                st.session_state.translation = result
                st.session_state.last_input = input_text

                st.session_state.history.append({
                    "input": input_text,
                    "output": result
                })

                st.session_state.pop("copy_translation", None)

            st.success("Translation completed successfully!")

        except Exception as e:

            st.error("Translation failed. Please check the model.")
            st.exception(e)


# =====================================================
# TRANSLATION OUTPUT
# =====================================================

if st.session_state.translation:

    st.write("")

    st.markdown(
        '<div class="section-title">🇮🇳 Marathi Translation</div>',
        unsafe_allow_html=True
    )

    safe_translation = html.escape(
        st.session_state.translation
    )

    st.markdown(
        f'<div class="output-card">{safe_translation}</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            label="⬇️ Download Translation",
            data=st.session_state.translation,
            file_name="ANUVAAD_AI_Marathi.txt",
            mime="text/plain",
            use_container_width=True
        )

    with col2:

        st.button(
            "📋 Copy Translation",
            on_click=lambda: st.session_state.update(
                copy_translation=st.session_state.translation
            ),
            use_container_width=True
        )

        if st.session_state.get("copy_translation"):

            st.code(
                st.session_state.copy_translation,
                language=None
            )


# =====================================================
# TRANSLATION HISTORY
# =====================================================

if st.session_state.history:

    st.divider()

    st.markdown("## 📚 Translation History")

    for index, item in enumerate(
        reversed(st.session_state.history),
        1
    ):

        with st.expander(f"Translation {index}"):

            st.markdown("**🇬🇧 English Input**")
            st.write(item["input"])

            st.markdown("**🇮🇳 Marathi Translation**")
            st.write(item["output"])


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown("""
<div style="text-align:center;">

<p style="color:#64748b; font-size:14px;">
Built with ❤️ by Sumit using Python, PyTorch,
Hugging Face Transformers and Streamlit.
</p>

<p style="color:#94a3b8; font-size:12px;">
ANUVAAD AI | Fine-tuned NLLB-200
</p>

</div>
""", unsafe_allow_html=True)
