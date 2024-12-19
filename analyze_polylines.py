import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

def read_and_plot_polylines(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Create a new figure
    plt.figure(figsize=(12, 12))
    
    # Find all polyline elements
    for polyline in root.findall('.//polyline'):
        # Get all vertices for this polyline
        x_coords = []
        y_coords = []
        
        for vertex in polyline.findall('vertex'):
            x = float(vertex.get('x'))
            y = float(vertex.get('y'))
            x_coords.append(x)
            y_coords.append(y)
        
        # Plot this polyline
        plt.plot(x_coords, y_coords, '-')
    
    # Set title and labels
    plt.title('Polyline Visualization')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.grid(True)
    
    # Make sure the aspect ratio is equal
    plt.axis('equal')
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Read and plot the polylines from input.xml
    read_and_plot_polylines("input.xml")
