# 1st Quarter Project - Receipt & SKU Generator

# BLANK ANSWERS:
# 1. getElementById
# 2. 'category'
# 3. product_name = document.getElementById('product_input')
# 4. (part of blank 3)
# 5. stock_qty
# 6. 'sku_output'
# 7. subtotal
# 8. * (multiplication)
# 9. + (addition)
# 10. innerHTML

def createOrder():
    """Receipt Generator - Calculate subtotal, VAT, and total"""
    item1 = document.getElementById("item1")
    item2 = document.getElementById("item2")
    item3 = document.getElementById("item3")
    item4 = document.getElementById("item4")
    item5 = document.getElementById("item5")

    # Calculate subtotal by multiplying price by checked status (1 or 0)
    subtotal = (float(item1.value) * item1.checked +
                float(item2.value) * item2.checked +
                float(item3.value) * item3.checked +
                float(item4.value) * item4.checked +
                float(item5.value) * item5.checked)

    # Calculate tax and total
    tax = subtotal * 0.12  # 12% VAT
    total = subtotal + tax

    html = f"<h3>RECEIPT</h3><p>Subtotal: ₱{subtotal:.2f}</p><p>VAT (12%): ₱{tax:.2f}</p><hr><p><strong>TOTAL: ₱{total:.2f}</strong></p>"
    document.getElementById("receipt").innerHTML = html

def generateSKU():
    """SKU Generator - Create unique stock keeping unit code"""
    category = document.getElementById("category").value
    product_name = document.getElementById("product_input").value
    stock_qty = document.getElementById("quantity").value

    if not category or not product_name or not stock_qty:
        document.getElementById("sku").innerHTML = "<p style='color: red;'>Fill all fields</p>"
        return

    # Format: [CAT-PROD-QTY]
    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + stock_qty
    html = f"<h3>{sku}</h3><p>Category: {category[:3].upper()}</p><p>Product: {product_name[:4].upper()}</p><p>Quantity: {stock_qty}</p>"
    document.getElementById("sku").innerHTML = html
