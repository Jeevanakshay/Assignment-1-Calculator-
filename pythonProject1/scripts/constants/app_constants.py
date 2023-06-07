"""Constants value of all the methods and class"""


class api_routers:
    Create_Post = "/models/{item_id}"
    Displaying_Get = "/return"
    Updating_Grocery = "/updating_items/{name}"
    Delete_Grocery = "/delete_snacks/{item_id}"
    Email = "/Email"
    Pipeline = "/total_sum"


class statement:
    Create = "No quantity is listed "
    create_successfully = "Successfully"
    update = "updated"
    update_if_not = "Not updated"
    delete = "Deleted"


class comments:
    total_price = "Total_Price"
    name = "name"
    list = "$set"
    total_cost = 'total'


class loggers:
    File_name_logger = 'log/app.log'

class Email_handler:
    Subject_obj = "Total price of the products "
    message = { "message": "Email sent successfully"}



class Aggregation:
    agg = [
        {
            '$addFields': {
                'Total_price': {
                    '$multiply': [
                        '$quantity', '$price'
                    ]
                }
            }
        }, {
            '$group': {
                '_id': None,
                'total': {
                    '$sum': '$Total_price'
                }
            }
        }, {
            '$project': {
                '_id': 0
            }
        }
    ]


api_obj = api_routers()
