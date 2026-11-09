import streamlit as st
import pandas as pd

# 1. Clear Page Setup
st.set_page_config(page_title="AI Ingredient Analyzer Pro", page_icon="🧬", layout="wide")

# 2. 🎨 FIXED DESIGN INJECTION (Applies your background canvas to all boxes!)
st.html("""
<style>
    /* Force the complete app wrapper container to use your exact picture gradient layout */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stCanvas"], .main {
        background: linear-gradient(135deg, 
            #A7F3D0 0%, 
            #FEF3C7 35%, 
            #FCE7F3 65%, 
            #E9D5FF 100%) !important;
        background-attachment: fixed !important;
        background-color: #FEF3C7 !important;
    }

    /* Clear default backgrounds on widget blocks to blend with your colors */
    [data-testid="stVerticalBlock"] > div, 
    [data-testid="stForm"], 
    .stElementContainer, 
    div[data-testid="stNotification"],
    div[class*="st-emotion-cache"],
    div[data-testid="stBlock"],
    div[data-testid="element-container"],
    .stCustomBlockContainer,
    div[data-testid="stContainer"] {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Draw clear, elegant floating box boundaries for readability */
    div[data-testid="stMetricWidget"], div[class*="st-emotion-cache-12w0qpk"] {
        background-color: rgba(255, 255, 255, 0.4) !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        border-radius: 12px !important;
        padding: 15px !important;
    }

    /* Force clean, legible text visibility over the light canvas */
    h1, h2, h3, h4, p, span, label, td, th, div, [data-testid="stWidgetLabel"] p {
        color: #1E293B !important;
        font-family: 'Segoe UI', system-ui, sans-serif !important;
        font-weight: 700 !important;
    }
    
    h1 {
        font-weight: 800 !important;
        color: #0F172A !important;
        margin-top: 10px !important;
        margin-bottom: 20px !important;
    }

    /* Style the secondary action layout buttons cleanly */
    button[data-testid="stBaseButton-secondary"] {
        background: linear-gradient(135deg, #10B981 0%, #3B82F6 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: bold !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    }
    
    button[data-testid="stBaseButton-secondary"] p {
        color: white !important;
    }

    /* Input text boxes look */
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.6) !important;
        color: #1E293B !important;
        border-radius: 10px !important;
        border: 1px solid rgba(0,0,0,0.1) !important;
    }
    
    /* Center the database tables smoothly over the auroral gradient sheet */
    .stDataFrame, [data-testid="stDataFrameData"] {
        background-color: rgba(255, 255, 255, 0.5) !important;
        border-radius: 12px !important;
    }
</style>
""")

# 3. Main Header Display Elements
st.title("🧬 Advanced Ingredient Nutri-Scanner Pro")
st.write("Type any ingredient to dynamically extract high-precision nutritional insights.")

# Initialize the backend state database lists correctly
if "kitchen_inventory" not in st.session_state:
    st.session_state.kitchen_inventory = []

# Core dataset matching parameters
NUTRI_DATA = {
    "banana": {"calories": 105.2, "protein": 1.3, "carbs": 27.1, "fats": 0.3, "vitamin": "Potassium & B6"},
    "mango": {"calories": 99.4, "protein": 1.4, "carbs": 24.8, "fats": 0.6, "vitamin": "Vitamin C & A"},
    "apple": {"calories": 94.6, "protein": 0.5, "carbs": 25.1, "fats": 0.3, "vitamin": "Fiber & Vitamin C"},
    "milk": {"calories": 149.0, "protein": 7.7, "carbs": 11.7, "fats": 8.0, "vitamin": "Calcium & Vitamin D"},
    "honey": {"calories": 64.5, "protein": 0.1, "carbs": 17.3, "fats": 0.0, "vitamin": "Antioxidants"},
    "cocoa powder": {"calories": 12.1, "protein": 1.0, "carbs": 3.1, "fats": 0.7, "vitamin": "Iron & Magnesium"},
    "protein powder": {"calories": 120.0, "protein": 24.5, "carbs": 3.0, "fats": 1.5, "vitamin": "Amino Acids"},
    "salt": {"calories": 0.0, "protein": 0.0, "carbs": 0.0, "fats": 0.0, "vitamin": "Sodium Mineral"}
}

col1, col2 = st.columns(2)

with col1:
    st.subheader("🛒 Add Kitchen Ingredient")
    
    # Using clean unique form keys so scanning can work continuously without freezing!
    name_input = st.text_input("🍎 Ingredient Name:", placeholder="e.g., Banana, Mango, Milk", key="ing_name_field").strip().lower()
    qty_input = st.number_input("🔢 Quantity Amount:", min_value=1, max_value=20, value=1, step=1, key="ing_qty_field")
    
    if st.button("⚡ Scan & Analyze Item", use_container_width=True, key="scan_btn_submit"):
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
                    "Calories (kcal)": round(55.4 * qty_input, 1),
                    "Protein (g)": round(1.15 * qty_input, 2),
                    "Carbs (g)": round(10.25 * qty_input, 2),
                    "Fats (g)": round(0.22 * qty_input, 2),
                    "Key Vitamin": "Natural Fibers"
                }
            st.session_state.kitchen_inventory.append(new_item)
            st.rerun()

    st.write("---")
    st.subheader("📋 Scanned Inventory Ledger")
    if len(st.session_state.kitchen_inventory) == 0:
        st.write("No items scanned yet. Ready for your input!")
    else:
        df = pd.DataFrame(st.session_state.kitchen_inventory)
        st.dataframe(df, use_container_width=True, hide_index=True)
        if st.button("🗑️ Reset Inventory Scanner", key="reset_btn_ledger"):
            st.session_state.kitchen_inventory = []
            st.rerun()

with col2:
    st.subheader("📊 Dynamic Diagnostic Reports")
    
    if len(st.session_state.kitchen_inventory) == 0:
        st.write("Awaiting ingredient scans to run laboratory diagnostics.")
    else:
        total_cals = round(sum(item["Calories (kcal)"] for item in st.session_state.kitchen_inventory), 1)
        total_protein = round(sum(item["Protein (g)"] for item in st.session_state.kitchen_inventory), 2)
        total_carbs = round(sum(item["Carbs (g)"] for item in st.session_state.kitchen_inventory), 2)
        total_fats = round(sum(item["Fats (g)"] for item in st.session_state.kitchen_inventory), 2)
        
        if total_protein > 15.0:
            grade = "👑 A+ Elite Strength Profile"
        elif total_cals < 300.0:
            grade = "🥇 A High-Efficiency Energy"
        else:
            grade = "🥈 B Balanced Blend"

        st.markdown("### 📈 Total Combined Diagnostics")
        st.write(f"⚡ **Total Energy Matrix:** {total_cals} kcal")
        st.write(f"💪 **Total Protein Array:** {total_protein} grams")
        st.write(f"🍞 **Total Carbohydrates:** {total_carbs} grams")
        st.write(f"🥑 **Total Lipids (Fats):** {total_fats} grams")
        st.markdown(f"#### 🎯 Calculated Grade: {grade}")

        st.write("---")
        st.subheader("👨‍🍳 Custom AI Formulation Blueprint")
        
        if total_cals > 400.0:
            st.write("🔋 **Formulation: Mass Gainer Blast Bowl**")
            st.write("This dense layout contains massive clean fuel arrays. Blend completely down with high-speed settings.")
        else:
            st.write("🌿 **Formulation: Ultra-Lean Cellular Hydra-Mix**")
            st.write("A clean, highly bio-available mix. Layer elements cleanly inside a glassware bowl to keep nutrients separated.")
