import streamlit as st
import pandas as pd
import datetime

# 1. Page Configuration
st.set_page_config(page_title="Smart Study Planner", page_icon="📅", layout="wide")
st.title("📅 My Smart Homework & Study Tracker")
st.write("Keep track of your school assignments, exams, and daily priorities in one place.")

# 2. Initialize Data Storage (Keeps track of tasks while the app runs)
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# 3. Create Two Columns: Left for adding tasks, Right for viewing them
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("➕ Add New Assignment")
    
    # Input fields for the user
    task_name = st.text_input("Assignment/Task Name:", placeholder="e.g., Math Exercises Page 42")
    subject = st.selectbox("Subject:", ["Math", "Science", "English", "History", "Coding", "Other"])
    due_date = st.date_input("Due Date:", datetime.date.today())
    priority = st.radio("Priority Level:", ["🔴 High", "🟡 Medium", "🟢 Low"])
    
    # Button to add the task to our list
    if st.button("🚀 Save Task", use_container_width=True):
        if task_name: # Make sure they typed something
            new_task = {
                "Task": task_name,
                "Subject": subject,
                "Due Date": due_date.strftime("%Y-%m-%d"),
                "Priority": priority,
                "Status": "❌ Incomplete"
            }
            st.session_state.tasks.append(new_task)
            st.success(f"Added: {task_name}")
            st.status("Updating your dashboard...").update(state="complete")
        else:
            st.error("Please type a task name first!")

with col2:
    st.subheader("📋 Your Current Agenda")
    
    if len(st.session_state.tasks) == 0:
        st.info("Nice job! Your schedule is clear. Add a task on the left to get started.")
    else:
        # Convert our task list into a beautiful interactive table (DataFrame)
        df = pd.DataFrame(st.session_state.tasks)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Action Center to mark things as done or clear the list
        st.write("---")
        if st.button("🗑️ Clear All Finished Tasks"):
            st.session_state.tasks = []
            st.rerun()

# 4. Motivation Sidebar
st.sidebar.subheader("💡 Coding Goal Tracker")
st.sidebar.write("Your typing skills make managing your schedule incredibly fast. Keep up the great work!")
