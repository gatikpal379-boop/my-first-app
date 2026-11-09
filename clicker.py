import streamlit as st
import pandas as pd

# 1. Page Settings
st.set_page_config(page_title="AI Ingredient Analyzer Pro", page_icon="🧬", layout="wide")

# 2. 🎨 SAFE BUILT-IN HTML GRADIENT INJECTION
# This bypasses the st.markdown firewall by using st.html natively!
st.html("""
<style>
    .premium-gradient-card {
        background: linear-gradient(135deg, 
            #FFFFFF 0%, 
            #E8F5E9 25%, 
            #2E7D32 50%, 
            #E0F7FA 75%, 
            #0D47A1 100%) !important;
        padding: 25px;
        border-radius: 16px;
        color: #1E1E2F !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 20px;
    }
    .premium-gradient-card h3, .premium-gradient-card h4, .premium-gradient-card p {
        color: #1E1E2F !important;
        font-family: 'Segoe UI', sans-serif;
    }
</style>
""")

# 3. Main App Heading
st.title("🧬 Advanced Ingredient Nutri-Scanner Pro")
st.write("Type any ingredient to dynamically extract high-precision nutritional insights and dynamic recipes.")

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
    qty_input = st.number_input("🔢 Quantity / Multiplier Amount (e.g., 1.5, 2.3):", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
    
    if st.button("⚡ Scan & Analyze Item", use_container_width=True):
        if name_input:
            if name_input in NUTRI_DATA:
                data = NUTRI_DATA[name_input]
                new_item = {
                    "Ingredient": name_input.title(),
                    "Quantity": round(qty_input, 1),
                    "Calories (kcal)": round(data["calories"] * qty_input, 1),
                    "Protein (g)": round(data["protein"] * qty_input, 2),
                    "Carbs (g)": round(data["carbs"] * qty_input, 2),
                    "Fats (g)": round(data["fats"] * qty_input, 2),
                    "Key Vitamin": data["vitamin"]
                }
                st.session_state.kitchen_inventory.append(new_item)
                st.success(f"Successfully scanned {name_input.title()}!")
                st.rerun()
            else:
                new_item = {
                    "Ingredient": name_input.title(),
                    "Quantity": round(qty_input, 1),
                    "Calories (kcal)": round(55.4 * qty_input, 1),
                    "Protein (g)": round(1.15 * qty_input, 2),
                    "Carbs (g)": round(10.25 * qty_input, 2),
                    "Fats (g)": round(0.22 * qty_input, 2),
                    "Key Vitamin": "Natural Fibers"
                }
                st.session_state.kitchen_inventory.append(new_item)
                st.warning(f"Added entry for '{name_input.title()}' using baseline data calculations.")
                st.rerun()
        else:
            st.error("Please type an ingredient name first!")

    st.write("---")
    st.subheader("📋 Scanned Inventory Ledger")
    if len(st.session_state.kitchen_inventory) == 0:
        st.info("No items scanned yet. Use your pro typing skills on the form above!")
    else:
        df = pd.DataFrame(st.session_state.kitchen_inventory)
        st.dataframe(df, use_container_width=True, hide_index=True)
        if st.button("🗑️ Reset Inventory Scanner"):
            st.session_state.kitchen_inventory = []
            st.rerun()

with col2:
    st.subheader("📊 Dynamic Diagnostic Reports")
    
    if len(st.session_state.kitchen_inventory) == 0:
        st.warning("Awaiting ingredient scans to run laboratory diagnostics.")
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

        # Safe injection block of your gradient card element
        st.html(f"""
            <div class="premium-gradient-card">
                <h3>📈 Total Combined Diagnostics</h3>
                <p><b>⚡ Total Energy Matrix:</b> {total_cals} kcal</p>
                <p><b>💪 Total Protein Array:</b> {total_protein} grams</p>
                <p><b>🍞 Total Carbohydrates:</b> {total_carbs} grams</p>
                <p><b>🥑 Total Lipids (Fats):</b> {total_fats} grams</p>
                <h4>🎯 Calculated Grade: {grade}</h4>
            </div>
        """)

        st.write("---")
        st.subheader("👨‍🍳 Custom AI Formulation Blueprint")
        
        if total_cals > 400.0:
            st.info("🔋 **Formulation: Mass Gainer Blast Bowl**")
            st.write("This dense layout contains massive clean fuel arrays. Blend completely down with high-speed settings. Serve chilled immediately for optimal muscle/energy cell absorption recovery.")
        else:
            st.success("🌿 **Formulation: Ultra-Lean Cellular Hydra-Mix**")
            st.write("A clean, highly bio-available mix. Layer elements cleanly inside a glassware bowl to keep nutrients separated and structurally intact. Top with powder accents for aesthetic symmetry.")
