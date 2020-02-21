graph_name = "Pizza Time"
bpmn = {"Pizza Customer": {"main":[
                {"label": "Hungry for pizza",
                 "type": "start",
                 "target":"Select a pizza"
                },
                {"label": "Select a pizza",
                 "type": "activity",
                 "target":"Order a pizza"
                },
                {"label": "Order a pizza",
                 "type": "activity",
                 "target": "call or wait"
                },
                {"name":"call or wait",
                 "type": "gateway",
                 "label": "event driven",
                 "target": [
                        "pizza received", 
                        "60 minutes"
                    ]
                },
                {"label": "pizza received",
                 "type": "event",
                 "target": "Pay for pizza"
                },
                {"label": "Pay for pizza",
                 "type": "activity",
                 "target": "Eat pizza"
                },
                {"label": "Eat pizza",
                 "type": "activity",
                 "target": "hunger satisfied"
                },
                {"label": "60 minutes",
                 "type": "event",
                 "target": "Ask for pizza"
                },
                {"label": "Ask for pizza",
                 "type": "activity",
                },
                {"label": "hunger satisfied",
                 "type": "end",
                },
            ]},
        "Pizza Vendor": {
            "Delivery Boy": [
                {"label": "Deliver the pizza",
                 "type": "activity",
                 "target": "Receive Payment"
                },
                {"label": "Receive Payment",
                 "type": "activity",
                 "target": "Process finish"
                },
                {"label": "Process finish",
                 "type": "end",
                },
            ],
            "Chef": [
                {"label": "Bake the pizza",
                 "type": "activity",
                 "target": "Deliver the pizza"
                }
            ],
            "clock": [
                {"label": "Order Received",
                    "type": "start",
                    "target":"Start cooking"
                },
                {"name": "Start cooking",
                    "label": "+",
                    "type": "gateway",
                    "target":["Where is my pizza",
                               "Bake the pizza"]
                },
                {"label": "Where is my pizza",
                "type": "event",
                "target": "Calm customer"
                },
                {"label": "Calm customer",
                "type": "activity",
                "target": "Where is my pizza"
                }
            ],
            },
        }

# Finally the special case of message flow contains an array of tuple pairs connecting node labels
# (label, label)
# When running the generation script will print all node names. Use those for the message flow below:
message_flow = [
    ("Pizza Customer_Order a pizza", "Pizza Vendor_Order Received"),
    ("Pizza Customer_Ask for pizza", "Pizza Vendor_Where is my pizza"),
    ("Pizza Vendor_Calm customer", "Pizza Customer_Ask for pizza"),
    ("Pizza Customer_Pay for pizza", "Pizza Vendor_Receive Payment"),
    ("Pizza Vendor_Receive Payment", "Pizza Customer_Pay for pizza")
]