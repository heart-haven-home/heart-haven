import streamlit as st
from openai import OpenAI
import streamlit as st
from openai import OpenAI

# Get the API key from Streamlit secrets
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)


# ------------------ Page Config ------------------
st.set_page_config(
    page_title="HeartHaven 🌸",
    page_icon="💜",
    layout="centered"
)

# ------------------ Custom CSS for Premium Fonts & Styling ------------------
st.markdown("""
<style>
/* Premium title font */
h1.heart-haven-title {
    font-family: 'Great Vibes', cursive;
    font-size: 60px;
    color: #FF5AA2;
    text-align: center;
    margin-bottom: 5px;
}

/* Elegant body font */
p.body-text {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 18px;
    color: #333333;
    text-align: center;
    line-height: 1.6;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

/* Sidebar minimal style */
.sidebar .block-container {
    padding: 1rem 1rem 1rem 1rem;
}
</style>
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ------------------ Sidebar: Premium Ravishing Design ------------------
st.sidebar.markdown("""
<style>
/* Gradient background for sidebar */
.sidebar .sidebar-content {
    background: linear-gradient(180deg, #FFDEE9 0%, #B5FFFC 100%);
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.15);
}

/* Section headers */
.sidebar h2 {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-weight: 700;
    color: #FF5AA2;
    margin-bottom: 10px;
}

/* Helpline, resource, and text */
.sidebar p, .sidebar a {
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 15px;
    color: #333333;
    line-height: 1.5;
    margin-bottom: 8px;
    text-decoration: none;
}

/* Link hover effect */
.sidebar a:hover {
    color: #FF69B4;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Helplines ------------------
st.sidebar.markdown("""
<div style="padding:10px; border-radius:15px; background-color:rgba(255,255,255,0.85); box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
<h2>🌈 Helplines</h2>
<p>📞 <strong>Trevor Project (US):</strong> 1-866-488-7386</p>
<p>📞 <strong>Samaritans (UK):</strong> 116 123</p>
<p>📞 <strong>AASRA (India):</strong> +91-9820466726</p>
</div>
""", unsafe_allow_html=True)

# ------------------ Resources ------------------
st.sidebar.markdown("""
<div style="margin-top:20px; padding:10px; border-radius:15px; background-color:rgba(255,255,255,0.85); box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
<h2>🧘 Resources</h2>
<p>🌿 <a href='https://www.youtube.com/watch?v=inpok4MKVLM' target='_blank'>Mindfulness Meditation</a></p>
<p>🌿 <a href='https://www.youtube.com/watch?v=30VMIEmA114' target='_blank'>Grounding Exercise</a></p>
</div>
""", unsafe_allow_html=True)

# ------------------ About the Founder ------------------
st.sidebar.markdown("""
<div style="margin-top:20px; padding:10px; border-radius:15px; background-color:rgba(255,255,255,0.85); box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
<h2>🌟 About the Founder</h2>
<p><strong>Naytik Jain</strong> is the passionate creator behind HeartHaven. Driven by a vision to make mental health support accessible, inclusive, and empathetic, Naytik believes everyone deserves a safe space to be heard.</p>
<p><em>“HeartHaven is my way of ensuring that every heart, no matter its journey, has a place to feel understood and supported.”</em></p>
</div>
""", unsafe_allow_html=True)

# ------------------ Suggested Prompts ------------------
st.sidebar.markdown("""
<div style="margin-top:20px; padding:10px; border-radius:15px; background-color:rgba(255,255,255,0.85); box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
<h2>💬 Suggested Prompts</h2>
<p>- How can I cope with stress today?</p>
<p>- Can you suggest some LGBTQ+ friendly resources?</p>
<p>- I’m feeling anxious, what should I do?</p>
<p>- Tips for self-care this week</p>
<p>- Ways to build confidence and resilience</p>
</div>
""", unsafe_allow_html=True)



# ------------------ Title & Description ------------------
st.markdown('<h1 class="heart-haven-title">HeartHaven</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="body-text">'
    "HeartHaven is your thoughtful, empathetic companion, designed to listen deeply and respond with care. "
    "Every response is crafted to be concise, actionable, and uplifting — no more than 150 words — "
    "to ensure clarity and focus. The system dynamically interprets your feelings and provides guidance, "
    "resources, and reflective suggestions tailored just for you. Here, your voice is heard, your identity is respected, "
    "and every response is designed to nurture emotional well-being. "
    ""
    "Founder: Naytik Jain"
    '</p>',
    unsafe_allow_html=True
)

# ------------------ Session State ------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": (
            "You are HeartHaven, a minimalist, empathetic counselor for LGBTQ+ individuals. "
            "Respond in a warm, solution-oriented, concise manner (max 150 words). "
            "Provide practical advice, calming techniques, affirmations, and reference resources when appropriate. "
            "If someone is in immediate crisis, gently remind them to contact trusted help or emergency services."
        )}
    ]

# ------------------ Display Chat ------------------
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ------------------ Chat Input ------------------
placeholder_text = "Share how you feel today… or ask a question for guidance 💌"

if "suggested" not in st.session_state:
    st.session_state.suggested = []

# Show suggested questions based on last AI response
if st.session_state.messages and st.session_state.messages[-1]["role"] == "assistant":
    st.session_state.suggested = [
        "Can you help me cope with anxiety?",
        "I feel misunderstood, what should I do?",
        "Give me a quick self-care tip.",
        "How can I feel more confident about my identity?"
    ]

if st.session_state.suggested:
    st.markdown("**Suggested prompts:**")
    for i, suggestion in enumerate(st.session_state.suggested):
        if st.button(suggestion, key=f"sugg_{i}"):
            st.session_state.chat_input = suggestion
            placeholder_text = suggestion

user_input = st.chat_input(placeholder_text)

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(f"**{user_input}**")

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("_HeartHaven is reflecting… 💭_")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state.messages
        )

        ai_reply = response.choices[0].message.content.strip()
        message_placeholder.markdown(ai_reply)

    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
