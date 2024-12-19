import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt

class PolylineParser:
    def __init__(self, xml_file):
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()
        self.polylines = []
        self.bounds = None
        self.parse_info()
        self.parse_polylines()

    def parse_info(self):
        info = self.root.find('info')
        if info is not None:
            bounds = info.find('bounds')
            if bounds is not None:
                self.bounds = {
                    'min_x': float(bounds.get('min_x')),
                    'min_y': float(bounds.get('min_y')),
                    'max_x': float(bounds.get('max_x')),
                    'max_y': float(bounds.get('max_y'))
                }

    def parse_polylines(self):
        layer = self.root.find('layer')
        if layer is None:
            return

        for polyline in layer.findall('polyline'):
            vertices = []
            for vertex in polyline.findall('vertex'):
                vertices.append({
                    'x': float(vertex.get('x')),
                    'y': float(vertex.get('y')),
                    'z': float(vertex.get('z'))
                })
            self.polylines.append(vertices)

    def plot_polylines(self, save_path=None):
        plt.figure(figsize=(12, 8))
        
        # Plot each polyline
        for polyline in self.polylines:
            x = [v['x'] for v in polyline]
            y = [v['y'] for v in polyline]
            plt.plot(x, y, '-', linewidth=1)

        # Set bounds if available
        if self.bounds:
            plt.xlim(self.bounds['min_x'], self.bounds['max_x'])
            plt.ylim(self.bounds['min_y'], self.bounds['max_y'])

        plt.title('Polyline Visualization')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.axis('equal')  # Equal aspect ratio

        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

def main():
    # Example usage
    parser = PolylineParser('input.xml')
    parser.plot_polylines('polylines.png')

if __name__ == '__main__':
    main()
