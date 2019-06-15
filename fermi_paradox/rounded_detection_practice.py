"""Calculate probability of detecting 32 LY-diameter radio bubble given 15.6 M
randomly distributed civilizations in the galaxy."""
import math
from random import uniform, random
from collections import Counter

# length units in light-years
DISC_RADIUS = 50_000
DISC_HEIGHT = 1_000
NUM_CIVS = 15_600_000
DETECTION_RADIUS = 16


def random_polar_coordinates_xyz():
    """Generate uniform random xyz point within a 3D disc."""
    r = random()
    theta = uniform(0, 2 * math.pi)
    x = round(math.sqrt(r) * math.cos(theta) * DISC_RADIUS, 3)
    y = round(math.sqrt(r) * math.sin(theta) * DISC_RADIUS, 3)
    z = round(uniform(0, DISC_HEIGHT), 3)
    return x, y, z


def rounded(n, base):
    """Round a number to the nearest number designated by base parameter."""
    return int(round(n / base) * base)


def distribute_civs():
    """Distribute xyz locations in galactic disc model and return list."""
    civ_locs = []
    while len(civ_locs) < NUM_CIVS:
        loc = random_polar_coordinates_xyz()
        civ_locs.append(loc)
    return civ_locs


def round_civ_locs(civ_locs):
    """Round xyz locatins and return list of rounded locations."""
    # convert radius to cubic dimensions:
    detect_distance = round((4 / 3 * math.pi * DETECTION_RADIUS ** 3) ** (1 / 3))
    print(f"\ndetection radius = {DETECTION_RADIUS} LY")
    print(f"cubic detection radius = {detect_distance} LY")

    # round civilization xyz to detection distance
    civ_locs_rounded = []

    for x, y, z in civ_locs:
        i = rounded(x, detect_distance)
        j = rounded(y, detect_distance)
        k = rounded(z, detect_distance)
        civ_locs_rounded.append((i, j, k))

    return civ_locs_rounded


def calc_prob_of_detection(civ_locs_rounded):
    """Count locations and calcualte probability of duplicate values."""
    overlap_count = Counter(civ_locs_rounded)
    overlap_rollup = Counter(overlap_count.values())
    num_single_civs = overlap_rollup[1]
    prob = 1 - (num_single_civs / NUM_CIVS)

    return overlap_rollup, prob


def main():
    """Call functions and print results."""
    civ_locs = distribute_civs()
    civ_locs_rounded = round_civ_locs(civ_locs)
    overlap_rollup, detection_prob = calc_prob_of_detection(civ_locs_rounded)
    print(f"length pre-rounded civ_locs = {len(civ_locs)}")
    print(f"length of rounded civ_locs_rounded = {len(civ_locs_rounded)}")
    print(f"overlap_rollup = {overlap_rollup}\n")
    print(f"probability of detection = {detection_prob:.3f}")

    # QC step to check rounding
    print("\nFirst 3 locations pre- and post-rounding:\n")
    for i in range(3):
        print(f"pre-round: {civ_locs[i]}")
        print(f"post-round: {civ_locs_rounded[i]}\n")


if __name__ == "__main__":
    main()
