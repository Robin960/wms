from flask import jsonify, request
from byrd_wms import app
from byrd_wms.models import Orders, Sku, Storage, OrderLine, InvalidUsage

#Reference Variables for all the Model Classes

ord = Orders()
sku = Sku()
st = Storage()
ol = OrderLine()

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response 


#All the routes are starting from /warehourse
#Default Route
@app.route("/")
@app.route("/warehouse", methods = ['GET'])
def home():    
    try:
        return jsonify("Welcome To Byrd Warehouse Management System,")
    except:
        raise InvalidUsage('This view is gone', status_code=400)

#Order Searching Route with Query Parameter
@app.route("/warehouse/orders", methods = ['GET'])
def getOrders():
    name = request.args['customer_name']
    items = ord.getOrders(name)
    try:
        return jsonify({'id':items.id,'Customer_Name':items.customer_name})
    except:
        return jsonify('No Information available for this Customer.')
#Delete the order from Orders Model with orderid

@app.route("/warehouse/delete/orders/<orderid>", methods = ['GET'])
def deleteOrder(orderid):
    ord.delOrder(orderid)
    try:
        return jsonify('Order Deleted Successfully')
    except:
        return jsonify('Not able to delete this order, something went wrong.')

#Add orders into the Orders Model with OrderID and Customer_Name
@app.route(u"/warehouse/add/orders/<orderid>/<name>", methods = ['GET'])
def addOrder(orderid,name):
    ord.addOrder(orderid,name)
    try:
        return jsonify('Order Added Successfully')
    except:
        return jsonify('Not able to add this order at the moment, please try with different parameters.')
#Update the customer_name in Orders Model with orderID
@app.route(u"/warehouse/update/orders/<orderid>/<name>", methods = ['GET'])
def updateOrder(orderid,name):
    ord.updateOrder(orderid,name)
    try:
        return jsonify('Order Updated Successfully')
    except:
        return jsonify('Order not updated, somethiing went wrong.')
#Get the Sku Model values with passing the SkuID
@app.route("/warehouse/sku/<skuid>", methods = ['GET'])
def skuID(skuid):
    products = sku.getSku(skuid)
    try:
        return jsonify({'id':products.id, 'Product_Name':products.product_name})
    except:
        return jsonify('No Information available for Sku:'+ skuid)
#Get the storage detail based on storage id
@app.route("/warehouse/storage/<st_id>", methods = ['GET'])
def storage(st_id):
    store = st.getID(st_id)
    try:
        return jsonify({'id':store.id, 'Stock':store.stock, 'SKU':store.SKU})
    except:
        return jsonify('No information available for StorageID:'+ st_id)

#Get information about OrderLine based on id
@app.route("/warehouse/orderline/<ol_id>", methods = ['GET'])
def orderLine(ol_id):
    ordLine = ol.getOlId(ol_id)
    try:
        return jsonify({'id':ordLine.id, 'SKU':ordLine.SKU, 'Quantity':ordLine.Quantity})
    except:
        return jsonify('No Information Avaialble For OrderID:'+ ol_id)
