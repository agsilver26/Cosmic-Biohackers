<h1 align="center">LifeLine</h1>
<p align="center">An autonomous, hybrid-offline health monitoring web software built for deep-space astronauts.</p>

**NASA Space Apps Challenge:** Health Monitoring Software for Astronauts on Space Missions

**Team Name:** Cosmic Biohackers

**Live Demo:** TODO

**Demo Video:** TODO

---

## THE PROBLEM
During deep-space astronaut missions (such as a trip to Mars), radio signals take up to **20 minutes each way** to travel between the spacecraft and Earth. This 40-minute round-trip communication lag turns treatable medical issues into life-threatening emergencies.

In critical events like cardiac arrest or severe trauma, brain damage occurs within minutes. Most astronauts are either engineers or pilots and not qualified for instant effective measures. They face a high risk of misdiagnosis oe medication errors. Unlike on the International Space Station, deep-space crews cannot quickly return to an Earth hospital. They only have the spacecraft as their treatment hub. Apart from this, these crews are small. If multiple crew members try taking care of one ill crewmate, this puts the entire mission in danger.

## OUR SOLUTION
**LifeLine** is a Python and Streamlit based web application designed to keep astronauts safe when communication delays prevent real-time support from Mission Control. Instead of waiting up to 40 minutes for a response from Earth, crew members can log their vitals and mental well-being directly into LifeLine for immediate, automated health assessments and long-term trend tracking.

To ensure astronauts always have medical guidance—even during complete communication blackouts, LifeLine features a built-in, health-focused AI assistant. When offline, the AI pulls verified medical protocols directly from a custom NASA-sourced medical PDF compiled by our team. When an internet connection is available, it expands its capabilities to provide detailed, open-source health advice.

---

## KEY FEATURES
* Astronauts input key metrics like heart rate, blood oxygen, bone density, muscle strength, body temperature, and radiation exposure, and receive instant feedback classifying each reading as **Abnormally Low**, **Standard**, or **Abnormally High**.
* A dedicated mental health section evaluates psychological status and provides actionable next step advice to help crews manage isolation and stress.
* Tracks both physical vitals and mental health trends over weeks or months, generating visual trends and downloadable reports for ongoing monitoring or delayed review by flight surgeons.
* Also contains a strictly health centered AI chatbot that answers crew questions using a preloaded, NASA-based medical PDF when offline, and seamlessly switches to detailed open source medical guidance when connections are restored.

---

## SOME SNIPS WITH THE PROGRAM IN ACTION

**Access Code Login:**
[Login Screen] we paste image link here

**Main Dashboard:**
[Dashboard] we paste image link here

**Abnormal Alert & Guidance:**
[Alert Screen] we paste image link here

---

## TECH STACK
* **Language:** Python
* **Web Framework / UI:** Streamlit
* **Processing Data and Analyzing Trends:** Pandas, NumPy
* **AI & Language Model:** Groq API
* **Offline Knowledge:** PyPDF (for searching through our custom NASA-based medical PDF)
* **Data Storage & Reporting:** JSON, Base64 (for downloadable trend reports)

---

## HOW TO RUN THIS PROJECT

1. Clone or download this repository to your computer and open a terminal inside the `project` folder.
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your AI API key:
   Create a `.streamlit/secrets.toml` file and add your Groq API key so the AI agent can connect. *(THIS IS A CRUCIAL STEP!)*
4. Launch Streamlit:
   ```bash
   streamlit run project.py
   ```
5. The dashboard will automatically open in your web browser at `http://localhost:8501`.

**Demo Astronaut Access Codes:**
Enter any of the codes below on the login screen. Each code opens an isolated profile so individual crew data stays separate:
* `6225` – Sohail
* `9653` – Yasmeen
* `3245` – Ahmed

---

## NASA RESOURCES USED
* https://www.nasa.gov/reference/risk-of-cardiovascular-adaptations/
* https://www.nasa.gov/reference/risk-of-hypoxia/
* https://www.nasa.gov/reference/risk-of-reduced-cardiorespiratory-and-musculoskeletal-fitness/
* https://www.nasa.gov/reference/risk-of-spaceflight-induced-bone-changes/
* https://data.nasa.gov/dataset/immediate-transcriptional-changes-in-response-to-high-dose-radiation-exposure-5977c
* https://data.nasa.gov/dataset/heart-flies-effect-of-microgravity-on-heart-function-in-drosophila-41550
* https://www.nasa.gov/reference/about-human-factors-and-behavioral-performance/
* https://data.nasa.gov/dataset/spaceflight-induced-sts-62-vertebral-bone-loss-in-ovariectomized-rats-is-associated-with-i
* https://data.nasa.gov/dataset/influence-of-gonadectomy-on-muscle-health-in-micro-and-partial-gravity-environments-in-rat-92e74
* https://data.nasa.gov/dataset/dose-dependent-skeletal-deficits-due-to-varied-reductions-in-mechanical-loading-in-rats-ti
* https://data.nasa.gov/dataset/spaceflight-induces-systemic-effects-on-extracellular-matrix-and-immune-system-in-differen-a0fab

---

## TEAM
* **Sohail Ahmad Jamil** – Building the AI and Designing
* **Ahmad Gulfam** – Worked on coding the main file
* **Yasmeen Almawlani** – Handled all the research based work of the project.
