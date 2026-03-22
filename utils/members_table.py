import argparse
import json

TABLE = """# Членове на НПО Пешачко

<table>
  <thead>
    <tr>
      <th>Име</th>
      <th>Дата</th>
      <th>Длъжност</th>
    </tr>
  </thead>
  <tbody>
{members}
  </tbody>
</table>
"""

MEMBER = """    <tr>
      <td>{name}</td>
      <td>{date}</td>
      <td>{position}</td>
    </tr>"""


def parse_args():
    parser = argparse.ArgumentParser(
        description="Form members HTML table given JSON file."
    )
    parser.add_argument("input", help="Input JSON file.")
    parser.add_argument("output", help="Output MD file.")
    return parser.parse_args()


def main(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as h:
        data = json.load(h)

    members = []
    for person in data:
        position = person.get("Длъжност", "")
        if position == "Председател":
            position = f"<b>{position}</b>"

        members.append(
            MEMBER.format(
                name=person["Име"],
                date=person["Дата"],
                position=position,
            )
        )

    with open(output_file, "w", encoding="utf-8") as h:
        h.write(TABLE.format(members="\n".join(members)))


if __name__ == "__main__":
    args = parse_args()
    main(args.input, args.output)
