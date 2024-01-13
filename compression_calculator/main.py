import json

def calculate_compression_ratio(params):
    cubic_inches_to_cc = 16.387  # Conversion factor

    # Extract parameters
    bore_diameter = params['bore_diameter']
    stroke_length = params['stroke_length']
    combustion_chamber_volume = params['combustion_chamber_volume']
    piston_dome_volume = params['piston_dome_volume']
    gasket_thickness = params['gasket_thickness']
    gasket_diameter = params['gasket_diameter']
    deck_height = params['deck_height']

    # Calculations
    cylinder_volume = (3.14159 * (bore_diameter / 2) ** 2 * stroke_length) * cubic_inches_to_cc
    gasket_volume = 3.14159 * (gasket_diameter / 2) ** 2 * gasket_thickness * cubic_inches_to_cc
    total_volume_bdc = cylinder_volume + combustion_chamber_volume + piston_dome_volume + gasket_volume + (3.14159 * (bore_diameter / 2) ** 2 * deck_height * cubic_inches_to_cc)
    clearance_volume_tdc = combustion_chamber_volume + piston_dome_volume + gasket_volume + (3.14159 * (bore_diameter / 2) ** 2 * deck_height * cubic_inches_to_cc)

    compression_ratio = total_volume_bdc / clearance_volume_tdc
    return compression_ratio

def calculate_quench(params):
    # Extract parameters
    deck_height = params['deck_height']
    compressed_gasket_thickness = params['gasket_thickness']

    # Calculate quench
    quench = deck_height + compressed_gasket_thickness
    return quench

def calculate_engine_displacement(params):
    # Extract parameters
    bore_diameter = params['bore_diameter']
    stroke_length = params['stroke_length']
    number_of_cylinders = params['number_of_cylinders']

    # Calculate engine displacement
    engine_displacement = (3.14159 / 4) * bore_diameter ** 2 * stroke_length * number_of_cylinders
    return engine_displacement

def load_parameters(file_path):
    with open(file_path, 'r') as file:
        params = json.load(file)
    return params

# Main program
file_path = 'engine_parameters.json'  # Replace with your file path
parameters = load_parameters(file_path)

compression_ratio = calculate_compression_ratio(parameters)
quench = calculate_quench(parameters)
engine_displacement = calculate_engine_displacement(parameters)

print(f"The calculated compression ratio is: {compression_ratio:.2f}:1")
print(f"Calculated quench is: {quench:.3f} inches")
print(f"Calculated engine displacement is: {engine_displacement:.2f} cubic inches")
