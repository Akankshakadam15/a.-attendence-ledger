import streamlit as st
import datetime

# Title
st.title("🎓 Student Attendance Ledger")

# Data structure to hold student attendance in session state
if "attendance_ledger" not in st.session_state:
    st.session_state.attendance_ledger = {}

attendance_ledger = st.session_state.attendance_ledger

# Add Student
st.header("➕ Add Student")
new_student = st.text_input("Enter student name")
if st.button("Add Student"):
    if new_student:
        if new_student not in attendance_ledger:
            attendance_ledger[new_student] = {}
            st.success(f"Student '{new_student}' added.")
        else:
            st.warning(f"Student '{new_student}' already exists.")
    else:
        st.error("Please enter a student name.")

# Mark Attendance
st.header("📝 Mark Attendance")
student_names = list(attendance_ledger.keys())
if student_names:
    selected_student = st.selectbox("Select student", student_names)
    status = st.radio("Attendance status", ["Present", "Absent"])
    if st.button("Mark Attendance"):
        date = datetime.date.today().isoformat()
        attendance_ledger[selected_student][date] = status
        st.success(f"Marked {status} for '{selected_student}' on {date}.")
else:
    st.info("No students available. Please add a student first.")

# View Attendance
st.header("📋 View Attendance")
if student_names:
    view_student = st.selectbox("Choose student to view attendance", student_names, key="view")
    if view_student in attendance_ledger:
        records = attendance_ledger[view_student]
        if records:
            st.subheader(f"Attendance for {view_student}")
            for date, status in sorted(records.items()):
                st.write(f"{date}: {status}")
        else:
            st.info("No attendance records yet.")
else:
    st.info("No students available to view.")

# List All Students
st.header("👥 All Students")
if attendance_ledger:
    st.write(list(attendance_ledger.keys()))
else:
    st.info("No students added yet.")
