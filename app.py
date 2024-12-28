import streamlit as st
from multimodal_search import MultimodalSearch

# Configure the page settings to hide default menu
st.set_page_config(
    page_title="Our Store",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={}  # This removes the three-dot menu
)

# Custom CSS to center the title and modify appearance
st.markdown("""
    <style>
    .title {
        text-align: center;
        padding: 20px;
        color: #2e4053;
        font-size: 50px;
        font-weight: bold;
        margin-bottom: 30px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)




def main():
    st.markdown("<h1 style='text-align: center; color: red;'>Fashion Cloth Search App</h1>", unsafe_allow_html=True)

    multimodal_search = MultimodalSearch()

    query = st.text_input("Enter your query:")
    if st.button("Search"):
        if len(query) > 0:
            results = multimodal_search.search(query)
            st.warning("Your query was "+query)
            st.subheader("Search Results:")
            col1, col2, col3 = st.columns([1,1,1])
            with col1:
                st.write(f"Score: {round(results[0].score*100, 2)}%")
                st.image(results[0].content, use_container_width=True)
            with col2:
                st.write(f"Score: {round(results[1].score*100, 2)}%")
                st.image(results[1].content, use_container_width=True)
            with col3:
                st.write(f"Score: {round(results[2].score*100, 2)}%")
                st.image(results[2].content, use_container_width=True)
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()
