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
    last_sentence_index = -1
    num_sentences = 0
    N = len(essay)
    for i in range(N):
        char = essay[i]
        if char == '.': 
            num_sentences += 1
            last_sentence_index = i
        if char == '\n': 
            if num_sentences > 5:
                print(f'{bcolors.FAIL}{num_sentences} sentences detected!\n')
                print(f'{bcolors.FAIL}sentence limit of 5 per paragraph exceeded!\n')
                print(f'... {essay[last_sentence_index:i+1]} ...')
                return False
            num_sentences = 0
    
    if num_sentences > 5:
        print(f'{bcolors.FAIL}{num_sentences} sentences detected!\n')
        print(f'{bcolors.FAIL}sentence limit of 5 per paragraph exceeded!\n')
        print(f'... {essay[last_sentence_index:i+1]} ...')
        return False

    return True

def check_past_tense(essay: str) -> bool:
    """
    :param essay: essay to check past tense for.
    :returns: 
        True if no past tense detected.
        False if any past tense detected.
    """
    words = essay.split(' ')
    for word in words:
        if word.endswith('ed'):
            print(f'{bcolors.FAIL}past tense word detected!')
            print(f'{bcolors.FAIL}\n{word}\n')
            return False
    return True
