# streamlit-global-state

Thanks to @Asaurus1 for the [idea here](https://github.com/streamlit/streamlit/issues/9031#issuecomment-2224333642).

Note the example in this repo (which can be run using `streamlit run app.py`) includes an example of preserving `st.data_editor()` objects between pages using the global state using [this module](https://github.com/andrew-weisman/streamlit-dataframe-editor/blob/main/streamlit_dataframe_editor_global.py). If you don't care about that, just delete everything having to do with the `streamlit_dataframe_editor_global` module in the examples and then you have a purely idiomatic set of examples for using the global state.
