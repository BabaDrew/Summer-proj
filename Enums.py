course_letters = ['AGHE', 'ANAT', 'ANIM', 'ANSH', 'APSC', 'ARAB', 'ARTC', 'ARTF', 'ARTH', 'ARTL', 'ASCX',
                  'ASTR', 'BADR', 'BCHM', 'BIOL', 'BIOM', 'BLCK', 'BMED', 'BMIF', 'BWRC', 'CANC', 'CBME',
                  'CHEE', 'CHEM', 'CHIN', 'CIL', 'CISC', 'CIVL', 'CLAS', 'CLST', 'CMAS', 'CMPE', 'COCA',
                  'COGS', 'COMM', 'COMP', 'CRSS', 'CURR', 'CUST', 'CWRI', 'DDHT', 'DEVS', 'DRAM', 'ECON',
                  'EDST', 'EERL', 'ELEC', 'EMPR', 'ENCH', 'ENGL', 'ENIN', 'ENPH', 'ENSC', 'EPID', 'FILM',
                  'FOCI', 'FOUN', 'FREN', 'FRST', 'GENG', 'GEOE', 'GEOL', 'GNDS', 'GPHY', 'GREK', 'GRMN',
                  'HEBR', 'HIST', 'HLTH', 'HPE', 'ICL', 'IDIS', 'INDG', 'INTN', 'INTS', 'INUK', 'ITLN',
                  'JAPN', 'JWST', 'KHS', 'KNPE', 'LANG', 'LATN', 'LAW', 'LIBS', 'LING', 'LISC', 'LLCU',
                  'LSM', 'MAPP', 'MATH', 'MECH', 'MEDS', 'MGMT', 'MICR', 'MINE', 'MIR', 'MNTC', 'MUTH',
                  'NSCI', 'NURS', 'PACT', 'PATH', 'PHAR', 'PHGY', 'PHIL', 'PHMI', 'PHYS', 'POLS', 'PORT',
                  'PPEC', 'PRAC', 'PROF', 'PSYC', 'QGSP', 'RELS', 'REPD', 'RHBS', 'RHL', 'SCCS', 'SOCY',
                  'SOFT', 'SPAN', 'STAM', 'STAT', 'SURP', 'TMED', 'WRIT']

pattern = r"([A-Za-z]{3,4})\s?(\d{3}$)"  # A-Z that occurs 3 to 4 times, with an optional space, and 3 digits

menu = {'1': 'Attendance', '2': 'Participation', '3': 'Quizzes', '4': 'Assignments', '5': 'Term Tests',
        '6': 'Midterms', '7': 'Exam', '8': 'Final Project'}