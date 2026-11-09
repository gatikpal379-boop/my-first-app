import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="AI Ingredient Analyzer Pro", page_icon="🥝", layout="wide")

# 2. 🎨 PREMIUM DESIGN INJECTION (Doodle Watermark Background + Custom Gradient Cards!)
st.html("""
<style>
    /* 🖼️ Set up the full page container with your doodle background layout */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stCanvas"], .main {
        position: relative !important;
        background-color: #FAF9F6 !important; /* Premium off-white clean base */
    }

    /* 🪄 Pure CSS Pseudo-element to make the background doodles look like a clean watermark */
    .stApp::before {
        content: "" !important;
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 100% !important;
        height: 100% !important;
        background-image: url('https://shutterstock.com') !important;
        background-repeat: repeat !important;
        background-size: 550px !important;
        opacity: 0.12 !important; /* Keeps the doodles soft so text stays fully readable */
        pointer-events: none !important;
        z-index: 0 !important;
    }

    /* 🟦 Hide standard system structural background lines */
    [data-testid="stHeader"] {
        background: transparent !important;
        background-color: transparent !important;
    }

    /* 📦 CUSTOM GRADIENT CARDS: Flows from White -> Mint -> Yellow -> Pink -> Purple */
    .premium-gradient-card {
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.95) 0%, 
            rgba(167, 243, 208, 0.9) 25%, 
            rgba(254, 243, 199, 0.9) 50%, 
            rgba(252, 231, 243, 0.9) 75%, 
            rgba(233, 213, 255, 0.95) 100%) !important;
        padding: 30px !important;
        border-radius: 20px !important;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08) !important;
        border: 2px solid rgba(255, 255, 255, 0.8) !important;
        margin-bottom: 25px !important;
        position: relative !important;
        z-index: 10 !important; /* Pushes the cards safely over the doodle canvas layer */
    }

    /* Clean transparent fallback defaults for Streamlit container components */
    [data-testid="stVerticalBlock"] > div, 
    [data-testid="stForm"], 
    .stElementContainer, 
    div[data-testid="stNotification"],
    div[class*="st-emotion-cache"],
    div[data-testid="stBlock"],
    div[data-testid="element-container"],
    .stCustomBlockContainer {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* ✍️ Heavy contrast dark slate typography color variables */
    h1, h2, h3, h4, p, span, label, td, th, div, [data-testid="stWidgetLabel"] p {
        color: #1E293B !important;
        font-family: 'Segoe UI', system-ui, sans-serif !important;
        font-weight: 700 !important;
    }
    
    h1 {
        font-weight: 800 !important;
        color: #0F172A !important;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
        margin-bottom: 5px !important;
    }

    /* Interactive custom stylized form layouts */
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.8) !important;
        color: #1E293B !important;
        border-radius: 10px !important;
        border: 1px solid rgba(0,0,0,0.15) !important;
        font-weight: 600 !important;
    }
    
    .stDataFrame {
        background-color: rgba(255, 255, 255, 0.7) !important;
        border-radius: 12px !important;
    }
</style>
""")

# 3. Main Headline Container Block
st.title("🍔 Advanced Food Nutri-Scanner Pro")
st.write("Type your food ingredients to dynamically run digital laboratory diagnostics and menu analytics.")

# Initialize the main system state inventories
if "kitchen_inventory" not in st.session_state:
    st.session_state.kitchen_inventory = []

# Upgraded data system encompassing both fruits and your new dinner doodle categories
NUTRI_DATA = {
    "banana": {"calories": 105.2, "protein": 1.3, "carbs": 27.1, "fats": 0.3, "vitamin": "Potassium & B6"},
    "mango": {"calories": 99.4, "protein": 1.4, "carbs": 24.8, "fats": 0.6, "vitamin": "Vitamin C & A"},
    "apple": {"calories": 94.6, "protein": 0.5, "carbs": 25.1, "fats": 0.3, "vitamin": "Fiber & Vitamin C"},
    "milk": {"calories": 149.0, "protein": 7.7, "carbs": 11.7, "fats": 8.0, "vitamin": "Calcium & Vitamin D"},
    "honey": {"calories": 64.5, "protein": 0.1, "carbs": 17.3, "fats": 0.0, "vitamin": "Antioxidants"},
    "pizza": {"calories": 285.0, "protein": 12.2, "carbs": 35.6, "fats": 10.4, "vitamin": "Calcium & Sodium"},
    "lobster": {"calories": 128.0, "protein": 27.5, "carbs": 0.0, "fats": 1.2, "vitamin": "Zinc & Vitamin B12"},
    "croissant": {"calories": 231.0, "protein": 4.7, "carbs": 26.1, "fats": 12.0, "vitamin": "Iron & Energy"},
    "salt": {"calories": 0.0, "protein": 0.0, "carbs": 0.0, "fats": 0.0, "vitamin": "Sodium Mineral"},
    "cocoa powder": {"calories": 12.1, "protein": 1.0, "carbs": 3.1, "fats": 0.7, "vitamin": "Iron & Magnesium"}
}

