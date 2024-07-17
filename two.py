# two.py

# Import relevant libraries
import streamlit as st
import multiprocessing as mp
import global_state_lib as gsl

# Function definition for testing multiprocessing
def f(x):
    return x*x

# Main function
def main():

    # Load the global state
    global_state = gsl.get_global_state()
    
    # Simulate cleanly returning from a page
    if st.button('Return'):
        st.warning('Returning')
        st.button('Restore page')
        return
    
    # Toggle widget
    key = 'toggle'
    if key not in global_state:
        global_state[key] = False
    st.toggle('Toggle me', key=key, value=global_state[key], on_change=gsl.assign_to_global_state, args=(global_state, key))

    # Run a parallel process
    if st.button('Run parallel process'):
        with mp.get_context('forkserver').Pool(4) as p:
            st.write(p.map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
