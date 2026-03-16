from flask import Flask, Response

app = Flask(__name__)

contracts = {
    1: "This contract is for John and building a shed",
    2: "This contract is for Mary and painting a house"
}

customers = ["John", "Mary"]

# -------------------------
# CONTRACT ROUTE
# -------------------------
@app.route("/contract/<int:id>")
def contract(id):

    if id in contracts:
        return contracts[id], 200

    return "Contract not found", 404


# -------------------------
# CUSTOMER ROUTE
# -------------------------
@app.route("/customer/<customer_name>")
def customer(customer_name):

    if customer_name in customers:
        return Response(status=204)

    return "Customer not found", 404


if __name__ == "__main__":
    app.run(debug=True)