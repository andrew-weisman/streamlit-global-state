# three.py

# Import relevant libraries
import streamlit as st
import multiprocessing as mp
import streamlit_dataframe_editor_global as sde
import pandas as pd
import global_state_lib as gsl

# Function definition for testing multiprocessing
def f(x):
    return x**3

# Main function
def main():

    # Load the global state
    global_state = gsl.get_global_state()

    # Selectbox widget
    key = 'selectbox'
    if key not in global_state:
        global_state[key] = 'one'
    st.selectbox('Selectbox', ['one', 'two', 'three'], key=key, index=['one', 'two', 'three'].index(global_state[key]), on_change=gsl.assign_to_global_state, args=(global_state, key))

    # Run a parallel process
    if st.button('Run parallel process'):
        with mp.get_context('forkserver').Pool(4) as p:
            st.write(p.map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    # Create a default dataframe
    df_default = pd.DataFrame({'a': [1, 2, 3], 'b': [False, False, True], 'c': [4, 5, 6]})

    # Dataframe editor widget 1
    key = 'dataframe_editor1'
    if key not in global_state:
        global_state[key] = sde.DataframeEditor(df_orig=df_default, df_description='first_df', state_holder=global_state)
    global_state[key].render_data_editor(on_change=gsl.assign_to_global_state, num_rows='dynamic')

    # Dataframe editor widget 2
    key = 'dataframe_editor2'
    if key not in global_state:
        global_state[key] = sde.DataframeEditor(df_orig=df_default, df_description='second_df', state_holder=global_state)
    global_state[key].render_data_editor(on_change=gsl.assign_to_global_state, num_rows='dynamic')
