import streamlit as st
from datetime import datetime

# Title and header
st.title("📱 Python Mobile Shop")
st.markdown("### Welcome to the Python Mobile Shop!")
st.divider()

# Default product list
if "products" not in st.session_state:
    st.session_state["products"] = {
        "1": {"SNO": 1, "Product": "Smart Phone", "In Stock": 20, "Price": 200},
        "2": {"SNO": 2, "Product": "Head Phones", "In Stock": 100, "Price": 30},
        "3": {"SNO": 3, "Product": "Screen Guard", "In Stock": 200, "Price": 5},
        "4": {"SNO": 4, "Product": "Chargers", "In Stock": 100, "Price": 10},
        "5": {"SNO": 5, "Product": "Memory Cards", "In Stock": 120, "Price": 50},
    }

# Sidebar Menu
menu = st.sidebar.radio(
    "Select Option:",
    ["Show All Products", "Buy Product", "Add Products (Admin)", "Exit"],
)

# -------------------------------
# OPTION 1: SHOW ALL PRODUCTS
# -------------------------------
if menu == "Show All Products":
    st.subheader("📋 All Available Products")
    st.table(st.session_state["products"].values())
    st.success("Program execution completed.")

# -------------------------------
# OPTION 2: BUY PRODUCT
# -------------------------------
elif menu == "Buy Product":
    st.subheader("🛒 Buy Product")
    products = st.session_state["products"]
    st.table(products.values())

    chooseproduct = st.selectbox("Select Product ID:", list(products.keys()))

    if chooseproduct:
        customername = st.text_input("Enter Your Name:")
        confirm = st.checkbox("Confirm Purchase")

        if confirm and customername.strip() != "":
            selected_product = products[chooseproduct]
            st.success("✅ Bill Generated")
            st.write(f"**Bill No:** 12345")
            st.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            st.write(f"**Customer Name:** {customername}")
            st.write(f"**Product:** {selected_product['Product']}")
            st.write(f"**Amount:** ${selected_product['Price']}")
            st.info("Program execution completed.")

# -------------------------------
# OPTION 3: ADD PRODUCTS (ADMIN)
# -------------------------------
elif menu == "Add Products (Admin)":
    st.subheader("🔐 Admin Panel")

    admin = st.text_input("Enter Admin Username:")
    password = st.text_input("Enter Password:", type="password")

    if admin == "admin" and password == "pass":
        st.success("✅ Admin verified.")
        st.write("Add new product details below:")

        productid = st.text_input("Enter Product ID:")
        productname = st.text_input("Enter Product Name:")
        productquantity = st.number_input("Enter Product Quantity:", min_value=1)
        price = st.number_input("Enter Product Price:", min_value=1)

        if st.button("Add Product"):
            if productid and productname:
                st.session_state["products"][productid] = {
                    "SNO": int(productid),
                    "Product": productname,
                    "In Stock": productquantity,
                    "Price": price,
                }
                st.success(f"✅ Product '{productname}' added successfully!")
                st.table(st.session_state["products"].values())
                st.info("Program execution completed.")
            else:
                st.warning("⚠️ Please enter all fields.")
    elif admin or password:
        st.error("❌ Invalid Username or Password")

# -------------------------------
# OPTION 4: EXIT
# -------------------------------
elif menu == "Exit":
    st.subheader("👋 Thank you for visiting Python Mobile Shop!")
    st.info("Program execution completed.")
