import streamlit as st
import socket
import time

# Setting up the page title and giving it a cool hacker vibe 😎
st.set_page_config(page_title="NetScanner", page_icon="🕵️‍♀️", layout="centered")

# Customizing the CSS to make it look like a real terminal (Matrix style!)
st.markdown("""
    <style>
    /* Dark background is a must for cybersecurity tools haha */
    .stApp {
        background-color: #0a0a0a;
    }
    h1, h2, h3, p, label {
        color: #00FF41 !important; 
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button {
        background-color: #00FF41;
        color: #0a0a0a;
        font-weight: bold;
        border-radius: 5px;
        border: 2px solid #00FF41;
    }
    .stButton>button:hover {
        background-color: #0a0a0a;
        color: #00FF41;
    }
    </style>
""", unsafe_allow_html=True)

# Main UI setup
st.title("🌐 NetScanner: Security Tool")
st.markdown("### 🔍 Scan IPs for Open Ports")

# Target IP input (Google's DNS is the default safe option)
target_ip = st.text_input("🎯 Enter Target IP Address:", "8.8.8.8")

# These are the most common ports hackers look for: FTP, SSH, HTTP, HTTPS
ports_to_scan = [21, 22, 80, 443, 8080]

if st.button("🚀 Start Scan"):
    st.info(f"Scanning Target: {target_ip}...")
    
    # Adding a progress bar just to make it look professional 🛠️
    progress_bar = st.progress(0)
    
    for i, port in enumerate(ports_to_scan):
        # Create a socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Timeout after 1 second so we don't wait forever
        
        result = sock.connect_ex((target_ip, port))
        
        # 0 means the connection was successful (port is open!)
        if result == 0:
            st.error(f"🚨 Port {port} (OPEN) - Vulnerable/Accessible!")
        else:
            st.success(f"🔒 Port {port} (CLOSED) - Secure.")
            
        sock.close()
        
        # Update progress bar
        progress_bar.progress((i + 1) / len(ports_to_scan))
        time.sleep(0.3) # Small delay for dramatic effect 🎬
        
    st.balloons()
    st.markdown("### 🎯 Scan Complete!")