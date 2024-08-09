import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

def db_connect():
    con = sqlite3.connect('items.db')
    return con

@app.route('/')
def welcome():
    return '<h1>Welcome to the items database</h1>'

@app.route('/item', methods=['GET'])
def get_emps():
    con = db_connect()
    cur = con.cursor()
    rows = cur.execute('select * from records').fetchall()
    con.close()
    return jsonify(rows)

@app.route('/item/', methods=['POST'])
def add_emp():
    con = db_connect()
    cur = con.cursor()
    new_item = request.get_json()
    id = new_item['id']
    Name = new_item['Name']
    code = new_item['code']
    category = new_item['category']
    size = new_item['size']
    Unit_price = new_item['Unit price']
    inventory = new_item['inventory']
    color = new_item['color']

    cur.execute("INSERT INTO records (id, Name, code, category, size, 'Unit price', inventory, color) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id, Name, code, category, size, Unit_price, inventory, color))
    con.commit()
    con.close()
    return new_item

@app.route('/item/<itemid>', methods=['PUT', 'PATCH'])
def mod_item(itemid):
    con = db_connect()
    cur = con.cursor()
    item = cur.execute('SELECT * FROM records WHERE id = ?', (itemid,)).fetchone()
    Name = item[1]
    code = item[2]
    category = item[3]
    size = item[4]
    Unit_price = item[5]
    inventory = item[6]
    color = item[7]
    update_item = request.get_json()
    if 'Name' in update_item:
        Name = update_item['Name']
    if 'code' in update_item:
        code = update_item['code']
    if 'category' in update_item:
        category = update_item['category']
    if 'size' in update_item:
        size = update_item['size']
    if 'Unit_price' in update_item:
        Unit_price = update_item['Unit_price']
    if 'inventory' in update_item:
        inventory = update_item['inventory']
    if 'color' in update_item:
        color = update_item['color']


    cur.execute("UPDATE records SET Name = ?, code = ?, category = ?, size = ?, 'Unit price' = ?, inventory = ?, color = ?'' WHERE id = ?", (Name, code, category, size, Unit_price, inventory, color))
    con.commit()
    con.close()
    return f'Record {itemid} was successfully updated!'

@app.route('/item/<itemid>', methods=['DELETE'])
def del_item(itemid):
    con = db_connect()
    cur = con.cursor()
    cur.execute('DELETE FROM records WHERE id = ?', (itemid,))
    con.commit()
    con.close()
    return f'Record {itemid} was successfully deleted!'

if __name__== "__main__":
    app.run(debug=True, port=5000)