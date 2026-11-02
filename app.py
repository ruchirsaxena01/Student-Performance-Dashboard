import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="EduAnalytics | Student Performance",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# DESIGN SYSTEM — PREMIUM LIGHT SAAS
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

:root {
    --ink: #172554;
    --muted: #64748B;
    --blue: #2563EB;
    --line: #E7ECF4;
    --surface: #FFFFFF;
}
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
.stApp {
    background:
      radial-gradient(circle at 88% 2%, rgba(191,219,254,.32), transparent 27%),
      linear-gradient(135deg, #F7F9FD 0%, #F1F5FB 100%);
    color: #1E293B;
}
.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
h1, h2, h3, h4 {
    font-family: 'Manrope', sans-serif !important;
    color: var(--ink) !important;
    letter-spacing: -0.035em;
}
p, label, .stCaption { color: #526078; }
[data-testid="stSidebar"] {
    background: rgba(255,255,255,.96);
    border-right: 1px solid var(--line);
}
[data-testid="stSidebar"] > div:first-child { padding-top: 1.5rem; }
[data-testid="stSidebar"] h1 {
    font-family: 'Manrope', sans-serif;
    font-size: 1.55rem;
    letter-spacing: -0.05em;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    padding: .45rem .55rem;
    border-radius: 9px;
}
[data-testid="stMetric"] {
    background: linear-gradient(145deg, #FFFFFF 0%, #F8FAFF 100%);
    border: 1px solid #E4EAF5;
    border-radius: 16px;
    padding: 18px 20px;
    box-shadow: 0 5px 18px rgba(30,64,175,.045);
    min-height: 122px;
}
[data-testid="stMetricLabel"] {
    color: #64748B !important;
    font-size: .82rem !important;
    font-weight: 600 !important;
}
[data-testid="stMetricValue"] {
    color: #1D4ED8 !important;
    font-family: 'Manrope', sans-serif !important;
    font-weight: 800 !important;
}
[data-testid="stMetricDelta"] { font-size: .78rem !important; }
div[data-testid="stVerticalBlock"] > div:has(> .section-anchor) { gap: .2rem; }
.stButton > button, .stDownloadButton > button {
    border: 0;
    border-radius: 10px;
    color: white;
    font-weight: 700;
    background: linear-gradient(115deg, #2563EB, #4F46E5);
    padding: .62rem 1rem;
    box-shadow: 0 5px 13px rgba(37,99,235,.16);
    transition: all .18s ease;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 8px 18px rgba(37,99,235,.22);
}
.stTextInput input, .stNumberInput input {
    border-radius: 10px;
    background: #FFFFFF;
}
.stSelectbox [data-baseweb="select"] > div,
.stMultiSelect [data-baseweb="select"] > div {
    border-radius: 10px;
    background: #FFFFFF;
}
[data-testid="stDataFrame"], [data-testid="stTable"] {
    border: 1px solid #E5EAF2;
    border-radius: 12px;
    overflow: hidden;
}
hr { border-color: #E4EAF3; }
[data-testid="stAlert"] { border-radius: 12px; }
div[data-testid="stPlotlyChart"] {
    background: #FFFFFF;
    border: 1px solid #E8EDF5;
    border-radius: 16px;
    padding: 8px 8px 0 8px;
    box-shadow: 0 5px 18px rgba(30,64,175,.035);
}
.hero {
    background: linear-gradient(115deg, #172554 0%, #1D4ED8 65%, #4F46E5 100%);
    border-radius: 20px;
    padding: 27px 30px;
    color: white;
    margin-bottom: 22px;
    box-shadow: 0 12px 28px rgba(30,64,175,.16);
}
.hero h1 { color: white !important; margin: 0 0 6px 0; font-size: 2rem; }
.hero p { color: rgba(255,255,255,.82) !important; margin: 0; font-size: .98rem; }
.hero-tag {
    display: inline-block;
    color: #DBEAFE;
    border: 1px solid rgba(219,234,254,.35);
    background: rgba(255,255,255,.10);
    border-radius: 100px;
    padding: 5px 11px;
    font-size: .72rem;
    font-weight: 700;
    letter-spacing: .08em;
    margin-bottom: 12px;
}
.section-note {
    color: #718096;
    font-size: .88rem;
    margin-top: -8px;
    margin-bottom: 14px;
}
.sidebar-brand {
    background: linear-gradient(135deg, #EFF6FF, #EEF2FF);
    border: 1px solid #DBEAFE;
    border-radius: 15px;
    padding: 15px 14px;
    margin-bottom: 14px;
}
.sidebar-brand small {
    color: #64748B;
    font-size: .68rem;
    letter-spacing: .11em;
    font-weight: 700;
}
.sidebar-brand div {
    color: #1E3A8A;
    font-family: 'Manrope', sans-serif;
    font-size: 1.3rem;
    font-weight: 800;
}
.footer {
    color: #94A3B8;
    font-size: .78rem;
    text-align: center;
    padding: 18px 0 0 0;
}
@media (max-width: 800px) {
    .block-container { padding: 1rem 1rem 2rem 1rem; }
    .hero { padding: 21px; }
    .hero h1 { font-size: 1.55rem; }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# CHART THEME
# =========================================================
def style_chart(fig, height=400):
    fig.update_layout(
        template="plotly_white",
        height=height,
        paper_bgcolor="rgba(255,255,255,0)",
        plot_bgcolor="#FFFFFF",
        font=dict(family="DM Sans, Arial", color="#475569", size=12),
        title_font=dict(family="Manrope, Arial", color="#172554", size=17),
        hoverlabel=dict(
            bgcolor="#172554",
            bordercolor="#172554",
            font=dict(color="#FFFFFF", size=12)
        ),
        legend=dict(
            bgcolor="rgba(255,255,255,0)",
            font=dict(color="#475569")
        ),
        margin=dict(l=35, r=25, t=55, b=40)
    )
    fig.update_xaxes(
        showgrid=False,
        zeroline=False,
        linecolor="#E2E8F0",
        tickfont=dict(color="#64748B")
    )
    fig.update_yaxes(
        showgrid=True,
        gridcolor="#EDF1F7",
        zeroline=False,
        linecolor="#E2E8F0",
        tickfont=dict(color="#64748B")
    )
    return fig


def page_header(title, subtitle, tag="EDUANALYTICS"):
    st.markdown(
        f"""
        <div class="hero">
          <div class="hero-tag">{tag}</div>
          <h1>{title}</h1>
          <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def section_heading(title, subtitle=None):
    st.markdown(f"### {title}")
    if subtitle:
        st.markdown(f'<div class="section-note">{subtitle}</div>', unsafe_allow_html=True)


# =========================================================
# DATA LOADING + VALIDATION
# =========================================================
@st.cache_data
def load_data():
    data = pd.read_csv("DA003_student_data.csv")
    required = [
        "Student_ID", "Attendance_Percentage", "Study_Hours_Per_Day",
        "Maths_Marks", "English_Marks", "Science_Marks",
        "Computer_Marks", "Total_Marks", "Average_Marks", "Result"
    ]
    missing = [column for column in required if column not in data.columns]
    if missing:
        raise ValueError("Dataset is missing required columns: " + ", ".join(missing))
    return data


try:
    df = load_data()
except FileNotFoundError:
    st.error("DA003_student_data.csv was not found. Keep the CSV file in the same folder as app.py.")
    st.stop()
except Exception as error:
    st.error(f"Unable to load the dataset: {error}")
    st.stop()


SUBJECTS = {
    "Mathematics": "Maths_Marks",
    "English": "English_Marks",
    "Science": "Science_Marks",
    "Computer": "Computer_Marks"
}
NUMERIC_COLUMNS = [
    "Attendance_Percentage", "Study_Hours_Per_Day",
    "Maths_Marks", "English_Marks", "Science_Marks",
    "Computer_Marks", "Average_Marks"
]


# =========================================================
# SIDEBAR / NAVIGATION / GLOBAL FILTERS
# =========================================================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
      <small>STUDENT PERFORMANCE SYSTEM</small>
      <div>🎓 EduAnalytics</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### Workspace")
    page = st.radio(
        "Navigation",
        ["Overview", "Subject Analysis", "Student Insights", "Correlation Analysis"],
        label_visibility="collapsed"
    )

    st.divider()
    st.markdown("#### Global filters")

    min_attendance, max_attendance = st.slider(
        "Attendance range (%)",
        min_value=0,
        max_value=100,
        value=(0, 100)
    )
    result_filter = st.selectbox("Student result", ["All", "Pass", "Fail"])

    st.divider()
    st.caption("PROJECT  ·  DA-003")
    st.caption(f"DATASET  ·  {len(df):,} synthetic records")
    st.caption("Built with Python · Streamlit · Plotly")


filtered_df = df[
    df["Attendance_Percentage"].between(min_attendance, max_attendance)
].copy()

if result_filter != "All":
    filtered_df = filtered_df[filtered_df["Result"] == result_filter]

if filtered_df.empty:
    st.warning("No students match the selected filters. Adjust the filters in the sidebar.")
    st.stop()


# =========================================================
# OVERVIEW PAGE
# =========================================================
if page == "Overview":
    page_header(
        "Academic Performance Overview",
        "A clear snapshot of student outcomes, subject performance and learning habits."
    )

    total_students = len(filtered_df)
    average_marks = filtered_df["Average_Marks"].mean()
    pass_percentage = filtered_df["Result"].eq("Pass").mean() * 100
    average_attendance = filtered_df["Attendance_Percentage"].mean()
    subject_averages = filtered_df[list(SUBJECTS.values())].mean()
    top_subject = subject_averages.idxmax().replace("_Marks", "")

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("👨‍🎓 Students in view", f"{total_students:,}")
    k2.metric("📊 Average marks", f"{average_marks:.2f} / 100")
    k3.metric("✅ Pass percentage", f"{pass_percentage:.1f}%")
    k4.metric("🏆 Top subject", top_subject)

    st.markdown("")
    st.caption(f"Average attendance across the current selection: **{average_attendance:.1f}%**")
    st.divider()

    section_heading("Subject performance", "Average marks across the four academic subjects.")
    subject_data = (
        subject_averages.rename(index={v: k for k, v in SUBJECTS.items()})
        .rename_axis("Subject").reset_index(name="Average Marks")
    )
    subject_data["Highlight"] = np.where(
        subject_data["Average Marks"] == subject_data["Average Marks"].max(),
        "Highest average", "Other subjects"
    )
    fig = px.bar(
        subject_data, x="Subject", y="Average Marks",
        color="Highlight",
        color_discrete_map={"Highest average": "#2563EB", "Other subjects": "#A5B4FC"},
        text="Average Marks"
    )
    fig.update_traces(texttemplate="%{text:.1f}", textposition="outside", cliponaxis=False)
    fig.update_yaxes(title="Average marks", range=[0, 110])
    fig.update_xaxes(title=None)
    fig.update_layout(showlegend=False, bargap=.48)
    st.plotly_chart(style_chart(fig, 390), use_container_width=True)

    st.divider()
    section_heading("Student habits & performance", "Explore how attendance and daily study time vary with average marks.")
    left, right = st.columns(2)

    with left:
        st.markdown("**Attendance vs average marks**")
        fig_attendance = px.scatter(
            filtered_df, x="Attendance_Percentage", y="Average_Marks",
            color="Average_Marks", color_continuous_scale="Blues",
            hover_data=["Student_ID"], opacity=.78
        )
        fig_attendance.update_layout(coloraxis_colorbar_title="Average")
        fig_attendance.update_xaxes(title="Attendance (%)")
        fig_attendance.update_yaxes(title="Average marks")
        st.plotly_chart(style_chart(fig_attendance, 370), use_container_width=True)

    with right:
        st.markdown("**Daily study hours vs average marks**")
        fig_study = px.scatter(
            filtered_df, x="Study_Hours_Per_Day", y="Average_Marks",
            color="Attendance_Percentage", color_continuous_scale="Viridis",
            hover_data=["Student_ID"], opacity=.78
        )
        fig_study.update_layout(coloraxis_colorbar_title="Attendance")
        fig_study.update_xaxes(title="Study hours per day")
        fig_study.update_yaxes(title="Average marks")
        st.plotly_chart(style_chart(fig_study, 370), use_container_width=True)

    st.divider()
    section_heading("Correlation snapshot", "Associations between learning habits, subject marks and overall average.")
    correlation = filtered_df[NUMERIC_COLUMNS].corr()
    fig_corr = px.imshow(
        correlation, text_auto=".2f", color_continuous_scale="RdBu_r",
        zmin=-1, zmax=1, aspect="auto"
    )
    fig_corr.update_layout(coloraxis_colorbar_title="Correlation")
    st.plotly_chart(style_chart(fig_corr, 520), use_container_width=True)
    st.info("Correlation describes association between variables; it does not prove that one variable causes another.")

    st.divider()
    section_heading("Student records", "Search the filtered dataset and export the records currently displayed.")
    search_id = st.text_input("Search by Student ID", placeholder="Type a student ID...")
    display_df = filtered_df.copy()
    if search_id.strip():
        display_df = display_df[
            display_df["Student_ID"].astype(str).str.contains(search_id.strip(), case=False, na=False)
        ]

    st.caption(f"Showing **{len(display_df):,}** of **{len(filtered_df):,}** filtered records")
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    st.download_button(
        "⬇️ Download filtered student data",
        data=display_df.to_csv(index=False).encode("utf-8"),
        file_name="student_performance_report.csv",
        mime="text/csv"
    )


# =========================================================
# SUBJECT ANALYSIS PAGE
# =========================================================
elif page == "Subject Analysis":
    page_header(
        "Subject Analysis",
        "Compare subject-level outcomes and identify stronger and weaker areas.",
        "ACADEMIC BREAKDOWN"
    )

    subject_averages = filtered_df[list(SUBJECTS.values())].mean()
    chart_data = pd.DataFrame({
        "Subject": list(SUBJECTS.keys()),
        "Average Marks": [subject_averages[column] for column in SUBJECTS.values()]
    }).sort_values("Average Marks", ascending=False)

    best = chart_data.iloc[0]
    weakest = chart_data.iloc[-1]
    c1, c2, c3 = st.columns(3)
    c1.metric("🏆 Highest average", best["Subject"], f'{best["Average Marks"]:.2f} marks')
    c2.metric("📉 Lowest average", weakest["Subject"], f'{weakest["Average Marks"]:.2f} marks')
    c3.metric("📚 Subjects analysed", len(chart_data))

    st.divider()
    section_heading("Average marks by subject", "Subjects are ordered from highest to lowest average.")
    fig = px.bar(
        chart_data, x="Subject", y="Average Marks",
        color="Average Marks", color_continuous_scale="Blues",
        text="Average Marks"
    )
    fig.update_traces(texttemplate="%{text:.2f}", textposition="outside", cliponaxis=False)
    fig.update_yaxes(title="Average marks", range=[0, 110])
    fig.update_xaxes(title=None)
    fig.update_layout(coloraxis_showscale=False, bargap=.42)
    st.plotly_chart(style_chart(fig, 440), use_container_width=True)

    st.divider()
    section_heading("Subject performance summary")
    st.dataframe(
        chart_data.reset_index(drop=True).style.format({"Average Marks": "{:.2f}"}),
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# STUDENT INSIGHTS PAGE
# =========================================================
elif page == "Student Insights":
    page_header(
        "Student Insights",
        "Review result distribution and explore the highest-performing student records.",
        "STUDENT EXPLORER"
    )

    total_students = len(filtered_df)
    highest_average = filtered_df["Average_Marks"].max()
    lowest_average = filtered_df["Average_Marks"].min()
    average_study_hours = filtered_df["Study_Hours_Per_Day"].mean()
    average_attendance = filtered_df["Attendance_Percentage"].mean()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("👨‍🎓 Students", f"{total_students:,}")
    c2.metric("Highest average", f"{highest_average:.2f}")
    c3.metric("Average study time", f"{average_study_hours:.2f} hrs/day")
    c4.metric("Average attendance", f"{average_attendance:.1f}%")

    st.divider()
    left, right = st.columns([1, 1.25])

    with left:
        section_heading("Pass vs fail", "Distribution within the current filtered group.")
        result_counts = (
            filtered_df["Result"].value_counts()
            .reindex(["Pass", "Fail"], fill_value=0)
            .rename_axis("Result").reset_index(name="Students")
        )
        fig_result = px.pie(
            result_counts, names="Result", values="Students", hole=.62,
            color="Result",
            color_discrete_map={"Pass": "#16A34A", "Fail": "#F97316"}
        )
        fig_result.update_traces(
            textposition="inside", textinfo="percent+label",
            marker=dict(line=dict(color="#FFFFFF", width=3))
        )
        st.plotly_chart(style_chart(fig_result, 390), use_container_width=True)

    with right:
        section_heading("Top 10 performing students", "Ranked by average marks in the current selection.")
        top_students = filtered_df.nlargest(10, "Average_Marks")[
            ["Student_ID", "Average_Marks", "Attendance_Percentage",
             "Study_Hours_Per_Day", "Result"]
        ].reset_index(drop=True)
        st.dataframe(
            top_students.style.format({
                "Average_Marks": "{:.2f}",
                "Attendance_Percentage": "{:.1f}%",
                "Study_Hours_Per_Day": "{:.1f}"
            }),
            use_container_width=True,
            hide_index=True,
            height=390
        )

    st.divider()
    section_heading("Find a student", "Enter a Student ID to view the matching academic record.")
    student_id = st.text_input("Student ID lookup", placeholder="Enter exact or partial Student ID")
    if student_id.strip():
        matches = filtered_df[
            filtered_df["Student_ID"].astype(str).str.contains(
                student_id.strip(), case=False, na=False
            )
        ]
        if matches.empty:
            st.warning("No matching student was found in the current filtered selection.")
        else:
            st.success(f"Found {len(matches)} matching record(s).")
            st.dataframe(matches, use_container_width=True, hide_index=True)

    st.info("This project uses synthetic student records for academic demonstration. The results should not be treated as real institutional findings.")


# =========================================================
# CORRELATION ANALYSIS PAGE
# =========================================================
elif page == "Correlation Analysis":
    page_header(
        "Correlation Analysis",
        "Explore the direction and strength of linear relationships between academic variables.",
        "RELATIONSHIP EXPLORER"
    )

    section_heading("Correlation heatmap", "Values closer to +1 or -1 indicate stronger linear association.")
    correlation = filtered_df[NUMERIC_COLUMNS].corr()
    fig_corr = px.imshow(
        correlation, text_auto=".2f", color_continuous_scale="RdBu_r",
        zmin=-1, zmax=1, aspect="auto"
    )
    fig_corr.update_layout(coloraxis_colorbar_title="Correlation")
    st.plotly_chart(style_chart(fig_corr, 590), use_container_width=True)

    st.divider()
    section_heading("Strongest relationships with average marks")
    average_corr = (
        correlation["Average_Marks"]
        .drop("Average_Marks")
        .sort_values(key=lambda values: values.abs(), ascending=False)
        .rename_axis("Variable")
        .reset_index(name="Correlation")
    )
    fig_strength = px.bar(
        average_corr, x="Correlation", y="Variable",
        orientation="h", color="Correlation",
        color_continuous_scale="RdBu", range_color=[-1, 1],
        text="Correlation"
    )
    fig_strength.update_traces(texttemplate="%{text:.2f}", textposition="outside", cliponaxis=False)
    fig_strength.update_xaxes(title="Correlation with average marks", range=[-1.15, 1.15])
    fig_strength.update_yaxes(title=None, autorange="reversed")
    fig_strength.update_layout(coloraxis_showscale=False)
    st.plotly_chart(style_chart(fig_strength, 390), use_container_width=True)

    st.markdown("**Quick interpretation**")
    a, b, c = st.columns(3)
    a.metric(" +1 ", "Strong positive")
    b.metric(" 0 ", "Little/no linear association")
    c.metric(" -1 ", "Strong negative")
    st.info("Correlation indicates association, not causation. Other factors may influence student performance.")


# =========================================================
# FOOTER
# =========================================================
st.markdown(
    '<div class="footer">EDUANALYTICS  ·  DA-003  ·  Student Academic Performance Analysis<br>'
    'Educational dashboard using synthetic student records</div>',
    unsafe_allow_html=True
)