class Mongo_db:
    db_grocery = "mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"


class api_routers:
    Create_Post = "/models/{item_id}"
    Displaying_Get = "/return"
    Updating_Grocery = "/updating_items/{name}"
    Delete_Grocery = "/delete_snacks/{item_id}"
    Email = "/Email"
    Pipeline = "/total_sum"


class Aggregation:
    agg =[
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
