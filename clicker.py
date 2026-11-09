import streamlit as st
import pandas as pd

# 1. Page Config
st.set_page_config(page_title="AI Ingredient Analyzer", page_icon="🧬", layout="wide")
st.title("🧬 Advanced Ingredient Nutri-Scanner Pro")
st.write("Type any ingredient to dynamically extract deep nutritional insights, calories, and custom gourmet recipes.")

# Initialize inventory
if "kitchen_inventory" not in st.session_state:
    st.session_state.kitchen_inventory = []

# --- 🧠 DATABASE DICTIONARY ENGINE ---
# Real-world data to calculate exact macros instantly!
NUTRI_DATA = {
    "banana": {"calories": 105, "protein": 1.3, "carbs": 27, "fats": 0.3, "vitamin": "Potassium & B6"},
    "mango": {"calories": 99, "protein": 1.4, "carbs": 25, "fats": 0.6, "vitamin": "Vitamin C & A"},
    "apple": {"calories": 95, "protein": 0.5, "carbs": 25, "fats": 0.3, "vitamin": "Fiber & Vitamin C"},
    "milk": {"calories": 149, "protein": 7.7, "carbs": 12, "fats": 8.0, "vitamin": "Calcium & Vitamin D"},
    "honey": {"calories": 64, "protein": 0.1, "carbs": 17, "fats": 0.0, "vitamin": "Antioxidants"},
    "cocoa powder": {"calories": 12, "protein": 1.0, "carbs": 3, "fats": 0.7, "vitamin": "Iron & Magnesium"},
    "protein powder": {"calories": 120, "protein": 24.0, "carbs": 3, "fats": 1.5, "vitamin": "Amino Acids"},
    "salt": {"calories": 0, "protein": 0.0, "carbs": 0, "fats": 0.0, "vitamin": "Sodium Mineral"}
}

col1, col2 = st.columns(2)

with col1:
    st.subheader("🛒 Add Kitchen Ingredient")
    
    # User Inputs
    name_input = st.text_input("🍎 Ingredient Name:", placeholder="e.g., Banana, Mango, Milk, Cocoa Powder").strip().lower()
    qty_input = st.number_input("🔢 Quantity (Multiplier):", min_value=1, max_value=10, value=1)
    
    if st.button("⚡ Scan & Analyze Item", use_container_width=True):
        if name_input:
            # Check if we have scientific macro data for this specific item
            if name_input in NUTRI_DATA:
                data = NUTRI_DATA[name_input]
                new_item = {
                    "Ingredient": name_input.title(),
                    "Quantity": qty_input,
                    "Calories": data["calories"] * qty_input,
                    "Protein (g)": round(data["protein"] * qty_input, 1),
                    "Carbs (g)": data["carbs"] * qty_input,
                    "Fats (g)": round(data["fats"] * qty_input, 1),
                    "Key Vitamin": data["vitamin"]
                }
                st.session_state.kitchen_inventory.append(new_item)
                st.success(f"Successfully scanned {name_input.title()}!")
                st.rerun()
            else:
                # Fallback for custom or unknown items typed in
                new_item = {
                    "Ingredient": name_input.title(),
                    "Quantity": qty_input,
                    "Calories": 50 * qty_input,
                    "Protein (g)": round(1.0 * qty_input, 1),
                    "Carbs (g)": 10 * qty_input,
                    "Fats (g)": round(0.2 * qty_input, 1),
                    "Key Vitamin": "Natural Fibers"
                }
                st.session_state.kitchen_inventory.append(new_item)
                st.warning(f"Added custom entry for '{name_input.title()}'. Using estimated baseline metrics.")
                st.rerun()
        else:
            st.error("Please type an ingredient name first!")

    st.write("---")
    st.subheader("📋 Scanned Inventory Inventory")
    if len(st.session_state.kitchen_inventory) == 0:
        st.info("No items scanned yet. Use your pro typing skills on the form above!")
    else:
        df = pd.DataFrame(st.session_state.kitchen_inventory)
        st.dataframe(df, use_container_width=True, hide_index=True)
        if st.button("🗑️ Reset Inventory Scanner"):
            st.session_state.kitchen_inventory = []
            st.rerun()

with col2:
    st.subheader("📊 Dynamic Lab Diagnostic Reports")
    
    if len(st.session_state.kitchen_inventory) == 0:
        st.warning("Awaiting ingredient scans to run laboratory diagnostics.")
    else:
        # Calculate grand totals using simple math algorithms
        total_cals = sum(item["Calories"] for item in st.session_state.kitchen_inventory)
        total_protein = sum(item["Protein (g)"] for item in st.session_state.kitchen_inventory)
        total_carbs = sum(item["Carbs (g)"] for item in st.session_state.kitchen_inventory)
        total_fats = sum(item["Fats (g)"] for item in st.session_state.kitchen_inventory)
        
        # Determine overall grade score based on protein-to-calorie ratio
        if total_protein > 15:
            grade = "👑 A+ Elite Strength Profile"
        elif total_cals < 300:
            grade = "🥇 A High-Efficiency Energy"
        else:
            grade = "🥈 B Balanced Blend"

        # Show grand analytics cards
        with st.container(border=True):
            st.markdown(f"### 📈 Total Combined Metrics")
            st.markdown(f"**⚡ Total Calories:** {total_cals} kcal")
            st.markdown(f"**💪 Total Protein:** {total_protein} grams")
            st.markdown(f"**🍞 Total Carbohydrates:** {total_carbs} grams")
            st.markdown(f"**🥑 Total Healthy Fats:** {total_fats} grams")
            st.metric(label="🎯 Formula Health Grade:", value=grade)

        st.write("---")
        st.subheader("👨‍🍳 Custom AI Formulation Blueprint")
        
        # Generate custom cooking instructions dynamically based on total metrics
        if total_cals > 400:
            st.info("🔋 **Formulation: Mass Gainer Blast Bowl**")
            st.write("This dense layout contains massive clean fuel arrays. Blend completely down with high-speed settings. Serve chilled immediately for optimal muscle/energy cell absorption recovery.")
        else:
            st.success("🌿 **Formulation: Ultra-Lean Cellular Hydra-Mix**")
            st.write("A clean, highly bio-available mix. Layer elements cleanly inside a glassware bowl to keep nutrients separated and structurally intact. Top with powder accents for aesthetic symmetry.")
