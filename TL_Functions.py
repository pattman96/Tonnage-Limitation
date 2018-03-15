def PI_1976(ship_dict):
    # define the maximum tonnage and when it applies
    max_tons = 70001;
    max_SDRperTon = 167
    base = 333000

    # define the ranges
    ranges = [
        [500, 3000, 500],
        [3001, 30000, 333],
        [30001, 70000, 250]
    ]

    for key in ship_dict:
        # this will be where the total SDRs are added up
        sdr = []
        sdr.append(base)
        # retrieve the tonnage from the key of ship_dict
        tonnage = ship_dict[key]

        for r in ranges:
            if all([tonnage > r[0], tonnage > r[1]]):
                sdr.append((r[1] - r[0]) * r[2])
            elif all([tonnage > r[0], tonnage <= r[1]]):
                sdr.append((tonnage - r[0]) * r[2])

        if tonnage > max_tons:
            sdr.append((tonnage - max_tons) * max_SDRperTon)

        ship_dict[key] = int(sum(sdr))
        print(ship_dict)
        return ship_dict

def No_PI_1976(ship_dict):
    # define the maximum tonnage and when it applies
    max_tons = 70001;
    max_SDRperTon = 83
    base = 167000

    # define the ranges
    ranges = [
        [501, 30000, 167],
        [30001, 70000, 125]
    ]

    for key in ship_dict:
        # this will be where the total SDRs are added up
        sdr = []
        sdr.append(base)
        # retrieve the tonnage from the key of ship_dict
        tonnage = ship_dict[key]
        print(sdr)

        for r in ranges:
            if all([tonnage > r[0], tonnage > r[1]]):
                sdr.append((r[1] - r[0]) * r[2])
            elif all([tonnage > r[0], tonnage <= r[1]]):
                sdr.append((tonnage - r[0]) * r[2])

        if tonnage > max_tons:
            sdr.append((tonnage - max_tons) * max_SDRperTon)

        print(sdr)
        ship_dict[key] = int(sum(sdr))
        print(ship_dict)
        return ship_dict

def PI_1996(ship_dict):
    # define the maximum tonnage and when it applies
    max_tons = 70001;
    max_SDRperTon = 604
    base = 3200000

    # define the ranges
    ranges = [
        [2001, 30000, 1208],
        [30001, 70000, 333]
    ]

    for key in ship_dict:
        # this will be where the total SDRs are added up
        sdr = []
        sdr.append(base)
        # retrieve the tonnage from the key of ship_dict
        tonnage = ship_dict[key]

        for r in ranges:
            if all([tonnage > r[0], tonnage > r[1]]):
                sdr.append((r[1] - r[0]) * r[2])
            elif all([tonnage > r[0], tonnage <= r[1]]):
                sdr.append((tonnage - r[0]) * r[2])

        if tonnage > max_tons:
            sdr.append((tonnage - max_tons) * max_SDRperTon)

        ship_dict[key] = int(sum(sdr))
        print(ship_dict)
        return ship_dict

def No_PI_1996(ship_dict):
    # define the maximum tonnage and when it applies
    max_tons = 70001;
    max_SDRperTon = 302
    base = 1510000

    # define the ranges
    ranges = [
        [2001, 30000, 604],
        [30001, 70000, 453]
    ]

    for key in ship_dict:
        # this will be where the total SDRs are added up
        sdr = []
        sdr.append(base)
        # retrieve the tonnage from the key of ship_dict
        tonnage = ship_dict[key]

        for r in ranges:
            if all([tonnage > r[0], tonnage > r[1]]):
                sdr.append((r[1] - r[0]) * r[2])
            elif all([tonnage > r[0], tonnage <= r[1]]):
                sdr.append((tonnage - r[0]) * r[2])

        if tonnage > max_tons:
            sdr.append((tonnage - max_tons) * max_SDRperTon)

        ship_dict[key] = int(sum(sdr))
        print(ship_dict)
        return ship_dict