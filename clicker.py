import streamlit as st
import pandas as pd

# 1. Page Settings
st.set_page_config(page_title="AI Fruit Recipe Builder", page_icon="🥝", layout="wide")

# 2. Main App Heading
st.title("🥝 Smart Fruit & Smoothie Recipe Builder")
st.write("Type in the fruits and ingredients you have at home, and our system will design a perfect, nutrient-filled treat!")

# Initialize storage for ingredients if it doesn't exist
if "fridge_items" not in st.session_state:
    st.session_state.fridge_items = []

# 3. Main Visual Layout Columns (2 Columns)
col1, col2 = st.columns(2)

with col1:
    st.subheader("🛒 Add Your Kitchen Ingredients")
    
    # Text input boxes for user inputs
    item_name = st.text_input("🍎 Ingredient Name:", placeholder="e.g., Banana, Mango, Salt, Cocoa Powder")
    item_qty = st.number_input("🔢 Quantity / Amount:", min_value=1, max_value=20, value=1, step=1)
    
    # Add Item Button
    if st.button("➕ Add to My Kitchen List", use_container_width=True):
        if item_name:
            new_item = {"Name": item_name.strip().title(), "Quantity": int(item_qty)}
            st.session_state.fridge_items.append(new_item)
            st.success(f"Added {item_name} to your inventory!")
            st.rerun()
        else:
            st.error("Please fill out the Ingredient Name box first!")

    # Display Current Inventory List
    st.write("---")
    st.subheader("📋 What You Have Added So Far:")
    if len(st.session_state.fridge_items) == 0:
        st.info("Your kitchen inventory is currently empty. Add ingredients above!")
    else:
        df = pd.DataFrame(st.session_state.fridge_items)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        if st.button("🗑️ Clear Entire List"):
            st.session_state.fridge_items = []
            st.rerun()

with col2:
    st.subheader("🤖 AI Recipe Suggestion Machine")
    
    if len(st.session_state.fridge_items) == 0:
        st.warning("Add some ingredients on the left column first to unlock AI recipes!")
    else:
        st.success("✨ Ingredients analyzed successfully!")
        
        # Turn list into easy-to-read string for matching logic
        names_list = [item["Name"].lower() for item in st.session_state.fridge_items]
        
        st.markdown("### 🏆 Top Recommended Recipe For You:")
        
        # --- SAFE INTELLIGENT MATCHING LOGIC USING NATIVE BOXES ---
        if any("banana" in n for n in names_list) or any("milk" in n for n in names_list):
            with st.container(border=True):
                st.markdown("#### ⚡ Option A: The Energizer Smoothie Bowl")
                st.write("**How to prepare:** Slice your fruits nicely, and toss them into a blender container. Add your powders before blending.")
                st.write("**Nutrient Value:** Rich in Potassium, Healthy Fibers, and Natural Energizing Carbs.")
            
        elif any("mango" in n for n in names_list) or any("orange" in n for n in names_list):
            with st.container(border=True):
                st.markdown("#### 🌴 Option B: Tropical Vitamin-C Blast")
                st.write("**How to prepare:** Dice your tropical fruits into fine small cubes. Layer them neatly inside a transparent glass container.")
                st.write("**Nutrient Value:** High Vitamin C immune support system and essential minerals.")
            
        else:
            with st.container(border=True):
                st.markdown("#### 🥗 Option C: Custom Gourmet Fruit Salad Infusion")
                st.write("**How to prepare:** Chop everything up evenly. Toss them together lightly inside a large mixing bowl.")
                st.write("**Nutrient Value:** Clean fiber profile, trace antioxidants, and natural fruit hydration.")

        # Dashboard Metrics
        st.write("---")
        st.markdown("### 📊 Aesthetic Dashboard Metrics")
        m1, m2 = st.columns(2)
        m1.metric(label="Total Ingredients Registered", value=len(st.session_state.fridge_items))
        m2.metric(label="Health Rating Tracker", value="⭐⭐⭐⭐⭐" if len(st.session_state.fridge_items) >= 3 else "⭐⭐⭐")
