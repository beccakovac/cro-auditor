import streamlit as st

st.set_page_config(page_title="CRO Auditor", page_icon="🔍")

st.title("CRO Auditor")
st.subheader("Coming soon")

url = st.text_input("Website URL", placeholder="https://example.com")

if url:
    st.write(f"You entered: {url}")

# Checks that the Claude API key is set up, without ever showing it on screen.
if st.secrets.get("ANTHROPIC_API_KEY", "").startswith("sk-ant-"):
    st.caption("✅ Claude API key found")
else:
    st.caption("⚠️ No Claude API key yet. Add it to .streamlit/secrets.toml")
