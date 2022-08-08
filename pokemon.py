#!/usr/bin/python3

import sys
import dataclasses

@dataclasses.dataclass
class Pokemon:
  number: int
  name: str
  hp: int
  attack: int
  defense: int
  sp_attack: int
  sp_defense: int
  speed: int
  total: int
  average: float

def main(argv):

  r = open('pokemon.txt').read()

  pokemon = []
  for line in r.strip().split('\n'):
    fields = line.split('\t')
    pokemon.append(
      Pokemon(
	number=int(fields[0]),
	name=fields[1],
	hp=int(fields[2]),
	attack=int(fields[3]),
	defense=int(fields[4]),
	sp_attack=int(fields[5]),
	sp_defense=int(fields[6]),
	speed=int(fields[7]),
	total=int(fields[8]),
	average=float(fields[9])))

  pokemon.sort(key=lambda p: p.total)
  if len(argv) == 1:
    print('Which pokemon?')
  else:
    for p in pokemon:
      if p.name.lower().startswith(argv[1].lower()):
        print(p)

if __name__ == "__main__":
  main(sys.argv)
