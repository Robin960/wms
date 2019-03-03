from byrd_wms import db


class Orders(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    customer_name = db.Column(db.String(50), nullable=False)

    def getOrders(self,name):
        orders = Orders.query.filter_by(customer_name=name).first()
        if orders is not None:
            return orders
        else:
            return 'Order ID is not valid'
            
    def delOrder(self, order_id):
        Orders.query.filter_by(id=order_id).delete()
        db.session.commit()
        return 'Order Deleted Successfully'

    def addOrder(self, order_id, name):
        newOrder = Orders(id=order_id, customer_name=name)
        db.session.add(newOrder)
        db.session.commit()
        return 'Order Added Successfully'

    def updateOrder(self, order_id, name):
        db.session.query(Orders).filter(Orders.id == order_id).update({Orders.customer_name:name}, synchronize_session = False)
        db.session.commit()
        return 'Order Updated Successfully' 
    
    def __repr__(self):
        return f"{self.id,self.customer_name}"

class Sku(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    product_name = db.Column(db.String(50), unique=True, nullable=False)

    def getSku(self,sku_id):
        skus = Sku.query.filter_by(id=sku_id).first()
        if skus is not None:
            return skus
        else:
            return 'Sku ID is not valid'

    def __repr__(self):
        return f"{self.id,self.product_name}"


class Storage(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    stock = db.Column(db.Integer, unique=False, nullable=False)
    SKU = db.Column(db.Integer, db.ForeignKey('sku.id'), nullable=False)

    def getID(self, storage_id):
        storage = Storage.query.filter_by(id=storage_id).first()
        if storage is not None:
            return storage
        else:
            return 'Storage ID is not valid'

    def __repr__(self):
        return f"{self.id,self.stock, self.SKU}"

class OrderLine(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    SKU = db.Column(db.Integer, db.ForeignKey('sku.id'), nullable=False)
    Quantity = db.Column(db.Integer, unique=False, nullable=False)
    
    def getOlId(self,ol_id):
        Order_Line = OrderLine.query.filter_by(id=ol_id).first()
        if Order_Line is not None:
            return Order_Line
        else:
            return 'OrderLine ID is not valid'

    def __repr__(self):
        return f"{self.id,self.SKU, self.Quantity}"


# 400 Error Handling
class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        res = dict(self.payload or ())
        res['message'] = self.message
        return res
 
#Create Tables From Models
"""         db.create_all()
        orderList = ''
        data = Orders.query.all()

        if data is None: 
        #Adding Data into Orders Table
            Order_1 = Orders(customer_name = 'AAA')
            Order_2 = Orders(customer_name = 'BBB')
            Order_3 = Orders(customer_name = 'CCC')
            Order_4 = Orders(customer_name = 'DDD')
            db.session.add(Order_1)
            db.session.add(Order_2)
            db.session.add(Order_3)
            db.session.add(Order_4)
            
            db.session.commit()
 """            

