import streamlit as st

#st.title("Demande pour Inès Rousse")

st.markdown("""
<style>
body {
    font-size: 50px;
}    
head {
    font-size: 50px;
}
main {
    font-size: 50px;
}
</style>
""", unsafe_allow_html=True)

if "step" not in st.session_state:
    st.session_state.step = "debut"
if "booleen" not in st.session_state:
    st.session_state.booleen = False
if "booleen2" not in st.session_state:
    st.session_state.booleen2 = False


if st.session_state.step == "debut":
    st.image("image3.png")
    st.image("image.png")

    col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns(10)

    with col4:
        if st.button("Oui"):
            st.session_state.booleen2 = True
    with col7:
        if st.button("Non"):
            st.session_state.booleen = True
    if st.session_state.booleen:
        st.session_state.booleen = False
        st.warning("Ceci n'est pas possible")
    if st.session_state.booleen2:
        st.session_state.booleen2 = False
        st.session_state.step = "suite"
        st.rerun()

if st.session_state.step == "suite":
    st.success("Bravo c'était la bonne réponse !")
    st.image("image.png")
    st.text("Je t'aime !",text_alignment="center")