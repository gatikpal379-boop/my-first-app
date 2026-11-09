import streamlit as st
import pandas as pd

# 1. Page Settings
st.set_page_config(page_title="AI Fruit Recipe Builder", page_icon="🥝", layout="wide")

# 2. 🎨 PREMIUM CSS CUSTOM STYLING
# This injects custom CSS directly into your app to make it look clean and modern!
st.markdown("""
    <style>
        /* Style the main title */
        h1 {
            color: #FF6B6B !important;
            font-family: 'Segoe UI', sans-serif;
            font-weight: 800 !important;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        
        /* Make the Add Ingredient button pop and glow */
        div.stButton > button:first-child {
            background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%) !important;
            color: white !important;
            font-weight: bold !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 12px 24px !important;
            box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4) !important;
            transition: all 0.2s ease-in-out !important;
        }
        
        div.stButton > button:first-child:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(255, 107, 107, 0.6) !important;
        }

        /* Style the background of our Recipe suggestion cards */
        .recipe-card {
            background-color: rgba(255, 255, 255, 0.05);
            border-left: 5px solid #4E65FF;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 15px;
        }
        
        /* Custom input fields styling */
        .stTextInput input {
            border-radius: 10px !important;
            border: 2px solid rgba(255,255,255,0.1) !important;
            background-color: rgba(0,0,0,0.2) !important;
        }
        
        .stTextInput input:focus {
            border-color: #FF6B6B !important;
        }
    </style>
""", unsafe_html=True)

# 3. Main App Heading
st.title("🥝 Smart Fruit & Smoothie Recipe Builder")
st.write("Type in the fruits and ingredients you have at home, and our system will design a perfect, nutrient-filled treat!")

# Initialize storage for ingredients if it doesn't exist
if "fridge_items" not in st.session_state:
    st.session_state.fridge_items = []

# 4. Main Visual Layout Columns
col1, col2 = st.columns()

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
        
        # --- INTELLIGENT MATCHING LOGIC USING STYLED HTML ---
        if any("banana" in n for n in names_list) or any("milk" in n for n in names_list):
            st.markdown("""
                <div class="recipe-card">
                    <h4 style="color:#4E65FF; margin-top:0;">⚡ Option A: The Energizer Smoothie Bowl</h4>
                    <p><b>How to prepare:</b> Take your fruits, slice them nicely, and toss them into a blender container. If you have powders (like protein or cocoa), add them right into the liquid pool before blending.</p>
                    <p><b>Nutrient Value:</b> Rich in Potassium, Healthy Fibers, and Natural Energizing Carbs. Perfect for active builders!</p>
                </div>
            """, unsafe_html=True)
            
            if any("salt" in n for n in names_list) or any("powder" in n for n in names_list):
                st.info("💡 Chef's Tip: Adding that pinch of salt helps balance out the sweetness of your fresh fruits, making it taste like a professional bakery item!")
                
        elif any("mango" in n for n in names_list) or any("orange" in n for n in names_list):
            st.markdown("""
                <div class="recipe-card" style="border-left-color: #FF8E53;">
                    <h4 style="color:#FF8E53; margin-top:0;">🌴 Option B: Tropical Vitamin-C Blast</h4>
                    <p><b>How to prepare:</b> Dice your tropical fruits into fine small cubes. Layer them neatly inside a transparent glass container so the colors look incredibly bright and stylish.</p>
                    <p><b>Nutrient Value:</b> High Vitamin C immune support system and essential minerals.</p>
                </div>
            """, unsafe_html=True)
            
        else:
            st.markdown("""
                <div class="recipe-card" style="border-left-color: #28a745;">
                    <h4 style="color:#28a745; margin-top:0;">🥗 Option C: Custom Gourmet Fruit Salad Infusion</h4>
                    <p><b>How to prepare:</b> Since you have a unique mix, chop everything up evenly. Toss them together lightly inside a large mixing bowl.</p>
                    <p><b>Nutrient Value:</b> Clean fiber profile, trace antioxidants, and natural fruit hydration matrices.</p>
                </div>
            """, unsafe_html=True)

        # Dashboard Metrics
        st.write("---")
        st.markdown("### 📊 Aesthetic Dashboard Metrics")
        m1, m2 = st.columns(2)
        m1.metric(label="Total Ingredients Registered", value=len(st.session_state.fridge_items))
        m2.metric(label="Health Rating Tracker", value="⭐⭐⭐⭐⭐" if len(st.session_state.fridge_items) >= 3 else "⭐⭐⭐")
