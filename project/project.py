import streamlit as st
import pandas as pd
import numpy as np
import json
import os
from datetime import datetime, timedelta
import base64
import random
from groq import Groq
from pypdf import PdfReader

# Background video
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def set_background(path="background.mp4"):
    full_path = os.path.join(BASE_DIR, path)
    if not os.path.exists(full_path):
        return
    video = base64.b64encode(open(full_path, "rb").read()).decode()
    st.markdown(f"""
    <style>
    .stApp {{background: transparent; }}
    #bg {{ position: fixed; inset: 0; width: 100vw; height: 100vh;
    object-fit: cover; z-index: -1; opacity: 0.35; }}
    </style>
    <video id="bg" autoplay muted loop playsinline src="data:video/mp4;base64,{video}"></video>
    """, unsafe_allow_html=True)

set_background()

#logo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(BASE_DIR, "logo.png")
if os.path.exists(logo_path):
    st.logo(logo_path)

#sidebar font and visibility
st.markdown("""
<style>
[data-testid="stTextInputRootElement"]:focus-within,
[data-baseweb="input"]:focus-within,
[data-baseweb="base-input"]:focus-within {
    border-color: #4f46e5 !important;
    box-shadow: 0 0 0 1px #4f46e5 !important;
}
[data-testid="stSidebar"] {
    background: rgba(10, 15, 30, 0.2) !important;
    backdrop-filter: blur(5px);
}
[data-testid="stSidebar"] > div:first-child { background: transparent !important; }


[data-testid="stSidebar"] [class*="st-key-nav_"] button p { font-size: 20px !important; }


[data-testid="stSidebar"] [class*="st-key-nav_"] button[kind="primary"],
[data-testid="stSidebar"] [class*="st-key-nav_"] button[data-testid="stBaseButton-primary"] {
    background-color: #4f46e5 !important;
    border-color: #4f46e5 !important;
    color: white !important;
}

[data-testid="stSidebar"] .st-key-logout button {
    background-color: #ef4444 !important;
    border-color: #ef4444 !important;
    color: white !important;
}
[data-testid="stSidebar"] .st-key-logout button:hover {
    background-color: #dc2626 !important;
    border-color: #dc2626 !important;
}
</style>
""", unsafe_allow_html=True)

groq_api = st.secrets["groq_api"]
client = Groq(api_key=groq_api)

#save previous data
file = "health.json"
def load_records():
    if os.path.exists(file):
        with open(file) as f:
            return json.load(f)
    return{}
def save_records(record):
    with open(file, "w") as f:
        json.dump(record, f, indent = 2)

