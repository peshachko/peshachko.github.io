#!/usr/bin/env python3
import argparse
import json
import math


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compute route length from lat/lng JSON file"
    )
    parser.add_argument("filename", help="Path to JSON file containing coordinates")
    return parser.parse_args()


def haversine(lat1, lon1, lat2, lon2):
    """Calculate the great-circle distance between two points on Earth (meters)."""
    earth_radius_meters = 6371000

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = (
        math.sin(dphi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return earth_radius_meters * c


def route_length(coordinates):
    return sum(haversine(*c1, *c2) for c1, c2 in zip(coordinates, coordinates[1:]))


def main():
    args = parse_args()
    with open(args.filename, "r") as f:
        data = json.load(f)

    length_km = route_length(data["coordinates"]) / 1000
    print(f"Route length: {length_km:.3f} km")


if __name__ == "__main__":
    main()
