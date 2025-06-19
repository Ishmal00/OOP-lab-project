import streamlit as st
from handler import FileHandler
from csv_handler import CSVHandler

file_handler = FileHandler()

st.set_page_config(page_title="OOP File Handling Project", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

# Login/signup area
if not st.session_state.logged_in:
    st.title("Login / Sign Up")

    option = st.radio("Select Option", ["Login", "Sign Up"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Submit"):
        if option == "Sign Up":
            success, msg = file_handler.sign_up(username, password)
            st.success(msg) if success else st.error(msg)
        else:
            success, msg = file_handler.login(username, password)
            if success:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success(msg)
            else:
                st.error(msg)
else:
    st.sidebar.title(f" Welcome, {st.session_state.username}")
    action = st.sidebar.radio("Choose Action", [" Text Record Handling", "CSV File Handler", "Logout"])

    if action == " Logout":
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    elif action == "Text Record Handling":
        st.title(" Your Text Records")

        data = file_handler.get_user_data(st.session_state.username)
        st.write("### Existing Records:")
        for i, record in enumerate(data):
            st.write(f"{i+1}. {record}")

        st.subheader("Add New Record")
        new_record = st.text_area("Enter text to save")
        if st.button("Add Record"):
            if new_record.strip():
                file_handler.add_record(st.session_state.username, new_record.strip())
                st.success("Record added!")
                st.rerun()

        st.subheader("Update Record")
        index_to_update = st.number_input("Enter record number to update", min_value=1, max_value=len(data), step=1)
        new_content = st.text_area("Enter new content")
        if st.button("Update"):
            file_handler.update_record(st.session_state.username, index_to_update - 1, new_content)
            st.success("Record updated!")
            st.rerun()

        st.subheader("Delete Record")
        index_to_delete = st.number_input("Enter record number to delete", min_value=1, max_value=len(data), step=1)
        if st.button("Delete"):
            file_handler.delete_record(st.session_state.username, index_to_delete - 1)
            st.success("Record deleted!")
            st.rerun()

    elif action == "CSV File Handler":
        st.title("CSV File Handler")

        uploaded = st.file_uploader(" Upload CSV File", type=["csv"])
        if uploaded:
            handler = CSVHandler(uploaded)
            success, msg = handler.load_data()
            if success:
                st.success("CSV Loaded Successfully")

                # Info
                shape, columns = handler.get_info()
                st.write(f"**Rows:** {shape[0]}, **Columns:** {shape[1]}")
                st.write("**Column Names:**", columns)

                # Data Preview
                st.subheader("Preview")
                st.dataframe(handler.df)

                # Summary
                st.subheader(" Summary")
                st.dataframe(handler.get_summary())

                # Search
                st.subheader(" Filter Column")
                col = st.selectbox("Select Column", columns)
                keyword = st.text_input("Search Keyword")
                if keyword:
                    filtered = handler.get_filtered(col, keyword)
                    st.dataframe(filtered)

                # Chart
                st.subheader("Visualize")
                col2 = st.selectbox("Choose column to plot", columns)
                chart_data = handler.get_chart_data(col2)
                if chart_data is not None:
                    st.bar_chart(chart_data)

                # Download
                st.subheader("Download Filtered CSV")
                st.download_button("Download", data=handler.download_csv(), file_name="filtered_data.csv", mime="text/csv")

            else:
                st.error(f"Failed to load file: {msg}")
