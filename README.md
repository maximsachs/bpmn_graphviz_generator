# BPMN Generation Tool
Using python and graphviz to automatically generate basic BPMN

The graph is specified in the `content_graph.py` file.

Three variables are specified. `graph_name` sets the filename to be used.
`bpmn` contains the graph nodes in a dictionairy. First the keys are the name of the pool. The values is a dictionairy again with the lane names as keys, and as values an array of dictionairies, one for each node. If there is only one lane in the pool, then does not print the lane label.
This results in the general structure of:
```
bpmn = {
    pool1:{
        lane1: [
            nodes
        ],
        lane2: [
            nodes
        ]
    }
    pool2: {
        lane 1: [
            nodes
        ]
    }
}
```

An example for a `nodes`:

```
{"name":"wait for availability",
 "type": "gateway",
 "label": "wait for availability",
 "target": [
        "Receiver Installation",
        "Took too long"
    ]
}
```
The parameters that need to be present is `type`. It specifies what kind of a node this is. Nodes may be `["start", "end", "event", "activity", "gateway"]` and will be rendered accordingly.
The `label` is what is being printed for this graph in the output. The label may be left empty (`""`) if no text is wanted for this node.
The `name` is an internal representation for `graphviz` to referr to this node. `graphviz` requires these names to be unique in the graph. They are automatically generated from the label. However if the label was left empty, then it is advisable to manually set a unique name, because there could be multiple nodes with empty label, and this would violate the uniqueness requirement for node names.
The `target` variable is used to definde to which other nodes a line shall be drawn. This may be the `label` or `name` of the other node.

The third variable to specify in the `content_graph` is the `message_flow`. It contains a list of tuples for `message` connections between nodes. Use the node name for this. When running the generation script will print all the node names to the console.
Example:
```
message_flow = [
    ("SpaceX_Promote Capability", "Starlink Customer_Evaluate Providers"),
    ("Starlink Customer_Order SpaceX", "SpaceX_Deploy Network"),
]
```

A full example for a `content_graph` file is shown below:

```
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
```