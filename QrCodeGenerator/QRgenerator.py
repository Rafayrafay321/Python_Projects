import streamlit as st
import qrcode
from io import BytesIO

# Function to generate QR code and return it as bytes
def Genr_QRcode(URL):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(URL)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    pngIM = BytesIO()
    img.save(pngIM, format="PNG")
    pngIM.seek(0)  # Reset buffer position

    return pngIM.getvalue()  # Return raw bytes

# Streamlit UI
st.title('QR Code Generator')

# Get URL input
Url = st.text_input("Enter the URL to generate the QR Code:")

# Store QR Code in session state to persist across reruns
if "qr_code" not in st.session_state:
    st.session_state.qr_code = None

# Reduce gap between buttons using smaller column spacing
col1, col_space, col2 = st.columns([1, 0.05, 1])

# Left column: Generate button
with col1:
    if st.button("Generate QR Code"):
        if Url:
            st.session_state.qr_code = Genr_QRcode(Url)  # Store in session state
            st.image(st.session_state.qr_code)  # Display QR code
        else:
            st.warning("Please enter a valid URL.")

# Right column: Download button (only when QR code is generated)
if st.session_state.qr_code:
    with col2:
        st.download_button(
            label="Download QR Code",
            data=st.session_state.qr_code,
            file_name="QRCode.png",
            mime="image/png"
        )

# Use CSS to further minimize the button spacing
st.markdown("""
    <style>
        div[data-testid="column"] {
            gap: 2px !important;
        }
    </style>
""", unsafe_allow_html=True)
