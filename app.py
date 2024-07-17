# app.py

# Import relevant libraries
import streamlit as st
import one
import two
import three
import global_state_lib as gsl

# Main function
def main():

    # Load the global state
    global_state = gsl.get_global_state()

    # Use the new st.naviation()/st.Page() API to create a multi-page app
    pg = st.navigation({
        'first section':
            [st.Page(one.main, title="Home", url_path='home'),
             st.Page(two.main, title="Second page", url_path='two')],
        'second section':
            [st.Page(three.main, title="Third page", url_path='three')],
        })

    # This is needed for the st.dataframe_editor() class (https://github.com/andrew-weisman/streamlit-dataframe-editor) but is also useful for seeing where we are and where we've been
    # This is necessary so we know to "fast forward" the editable dataframe when we return to a page with one on it
    global_state['current_page_name'] = pg.url_path if pg.url_path != '' else 'Home'
    if 'previous_page_name' not in global_state:
        global_state['previous_page_name'] = global_state['current_page_name']

    # On every page, display its title
    st.title(pg.title)

    # Output where we are and where we just were
    st.write(f'Your page location: {global_state["current_page_name"]}')
    st.write(f'Previous page location: {global_state["previous_page_name"]}')

    # Render the select page
    pg.run()

    # Update the previous page location
    global_state['previous_page_name'] = global_state['current_page_name']

# Needed for rendering pages that use multiprocessing (https://docs.python.org/3/library/multiprocessing.html#the-spawn-and-forkserver-start-methods)
if __name__ == '__main__':
    main()
