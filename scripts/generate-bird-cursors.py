"""Draw hand-authored 32 x 32 bird cursors (Python standard library only)."""

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


# Short rows are padded with transparency to keep the drawings easy to edit.
BIRDS = {
    "cockatoo": PIXELS,
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


def chunk(kind, data):
    return (
        struct.pack(">I", len(data))
        + kind
        + data
        + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)
    )


def draw(name, drawing):
    rows = drawing.strip().splitlines() if isinstance(drawing, str) else drawing
    assert len(rows) == 32 and all(len(row) <= 32 for row in rows), name
    rows = [row.ljust(32, ".") for row in rows]
    scanlines = b"".join(
        b"\x00" + b"".join(bytes(PALETTE[pixel]) for pixel in row)
        for row in rows
    )
    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", 32, 32, 8, 6, 0, 0, 0))
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
