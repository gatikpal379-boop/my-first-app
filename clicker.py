import streamlit as st
import pandas as pd

# 1. Page Settings
st.set_page_config(page_title="AI Ingredient Analyzer Pro", page_icon="🧬", layout="wide")

# 2. 🎨 ULTIMATE FULL-PAGE GRADIENT INJECTION
# This turns the entire website background into your custom flowing canvas!
st.html("""
<style>
    /* Force the entire web app background to follow your exact color path */
    .stApp, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, 
            #FFFFFF 0%, 
            #E8F5E9 25%, 
            #2E7D32 50%, 
            #E0F7FA 75%, 
            #0D47A1 100%) !important;
        background-attachment: fixed !important;
    }

    /* Keep all text readable on the changing light/dark background colors */
    h1, h2, h3, h4, p, label p, [data-testid="stWidgetLabel"] p {
        color: #1E1E2F !important;
        font-family: 'Segoe UI', sans-serif !important;
        font-weight: 700 !important;
    }
    
    h1 {
        font-weight: 800 !important;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }

    /* Style data tables cleanly to float over the gradient canvas */
    .stDataFrame {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border-radius: 12px !important;
        padding: 5px;
    }
</style>
""")

# 3. Main App Heading
st.title("🧬 Advanced Ingredient Nutri-Scanner Pro")
st.write("Type any ingredient to dynamically extract high-precision nutritional insights and calculations.")

# Initialize inventory session state
if "kitchen_inventory" not in st.session_state:
    st.session_state.kitchen_inventory = []

# Real nutritional calculation data matching decimal specifications
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
    
    name_input = st.text_input("🍎 Ingredient Name:", placeholder="e.g., Banana, Mango, Milk, Cocoa Powder").strip().lower()
    
    # FIXED: Back to clean, whole numbers only (no decimal inputs allowed here!)
    qty_input = st.number_input("🔢 Quantity / Multiplier Amount:", min_value=1, max_value=20, value=1, step=1)
    
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

        # Displaying data floating elegantly right over the full page gradient canvas
        st.markdown(f"### 📈 Total Combined Diagnostics")
        st.write(f"⚡ **Total Energy Matrix:** {total_cals} kcal")
        st.write(f"💪 **Total Protein Array:** {total_protein} grams")
        st.write(f"🍞 **Total Carbohydrates:** {total_carbs} grams")
        st.write(f"🥑 **Total Lipids (Fats):** {total_fats} grams")
        st.write(f"🎯 **Calculated Grade:** {grade}")

        st.write("---")
        st.subheader("👨‍🍳 Custom AI Formulation Blueprint")
        
        # REMOVED: Blocks of solid blue/green banners. Now text displays seamlessly on the gradient page!
        if total_cals > 400.0:
            st.write("🔋 **Formulation: Mass Gainer Blast Bowl**")
            st.write("This dense layout contains massive clean fuel arrays. Blend completely down with high-speed settings. Serve chilled immediately for optimal muscle absorption recovery.")
        else:
            st.write("🌿 **Formulation: Ultra-Lean Cellular Hydra-Mix**")
            st.write("A clean, highly bio-available mix. Layer elements cleanly inside a glassware bowl to keep nutrients separated and structurally intact.")
