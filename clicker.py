import streamlit as st

st.set_page_config(page_title="My First App", page_icon="🎮")
st.title("🎮 Super Fast Clicker Game")

# Initialize the game scores
if "score" not in st.session_state:
    st.session_state.score = 0
if "high_score" not in st.session_state:
    st.session_state.high_score = 0

# Track the highest score achieved this session
if st.session_state.score > st.session_state.high_score:
    st.session_state.high_score = st.session_state.score

# Display the scores side by side
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Your Code Score", value=st.session_state.score)
with col2:
    st.metric(label="🏆 High Score", value=st.session_state.high_score)

# Main action button
if st.button("⌨️ CLICK HERE TO SCORE POINTS", use_container_width=True):
    st.session_state.score += 1
    st.rerun()

# Secret code box
cheat = st.text_input("🤫 Secret Code Box:")
if cheat == "speed":
    st.session_state.score += 5000
    st.success("💥 Added 5,000 bonus points!")

st.divider()

# Reset Button
if st.button("🔄 Reset Score"):
    st.session_state.score = 0
    st.rerun()
