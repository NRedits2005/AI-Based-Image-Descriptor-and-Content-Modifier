import streamlit as st

st.set_page_config(page_title="NR Portfolio", layout="wide")

st.markdown(
    """
    <style>
    :root {
        --bg: #0b0b0b;
        --card: #161616;
        --accent: #ff8c00;
        --accent-soft: rgba(255, 140, 0, 0.12);
        --text: #f5f5f5;
        --muted: #c7c7c7;
    }
    [data-testid="stAppViewContainer"] {
        background-color: var(--bg);
        color: var(--text);
    }
    [data-testid="stHeader"] {
        background: transparent;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: var(--muted);
        margin-bottom: 1.5rem;
    }
    .accent {
        color: var(--accent);
    }
    .card {
        background: var(--card);
        border: 1px solid #262626;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 0 0 1px rgba(255, 140, 0, 0.08);
    }
    .chip {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        background: var(--accent-soft);
        color: var(--accent);
        font-size: 0.85rem;
        margin: 4px 6px 4px 0;
        border: 1px solid rgba(255, 140, 0, 0.35);
    }
    .cta {
        display: inline-block;
        padding: 12px 18px;
        border-radius: 10px;
        background: var(--accent);
        color: #111111;
        font-weight: 600;
        text-decoration: none;
        margin-right: 12px;
    }
    .secondary {
        background: transparent;
        color: var(--text);
        border: 1px solid var(--accent);
    }
    hr {
        border-color: #2b2b2b;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-title">Naveen Raj <span class="accent">Portfolio</span></div>
    <div class="hero-subtitle">
        AI + Product engineer crafting intelligent experiences, from image understanding to human-centered
        interfaces.
    </div>
    <a class="cta" href="#projects">View Projects</a>
    <a class="cta secondary" href="#contact">Get in Touch</a>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

left, right = st.columns([2, 1], gap="large")
with left:
    st.markdown(
        """
        <div class="card">
            <h3>About</h3>
            <p>
                I design and build AI-powered products that blend analytics, automation, and delightful UX.
                My focus is on shipping reliable, scalable solutions that simplify complex workflows and
                generate measurable value for teams.
            </p>
            <p>
                Recent work includes multimodal assistants, content transformation pipelines, and deployment
                tooling for rapid experimentation.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        """
        <div class="card">
            <h3>Quick Facts</h3>
            <p><strong>Location:</strong> Nagercoil, India</p>
            <p><strong>Focus:</strong> AI/ML, Full-stack, UX Systems</p>
            <p><strong>Availability:</strong> Open to collaborations</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("### Core Skills")
st.markdown(
    """
    <span class="chip">Generative AI</span>
    <span class="chip">Python</span>
    <span class="chip">Streamlit</span>
    <span class="chip">Computer Vision</span>
    <span class="chip">Prompt Engineering</span>
    <span class="chip">Product Strategy</span>
    <span class="chip">Automation</span>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("## Projects")

project_col1, project_col2, project_col3 = st.columns(3, gap="large")

with project_col1:
    st.markdown(
        """
        <div class="card">
            <h4>NR Image Descriptor</h4>
            <p>
                A multimodal assistant that generates rich descriptions from images and enables iterative
                refinements through natural language.
            </p>
            <p class="accent"><strong>Stack:</strong> Gemini · Streamlit · Python</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with project_col2:
    st.markdown(
        """
        <div class="card">
            <h4>Content Modifier Studio</h4>
            <p>
                A workflow to transform product content into multiple tones and formats while preserving brand
                voice.
            </p>
            <p class="accent"><strong>Stack:</strong> LLMs · Automation · UI Systems</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with project_col3:
    st.markdown(
        """
        <div class="card">
            <h4>Insight Dashboard</h4>
            <p>
                Visual analytics for monitoring model outputs, feedback loops, and content quality KPIs.
            </p>
            <p class="accent"><strong>Stack:</strong> Data Viz · Python · Product Analytics</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

st.markdown("## Experience Highlights")
experience_left, experience_right = st.columns([1.3, 1], gap="large")

with experience_left:
    st.markdown(
        """
        <div class="card">
            <h4>Product & AI Leadership</h4>
            <ul>
                <li>Built AI-first workflows that cut manual review time by 40%.</li>
                <li>Designed prompt libraries that improved consistency across multi-team projects.</li>
                <li>Delivered end-to-end prototypes from research to deployment.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with experience_right:
    st.markdown(
        """
        <div class="card">
            <h4>Tooling & Operations</h4>
            <ul>
                <li>Automated content QA with human-in-the-loop review flows.</li>
                <li>Created dashboards for visibility into model performance.</li>
                <li>Optimized pipelines for faster experimentation cycles.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("## Contact")
contact_left, contact_right = st.columns([1.4, 1], gap="large")

with contact_left:
    st.markdown(
        """
        <div class="card">
            <h4>Let's build something bold.</h4>
            <p>
                I love collaborating on ambitious AI and product initiatives. Reach out for partnerships,
                consulting, or full-time opportunities.
            </p>
            <p><strong>Email:</strong> naveenmadhan86@gmail.com</p>
            <p><strong>Phone:</strong> +91 7501199896</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with contact_right:
    st.markdown(
        """
        <div class="card">
            <h4>Availability</h4>
            <p>Open for select projects starting next month.</p>
            <p class="accent"><strong>Preferred:</strong> AI product strategy, prototyping, UX systems</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
