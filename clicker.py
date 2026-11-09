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

# 3. Main Visual Layout Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("🛒 Add Your Kitchen Ingredients")
    
    item_name = st.text_input("🍎 Ingredient Name:", placeholder="e.g., Banana, Mango, Salt, Cocoa Powder")
    item_qty = st.text_input("🔢 Quantity / Amount:", placeholder="e.g., 2 pieces, 1 pinch, 2 spoons")
    item_type = st.selectbox("📦 Category Type:", ["Fruit 🍓", "Powder 🍫", "Spice/Salt 🧂", "Liquid/Milk 🥛"])
    
    if st.button("➕ Add to My Kitchen List", use_container_width=True):
        if item_name and item_qty:
            new_item = {"Name": item_name.strip().title(), "Quantity": item_qty.strip(), "Type": item_type}
            st.session_state.fridge_items.append(new_item)
            st.success(f"Added {item_name} to your inventory!")
            st.rerun()
        else:
            st.error("Please fill out both the Name and Quantity boxes first!")

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
        
        names_list = [item["Name"].lower() for item in st.session_state.fridge_items]
        
        st.markdown("### 🏆 Top Recommended Recipe For You:")
        
        if any("banana" in n for n in names_list) or any("milk" in n for n in names_list):
            with st.container(border=True):
                st.markdown("#### ⚡ Option A: The Energizer Smoothie Bowl")
                st.write("**How to prepare:** Slice fruits evenly, toss into a blender container. Add your powders before blending.")
                st.write("**Nutrient Value:** Rich in Potassium, Healthy Fibers, and Natural Energizing Carbs.")
            
            if any("salt" in n for n in names_list) or any("powder" in n for n in names_list):
                st.info("💡 *Chef's Tip:* Adding a pinch of salt balances the fruit sweetness perfectly!")
                
        elif any("mango" in n for n in names_list) or any("orange" in n for n in names_list):
            with st.container(border=True):
                st.markdown("#### 🌴 Option B: Tropical Vitamin-C Blast")
                st.write("**How to prepare:** Dice tropical fruits into small cubes. Layer them neatly inside a transparent glass container.")
                st.write("**Nutrient Value:** High Vitamin C immune support system.")
            
        else:
            with st.container(border=True):
                st.markdown("#### 🥗 Option C: Custom Gourmet Fruit Salad Infusion")
                st.write("**How to prepare:** Chop everything up evenly and toss together lightly inside a large mixing bowl.")
                st.write("**Nutrient Value:** Clean fiber profile and natural antioxidants.")

        st.write("---")
        st.markdown("### 📊 Aesthetic Dashboard Metrics")
        m1, m2 = st.columns(2)
        m1.metric(label="Total Ingredients Registered", value=len(st.session_state.fridge_items))
        m2.metric(label="Health Rating Tracker", value="⭐⭐⭐⭐⭐" if len(st.session_state.fridge_items) >= 3 else "⭐⭐⭐")