#stored data
<<<<<<< HEAD
astronauts = {"6225": "Sohail", "3245": "Ahmed", "9653": "Yasmeen"}
=======
astronauts = {"6225": "Sohail", "9653": "Yasmeen", "3245": "Ahmed"}
>>>>>>> 269e1cd47b569941b2363127d3785c50991d969f
previous = {"Heart Rate": 72, "Blood Oxygen": 97, "Bone Density": 1.0, "Muscle Strength": 460, "Body Temperature": 36.8, "Radiation": 2.5}
quotes = [
    "Even among the stars, you're never alone.",
    "One small step at a time, astronaut.",
    "Rest is part of the mission too.",
    "You're made of the same Stardust you explore.",
    "Take a breath; the universe can wait a moment.",
    "A little reminder from Earth: you matter.",
]
ranges = {
    "Heart Rate": (60, 100, "bpm"),
    "Blood Oxygen": (95, 100, "%"),
    "Bone Density": (0.8, 1.2, "g/cm^2"),
    "Muscle Strength": (290, 100000, "N"),
    "Body Temperature": (36.1, 37.2, "°C"),
    "Radiation": (2, 3, "μGy")
}
threshold = {
    "Blood Oxygen": 20,
    "Bone Density": 50,
    "Body Temperature": 20,
    "Heart Rate": 50,
    "Muscle Strength": 50,
    "Stress": 50,
    "Sleep": 50,
    "Loneliness": 50,
    "Energy": 50,
}
windows = {"Bone Density": 30, "Radiation": 30}
minimum_readings = 3
mental = ["Stress", "Sleep", "Loneliness", "Energy"]
messages = {
    "Heart Rate": "Persistent heart rate abnormalities detected. Possible cardiovascular strain or physiological stress.",
    "Blood Oxygen": "Repeated low blood oxygen detected. Possible respiratory or oxygenation impairment.",
    "Bone Density": "Progressive bone density decline detected. Possible bone demineralization.",
    "Muscle Strength": "Persistent muscle strength reduction detected. Possible muscle deconditioning.",
    "Body Temperature": "Repeated temperature abnormalities detected. Possible infection, inflammation, or temperature regulation disturbance.",
    "Radiation": "Radiation exposure above the expected range detected in the monthly check. Possible elevated exposure.",
    "Stress": "Persistent high stress detected. Possible psychological strain or adaptation difficulties.",
    "Sleep": "Repeated insufficient sleep detected. Possible sleep disruption and fatigue.",
    "Loneliness": "Persistent loneliness detected. Possible social isolation and psychological strain.",
    "Energy": "Persistent low energy detected. Possible fatigue, inadequate recovery, or psychological strain.",
}
early = {
    "Heart Rate": ["Reduce physical activity temporarily.", "Allow time for rest and recovery.", "Maintain adequate hydration."],
    "Blood Oxygen": ["Sit comfortably and rest.", "Check that the monitoring device is positioned correctly.", "Ensure the cabin oxygen system is functioning normally."],
    "Bone Density": ["Maintain the prescribed resistance and weight-bearing exercise program.", "Follow the approved calcium and vitamin D nutrition plan."],
    "Muscle Strength": ["Follow the scheduled resistance exercise program.", "Allow sufficient recovery between sessions.", "Maintain adequate protein and nutritional intake.", "Monitor exercise performance."],
    "Body Temperature": ["Adjust clothing and environmental comfort.", "Maintain adequate hydration.", "Avoid excessive physical exertion."],
    "Radiation": ["Identify the source of exposure.", "Follow the scheduled dosimetry monitoring.", "Review available shielding and exposure reduction measures."],
    "Stress": ["Take a short break from demanding tasks.", "Practice controlled breathing or relaxation techniques.", "Engage in a preferred recreational activity.", "Maintain communication with crewmates."],
    "Sleep": ["Maintain a consistent sleep schedule.", "Reduce screen exposure before sleeping.", "Reduce unnecessary noise and light.", "Avoid excessive caffeine intake.", "Allow sufficient time for rest."],
    "Loneliness": ["Schedule social activities with crewmates.", "Participate in group recreational activities.", "Keep in touch with family and friends on Earth when possible."],
    "Energy": ["Take a suitable rest period.", "Maintain adequate hydration.", "Eat balanced meals.", "Adjust physical activity according to recovery needs.", "Maintain a consistent sleep schedule."],
}
alert_advice = {
    "Heart Rate": ["Assess for symptoms such as dizziness, chest pain, or breathlessness.", "Review recent activity, hydration, and sleep.", "Perform an ECG if directed by the medical team.", "Follow the prescribed cardiovascular assessment protocol."],
    "Blood Oxygen": ["Assess breathing difficulties, chest discomfort, and dizziness.", "Evaluate cabin oxygen and pressure conditions.", "Follow the spacecraft's respiratory emergency protocol.", "Supplemental oxygen or other treatment should only be given according to medical and mission protocols."],
    "Bone Density": ["Assess exercise intensity and adherence.", "Review nutritional intake and possible deficiencies.", "Medical specialists may need to consider further investigations or treatments."],
    "Muscle Strength": ["Evaluate muscle loss and physical performance.", "Review the resistance training program.", "Consider physiotherapy or a modified exercise plan.", "Assess nutritional status and recovery."],
    "Body Temperature": ["Assess for infection-related symptoms.", "Evaluate cabin temperature and environmental conditions.", "Follow the appropriate infection-control or temperature management protocol."],
    "Radiation": ["Assess the exposure level, duration, and radiation type.", "Follow the radiation emergency protocol.", "Reduce further exposure using approved shielding or relocation procedures.", "Arrange medical evaluation based on the estimated dose."],
    "Stress": ["Identify possible causes such as workload, isolation, or sleep disruption.", "Introduce stress management activities into the daily schedule."],
    "Sleep": ["Review the sleep schedule and workload.", "Evaluate environmental factors affecting sleep.", "Consider sleep monitoring and assessment."],
    "Loneliness": [],
    "Energy": ["Evaluate sleep quality and workload.", "Assess nutritional intake and hydration.", "Investigate possible causes such as anemia or infection."],
}

