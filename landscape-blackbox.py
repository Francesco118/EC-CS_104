import math

# Constants
BAG_COVERAGE = 2000  # square feet
BAG_COST = 27.00  # dollars
NITROGEN_PER_BAG = 1.0  # pounds
POTASSIUM_PER_BAG = 0.125  # pounds
TECHNICIAN_RATE = 20.00  # dollars per hour
TECHNICIAN_COVERAGE = 2500  # square feet per hour

def calculate_fertilizer(lawn_areas):
    total_area = sum(area for area in lawn_areas if area > 0)
    bags_needed = math.ceil(total_area / BAG_COVERAGE)
    fertilizer_cost = bags_needed * BAG_COST
    labor_hours = math.ceil(total_area / TECHNICIAN_COVERAGE)
    labor_cost = labor_hours * TECHNICIAN_RATE
    total_cost = fertilizer_cost + labor_cost
    nitrogen_applied = bags_needed * NITROGEN_PER_BAG
    potassium_applied = bags_needed * POTASSIUM_PER_BAG
    
    return {
        'bags_needed': bags_needed,
        'fertilizer_cost': fertilizer_cost,
        'labor_hours': labor_hours,
        'labor_cost': labor_cost,
        'total_cost': total_cost,
        'nitrogen_applied': round(nitrogen_applied, 3),
        'potassium_applied': round(potassium_applied, 3)
    }

def main():
    lawn_areas = []
    for area in ['front', 'back', 'left', 'right']:
        length = float(input(f"Enter length of {area} lawn (in feet): "))
        width = float(input(f"Enter width of {area} lawn (in feet): "))
        lawn_areas.append(length * width)
    
    results = calculate_fertilizer(lawn_areas)
    
    print("Results:")
    print(f"Bags of fertilizer needed: {results['bags_needed']}")
    print(f"Cost of fertilizer: ${results['fertilizer_cost']:.2f}")
    print(f"Minimum labor hours: {results['labor_hours']}")
    print(f"Cost of labor: ${results['labor_cost']:.2f}")
    print(f"Total cost: ${results['total_cost']:.2f}")
    print(f"Nitrogen applied: {results['nitrogen_applied']} pounds")
    print(f"Potassium applied: {results['potassium_applied']} pounds")

if __name__ == "__main__":
    main()