from prettytable import PrettyTable

def calculate_drive_ratios(transmission_gear_ratios, rear_diff_ratio):
    return [gear_ratio * rear_diff_ratio for gear_ratio in transmission_gear_ratios]

def calculate_cruise_rpm(drive_ratio, tire_diameter, speeds_mph, shift_rpm=5000):
    return {speed: round((speed * drive_ratio * 336) / tire_diameter) for speed in speeds_mph if (speed * drive_ratio * 336) / tire_diameter <= shift_rpm}

def create_rpm_table(transmission_gear_ratios, rear_diff_ratios, tire_diameter, speeds_mph, shift_rpm):
    for rear_diff_ratio in rear_diff_ratios:
        print(f"\nRear Diff Ratio: {rear_diff_ratio}")
        table = PrettyTable()
        table.field_names = ["C6 Gear"] + [f"{speed} MPH" for speed in speeds_mph]

        overall_drive_ratios = calculate_drive_ratios(transmission_gear_ratios, rear_diff_ratio)
        for gear, drive_ratio in enumerate(overall_drive_ratios, start=1):
            cruise_rpms = calculate_cruise_rpm(drive_ratio, tire_diameter, speeds_mph, shift_rpm)
            if cruise_rpms:  # Only add rows for gears with valid RPM values
                row = [f"{transmission_gear_ratios[gear-1]}"] + [f"{cruise_rpms.get(speed, '-')} RPM" for speed in speeds_mph]
                table.add_row(row)

        print(table)

# Default Input Values
transmission_gear_ratios = [2.40, 1.40, 1.0]  # Transmission gear ratios
rear_diff_ratios = [2.75, 3.50, 3.89, 4.11]  # Multiple rear differential gear ratios
tire_diameter = 31.0  # Tire diameter in inches
speeds_mph = [30, 40, 60, 70, 90]  # Preset cruising speeds
shift_rpm = 5000  # Shifting RPM

# Create and display the RPM table
create_rpm_table(transmission_gear_ratios, rear_diff_ratios, tire_diameter, speeds_mph, shift_rpm)
