graph_name = 'SpaceX_bpmn_1'
bpmn = {
        "SpaceX": {
            "Marketing":[
                {"label": "Promote Capability",
                 "type": "activity",
                },
            ],
            "System Engineering": [
                {"label": "Develop Capability",
                 "type": "activity",
                 "target": ["Deploy Network",
                            "Promote Capability"]
                },
                {"label": "Deploy Network",
                 "type": "activity",
                 "target": "Install Customer Devices"
                },
                {"label": "Install Customer Devices",
                 "type": "activity",
                 "target": "Operate Service"
                },
                {"label": "Operate Service",
                 "type": "activity",
                 "target": "Collect Payment"
                },
                {"label": "Collect Payment",
                 "type": "event",
                 "target": "Develop Capability"
                },
            ],
            },
        "Starlink Customer": {"main":[
                {"label": "Need Internet",
                 "type": "start",
                 "target":"Evaluate Providers"
                },
                {"label": "Evaluate Providers",
                 "type": "activity",
                 "target":"Order SpaceX"
                },
                {"label": "Order SpaceX",
                 "type": "activity",
                 "target": "wait for availability"
                },
                {"name":"wait for availability",
                 "type": "gateway",
                 "label": "wait for availability",
                 "target": [
                        "Receiver Installation",
                        "Took too long"
                    ]
                },
                {"label": "Receiver Installation",
                 "type": "event",
                 "target": "Subscription Payments"
                },
                {"label": "Subscription Payments",
                 "type": "activity",
                 "target": "Use Internet Service"
                },
                {"label": "Took too long",
                 "type": "event",
                 "target": "Abandon SpaceX\nswitch ISP"
                },
                {"label": "Abandon SpaceX\nswitch ISP",
                 "type": "activity",
                },
                {"label": "Use Internet Service",
                 "type": "end",
                },
            ]},
        }

# Finally the special case of message flow contains an array of tuple pairs connecting node labels
# (label, label)
# When running the generation script will print all node names. Use those for the message flow below:
message_flow = [
    ("SpaceX_Promote Capability", "Starlink Customer_Evaluate Providers"),
    ("Starlink Customer_Order SpaceX", "SpaceX_Deploy Network"),
    ("Starlink Customer_Subscription Payments", "SpaceX_Collect Payment"),
    ("SpaceX_Install Customer Devices", "Starlink Customer_Receiver Installation")
]