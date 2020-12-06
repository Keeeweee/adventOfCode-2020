batch = [line.rstrip('\n') for line in open('data/data.txt')]

class Passport:
    def __init__(self, batchPassport: str):
        self.compulsoryFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        self.optionalFields = ['cid']
        self.values = {}
        splittedBatch = batchPassport.split(' ')
        for entry in splittedBatch:
            key, value = entry.split(':')
            self.values[key] = value

    def isValid(self) -> bool:
        for field in self.compulsoryFields:
            if field not in self.values.keys():
                print(f'Field {field} is missing')
                return False

        return True

    def __str__(self):
        return str(self.values)


passportLine = ''
passports = []
for line in batch:
    if line == '':
        passports.append(passportLine.strip())
        passportLine = ''
        continue

    passportLine += ' '
    passportLine += line
passports.append(passportLine.strip())
count = 0
for batchPassport in passports:
    passport = Passport(batchPassport)
    if passport.isValid():
        count += 1
    else:
        print(passport)

print(count)