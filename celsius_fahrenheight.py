import streamlit

streamlit.title("Celsius to Fahrenheight converter")

fahrenheight = streamlit.slider("Fahrenheight", -40, 120)
if (streamlit.button("Convert to celsius")):
    celsius = (fahrenheight - 32) * 100 / 180
    streamlit.latex(f'{celsius:.1f}^\circ\,C')
celsius = streamlit.slider("Celsius", -40, 60)
if (streamlit.button("Convert to Fahrenheight")):
    fahrenheight= (celsius) * 180 / 100 + 32
    streamlit.latex(f'{fahrenheight:.1f}^\circ\,F')