col1, col2 = st.columns(2)

with col1:
    # 🛒 Wrap inputs inside your pastel gradient layout block card container
    st.markdown('<div class="premium-gradient-card">', unsafe_html=True)
    st.subheader("🛒 Add Menu Ingredient")
    
    name_input = st.text_input("🍳 Ingredient / Dish Name:", placeholder="e.g., Banana, Pizza, Lobster, Croissant", key="name_box").strip().lower()
    qty_input = st.number_input("🔢 Quantity Count (Whole Numbers):", min_value=1, max_value=20, value=1, step=1, key="qty_box")
    
    if st.button("⚡ Scan & Analyze Item", use_container_width=True, key="scan_action"):
        if name_input:
            if name_input in NUTRI_DATA:
                data = NUTRI_DATA[name_input]
                new_item = {
                    "Ingredient": name_input.title(),
                    "Quantity": int(qty_input),
                    "Calories (kcal)": round(data["calories"] * qty_input, 1),
                    "Protein (g)": round(data["protein"] * qty_input, 2),
                    "Carbs (g)": round(data["carbs"] * qty_input, 2),
                    "Fats (g)": round(data["fats"] * qty_input, 2),
                    "Key Vitamin": data["vitamin"]
                }
            else:
                new_item = {
                    "Ingredient": name_input.title(),
                    "Quantity": int(qty_input),
                    "Calories (kcal)": round(75.5 * qty_input, 1),
                    "Protein (g)": round(2.1 * qty_input, 2),
                    "Carbs (g)": round(12.4 * qty_input, 2),
                    "Fats (g)": round(1.1 * qty_input, 2),
                    "Key Vitamin": "Antioxidants & Fibers"
                }
            st.session_state.kitchen_inventory.append(new_item)
            st.rerun()
    st.markdown('</div>', unsafe_html=True)

    st.write("---")
    st.subheader("📋 Scanned Inventory Ledger")
    if len(st.session_state.kitchen_inventory) == 0:
        st.write("No items scanned yet. Use your typing speed to populate the analyzer.")
    else:
        df = pd.DataFrame(st.session_state.kitchen_inventory)
        st.dataframe(df, use_container_width=True, hide_index=True)
        if st.button("🗑️ Reset Inventory Scanner", key="reset_action"):
            st.session_state.kitchen_inventory = []
            st.rerun()

with col2:
    st.subheader("📊 Dynamic Diagnostic Reports")
    
    if len(st.session_state.kitchen_inventory) == 0:
        st.write("Awaiting ingredient scans to calculate diagnostic graphs.")
    else:
        total_cals = round(sum(item["Calories (kcal)"] for item in st.session_state.kitchen_inventory), 1)
        total_protein = round(sum(item["Protein (g)"] for item in st.session_state.kitchen_inventory), 2)
        total_carbs = round(sum(item["Carbs (g)"] for item in st.session_state.kitchen_inventory), 2)
        total_fats = round(sum(item["Fats (g)"] for item in st.session_state.kitchen_inventory), 2)
        
        if total_protein > 15.0:
            grade = "👑 A+ Gourmet Elite Profile"
        elif total_cals < 350.0:
            grade = "🥇 A High-Efficiency Vitality Blend"
        else:
            grade = "🥈 B Balanced Feast Array"

        # 📊 Wrap diagnostics display metrics output into your customized gradient display card container
        st.markdown(f"""
            <div class="premium-gradient-card">
                <h3>📈 Total Combined Analytics</h3>
                <p><b>⚡ Combined Caloric Weight:</b> {total_cals} kcal</p>
                <p><b>💪 Macro Protein Level:</b> {total_protein} grams</p>
                <p><b>🍞 Macro Carbohydrates:</b> {total_carbs} grams</p>
                <p><b>🥑 Lipids Profile (Fats):</b> {total_fats} grams</p>
                <h4>🎯 Calculated Menu Grade: {grade}</h4>
            </div>
        """, unsafe_html=True)

        st.write("---")
        st.subheader("👨‍🍳 Custom AI Formulation Blueprint")
        
        if total_cals > 400.0:
            st.write("🔋 **Formulation: Hearty Artisan Platter**")
            st.write("This structural compilation provides massive caloric fuel cells. Arrange components cleanly on flat tableware. Serve immediately for optimal nutrient distribution.")
        else:
            st.write("🌿 **Formulation: Lite Gourmet Infusion**")
            st.write("A clean, highly biological, trace-mineral blend. Toss elements cleanly in a transparent mixing bowl to maintain aesthetic design metrics.")
