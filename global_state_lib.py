# global_state_lib.py

# This is a library that contains the GlobalState class and functions to manage the global state in Streamlit. Using this library will continuously update an app's state so e.g. on unstable platforms if the session is temporarily disconnected you won't be left with an empty session state.

# Import relevant libraries
import streamlit as st
import streamlit_dataframe_editor_global as sde


# Define a class to hold the global state
class GlobalState:

    # Constructor
    def __init__(self):
        pass

    # Method to return all attribute names in the object
    def get_key_names(self):
        return list(self.__dict__.keys())

    # Method to reset the global state. We can safely assume that defaults are defined in the main code, just as we would with Streamlit session state
    def reset_global_state(self):
        for attr in self.get_key_names():  # Create a list to safely iterate
            delattr(self, attr)

    # Implement __setitem__ to support item assignment
    def __setitem__(self, key, value):
        setattr(self, key, value)

    # Optionally, implement __getitem__ to support item access
    def __getitem__(self, key):
        return getattr(self, key, None)
    
    # Implement __contains__ to support 'in' checks
    def __contains__(self, key):
        return hasattr(self, key)


# Need this function to assign to the global state via the session state while avoiding the Streamlit "every other" issue
def assign_to_global_state(global_state, common_key, callback=None, args=(), kwargs=None):
    if kwargs is None:
        kwargs = {}
    global_state[common_key] = st.session_state[common_key]
    del st.session_state[common_key]  # don't need this anymore and in fact if we didn't delete it, we'd likely have problems since widgets would then be set by both the initial value and the session state key
    if callback is not None:
        callback(*args, **kwargs)


# Function to create or retrieve the global state instance
@st.cache_resource
def initialize_global_state():
    return GlobalState()


# Get the global state and fast forward the editable dataframes if necessary
def get_global_state():
    global_state = initialize_global_state()
    if 'fresh_session_state' not in st.session_state:
        for key in global_state.get_key_names():
            if key.endswith('__dataframe_editor'):
                key_changes_dict = key
                key_df_orig = key.removesuffix('_changes_dict' + '__dataframe_editor')
                sde.fast_forward_editable_dataframe_in_state(global_state, key_df_orig, key_changes_dict)
        st.session_state['fresh_session_state'] = False
    return global_state
