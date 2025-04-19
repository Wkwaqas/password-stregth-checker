import re
import streamlit as st

def check_password_strength(password):
    score = 0
    feedback = []
    if len(password) >= 8:
        score += 1
        feedback.append(("✅ Length is good (8+ characters)", "green"))
    else:
        feedback.append(("❌ Too short - Use at least 8 characters", "red"))
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
        feedback.append(("✅ Contains both uppercase and lowercase letters", "green"))
    else:
        feedback.append(("❌ Add both uppercase and lowercase letters", "red"))
    if re.search(r"\d", password):
        score += 1
        feedback.append(("✅ Contains a number", "green"))
    else:
        feedback.append(("❌ Add at least one number (0-9)", "red"))
    if re.search(r"[!@#$%^&*]", password):
        score += 1
        feedback.append(("✅ Contains a special character (!@#$%^&*)", "green"))
    else:
        feedback.append(("❌ Add a special character (!@#$%^&*)", "red"))


    if " " in password:
        feedback.append(("❌ Password should not contain spaces", "red"))
    else:
        score += 1
        feedback.append(("✅ No spaces in the password", "green"))

    return score, feedback


st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.markdown("## 🔐 Password Strength Checker")
st.write("Check if your password is strong enough to keep your data safe.")

with st.expander("🧠 Password Tips"):
    st.markdown("""
    - Use **at least 8 characters**.
    - Mix **uppercase and lowercase** letters.
    - Include **numbers** and **special characters**.
    - Avoid using **dictionary words**, **names**, or **birthdays**.
    """)


password = st.text_input("Enter your password", type="password")




if password:
    score, feedback = check_password_strength(password)

    strength_levels = {
        5: ("🟩🟩🟩🟩🟩 Very Strong!", "success"),
        4: ("🟩🟩🟩🟩⬜ Strong", "success"),
        3: ("🟨🟨🟨⬜⬜ Moderate", "warning"),
        2: ("🟧🟧⬜⬜⬜ Weak", "warning"),
        1: ("🟥⬜⬜⬜⬜ Very Weak", "error"),
        0: ("⬜⬜⬜⬜⬜ Extremely Weak", "error"),
    }

    level_msg, level_type = strength_levels.get(score, strength_levels[0])
    st.markdown(f"### Password Strength: {level_msg}")
    st.progress(score / 5)


    st.markdown("### ✅ Suggestions & Checks:")
    for message, color in feedback:
        st.markdown(f"<span style='color:{color}'>{message}</span>", unsafe_allow_html=True)

    
    if score < 5:
        if st.checkbox("🔁 Try a new password?"):
            new_password = st.text_input("Enter new password", type="password", key="new_password")
            if new_password:
                st.markdown("---")
                st.subheader("🔄 Checking New Password")
                new_score, new_feedback = check_password_strength(new_password)
                new_msg, new_type = strength_levels.get(new_score, strength_levels[0])
                st.markdown(f"### Password Strength: {new_msg}")
                st.progress(new_score / 5)

                st.markdown("### ✅ Suggestions & Checks:")
                for message, color in new_feedback:
                    st.markdown(f"<span style='color:{color}'>{message}</span>", unsafe_allow_html=True)
