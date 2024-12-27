import schemdraw
import schemdraw.elements as elm
import sys
import json

schemdraw.theme('dark')
# Function to draw the circuit from JSON
def draw_circuit_from_json():
    with schemdraw.Drawing(file='.\schema.svg', show=False) as d:
        json_obj = sys.argv[2]
        circuit = json.loads(json_obj)

        nodes = {}
        current_node_key = "start"

        while current_node_key:
            node = circuit["nodes"].get(current_node_key)
            component = node["component"]
            direction = node["direction"]
            label = node.get("label", "")
            next_node_key = node.get("connections", None)

            # Draw each component based on its type
            if component == "Battery":
                match direction:
                    case "up":
                        element = d.add(elm.Battery().label(label, loc='top').up())
                    case "down":
                        element = d.add(elm.Battery().label(label, loc='bottom').down())
                    case "right":
                        element = d.add(elm.Battery().label(label, loc='bottom').right())
                    case "left":
                        element = d.add(elm.Battery().label(label, loc='bottom').left())
                    
            elif component == "Capacitor":
                match direction:
                    case "up":
                        element = d.add(elm.Capacitor().label(label).up())
                    case "down":
                        element = d.add(elm.Capacitor().label(label).down())
                    case "right":
                        element = d.add(elm.Capacitor().label(label).right())
                    case "left":
                        element = d.add(elm.Capacitor().label(label).left())

            elif component == "Resistor":
                match direction:
                    case "up":
                        element = d.add(elm.Resistor().label(label).up())
                    case "down":
                        element = d.add(elm.Resistor().label(label).down())
                    case "right":
                        element = d.add(elm.Resistor().label(label).right())
                    case "left":
                        element = d.add(elm.Resistor().label(label).left())
            
            elif component == "SourceSin":
                match direction:
                    case "up":
                        element = d.add(elm.SourceSin().label(label).up())
                    case "down":
                        element = d.add(elm.SourceSin().label(label).down())
                    case "right":
                        element = d.add(elm.SourceSin().label(label).right())
                    case "left":
                        element = d.add(elm.SourceSin().label(label).left())
                
            elif component == "Diode":
                match direction:
                    case "up":
                        element = d.add(elm.Diode().label(label).up())
                    case "down":
                        element = d.add(elm.Diode().label(label).down())
                    case "right":
                        element = d.add(elm.Diode().label(label).right())
                    case "left":
                        element = d.add(elm.Diode().label(label).left())
                    
            elif component == "Wire":
                match direction:
                    case "up":
                        element = d.add(elm.Line().up())
                    case "down":
                        element = d.add(elm.Line().down())
                    case "right":
                        element = d.add(elm.Line().right())
                    case "left":
                        element = d.add(elm.Line().left())

            # Update the current node
            nodes[current_node_key] = element.end
            current_node_key = next_node_key

        print("OK")


# Draw the circuit using the JSON
if sys.argv[1] == 'draw_circuit_from_json':
    draw_circuit_from_json()

