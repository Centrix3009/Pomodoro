import streamlit as st
import time

# CSS by andfanilo
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

#---------------------------------#
st.write("""
# The Pomodoro App

Let's do some focus work and upskill.

Developed by: [Devanshu](https://github.com/Centrix3009)
""")

# Initialize session state variables
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
if 'stop' not in st.session_state:
    st.session_state.stop = False

# Timer durations
t1 = 1500  # Work time (25 minutes)
t2 = 300   # Break time (5 minutes)

# Timer logic
def start_timer(duration):
    with st.empty():
        for t in range(duration, 0, -1):
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"⏳ {timer}")
            time.sleep(1)
            if st.session_state.stop:
                break
        if not st.session_state.stop:
            st.success("🔔 25 minutes is over! Time for a break!")

def start_break():
    with st.empty():
        for t in range(t2, 0, -1):
            mins2, secs2 = divmod(t, 60)
            timer2 = '{:02d}:{:02d}'.format(mins2, secs2)
            st.header(f"⏳ {timer2}")
            time.sleep(1)
            if st.session_state.stop:
                break
        if not st.session_state.stop:
            st.error("⏰ 5 minute break is over!")

# Start button
if st.button("Start"):
    st.session_state.timer_running = True
    st.session_state.stop = False  # Reset stop state
    start_timer(t1)
    if not st.session_state.stop:  # Only start break if not stopped
        start_break()

# Show Stop button only if the timer is running
if st.session_state.timer_running:
    if st.button("Stop"):
        st.session_state.stop = True  # Set stop state to true
        st.session_state.timer_running = False
