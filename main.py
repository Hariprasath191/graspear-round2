def process_order(order_legs, order_wings, order_flesh):
    # Parts per chicken
    c_legs = 2
    c_wings = 2
    c_flesh = 1

    leg_w = 0.250
    wing_w = 0.250
    flesh_w = 1.0

    n_legs = order_legs
    n_wings = order_wings
    n_flesh = order_flesh

    c_for_legs = -(-n_legs // c_legs)  
    c_for_wings = -(-n_wings // c_wings)
    c_for_flesh = -(-n_flesh // c_flesh)

    total_chickens_needed = max(c_for_legs, c_for_wings, c_for_flesh)

    remaining_legs = total_chickens_needed * c_legs - n_legs
    remaining_wings = total_chickens_needed * c_wings - n_wings
    remaining_flesh = total_chickens_needed * c_flesh - n_flesh

    # Total weights
    order_weight = n_legs * leg_w + n_wings * wing_w + n_flesh * flesh_w
    remaining_weight = remaining_legs * leg_w + remaining_wings * wing_w + remaining_flesh * flesh_w

    print(f"Customer order weight: {order_weight} kg")
    print(f"Whole chickens needed: {total_chickens_needed}")
    print(f"Remaining: {remaining_legs} legs, {remaining_wings} wings, {remaining_flesh} flesh portions")
    print(f"Remaining inventory weight: {remaining_weight} kg")

legs=int(input("Enter the legs : "))
wings=int(input("Enter the wings : "))
flesh=int(input("Enter the flesh : "))
#process_order(24, 13, 7)
process_order(legs,wings,flesh)
