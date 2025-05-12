import cohere
import streamlit as st

cohere_api_key = "cohere_api_key"
co = cohere.Client(cohere_api_key)

def generate_reply(email_content):
    response = co.generate(
        model='command-xlarge',
        prompt=f"You are an email assistant. Reply professionally to this email:\n\n{email_content}",
        max_tokens=150
    )
    return response.generations[0].text.strip()

st.title("Automated Email Reply Generator")
st.markdown("Provide the email content below, and the assistant will generate a professional reply.")

email_content = st.text_area("Enter the email content:", height=200)

if st.button("Generate Reply"):
    if email_content.strip():
        with st.spinner("Generating reply..."):
            try:
                reply = generate_reply(email_content)
                st.success("Reply Generated!")
                st.text_area("Generated Reply:", reply, height=200)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter email content to generate a reply.")
