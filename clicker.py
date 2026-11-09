import streamlit as st
import pandas as pd
import os

# 1. Page Settings
st.set_page_config(page_title="AI Fruit Recipe Builder", page_icon="🥝", layout="wide")

# 2. ⚡ PROFESSIONAL METHOD: Read separate CSS file safely
if os.path.exists("style.css"):
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_html=True)

# 3. Main App Heading
st.title("🥝 Smart Fruit & Smoothie Recipe Builder")
st.write("Type in the fruits and ingredients you have at home, and our system will design a perfect, nutrient-filled treat!")

# Initialize storage for ingredients if it doesn't exist
if "fridge_items" not in st.session_state:
    st.session_state.fridge_items = []

# 4. Main Visual Layout Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("🛒 Add Your Kitchen Ingredients")
    
    # Text input boxes for user inputs
    item_name = st.text_input("🍎 Ingredient Name:", placeholder="e.g., Banana, Mango, Salt, Cocoa Powder")
    item_qty = st.text_input("🔢 Quantity / Amount:", placeholder="e.g., 2 pieces, 1 pinch, 2 spoons")
    item_type = st.selectbox("📦 Category Type:", ["Fruit 🍓", "Powder 🍫", "Spice/Salt 🧂", "Liquid/Milk 🥛"])
    
    # Add Item Button
    if st.button("➕ Add to My Kitchen List", use_container_width=True):
        if item_name and item_qty:
            new_item = {"Name": item_name.strip().title(), "Quantity": item_qty.strip(), "Type": item_type}
            st.session_state.fridge_items.append(new_item)
            st.success(f"Added {item_name} to your inventory!")
            st.rerun()
        else:
            st.error("Please fill out both the Name and Quantity boxes first!")

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
        
        # --- SAFE INTELLIGENT MATCHING LOGIC ---
        if any("banana" in n for n in names_list) or any("milk" in n for n in names_list):
            with st.container(border=True):
                st.markdown("#### ⚡ Option A: The Energizer Smoothie Bowl")
                st.write("**How to prepare:** Take your fruits, slice them nicely, and toss them into a blender container. If you have powders (like protein or cocoa), add them right into the liquid pool before blending.")
                st.write("**Nutrient Value:** Rich in Potassium, Healthy Fibers, and Natural Energizing Carbs. Perfect for active builders!")
            
            if any("salt" in n for n in names_list) or any("powder" in n for n in names_list):
                st.info("💡 *Chef's Tip:* Adding that pinch of salt helps balance out the sweetness of your fresh fruits, making it taste like a professional bakery item!")
                
        elif any("mango" in n for n in names_list) or any("orange" in n for n in names_list):
            with st.container(border=True):
                st.markdown("#### 🌴 Option B: Tropical Vitamin-C Blast")
                st.write("**How to prepare:** Dice your tropical fruits into fine small cubes. Layer them neatly inside a transparent glass container so the colors look incredibly bright and stylish.")
                st.write("**Nutrient Value:** High Vitamin C immune support system and essential minerals.")
            
        else:
            with st.container(border=True):
                st.markdown("#### 🥗 Option C: Custom Gourmet Fruit Salad Infusion")
                st.write("**How to prepare:** Since you have a unique mix, chop everything up evenly. Toss them together lightly inside a large mixing bowl.")
                st.write("**Nutrient Value:** Clean fiber profile, trace antioxidants, and natural fruit hydration matrices.")

        # Dashboard Metrics
        st.write("---")
        st.markdown("### 📊 Aesthetic Dashboard Metrics")
        m1, m2 = st.columns(2)
        m1.metric(label="Total Ingredients Registered", value=len(st.session_state.fridge_items))
        m2.metric(label="Health Rating Tracker", value="⭐⭐⭐⭐⭐" if len(st.session_state.fridge_items) >= 3 else "⭐⭐⭐")
