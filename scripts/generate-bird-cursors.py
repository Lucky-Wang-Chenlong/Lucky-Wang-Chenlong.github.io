"""Draw hand-authored pixel bird cursors (Python standard library only)."""

from pathlib import Path
import struct
import zlib


# One character = one pixel. Dots are transparent; K is the dark outline.
PIXELS = [
    "................................",
    "..............KK................",
    ".............KYYK..KK...........",
    "............KYYK.KYYK...........",
    "............KYYKKYYK..KK........",
    "...........KYYYKYYK..KYYK.......",
    "...........KYYYYYYKKYYYK........",
    "..........KYYYYYYYYYYK..........",
    ".........KKKKYYYYYYKK...........",
    "........KWWWWKKKKKK.............",
    ".......KWWWWWWWWWWK.............",
    "......KWWWWWWWWWWWWK............",
    ".....KKKWWKWKWWWWWWK............",
    "....KGGGKWWKKWWWWWWK............",
    "....KGGKKWWWWWWWWWSK............",
    ".....KGKWWWWWWWWSSSK............",
    "......KKWWWWWWWWSSSK............",
    ".......KWWWWWWWWWWWK............",
    ".......KWWWWWSSWWWWWK...........",
    ".......KWWWWKSSSWWWWK...........",
    ".......KWWWWKWWSSWWWK...........",
    ".......KWWWWKWWWSSWWK...........",
    "........KWWWKWWWWSSWK...........",
    "........KWWWWSWWWSSSK...........",
    ".........KWWWWSWSSSSKK..........",
    "..........KWWWWSSSSKWSK.........",
    "...........KKWWSSKKWWSK.........",
    "............KSKKK..KWWYK........",
    "..........KKKGK.KGKKKYYK........",
    ".........KGGGGKKGGGGKKKK........",
    "..........KKKK..KKKK............",
    "................................",
]

PALETTE = {
    ".": (0, 0, 0, 0),
    "K": (53, 52, 59, 255),
    "W": (255, 253, 242, 255),
    "S": (208, 212, 212, 255),
    "Y": (255, 216, 61, 255),
    "G": (111, 117, 132, 255),
    "L": (255, 237, 148, 255),
    "C": (234, 200, 111, 255),
    "O": (249, 149, 46, 255),
    "R": (226, 91, 49, 255),
    "B": (62, 74, 87, 255),
    "T": (87, 158, 169, 255),
    "P": (255, 171, 132, 255),
    "F": (242, 121, 104, 255),
    "V": (119, 194, 89, 255),
    "D": (53, 130, 82, 255),
    "A": (177, 220, 109, 255),
}

# Use the other birds' crisp cream, slate, and warm accent colors.
PALETTE.update({
    color: PALETTE[shared]
    for color, shared in {
        "h": "W", "s": "S", "d": "G", "b": "K", "l": "B",
        "q": "Y", "a": "C", "r": "R", "w": "W",
    }.items()
})


def pixel_polygon(grid, color, points):
    """Fill a hand-authored polygon on an integer pixel grid, without smoothing."""
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            px, py = x + 0.5, y + 0.5
            inside = False
            for (ax, ay), (bx, by) in zip(points, points[1:] + points[:1]):
                if (ay > py) != (by > py):
                    if px < (bx - ax) * (py - ay) / (by - ay) + ax:
                        inside = not inside
            if inside:
                grid[y][x] = color


def pixel_line(grid, color, points):
    """Draw one-pixel feather, bill, and leg details with Bresenham's line."""
    for (x, y), (end_x, end_y) in zip(points, points[1:]):
        dx, dy = abs(end_x - x), -abs(end_y - y)
        sx, sy = (1 if x < end_x else -1), (1 if y < end_y else -1)
        error = dx + dy
        while True:
            if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
                grid[y][x] = color
            if x == end_x and y == end_y:
                break
            twice = 2 * error
            if twice >= dy:
                error += dy
                x += sx
            if twice <= dx:
                error += dx
                y += sy


