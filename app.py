import streamlit as st
from blackjack_logic import get_blackjack_action

st.set_page_config(page_title="Shady's Edge", page_icon="🧥")

# Load logo
st.image("shadys_logo.png", width=100)

# App title
st.title("🎲 Shady's Edge")
st.markdown("**8-Deck • Dealer Stands on Soft 17 • No Surrender**")

# Card value mapping with emoji & suits
card_labels = {
    2: "2♠️", 3: "3♥️", 4: "4♦️", 5: "5♣️", 6: "6♠️",
    7: "7♥️", 8: "8♦️", 9: "9♣️", 10: "🔟", 11: "🅰️ (Ace)"
}
card_values = list(card_labels.keys())

# Color mapping for action types
color_map = {
    "Hit": "#FF4B4B",       # Red
    "Stand": "#4CAF50",     # Green
    "Double": "#FFD700",    # Gold
    "Split": "#00BCD4"      # Teal
}

# UI dropdowns
col1, col2 = st.columns(2)
with col1:
    player_card_1 = st.selectbox("Your First Card", card_values, format_func=lambda x: card_labels[x])
with col2:
    player_card_2 = st.selectbox("Your Second Card", card_values, format_func=lambda x: card_labels[x])

dealer_card = st.selectbox("Dealer's Upcard", card_values, format_func=lambda x: card_labels[x])

# Get result
if st.button("🎯 Get Recommended Play"):
    result = get_blackjack_action([player_card_1, player_card_2], dealer_card)

    emoji_map = {
        "Hit": "💥 SMASH THAT SHIT",
        "Stand": "🧊 CHILL",
        "Double": "💸 2x THAT SHIT",
        "Split": "🔪 CHOP 'EM UP"
    }

    styled_result = emoji_map.get(result, result)
    result_color = color_map.get(result, "#FFFFFF")

    # Confetti on baller moves
    if result == "Split" or (player_card_1 == 11 and player_card_2 == 11):
        st.balloons()

    # Styled output box with animation
    st.markdown(
        f"""
        <div style='text-align:center; padding: 20px;
                    background-color:#1e1e1e;
                    border-radius:15px;
                    border: 3px solid {result_color};
                    box-shadow: 0px 0px 25px {result_color}AA;
                    animation: pulse 1s ease-in-out infinite;'>
            <h2 style='color:{result_color}; font-size: 32px;'>Recommended Play:</h2>
            <h1 style='color:white; font-size: 48px;'>{styled_result}</h1>
        </div>

        <style>
        @keyframes pulse {{
            0% {{ box-shadow: 0 0 10px {result_color}; }}
            50% {{ box-shadow: 0 0 20px {result_color}AA; }}
            100% {{ box-shadow: 0 0 10px {result_color}; }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
