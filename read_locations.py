def read_locations():
    locations = []
    with open("MOCK_DATA.csv", encoding="utf8") as f:
        i = 0
        for line in f:
            i += 1
            if i == 1:
                continue            
            # print(line.strip())
            parts = line.strip().split(",")
            name = parts[0]
            coord = parts[1] + "," + parts[2]
            locations.append((name, coord))
    return locations

if __name__ == "__main__":
    for name, coords in read_locations():
        print(f"{name} --- {coords}")
    print("Hello, ez a read_locations modul")