def night_heron(stretched=False):
    """A broad, level body with a continuous tucked or extended throat."""
    grid = [["."] * 40 for _ in range(44)]
    head_shift = 2 if stretched else 3

    def body_polygon(color, points):
        # Tuck the extended pose's breast inward by one pixel.
        pixel_polygon(grid, color, [
            (x + int(stretched and x < 21 and 23 <= y <= 32), y)
            for x, y in points
        ])
    # Slender bent legs and toes, behind the body. These never move on click.
    pixel_polygon(grid, "a", [(24, 32), (27, 33), (24, 38), (20, 42), (18, 42), (22, 37)])
    pixel_polygon(grid, "q", [(24, 33), (26, 33), (23, 38), (19, 41), (18, 41), (22, 37)])
    pixel_line(grid, "a", [(28, 34), (27, 37), (25, 40), (28, 40)])
    pixel_line(grid, "q", [(27, 35), (26, 37), (24, 40)])
    pixel_line(grid, "K", [(15, 42), (19, 41), (24, 41)])
    pixel_line(grid, "a", [(16, 41), (20, 40), (23, 40)])
    # Widen the breast and belly, flatten the back, and lift the tail. These
    # contours are redrawn on the grid rather than rotating the old sprite.
    body_polygon("K", [(12, 23), (21, 22), (28, 23), (33, 25), (39, 29), (39, 31), (34, 30), (30, 33), (25, 35), (17, 34), (12, 32), (9, 29), (9, 26)])
    body_polygon("s", [(12, 24), (21, 23), (28, 24), (33, 26), (38, 29), (38, 30), (33, 29), (29, 32), (25, 34), (17, 33), (12, 31), (10, 28), (10, 26)])
    body_polygon("h", [(12, 24), (20, 24), (23, 27), (28, 30), (31, 31), (25, 33), (18, 32), (13, 30), (11, 28), (11, 26)])

    # Overlap the neck with the breast so the body's top outline cannot split
    # the two. Both poses keep the tail and feet in place.
    upper = [["."] * 40 for _ in range(28)]

    def neck_polygon(target, color, points):
        # Follow the head leftward, tapering the shift into the fixed breast.
        pixel_polygon(target, color, [
            (x - max(0, min(head_shift, (26 - y) // 2))
             + int(stretched and x <= 15 and y >= 24), y)
            for x, y in points
        ])

    if stretched:
        neck_polygon(upper, "K", [(15, 12), (27, 12), (27, 17), (28, 20), (29, 23), (31, 26), (31, 28), (9, 28), (10, 24), (14, 21), (15, 17)])
        throat = [(16, 12), (21, 12), (22, 16), (22, 19), (24, 22), (27, 25), (27, 28), (10, 28), (11, 25), (15, 22), (16, 18)]
        throat_shadow = [(20, 15), (22, 16), (22, 19), (24, 22), (27, 25), (27, 28), (24, 28), (22, 24), (20, 21), (20, 18)]
        neck_back = [(22, 11), (26, 12), (26, 17), (27, 20), (28, 23), (30, 26), (30, 28), (26, 28), (24, 24), (22, 21), (21, 17), (21, 13)]
    else:
        neck_polygon(upper, "K", [(14, 19), (20, 20), (26, 22), (29, 25), (31, 28), (9, 28), (10, 24)])
        throat = [(15, 20), (20, 21), (24, 23), (27, 26), (27, 28), (10, 28), (11, 25)]
        throat_shadow = [(22, 22), (24, 23), (27, 26), (27, 28), (24, 28), (23, 25)]
        neck_back = [(23, 20), (25, 21), (28, 24), (30, 27), (30, 28), (26, 28), (24, 25), (22, 23)]
    rise = -8 if stretched else 0

    def head_polygon(color, points):
        pixel_polygon(upper, color, [(x - head_shift, y + rise) for x, y in points])

    head_polygon("K", [(10, 16), (11, 14), (14, 12), (18, 11), (22, 12), (25, 15), (27, 18), (28, 21), (26, 23), (22, 23), (18, 22), (14, 20), (11, 18)])
    head_polygon("b", [(11, 15), (14, 13), (18, 12), (21, 12), (24, 15), (26, 18), (27, 22), (25, 23), (22, 19), (18, 15)])
    head_polygon("l", [(14, 13), (18, 12), (21, 13), (25, 17), (23, 16), (20, 14)])
    head_polygon("h", [(11, 16), (14, 15), (17, 13), (20, 14), (21, 17), (23, 20), (25, 22), (21, 22), (17, 20), (13, 18)])
    head_polygon("s", [(14, 19), (18, 20), (22, 21), (25, 23), (21, 23), (17, 21)])
    # Fill the throat after the head: its lower outline must not draw a dark
    # crossbar through the neck. Carry the same fill into the broad breast.
    neck_polygon(upper, "h", throat)
    neck_polygon(upper, "s", throat_shadow)
    # Extend the slate nape alongside the pale throat, all the way to the wing.
    neck_polygon(upper, "l", neck_back)
    # Keep the bill tip inside the canvas as the tucked head moves forward.
    pixel_polygon(upper, "K", [(max(0, x - head_shift), y + rise)
                               for x, y in [(2, 21), (6, 17), (11, 15), (12, 16), (11, 18), (7, 20)]])
    pixel_polygon(upper, "G", [(max(0, x - head_shift), y + rise)
                               for x, y in [(3, 20), (10, 16), (10, 17)]])
    # Red iris, dark pupil, pale eyebrow, and two fine trailing nape plumes.
    for x, y, color in [(14, 15, "a"), (15, 15, "r"), (16, 15, "a"),
                        (14, 16, "r"), (15, 16, "K"), (16, 16, "r"),
                        (14, 17, "a"), (15, 17, "r"), (16, 17, "a"),
                        (14, 14, "h"), (15, 14, "h")]:
        upper[y + rise][x - head_shift] = color
    pixel_line(upper, "w", [(x - head_shift, y + rise)
                            for x, y in [(21, 12), (25, 12), (29, 14), (33, 17), (36, 21)]])
    pixel_line(upper, "s", [(x - head_shift, y + rise)
                            for x, y in [(22, 13), (27, 15), (31, 18)]])
    for y, row in enumerate(upper):
        for x, color in enumerate(row):
            if color != ".":
                grid[y][x] = color
    # The wing follows the flatter back, with a broad slate panel and a short
    # raised tail. Draw it last to blend the neck's rear edge into the shoulder.
    pixel_polygon(grid, "b", [(22, 23), (28, 23), (33, 25), (39, 29), (39, 31), (34, 30), (30, 32), (25, 30), (21, 27)])
    pixel_polygon(grid, "l", [(23, 24), (28, 24), (32, 26), (37, 29), (33, 29), (29, 31), (25, 29), (22, 26)])
    pixel_polygon(grid, "d", [(22, 26), (26, 29), (30, 31), (33, 29), (35, 30), (30, 32), (25, 30)])
    if stretched:
        # Keep the slate fill continuous across the wing's top outline too.
        neck_polygon(grid, "l", [(24, 21), (26, 21), (28, 23), (29, 25), (26, 25), (24, 23)])
    pixel_line(grid, "l", [(34, 29), (37, 30)])
    return ["".join(row) for row in grid]


# Short rows are padded with transparency to keep the drawings easy to edit.
BIRDS = {
    "cockatoo": PIXELS,
    "night-heron": night_heron(),
    "cockatiel": """
................................
................K
...............KYK
..............KYYK
.............KYYK.K
............KYYKKYK
...........KYYYYYK
..........KYYYYYK
.........KLLLLLLK
........KLLLLLLLLK
.......KLLKWKLLLLK
......KKLLKKLLLLLK
.....KGGKLLLLLOOLK
.....KGKLLLLLOOROK
......KKLLLLLLOOLK
.......KLLLLLLLLLK
.......KLLLLWWLLLLK
.......KLLLKWWWLLLK
.......KLLLKWWWWLLK
........KLLKWWWWCLK
........KLLLKWWCCLK
.........KLLLKCCCLK
..........KLLLCCCK
...........KLLCCK
...........KCKKCLK
.........KKGKK.KCLK
.........KKKK...KCLK
.................KCLK
..................KCLK
...................KLLK
....................KKK
................................
""",
    "toucan": """
................................
................................
................................
................................
.................KKKKKK
...............KKBBBBBBK
......KKKKKKKKKBBBBBBBBBBK
....KKYYYYYYYYOKWWWWBBBBK
...KYYYYYYYYOOOKWTKWKBBBK
..KYYYYYYYOOOOOKWTKKKBBBK
..KKKOOOOOOOOOOKWWWWBBBBK
..KBBKOOOOORRRRKWWWBBBBBK
...KBBKKKKKKKKKWWWWWBBBBK
....KK.........KWWWWBBBBK
...............KWWWWWBBBK
...............KWWWWWBBBBK
...............KWWWWWBBBBK
...............KWWWWBKBBBBK
...............KWWWBBKBBBBK
...............KWWBBBKBBBGK
...............KBBBBBKBBGGK
................KBBBBBGGGK
................KBBBBGGGKK
.................KBBBBBKBK
..................KBBBKBBK
..................KRRKBBBK
.................KKGKKBBBK
................KGGGKKBBBK
.................KKK.KBBBK
......................KKK
................................
................................
""",
    "lovebird": """
................................
................................
................................
................................
............KKKKKK
..........KKFFFFFFKK
.........KFFFPPPPPPVK
........KFFPPPPPPPPVVK
.......KFFFPPKWKPPPVVK
......KKFFFPPKKPPPPVVK
.....KRRKFFPPPPPPPPVVK
.....KORKFFPPPPPPPVVVK
......KRKFFFPPPPPVVVVK
.......KKFFFFPPPVVVVVK
........KFFFFPPAVVVVVK
........KAAAAAAVVVVVVVK
........KAAAAAVVVVVVVVK
........KAAAAVVVKDDVVVK
........KAAAVVVVKVDVVVK
........KAAAVVVVKVVDVVK
........KAAAVVVVKVVDDVK
.........KAAVVVVKVDDDDK
.........KVVVVVVVDDDDDK
..........KVVVVVVDDDDK
...........KVVVVDDDDK
............KDDDDDKDVK
............KGKKGK.KDVK
..........KKGGKGGGK.KTK
...........KKK.KKK...KK
................................
................................
................................
""",
}


def cockatoo_spread_wings():
    """Sweep both wings backward from a reshaped shoulder and breast."""
    grid = [["."] * 32 for _ in range(32)]
    # The bird faces left, so both wings extend to the right. The farther wing
    # rises behind the neck; the nearer wing fans out below it in perspective.
    pixel_polygon(grid, "K", [(18, 18), (20, 13), (23, 9), (27, 6), (30, 4),
                              (31, 4), (31, 8), (29, 11), (30, 10), (30, 13),
                              (26, 17), (22, 20)])
    pixel_polygon(grid, "W", [(19, 18), (21, 13), (24, 10), (28, 7), (30, 6),
                              (30, 8), (27, 12), (29, 12), (25, 16), (22, 19)])
    pixel_polygon(grid, "L", [(20, 17), (23, 13), (26, 11), (24, 15), (22, 18)])
    pixel_line(grid, "S", [(29, 8), (25, 13)])
    pixel_line(grid, "S", [(28, 13), (24, 16)])

    # Open the shoulder and narrow the belly, replacing the resting sprite's
    # folded wing. Keep the face, crest, beak hotspot, tail, and feet anchored.
    pixel_polygon(grid, "K", [(7, 16), (18, 16), (21, 19), (21, 23), (18, 26),
                              (16, 28), (12, 28), (9, 25), (7, 22)])
    pixel_polygon(grid, "W", [(8, 16), (17, 16), (20, 19), (20, 23), (17, 26),
                              (15, 27), (12, 27), (10, 24), (8, 22)])
    pixel_polygon(grid, "S", [(17, 19), (20, 20), (20, 23), (17, 26), (15, 27),
                              (13, 26), (16, 24)])
    for y, row in enumerate(PIXELS[:17]):
        for x, color in enumerate(row):
            if color != ".":
                grid[y][x] = color

    # A continuous pale shoulder leads into long, backward-pointing feathers.
    pixel_polygon(grid, "K", [(13, 19), (16, 17), (21, 16), (26, 14), (30, 11),
                              (31, 11), (31, 15), (29, 18), (31, 17), (31, 20),
                              (28, 22), (29, 22), (26, 25), (22, 26), (18, 25),
                              (15, 23)])
    pixel_polygon(grid, "W", [(14, 19), (17, 18), (22, 17), (27, 15), (30, 13),
                              (30, 15), (27, 19), (30, 19), (27, 21), (24, 24),
                              (21, 25), (18, 24), (16, 22)])
    pixel_polygon(grid, "L", [(17, 20), (22, 19), (27, 17), (25, 21), (22, 24),
                              (19, 23)])
    pixel_line(grid, "S", [(29, 15), (25, 19), (23, 20)])
    pixel_line(grid, "S", [(28, 20), (24, 23), (22, 24)])
    pixel_line(grid, "S", [(18, 24), (21, 25), (25, 24)])
    # Blend the wing root into the breast instead of leaving a dark seam.
    pixel_polygon(grid, "W", [(12, 18), (16, 18), (18, 23), (16, 24), (13, 22)])
    for y in range(25, 27):
        for x in range(19, 32):
            if PIXELS[y][x] != "." and grid[y][x] == ".":
                grid[y][x] = PIXELS[y][x]
    for y in range(27, 32):
        for x, color in enumerate(PIXELS[y]):
            if color != ".":
                grid[y][x] = color
    return ["".join(row) for row in grid]


# These birds move their wings or neck instead of opening their beaks.
PRESSED_POSES = {
    "cockatoo": cockatoo_spread_wings(),
    "night-heron": night_heron(stretched=True),
}


# Hand-drawn beak patches for the pressed frame. Keep the head, body, and
# upper-beak hotspot fixed; lower the bottom beak and expose a pink tongue.
OPEN_BEAKS = {
    "cockatiel": (5, 12, [
        "KGGKL",
        "KGKKL",
        ".K.MK",
        "..KPK",
        ".KGKL",
        "..KKL",
    ]),
    "toucan": (2, 11, [
        "KBBKKKKKKKKKK",
        ".KK........MK",
        "..........MPK",
        "........KRRRK",
        ".....KKKOOOK.",
        "...KKOOOOK...",
        "...KRRKKK....",
        "....KK.......",
    ]),
    "lovebird": (5, 10, [
        "KRRKFF",
        "KORKFF",
        ".KK.MK",
        "...KPK",
        ".KRRKF",
        "..KKFF",
    ]),
}
PALETTE["M"] = (137, 57, 72, 255)


def open_beak(name, drawing):
    rows = drawing.strip().splitlines() if isinstance(drawing, str) else drawing
    rows = [row.ljust(32, ".") for row in rows]
    x, y, patch = OPEN_BEAKS[name]
    for offset, pixels in enumerate(patch):
        row = rows[y + offset]
        rows[y + offset] = row[:x] + pixels + row[x + len(pixels):]
    return rows


def chunk(kind, data):
    return (
        struct.pack(">I", len(data))
        + kind
        + data
        + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
    )


def draw(name, drawing):
    rows = drawing.strip().splitlines() if isinstance(drawing, str) else drawing
    width, height = (40, 44) if name.startswith("night-heron") else (32, 32)
    assert len(rows) == height and all(len(row) <= width for row in rows), name
    rows = [row.ljust(width, ".") for row in rows]
    scanlines = b"".join(
        b"\x00" + b"".join(bytes(PALETTE[pixel]) for pixel in row)
        for row in rows
    )
    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(scanlines, 9))
        + chunk(b"IEND", b"")
    )
    target = Path(__file__).resolve().parents[1] / "assets/img/cursor" / f"{name}.png"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(png)
    print(f"Wrote {target} ({len(png)} bytes)")


if __name__ == "__main__":
    for name, drawing in BIRDS.items():
        draw(name, drawing)
        if name in PRESSED_POSES:
            suffix = "tall" if name == "night-heron" else "open"
            draw(f"{name}-{suffix}", PRESSED_POSES[name])
        else:
            draw(f"{name}-open", open_beak(name, drawing))