if "record" not in st.session_state:
    st.session_state.record = load_records()

#Login page:
if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:
    #logo
    c1, c2, c3 = st.columns([1, 2, 1])
    logo_path = os.path.join(BASE_DIR, "logo.png")
    if os.path.exists(logo_path):
        c2.image(logo_path, width=600)

    st.subheader("Log in")
    with st.form("login_form"):
        code = st.text_input("Enter your astronaut code")
        login = st.form_submit_button("Log in")
    if login:
        if code in astronauts:
            st.session_state.user = astronauts[code]
            st.rerun()
        else:
            st.error("Invalid code. Try again.")

else:
    def goto(page):
         st.session_state.section = page
    #menu
    #menu
    pages = ["Dashboard", "Weekly Health Check", "Astronaut Health Report",
            "Heart Rate", "Blood Oxygen", "Bone Density", "Muscle Strength",
            "Body Temperature", "Radiation", "Mental Wellbeing", "Polaris AI"]

    if "section" not in st.session_state:
        st.session_state.section = "Dashboard"

    st.sidebar.header("Menu")
    for page in pages:
        st.sidebar.button(
            page,
            key=f"nav_{page.replace(' ', '_')}",
            use_container_width=True,
            type="primary" if st.session_state.section == page else "secondary",
            on_click=goto,
            args=(page,),
        )

    st.sidebar.divider()
    if st.sidebar.button("Log out", key="logout", use_container_width=True):
        st.session_state.user = None
        st.session_state.pop("messages", None)
        st.rerun()

    section = st.session_state.section

    record = st.session_state.record.setdefault(st.session_state.user, [previous.copy()])
    mind = st.session_state.record.setdefault("_mind", {}).setdefault(st.session_state.user, [])
    latest = record[-1]
    prev = record[-2] if len(record) > 1 else None

    def delta(metric, unit=""):
        if prev is None:
            return None
        diff = latest[metric] - prev[metric]
        if metric == "Radiation":
            return f"{diff:+.2f}{unit}"
        return f"{diff:+.1f}{unit}"

    def chart(metric):
        df = pd.DataFrame(record)[[metric]].tail(15)
        df.index = range(1, len(df)+1)
        st.line_chart(df)

