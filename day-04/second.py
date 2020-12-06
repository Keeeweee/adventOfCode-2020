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

    def hasAllFields(self) -> bool:
        for field in self.compulsoryFields:
            if field not in self.values.keys():
                print(f'Field {field} is missing')
                return False
        return True

    @staticmethod
    def _dateValidator(date, min, max) -> bool:
        if len(date) > 4:
            return False
        return min <= int(date) <= max

    @staticmethod
    def _birthYearIsValid(date: str) -> bool:
        return Passport._dateValidator(date, 1920, 2002)

    @staticmethod
    def _issueYearIsValid(date: str) -> bool:
        return Passport._dateValidator(date, 2010, 2020)

    @staticmethod
    def _expirationYearIsValid(date: str) -> bool:
        return Passport._dateValidator(date, 2020, 2030)

    @staticmethod
    def _heightIsValid(height: str) -> bool:
        try:
            number = int(height[:-2])
            units = height[-2:]
        except ValueError:
            return False

        if units == 'cm':
            return 150 <= number <= 193
        if units == 'in':
            return 59 <= number <= 76
        return False

    @staticmethod
    def _hairColorIsValid(color: str) -> bool:
        if color[0] != '#':
            return False

        try:
            int(color[1:], 16)
            return True
        except ValueError:
            return False

    @staticmethod
    def _eyeColorIsValid(color: str) -> bool:
        availableColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return color in availableColors

    @staticmethod
    def _pidIsValid(pid: str) -> bool:
        return len(pid) == 9 and pid.isdigit()

    @staticmethod
    def _cidIsValid(cid: str) -> bool:
        return True

    def isValid(self):
        validators = {
            'byr': Passport._birthYearIsValid,
            'iyr': Passport._issueYearIsValid,
            'eyr': Passport._expirationYearIsValid,
            'hgt': Passport._heightIsValid,
            'hcl': Passport._hairColorIsValid,
            'ecl': Passport._eyeColorIsValid,
            'pid': Passport._pidIsValid,
            'cid': Passport._cidIsValid
        }
        if not self.hasAllFields():
            return False

        for key, value in self.values.items():
            if not validators[key](value):
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