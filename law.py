import google.generativeai as genai
import streamlit as st
from datetime import date

# Configure Generative AI
genai.configure(api_key="AIzaSyCW1hE-AyYTEoT83DD8apI2I9uoq_urCjo")
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit App Configuration
st.set_page_config(
    page_title="CASE-CAPSULE",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for light theme and styling
st.markdown(
    """
    <style>
        /* Light Theme Colors */
        :root {
            --primary-color: #2196F3;
            --secondary-color: #1976D2;
            --background-color: #ffffff;
            --text-color: #333333;
            --border-color: #e0e0e0;
        }

        body {
            color: var(--text-color);
            font-family: 'Segoe UI', sans-serif;
        }

        .main {
            background: var(--background-color);
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }

        /* Animated Buttons */
        .stButton button {
            background-color: var(--primary-color);
            color: white;
            font-size: 16px;
            font-weight: 600;
            border-radius: 8px;
            padding: 12px 24px;
            margin: 10px;
            transition: all 0.3s ease;
            border: none;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .stButton button:hover {
            background-color: var(--secondary-color);
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .stButton button:active {
            transform: translateY(0);
        }

        /* Input Fields */
        .stTextInput > div, .stTextArea > div {
            border: 2px solid var(--border-color);
            border-radius: 8px;
            background-color: #f5f5f5;
            transition: all 0.3s ease;
        }

        .stTextInput > div:focus-within, .stTextArea > div:focus-within {
            border-color: var(--primary-color);
            box-shadow: 0 0 0 2px rgba(33, 150, 243, 0.1);
        }

        /* Select Box */
        .stSelectbox > div {
            border-radius: 8px;
            background-color: #f5f5f5;
            border: 2px solid var(--border-color);
            transition: all 0.3s ease;
        }

        .stSelectbox > div:hover {
            border-color: var(--primary-color);
        }

        /* Radio Buttons */
        .stRadio > div {
            background-color: transparent;
        }

        /* Container Spacing */
        .block-container {
            padding: 2rem 3rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        /* Headings */
        h1, h2, h3, h4 {
            color: var(--text-color);
            font-weight: 600;
            margin-bottom: 1rem;
        }

        h1 {
            font-size: 2.5rem;
            background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 2rem;
        }

        /* Cards and Containers */
        .element-container {
            background: white;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease;
        }

        .element-container:hover {
            transform: translateY(-2px);
        }

        /* Footer */
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background: white;
            color: var(--text-color);
            text-align: center;
            padding: 15px;
            font-size: 14px;
            border-top: 1px solid var(--border-color);
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .block-container {
                padding: 1rem;
            }

            h1 {
                font-size: 2rem;
            }

            .stButton button {
                width: 100%;
                margin: 5px 0;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Menu
st.sidebar.title("⚖️ Menu")
options = st.sidebar.radio("Select Task", ["Draft Document", "FAQs", "Case Summarization"])

# App Title and Description
st.title("🎯 CASE-CAPSULE: Your Legal Assistant")
st.markdown("A smart platform for drafting legal documents, answering FAQs, and summarizing cases.")

# Predefined Document Templates
TEMPLATES = {
    "Nikkah Nama": """
        NIKKAH NAMA
        ...
    """,

}

# Draft Legal Document Section
if options == "Draft Document":
    with st.container():
        st.subheader("📜 Draft Legal Documents")
        doc_type = st.selectbox("Select Document Type", list(TEMPLATES.keys()), index=0)
        st.markdown(f"### **Drafting {doc_type}**")

        # Add Additional Input Sections
        reg_no = st.text_input("🔢 Registration Number")
        draft_date = st.date_input("📅 Draft Date", value=date.today())

        if doc_type == "Nikkah Nama":
            groom_name = st.text_input("💼 Groom's Full Name")
            groom_id = st.text_input("🔖 Groom's ID (e.g., CNIC)")
            groom_address = st.text_area("📍 Groom's Address")
            groom_profession = st.text_input("💼 Groom's Profession")
            bride_name = st.text_input("👰 Bride's Full Name")
            bride_id = st.text_input("🔖 Bride's ID (e.g., CNIC)")
            bride_address = st.text_area("📍 Bride's Address")
            wali_name = st.text_input("🛡️ Wali's Full Name")
            mehr_amount = st.number_input("💰 Mehr Amount (PKR)", min_value=0)
            mehr_mode = st.selectbox("💳 Mehr Payment Mode", ["Immediate", "Deferred", "Both"])
            witness1_name = st.text_input("👤 Witness 1 Full Name")
            witness2_name = st.text_input("👤 Witness 2 Full Name")
            nikah_registrar_name = st.text_input("✒️ Nikah Registrar's Name")
            nikkah_conditions = st.text_area("📝 Terms and Conditions")

            if st.button(f"🖋️ Generate {doc_type}"):
                st.success(f"{doc_type} generated successfully!")
                st.text_area(
                    "Generated Document",
                    f"Nikkah Nama for {groom_name} and {bride_name} on {draft_date}",
                    height=400,
                )

# FAQs Section
elif options == "FAQs":
    st.subheader("💡 Legal Advice & FAQs")
    st.markdown("### Ask a legal question, and our AI will assist you.")
    question = st.text_input("❓ Ask your question here")
    if st.button("🔍 Get Advice"):
        response = model.generate_content(f"Answer this legal question for Pakistan: {question}")
        st.success(response.text)

# Case Summarization Section
elif options == "Case Summarization":
    st.subheader("📚 Summarize My Case")
    st.markdown("### Provide details of your case, and we will summarize it for you.")
    case_details = st.text_area("📝 Enter case details")
    if st.button("📄 Summarize"):
        response = model.generate_content(f"Summarize this case FOR PAKISTAN: {case_details}")
        st.info(response.text)

# Footer Section
st.markdown(
    """
    <div class="footer">
        &copy; 2025 CASE-CAPSULE | Powered by B & H
    </div>
    """,
    unsafe_allow_html=True,
)
