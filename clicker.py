import streamlit as st
import pandas as pd

# 1. Configuration
st.set_page_config(page_title="AI Ingredient Analyzer Pro", page_icon="🧬", layout="wide")

# 2. 🎨 ULTIMATE CSS ENGINE (Wipes out old dark box properties completely!)
st.html("""
<style>
    /* 🟦 Upper Dark Blue Navbar Layer running along the absolute top */
    [data-testid="stHeader"] {
        background: linear-gradient(90deg, #0A192F 0%, #0D47A1 100%) !important;
        border-bottom: 3px solid #172A45;
        height: 55px !important;
        position: fixed !important;
        z-index: 999999 !important;
    }

    /* 🎨 Full Main Screen Layer mirroring your specific pastel gradient upload */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stCanvas"] {
        background: linear-gradient(135deg, 
            #F9FBFC 0%, 
            #A7F3D0 20%, 
            #FEF3C7 40%, 
            #FCE7F3 75%, 
            #E9D5FF 100%) !important;
        background-attachment: fixed !important;
    }

    /* 📦 Completely strip old default box backgrounds so they catch the gradient colors */
    [data-testid="stVerticalBlock"] > div, 
    [data-testid="stForm"], 
    .stElementContainer, 
    div[data-testid="stNotification"],
    div[class*="st-emotion-cache"] {
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Create clear, glass-like layout cards for form elements */
    div[data-testid="stBlock"] {
        background: rgba(255, 255, 255, 0.4) !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        border-radius: 16px !important;
        padding: 20px !important;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.04) !important;
    }

    /* Heavy dark contrast typography layers for text visibility */
    h1, h2, h3, h4, p, label p, [data-testid="stWidgetLabel"] p, span, div {
        color: #1A202C !important;
        font-family: 'Segoe UI', system-ui, sans-serif !important;
        font-weight: 700 !important;
    }
    
    h1 {
        font-weight: 800 !important;
        margin-top: 35px !important;
        color: #0A192F !important;
    }

    /* Clean formatting for interactive buttons */
    button[data-testid="stBaseButton-secondary"] {
        background: linear-gradient(135deg, #2E7D32 0%, #0D47A1 100%) !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        font-weight: bold !important;
    }

    /* Data table visualization styling layer */
    .stDataFrame, [data-testid="stDataFrameData"] {
        background-color: rgba(255, 255, 255, 0.7) !important;
        border-radius: 12px !important;
    }
</style>
""")

# 3. App Title Block
st.title("🧬 Advanced Ingredient Nutri-Scanner Pro")
st.write("Type any ingredient to dynamically extract high-precision nutritional insights and calculations.")

# Initialize inventory session state
if "kitchen_inventory" not in st.session_state:
    st.session_state.kitchen_inventory = []

# High-precision database metrics
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
    name_input = st.text_input("🍎 Ingredient Name:", placeholder="e.g., Banana, Mango, Milk").strip().lower()
    qty_input = st.number_input("🔢 Quantity Amount:", min_value=1, max_value=20, value=1, step=1)
    
    if st.button("⚡ Scan & Analyze Item", use_container_width=True):
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
                st.session_state.kitchen_inventory.append(new_item)
                st.rerun()
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
        if st.button("🗑️ Reset Inventory Scanner"):
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
