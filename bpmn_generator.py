#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxim
conda install -c anaconda graphviz
"""

import graphviz as gv
import os
import datetime

# When installing Graphviz on Windows use the line below (adjust the path)
# os.environ["PATH"] += os.pathsep + 'C:\Program Files (x86)\Graphviz2.38/bin/'

from content_graph import *
# from pizza_example import *


root_folder_path = os.path.dirname(os.path.realpath(__file__))

# Setting up directed graph
# graph_name = 'SpaceX_bpmn_1'
graph_format = "png"
graph_output_path = root_folder_path+"/output"
dot = gv.Digraph(comment=graph_name, format=graph_format, engine='dot')
dot.attr(mode='kk')
dot.attr(overlap='scalexy')
dot.attr(splines="ortho")
# dot.attr(rankdir="LR")
# dot.attr(splines="true")
dot.attr(ratio="auto")
# dot.attr(ratio="0.6")
# dot.attr(concentrate="true")
# dot.attr(margin="0.2")
today = datetime.date.today()
current_date_str = today.strftime("%d %B %Y")
# dot.attr(label=graph_name+" - "+current_date_str, labelloc="t")
default_fontcolor = "black"
edge_label_color = "#d15411"
default_style = ""
default_fillcolor1 = "#7CA4FA"
linecolor = "#2f658f"
default_fontname = "sans bold"
default_penwidth = 2

# ------------------ Node setup-------------------------
# Dictionairy Specifying the Pool, then one level deeper the Lane, then an dict of parameters.
# Types must be in ["start", "end", "event", "activity", "gateway"]




# Das program --------------------

all_nodes = []
for pool in bpmn:
    # Subgraphs need to begin their name with cluster or else no work
    pool_name= "cluster_"+pool.replace(" ", "_")
    with dot.subgraph(name=pool_name) as pool_dot:
        pool_dot.attr(label=pool, color=default_fillcolor1, style="")
        lanes = bpmn[pool]
        for lane in lanes:
            lane_nodes = bpmn[pool][lane]
            lane_name = "_".join(["cluster",pool,lane]).replace(" ", "_")
            with pool_dot.subgraph(name=lane_name) as pool_lane_dot:
                pool_lane_dot.attr(color=default_fillcolor1, style="")
                # pool_lane_dot.attr(margin="20")
                if len(lanes) > 1:
                    pool_lane_dot.attr(label=lane)
                else:
                    pool_lane_dot.attr(label="")
                for index, node in enumerate(lane_nodes):
                    node_label = node.get("label","")
                    node_name = pool+"_"+node.get("name", node.get("label","_".join(["pool",pool,"main",str(index)])))
                    all_nodes.append(node_name)
                    node_target = node.get("target","")
                    node_type = node.get("type", "activity")
                    node_style = default_style
                    node_penwidth = str(default_penwidth)
                    node_fixedsize = "false"
                    node_margin ="0,1"
                    # Node formatting
                    if node_type in ["start", "end", "event"]:
                        node_fixedsize = "shape"
                        node_margin = "0,05"
                        # node_label = "\n"+node_label
                        if node_type in ["start", "end"]:
                            node_shape = "circle"
                            if node_type in ["end"]:
                                node_penwidth = str(default_penwidth*3.5)
                        elif node_type in ["event"]:
                            node_shape = "doublecircle"
                    elif node_type in ["activity"]:
                        node_shape = "box"
                        node_style= "rounded"
                    elif node_type in ["gateway"]:
                        node_shape = "diamond"
                    # Adding Nodes:
                    pool_lane_dot.node(
                        name=node_name,
                        label=node_label,
                        width="0,35",
                        shape = node_shape,
                        color=default_fillcolor1,
                        style=node_style,
                        penwidth=node_penwidth,
                        margin=node_margin,
                        # fixedsize=node_fixedsize,
                        # fontname= default_fontname,
                        )
                    
                    # Adding Edges:
                    if node_target:
                        if isinstance(node_target, list):
                            for index, target in enumerate(node.get("target",[])):
                                if isinstance(target,tuple):
                                    target, edge_label = target
                                    pool_lane_dot.edge(node_name, pool+"_"+target, color=edge_label_color, xlabel=edge_label, fontcolor=edge_label_color, fontname= default_fontname)
                                else:
                                    pool_lane_dot.edge(node_name, pool+"_"+target, color=linecolor)
                        else:
                            if isinstance(node_target,tuple):
                                target, edge_label = node_target
                                pool_lane_dot.edge(node_name, pool+"_"+target, color=edge_label_color, xlabel=edge_label, fontcolor=edge_label_color, fontname= default_fontname)
                            else:
                                pool_lane_dot.edge(node_name, pool+"_"+node_target, color=linecolor)

for origin, target in message_flow:
    dot.edge(origin, target, style="dashed", dir="forward", arrowhead="empty", color=linecolor)

print("\n".join(all_nodes))
dot.render(graph_output_path+"/"+graph_name+"_"+current_date_str.replace(" ","-"), view=False)


