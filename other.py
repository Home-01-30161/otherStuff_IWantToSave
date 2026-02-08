import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="LOG_084: RECOVERY", page_icon="🕵️‍♂️")

# Initialize session state to track progress
if 'stage' not in st.session_state:
    st.session_state.stage = 1

def check_password(input_pass, correct_pass, next_stage):
    if input_pass == correct_pass:
        st.session_state.stage = next_stage
        st.rerun()
    elif input_pass:
        st.error("❌ ERROR: DECRYPTION FAILED. UNAUTHORIZED ACCESS ATTEMPT.")

st.title("📂 ENCRYPTED_FILES")
st.write("System decrypting... Please provide the authorization tokens.")

# --- Stage 1 ---
if st.session_state.stage == 1:
    pw1 = st.text_input("Level 1 Decryption Key:", type="password")
    if st.button("Decrypt Layer 1"):
        check_password(pw1, "wish you luck", 2)

# --- Stage 2 ---
elif st.session_state.stage == 2:
    st.warning("⚠️ Layer 1 Decrypted. Memory leak detected.")
    pw2 = st.text_input("Level 2 Decryption Key:", type="password")
    if st.button("Decrypt Layer 2"):
        check_password(pw2, "AperiSolveIsAGreatToolForCTF", 3)

# --- Stage 3 ---
elif st.session_state.stage == 3:
    st.warning("⚠️ Layer 2 Decrypted. File integrity failing.")
    pw3 = st.text_input("Final Flag (Root Access):", type="password")
    if st.button("Execute Final Decryption"):
        check_password(pw3, "ctf{takingbackmymind}", 4)

# --- Final Success: The Story ---
elif st.session_state.stage == 4:
    st.snow()  # Changed balloons to snow for a "chilly" atmosphere
    
    st.markdown("# LOG_084: The Basement is Leaking")
    st.write("**Author:** 'Root_Access' (Pibul)")
    st.write("**Timestamp:** January 1, 2016 | 03:14 AM")
    
    st.divider()

    st.markdown("### The Collection")
    st.info("I’ve spent ten years breaking into systems I wasn’t supposed to be in. I think I’m the system being breached now.")
    st.write("""
    It started during the 'Physical Pentesting' phase of my career. I started picking up... souvenirs. 
    An antique brass key, a rusted iron 'warding' plate from Prague, and a stone figurine.
    I bought the house to display them. I thought I was building a museum. I was building a cage.
    """)

    st.markdown("### The Noise")
    st.write("""
    The sounds aren't creaks. It’s rhythmic. Like someone dragging a heavy, wet sack of grain across 
    the floorboards directly beneath my bed. I checked the Nest cam. It showed 40 minutes of packet loss. 
    Then, for three seconds, I saw myself standing in the corner, staring at the figurine, holding a 
    kitchen knife I don’t remember taking downstairs.
    """)

    st.markdown("### The Corruption of Memory")
    st.error("I forgot my sister’s middle name today.")
    st.write("""
    Every time a memory disappears, I see *him*. He’s tall—too tall. 
    He stands at the periphery of my vision. If you find this, don't look for the house. 
    If you find something buried where it shouldn't be, leave it in the dirt.
    """)

    st.code("Connection Terminated: [Unexpected EOF]", language="bash")

    if st.button("Wipe System (Restart)"):
        st.session_state.stage = 1
        st.rerun()