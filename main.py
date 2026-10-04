

from pyscript import document

def create_order():
    """Receipt Generator - Calculate subtotal, VAT, and total"""
    # Get input values
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")
    prod5 = document.getElementById("item5")

    # Calculate subtotal 
    subtotal = (float(prod1.value) * prod1.checked +
                float(prod2.value) * prod2.checked +
                float(prod3.value) * prod3.checked +
                float(prod4.value) * prod4.checked +
                float(prod5.value) * prod5.checked)

    tax_rate = 0.12  # 12% VAT
    tax = subtotal * tax_rate
    total = subtotal + tax

    receipt = f"""<h3>RECEIPT</h3>
    <p>Subtotal: ₱{subtotal:.2f}</p>
    <p>VAT (12%): ₱{tax:.2f}</p>
    <hr>
    <p><strong>TOTAL: ₱{total:.2f}</strong></p>"""

    document.getElementById("show").innerHTML = receipt


def clear_receipt():
    """Clear receipt and reset checkboxes"""
    document.getElementById("item1").checked = False
    document.getElementById("item2").checked = False
    document.getElementById("item3").checked = False
    document.getElementById("item4").checked = False
    document.getElementById("item5").checked = False
    document.getElementById("show").innerHTML = ""


def SKU_generator():
    """SKU Generator - Create unique stock keeping unit code"""
    document.getElementById('sku_output').innerHTML = ""

    category = document.getElementById('category').value
    product_name = document.getElementById('product_input').value
    stock_qty = document.getElementById('quantity').value

    if not category or not product_name or not stock_qty:
        document.getElementById('sku_output').innerHTML = "<p style='color: red;'>Please fill in all fields</p>"
        return

    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)

    sku_display = f"""<h3>{sku}</h3>
    <p>Category Code: {category[:3].upper()}</p>
    <p>Product Code: {product_name[:4].upper()}</p>
    <p>Stock Quantity: {stock_qty}</p>"""

    document.getElementById('sku_output').innerHTML = sku_display


def clear_sku():
    """Clear SKU form and output"""
    document.getElementById('category').value = ""
    document.getElementById('product_input').value = ""
    document.getElementById('quantity').value = ""
    document.getElementById('sku_output').innerHTML = ""
