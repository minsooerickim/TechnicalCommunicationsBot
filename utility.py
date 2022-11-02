class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


def check_num_sentences_in_paragraph(essay: str) -> bool:
    """
    :param essay: check each paragraph doesn't exceed 5 sentences.
    :returns: 
        True if no paragraphs exceed 5 sentences.
        False if more than 5 sentences per paragraph is detected.
    """
    error_detected = False
    last_paragraph_index = 0
    num_sentences = 0
    N = len(essay)
    for i in range(N):
        char = essay[i]
        if char == '.': 
            num_sentences += 1
        if char == '\n': 
            if num_sentences > 5:
                error_detected = True
                print('\n')
                print(f'\n {bcolors.FAIL}{num_sentences} sentences detected in 1 paragraph!\n')
                print(f'{bcolors.WARNING}sentence limit of 5 per paragraph exceeded!\n')
                print(f'... {essay[last_paragraph_index:i]} ...')
            last_paragraph_index = i+1
            num_sentences = 0
    
    if num_sentences > 5:
        print('\n')
        print(f'\n {bcolors.FAIL}{num_sentences} sentences detected!\n')
        print(f'{bcolors.WARNING}sentence limit of 5 per paragraph exceeded!\n')
        print(f'... {essay[last_paragraph_index:i]} ...')
        return False

    return not error_detected

def check_past_tense(essay: str) -> bool:
    """
    :param essay: essay to check past tense for.
    :returns: 
        True if no past tense detected.
        False if any past tense detected.
    """
    error_detected = False
    words = essay.split(' ')
    for word in words:
        if word.endswith('ed'):
            error_detected = True
            print('\n')
            print(f'\n {bcolors.FAIL}past tense word detected!')
            print(f'{bcolors.WARNING}\n{word}\n')

    return not error_detected

def word_count_per_sentence(essay: str) -> bool:
    """
    Each sentence cannot exceed 25 words.

    :param essay: essay to check the word counts for.
    :returns: 
        True if check passed.
        False if check fails.
    """
    error_detected = False
    split_by_period = essay.split('.')
    for split in split_by_period:
        split_by_space = split.split(' ')
        if len(split_by_space) > 25:
            error_detected = True
            print('\n')
            print(f'\n {bcolors.FAIL}{len(split_by_space)} words detected in a single sentece!\n')
            print(f'{bcolors.WARNING}... {split} ...')

    return not error_detected