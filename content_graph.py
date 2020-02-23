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
                 "target": "Install Customer Devices\n1000 MB/s"
                },
                {"label": "Install Customer Devices\n1000 MB/s",
                 "type": "activity",
                 "target": "Operate Service"
                },
                {"label": "Operate Service",
                 "type": "activity",
                 "target": "Collect\nPayment"
                },
                {"label": "Collect\nPayment",
                 "type": "event",
                 "target": ("Develop Capability", "Reinvest\nall profits")
                },
            ],
        },
        "ViaSat/Iridium": {
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
                 "target": "Install Customer Devices\n10 MB/s"
                },
                {"label": "Install Customer Devices\n10 MB/s",
                 "type": "activity",
                 "target": "Connect to NOC Hub"
                },
                {"label": "Connect to NOC Hub",
                 "type": "activity",
                 "target": "Routing\nselection"
                },
                {"name":"Routing\nselection",
                 "type": "gateway",
                 "label": "Routing\nselection",
                 "target": [
                        "Sat.\nNetwork",
                        ("Conv.\nNetwork", "if\navail."),
                    ]
                },
                {"label": "Sat.\nNetwork",
                 "type": "event",
                 "target": "Operate Service"
                },
                {"label": "Conv.\nNetwork",
                 "type": "event",
                 "target": "Operate Service"
                },
                {"label": "Operate Service",
                 "type": "activity",
                 "target": "Collect\nPayment"
                },
                {"label": "Collect\nPayment",
                 "type": "event",
                 "target": [
                     "Take\nProfit",
                     "Develop Capability"
                 ]
                },
                {"label": "Take\nProfit",
                 "type": "end",
                },
            ],
            },
        "Conventional ISP's":{
            "Marketing":[
                {"label": "Promote Capability",
                 "type": "activity",
                },
            ],
            "System Operations":[
                {"label": "Develop Capability",
                 "type": "activity",
                 "target": ["Select\nConnection\nType",
                            "Promote Capability"]
                },
                {"name":"Select\nConnection\nType",
                 "type": "gateway",
                 "label": "Select\nConnection\nType",
                 "target": [
                        "DSL\n40\nMB/s",
                        "Ethernet\n100\nMB/s",
                        "Fiber\n1000\nMB/s"
                    ]
                },
                {"label": "Ethernet\n100\nMB/s",
                 "type": "event",
                 "target": "Connect user to FDDI"
                },
                {"label": "DSL\n40\nMB/s",
                 "type": "event",
                 "target": "Connect user to FDDI"
                },
                {"label": "Fiber\n1000\nMB/s",
                 "type": "event",
                 "target": "Connect user to FDDI"
                },
                {"label": "Connect user to FDDI",
                 "type": "activity",
                 "target":"Collect\nPayment"
                },
                {"label": "Collect\nPayment",
                 "type": "event",
                 "target": [
                     "Take\nProfit",
                     "Develop Capability"
                 ]
                },
                {"label": "Take\nProfit",
                 "type": "end",
                },
            ]
        },
        "Customer": {"main":[
                {"label": "Need\nInternet",
                 "type": "start",
                 "target":"Type of\nconnection"
                },
                {"label": "Type of\nconnection",
                 "type": "gateway",
                 "target":[
                        "Home\nInternet",
                        "Business\nInternet"
                    ]
                },
                {"label": "Home\nInternet",
                 "type": "event",
                 "target": "Evaluate existing ISP's"
                },
                {"label": "Business\nInternet",
                 "type": "event",
                 "target": "Evaluate existing ISP's"
                },
                {"label": "Evaluate existing ISP's",
                 "type": "activity",
                 "target":"Select\nISP"
                },
                {"name":"Select\nISP",
                 "type": "gateway",
                 "label": "Select\nISP",
                 "target": [
                        ("Order\nSpaceX", "high coverage\nlow cost\nlow latency"),
                        ("Order\nViaSat/\nIridium", "good coverage\nhigh cost\nhigh latency"),
                        ("Order\nconv.\nISP", "low coverage\nlow cost\nlow latency"),
                    ]
                },
                {"label": "Order\nSpaceX",
                 "type": "event",
                 "target": "wait for\navailability"
                },
                {"label": "Order\nViaSat/\nIridium",
                 "type": "event",
                 "target": "wait for\navailability"
                },
                {"label": "Order\nconv.\nISP",
                 "type": "event",
                 "target": "wait for\navailability"
                },
                {"name":"wait for\navailability",
                 "type": "gateway",
                 "label": "wait for\navailability",
                 "target": [
                        "Receiver\ninstall",
                        "Took\ntoo\nlong"
                    ]
                },
                {"label": "Receiver\ninstall",
                 "type": "event",
                 "target": "Requirements\nfulfilled"
                },

                {"label": "Requirements\nfulfilled",
                 "type": "gateway",
                 "target": [
                        ("Subscription Payments", "yes"),
                        ("Abandon ISP\nswitch to competitor", "no")
                    ]
                },
                {"label": "Subscription Payments",
                 "type": "activity",
                 "target": "Use\nInternet\nService"
                },
                {"label": "Took\ntoo\nlong",
                 "type": "event",
                 "target": "Abandon ISP\nswitch to competitor"
                },
                {"label": "Abandon ISP\nswitch to competitor",
                 "type": "activity",
                 "target": "Select\nISP"
                },
                {"label": "Use\nInternet\nService",
                 "type": "end",
                },
            ]},
        }

# Finally the special case of message flow contains an array of tuple pairs connecting node labels
# (label, label)
# When running the generation script will print all node names. Use those for the message flow below:
message_flow = [
    ("SpaceX_Promote Capability", "Customer_Evaluate existing ISP's"),
    ("Customer_Order\nSpaceX", "SpaceX_Deploy Network"),
    ("Customer_Subscription Payments", "SpaceX_Collect\nPayment"),
    ("SpaceX_Install Customer Devices\n1000 MB/s", "Customer_Receiver\ninstall"),
    ("Customer_Order\nconv.\nISP", "Conventional ISP's_Select\nConnection\nType"),
    ("Conventional ISP's_Connect user to FDDI", "Customer_Receiver\ninstall"),
    ("Customer_Subscription Payments", "Conventional ISP's_Collect\nPayment"),
    ("Conventional ISP's_Promote Capability", "Customer_Evaluate existing ISP's"),
    ("ViaSat/Iridium_Promote Capability", "Customer_Evaluate existing ISP's"),
    ("Customer_Order\nViaSat/\nIridium", "ViaSat/Iridium_Deploy Network"),
    ("ViaSat/Iridium_Install Customer Devices\n10 MB/s", "Customer_Receiver\ninstall"),
    ("Customer_Subscription Payments", "ViaSat/Iridium_Collect\nPayment"),
]