#wellbeing stuff
    lonely = ["Connected", "Mostly connected", "A bit lonely", "Lonely", "Very lonely"]
    energy = {
        "Drained": ("Running on empty, need rest."),
        "Steady Flow": ("Balanced and sustainable."),
        "Energized": ("Alert, sharp, and ready."),
        "Hyper Focused": ("High voltage productivity."),
    }
    factors = ["Heavy Workload", "Great Sleep", "Physical Fatigue", "Crew Time", "Call with family", "Quiet Space"]

    def stress_condition(v):
        if v < 20:
            return "Serene and Calm", "#22d3ee"
        elif v < 40:
            return "Relaxed", "#34d399"
        elif v < 60:
            return "Moderated Stress", "#f590eb"
        elif v < 80:
            return "Elevated Tension", "#f97316"
        else:
            return "High Tension", "#ef4444"

    def stress_bar(v):
        label, colour = stress_condition(v)
        st.markdown(f"""
<div style="position:relative;height:14px;border-radius:8px;margin:22px 6px 30px;
background:linear-gradient(90deg,#6366f1,#22d3ee,#10b981,#f59e0b,#ef4444);">
<div style="position:absolute;left:calc({v}% - 14px);top:-7px;width:28px;height:28px;border-radius:50%;
background:#fff;border:3px solid #0b0f1a;box-shadow:0 0 14px {colour};"></div></div>
<div style="display:flex;justify-content:space-between;align-items:center;">
<span style="color:#22d3ee;"> Serene &amp; Calm</span>
<b style="color:{colour};font-size:20px;">{label}</b>
<span style="color:#ef4444;"> High Tension</span></div>
""", unsafe_allow_html=True)

    def mind_chart(metric):
        df = pd.DataFrame(mind)[[metric]].tail(15)
        df.index = range(1, len(df)+1)
        if len(df) < 2:
            st.info("Save more to see a trend!")
        else:
            st.line_chart(df)



    # Floating Polaris AI button
    if os.path.exists("iconAI.png"):
        with open("iconAI.png", "rb") as img_file:
            ai_image = base64.b64encode(img_file.read()).decode()

        st.markdown(f"""
        <style>
        div.st-key-polaris_float_button {{
            position: fixed;
            bottom: 25px;
            right: 25px;
            z-index: 999999;
        }}

        div.st-key-polaris_float_button button {{
            width: 75px;
            height: 75px;
            border-radius: 50%;
            border: 2px solid #a5b4fc;
            background-color: #000000;
            background-image: url("data:image/png;base64,{ai_image}");
            background-size: 100% 100%;
            background-position: center center;
            background-repeat: no-repeat;
            box-shadow: 0 0 20px rgba(168, 85, 247, 0.6);
            transition: all 0.3s ease;
        }}

        div.st-key-polaris_float_button button:hover {{
            transform: scale(1.12);
            box-shadow: 0 0 30px rgba(103, 232, 249, 0.9);
            border-color: #67e8f9;
        }}

        div.st-key-polaris_float_button button p {{
            visibility: hidden;
        }}
        </style>
        """, unsafe_allow_html=True)

        st.button(
            "Polaris AI",
            key="polaris_float_button",
            on_click=goto,
            args=("Polaris AI",)
        )


    no_high = ["Muscle Strength"]   
    no_low = ["Radiation"]          

    def check(metric, value):
        low, high, unit = ranges[metric]
        if value > high and metric not in no_high:
            return "high"
        elif value < low and metric not in no_low:
            return "low"
        return "normal"

    def abnormal(entry):
        result = []
        for m in ranges:
            if m in entry and check(m, entry[m]) != "normal":
                result.append((m, check(m, entry[m]), entry[m]))
        return result

    def alert(items):
        for m, status, value in items:
            low, hi, unit = ranges[m]
            if m in no_high:
                normal = f"at least {low} {unit}"
            else:
                normal = f"{low} to {hi} {unit}"
            st.write(f"*{m}* is *{status}*: {value:g} {unit} (normal {normal})")
            if st.button(f"Read more about {m}", key=f"dlg_{m}", on_click=goto, args=(m,)):
                st.rerun()
    alertmessage = st.dialog("*Danger:* Abnormal reading")(alert) if hasattr(st, "dialog") else None

    def recent(entries, days):
        cutoff = datetime.now() - timedelta(days = days)
        result = []
        for e in entries:
            if "Date" in e:
                date = datetime.strptime(e["Date"], "%Y-%m-%d %H:%M")
                if date >= cutoff:
                    result.append(e)

        return result

    def is_abnormal(metric, e):
        if metric == "Stress":
            return e["Stress"] >= 80
        if metric == "Sleep":
            return e["Sleep"] in [7, 8]
        if metric == "Loneliness":
            return e["Loneliness"] >= 3
        if metric == "Energy":
            return e["Energy"] == "Drained"
        return check(metric, e[metric]) != "normal"

    def assess(metric):
        source = mind if metric in mental else record
        entries = [
            e for e in recent(source, windows.get(metric, 7))
            if metric in e
        ]
        bad = [e for e in entries if is_abnormal(metric, e)]
        if not bad:
            return "None", 0, 0, len(entries)
        pct = len(bad) / len(entries) * 100
        if metric == "Radiation":
            level = "Alert" if is_abnormal(metric, entries[-1]) else "Early"
        elif len(entries) >= minimum_readings and pct >= threshold[metric]:
            level = "Alert"
        else:
            level = "Early"
        return level, pct, len(bad), len(entries)

    def multiplealerts():
        alerting = [m for m in ranges if assess(m)[0] == "Alert"]
        def hit(m, status):
            return m in alerting and m in latest and check(m, latest[m]) == status
        found = []
        if hit("Heart Rate", "high") and hit("Blood Oxygen", "low"):
            found.append("High heart rate + low blood oxygen: Possible hypoxemia, breathlessness and confusion.")
        if hit("Bone Density", "low") and hit("Muscle Strength", "low"):
            found.append("Low bone density + low muscle strength: Possible musculoskeletal deterioration.")
        if hit("Heart Rate", "high") and hit("Body Temperature", "high"):
            found.append("High heart rate + high body temperature: Possible heat stress, dehydration or infection.")
        if hit("Blood Oxygen", "low") and hit("Heart Rate", "high") and "Body Temperature" in alerting:
            found.append("Low blood oxygen + high heart rate + abnormal temperature: Possible respiratory illness or systemic infection.")
        return found

    def show_steps(metric):
        level, pct, bad, total = assess(metric)
        days = windows.get(metric, 7)
        st.subheader(f"Health Check: {metric}")
        if total == 0:
            st.info(f"No readings in the last {days} days yet.")
            return
        if level == "None":
            st.success(f"No abnormalities in the last {days} days.")
            return
        st.caption(f"{bad} of {total} readings abnormal in the last {days} days ({pct:.0f}%).")
        if level == "Early":
            st.warning("Early signs. Try these simple steps:")
            steps = early[metric]
        else:
            st.error(messages[metric])
            steps = alert_advice[metric]
        for n, step in enumerate(steps, 1):
            st.write(f"{n}. {step}")
        st.caption("These are possible health concerns, not a diagnosis. Never take medication or change cabin oxygen or radiation shielding without approved mission protocol and medical supervision.")

    #dashboard
    if section == "Dashboard":
        st.title(f"Welcome, {st.session_state.user}!")
        st.header("Dashboard")
        st.info(random.choice(quotes))



        st.subheader("Enter today's data")
        with st.form("entry"):
            c1, c2 = st.columns(2)
            heart = c1.number_input("Heart Rate (bpm)", 0, 250, 72)
            blood = c2.number_input("Blood Oxygen (%)", 0.0, 1000.0, 97.0, step = 0.1)
            bone = c1.number_input("Bone Density (g/cm^2)", 0.0, 5.0, 1.0, step = 0.1)
            strength = c2.number_input("Muscle Strength (N)", 0.0, 99999.0, 460.0, step = 0.5)
            temperature = c1.number_input("Body Temperature (°C)", 0.0, 100.0, 36.8, step = 0.1, format = "%.2f")
            radiation = c2.number_input("Radiation (μGy)", 0.00, 10.00, 2.50, step = 0.01, format = "%.2f")
            submit = st.form_submit_button("Submit")

        if submit:
            record.append({
                "Heart Rate": heart,
                "Blood Oxygen": blood,
                "Bone Density": bone,
                "Muscle Strength": strength,
                "Body Temperature": temperature,
                "Radiation": radiation,
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M")
            })
            save_records(st.session_state.record)
            flags = abnormal(record[-1])
            if flags and alertmessage:
                alertmessage(flags)


        latest = record[-1]
        prev = record[-2] if len(record) > 1 else None

        st.button("Check Your Psychological Wellbeing.", on_click=goto, args=("Mental Wellbeing",), use_container_width = True)
        st.subheader("Latest Health Summary")
        col1, col2, col3 = st.columns(3)
        col1.metric("Heart Rate", f"{latest['Heart Rate']:.0f} bpm", delta("Heart Rate", " bpm"), delta_color="normal")
        col2.metric("Blood Oxygen", f"{latest['Blood Oxygen']:.1f}%", delta("Blood Oxygen", "%"))
        col3.metric("Bone Density", f"{latest['Bone Density']:.1f} g/cm^2", delta("Bone Density", " g/cm^2"))
        col1.metric("Muscle Strength", f"{latest['Muscle Strength']:.1f} N", delta("Muscle Strength", "N"))
        col2.metric("Body Temperature", f"{latest['Body Temperature']:.1f}°C", delta("Body Temperature", "°C"))
        col3.metric("Radiation", f"{latest['Radiation']:.2f} μGy", delta("Radiation", " μGy"), delta_color="inverse")

        if prev is None:
            st.info("Previous data. Compare with today's readings")

    # Weekly Health Check
    elif section == "Weekly Health Check":

        st.title("Weekly Health Check")
        st.caption("Your personal astronaut health monitoring center.")

        st.info("Review your recent mental wellbeing and physical health readings to identify potential trends.")

        health_metrics = list(ranges.keys()) + mental

        alerts = []
        earlysigns = []
        healthy = []

        for metric in health_metrics:
            level, pct, bad, total = assess(metric)

            if level == "Alert":
                alerts.append(metric)
            elif level == "Early":
                earlysigns.append(metric)
            else:
                healthy.append(metric)

        c1, c2, c3 = st.columns(3)

        c1.metric("Alerts", len(alerts))
        c2.metric("Early Signs", len(earlysigns))
        c3.metric("Stable Metrics", len(healthy))

        st.divider()

        if alerts:
            st.subheader("Attention Required 🚨")

            for metric in alerts:
                if metric in messages:
                    st.error(messages[metric])
                page = (
                    "Mental Wellbeing"
                    if metric in mental
                    else metric
                )
                st.button(
                    f"View {metric}",
                    key=f"weekly_alert{metric}",
                    on_click=goto,
                    args=(page,)
                )

        if earlysigns:
            st.subheader("Early Warning Signs ⚠️")

            for metric in earlysigns:
                st.warning(
                    f"Abnormal readings are appearing for {metric}."
                )
                page = (
                    "Mental Wellbeing"
                    if metric in mental
                    else metric
                )
                st.button(
                    f"Review {metric}",
                    key=f"weekly_early{metric}",
                    on_click=goto,
                    args=(page,)
                )

        if healthy:
            st.subheader("Stable Metrics ✅")

            st.write(", ".join(healthy))

        combined = multiplealerts()
        if combined:
            st.divider()
            st.subheader("Combined Health Alerts")
            for message in combined:
                st.error(message)

        radiation_records = recent(record, 30)
        if not radiation_records:
            st.info("Monthly radiation check is due.")

    #Astronaut Health Report
    elif section == "Astronaut Health Report":

        st.title("Astronaut Health Report")
        st.caption("Comprehensive health monitoring summary")

        period = st.selectbox(
            "Select report period",
            ["Last 7 days", "Last 30 days", "Last 90 days", "All records"]
        )

        if period == "Last 7 days":
            days = 7
        elif period == "Last 30 days":
            days = 30
        elif period == "Last 90 days":
            days = 90
        else:
            days = None

        if days is None:
            report_records = record
            report_mind = mind
        else:
            report_records = recent(record, days)
            report_mind = recent(mind, days)

        st.divider()

        st.subheader("Astronaut Information")
        st.write(f"*Astronaut:* {st.session_state.user}")
        st.write(f"*Report period:* {period}")
        st.write(f"*Physical readings:* {len(report_records)}")
        st.write(f"*Mental wellbeing readings:* {len(report_mind)}")

        st.divider()
        st.subheader("Physical Health History")

        if report_records:
            physical_df = pd.DataFrame(report_records)

            if "Date" in physical_df.columns:
                st.dataframe(
                    physical_df,
                    use_container_width=True,
                    hide_index=True
                )

        st.divider()
        st.subheader("Mental Wellbeing History")

        if report_mind:
            mental_df = pd.DataFrame(report_mind)

            if "Date" in mental_df.columns:
                st.dataframe(
                    mental_df,
                    use_container_width=True,
                    hide_index=True
                )

            latest_mind = report_mind[-1]

        st.divider()
        st.subheader("Combined Health Alerts")

        combined = multiplealerts()

        if combined:
            for message in combined:
                st.warning(message)
        else:
            st.success("No combined alerts currently detected.")

        st.divider()
        st.subheader("Download Report")

        st.caption("This report is not a medical diagnosis.")

        report_html = f"""
        <html>
        <head>
            <title>Astronaut Health Report</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    color: #222;
                }}
                h1, h2 {{
                    color: #243b80;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background: #243b80;
                    color: white;
                }}
                @media print {{
                    button {{ display: none; }}
                }}
            </style>
        </head>
        <body>
            <h1>Astronaut Health Report</h1>
            <h2>Astronaut: {st.session_state.user}</h2>
            <p>Report period: {period}</p>

            <h2>Physical Health</h2>
            {pd.DataFrame(report_records).to_html(index=False)}

            <h2>Mental Wellbeing</h2>
            {pd.DataFrame(report_mind).to_html(index=False)}

            <p>
                This report is generated from recorded monitoring data.
                It is not a medical diagnosis.
            </p>
        </body>
        </html>
        """

        st.download_button(
            "Downloadable Health Report",
            data=report_html,
            file_name="polaris_health_report.html",
            mime="text/html"
        )


    #Heart Rate
    elif section == "Heart Rate":
        st.title("Heart Rate")
        st.metric("Today", f"{latest['Heart Rate']:.0f} bpm", delta("Heart Rate", " bpm"))
        st.subheader("Last 15 days record")
        chart("Heart Rate")
        show_steps("Heart Rate")

    #Blood Oxygen
    elif section == "Blood Oxygen":
        st.title("Blood Oxygen Levels")
        st.metric("Today", f"{latest['Blood Oxygen']:.1f}%", delta("Blood Oxygen", "%"))
        st.subheader("Last 15 days levels")
        chart("Blood Oxygen")
        show_steps("Blood Oxygen")

    #Bone Density
    elif section == "Bone Density":
        st.title("Bone Density")
        st.metric("Today", f"{latest['Bone Density']:.1f} g/cm^2", delta("Bone Density", "g/cm^2"))
        st.subheader("Last 15 days levels")
        chart("Bone Density")
        show_steps("Bone Density")

    #Muscle Strength and Endurance
    elif section == "Muscle Strength":
        st.title("Muscle Strength and Endurance")
        st.metric("Today", f"{latest['Muscle Strength']:.1f} N", delta("Muscle Strength", " N"))
        st.subheader("Last 15 days record")
        chart("Muscle Strength")
        show_steps("Muscle Strength")

    #Body Temperature
    elif section == "Body Temperature":
        st.title("Body Temperature")
        st.metric("Today", f"{latest['Body Temperature']:.1f} °C", delta("Body Temperature", "°C"))
        st.subheader("Last 15 days temperature")
        chart("Body Temperature")
        show_steps("Body Temperature")

    #Radiation
    elif section == "Radiation":
        st.title("Radiation Levels")
        st.metric("Today", f"{latest['Radiation']:.2f} μGy", delta("Radiation", " μGy"), delta_color = "inverse")
        st.subheader("Last 15 days levels")
        chart("Radiation")
        show_steps("Radiation")

    #Mental Well-being
    elif section == "Mental Wellbeing":
        st.title("Mind and Wellbeing")
        tab_check, tab_trend = st.tabs(["Check-in", "Trends"])

        with tab_check:
            with st.container(border = True):
                st.subheader("Stress and Mind State")
                st.caption("Drag along the spectrum!")
                stress = st.slider("Stress level", 0, 100, 50, key = "stress", label_visibility = "collapsed")
                stress_bar(stress)

            with st.container(border = True):
                st.subheader("Sleep and Connection")
                s1, s2 = st.columns(2)
                sleep = s1.slider("Hours slept last night", 0.0, 12.0, 7.0, step = 0.5, key = "sleep")
                lonely_label = s2.select_slider("How connected do you feel?", options=lonely, value="Mostly connected", key="lonely")

            with st.container(border=True):
                st.subheader("Current Energy & Vitality")
                st.caption("Select the card that mirrors your current internal fuel.")
                if "energy" not in st.session_state:
                    st.session_state.energy = "Steady Flow"
                cols = st.columns(2)
                for i, (name, (desc)) in enumerate(energy.items()):
                    with cols[i % 2]:
                        chosen = st.session_state.energy == name
                        if st.button(f"{name}", key=f"energy_{name}", use_container_width=True,
                                     type="primary" if chosen else "secondary"):
                            st.session_state.energy = name
                            st.rerun()
                        st.caption(desc)

            with st.container(border=True):
                st.subheader("Enivironment Drivers")
                st.caption("Tap the factors influencing your mindset right now.")
                if hasattr(st, "boxes"):
                    factors = st.pills("Factors", factors, selectmode = "multi", key = "factors", label_visibility = "collapsed")
                else:
                    factors = st.multiselect("Factors", factors, key = "factors", label_visibility = "collapsed")

            if st.button("Save", type = "primary"):
                mind.append({
                    "Sleep": sleep,
                    "Stress": stress,
                    "Loneliness": lonely.index(lonely_label),
                    "Energy": st.session_state.energy,
                    "Factors": list(factors or []),
                    "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                })
                save_records(st.session_state.record)
                st.success("Saved. Check Trends tab.")

        with tab_trend:
            if not mind:
                st.info("No selections. Please save one.")
            else:
                m = mind[-1]
                p = mind[-2] if len(mind) > 1 else None

                def chg(key, unit = "", nd = 1):
                    if p is None:
                        return None
                    d = round(m[key] - p[key], nd) + 0.0
                    return (f"{d:+.{nd}f}{unit}")
                a1, a2, a3 = st.columns(3)
                a1.metric("Sleep", f"{m['Sleep']:.1f} hrs", chg("Sleep", " hrs"))
                a2.metric("Stress", f"{m['Stress']}%", chg("Stress", nd = 0), delta_color = "inverse")
                a3.metric("Loneliness", lonely[m['Loneliness']], chg("Loneliness", nd = 0), delta_color = "inverse")

                st.write(f"*Energy:* {m['Energy']}")
                st.write(f"*Factors:* {', '.join(m['Factors']) if m['Factors'] else 'None selected'}")

                if m["Sleep"] < 7:
                    st.warning("Sleep was under 7 hours. Aim for 7 to 8 hours.")
                elif m["Stress"] > 80:
                    st.warning("Stress is high. Try a slow-breathing break and consult the flight surgeon.")
                elif m["Loneliness"] >= 3:
                    st.warning("Feeling isolated is normal. Try to schedule a call with family or crew time.")

                st.subheader("Sleep (hrs)")
                mind_chart("Sleep")
                st.subheader("Stress")
                mind_chart("Stress")
                st.subheader("Loneliness")
                mind_chart("Loneliness")
                for name in mental:
                    show_steps(name)

    #polaris ai
    elif section == "Polaris AI":
        st.title("Polaris AI Assistant")
        st.caption("Real-time health monitoring support system.")

        @st.cache_resource
        def loadnextract_pdf(file_path="final_summary.pdf"):
            if not os.path.exists(file_path):
                return ""
            try:
                reader = PdfReader(file_path)
                extractedtext = ""
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        extractedtext += text + "\n"
                return extractedtext
            except Exception:
                return ""

        pdfknowledge = loadnextract_pdf("final_summary.pdf")

        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": f"Hello Astronaut {st.session_state.user}. I am Polaris. How can I help you today?"}
            ]

        # show chat as it goes on
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input("Ask about your biometric status, mission checks, or logs..."):
            # show what user typed
            with st.chat_message("user"):
                st.markdown(prompt)

            # save conversation logs
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("assistant"):
                filler_reply = st.empty()
                full_reply = ""

                system_instruction = (
                    "You are Polaris AI, a medical assistant for astronauts in space.\n"
                    "Use the following health documentation to answer the user's questions first.\n"
                    "If the answer cannot be found in the documentation, use your general knowledge or online databases to answer seamlessly. Strictly stick to the astronaut's wellbeing and politely refuse to answer anything irrelevant.\n\n"
                    f"--- DOCUMENTATION BASELN ---\n{pdfknowledge}\n--- END DOCUMENTATION ---"
                )

                api_messages = [{"role": "system", "content": system_instruction}]
                for m in st.session_state.messages:
                    api_messages.append({"role": m["role"], "content": m["content"]})

                try:
                    completion = client.chat.completions.create(
                        model="openai/gpt-oss-20b",
                        messages=api_messages,
                        stream=True
                    )

                    for chunk in completion:
                        if chunk.choices and len(chunk.choices) > 0:
                            delta_content = chunk.choices[0].delta.content
                            if delta_content:
                                full_reply += delta_content
                                filler_reply.markdown(full_reply + "▌")

                    filler_reply.markdown(full_reply)

                    # save the ai assistant response
                    st.session_state.messages.append({"role": "assistant", "content": full_reply})

                except Exception as e:
                    st.error(f"Failed to communicate with Polaris AI matrix: {e}")