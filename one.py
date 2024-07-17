# one.py

# Import relevant libraries
import streamlit as st
import global_state_lib as gsl

# Main function
def main():

    # Load the global state
    global_state = gsl.get_global_state()

    # Slider widget
    key = 'slider'
    if key not in global_state:
        global_state[key] = 40
    st.slider("Slider", 0, 100, key=key, value=global_state[key], on_change=gsl.assign_to_global_state, args=(global_state, key))

    # Display dataframe_editor2's contents (from three.py)
    if 'dataframe_editor2' in global_state:
        st.dataframe(global_state['dataframe_editor2'].reconstruct_edited_dataframe(), hide_index=True)
    else:
        st.write('No dataframe editors have been initialized; do so on the third page')
